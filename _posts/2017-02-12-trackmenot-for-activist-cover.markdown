---
layout: post
status: publish
published: true
title: Use TrackMeNot to Provide Online Cover for Activists
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: https://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: https://groovecoder.com
date: '2017-02-12 21:00:00 -0600'
date_gmt: '2017-02-12 21:00:00'
tags:
- privacy
- obfuscation
- activism
---
I just finished <a href="https://www.amazon.com/gp/product/0262529866/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0262529866&linkCode=as2&tag=groovecoder-20&linkId=e1daefabd57ddb6522ea27464a6e40a1" target="_blank">Obfuscation</a>
by Finn Brunton and Helen Nissenbaum. I liked its examples of
surveillance-attacking tools that go beyond try-to-hide-better privacy
practices. I have now added both
[TrackMeNot](https://addons.mozilla.org/en-US/firefox/addon/trackmenot/) and
[AdNauseam](https://addons.mozilla.org/en-US/firefox/addon/adnauseam/) to
Firefox.

Lately I - and I'm sure many others - have wondered how to apply some tech
savvy to helping activists. I've been showing some of my more activist friends
[privacy tools](https://www.privacytools.io/). But I felt like I wanted to
*do something specific* to help.

Enter obfuscation.

One goal of obfuscation can be to provide cover - i.e., 

> ... keeping an adversary from definitively connecting particular activities,
> outcomes, or objects to an actor. Obfuscation for cover involves concealing
> the action in the space of other actions.
- <a href="https://www.amazon.com/gp/product/0262529866/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0262529866&linkCode=as2&tag=groovecoder-20&linkId=e1daefabd57ddb6522ea27464a6e40a1" target="_blank">Obfuscation</a>

To help provide cover for activists online, you can:

1. Install [TrackMeNot](https://cs.nyu.edu/trackmenot/)
2. Customize its search terms using RSS feeds of activist sites.

This will force anyone surveilling  activists via online search terms to sort
thru your noise in the system.

### Install TrackMeNot

This is super-easy. [TrackMeNot](https://cs.nyu.edu/trackmenot/) is available
for both Firefox and Chrome.

![TrackMeNot addons.mozilla.org Screenshot](/uploads/amo-trackmenot.png)

### Customize search terms

TrackMeNot polls a list of RSS feeds for titles to create randomized search
phrases. By default, it uses popular news sites: nytimes.com, cnn.com,
msnbc.com, and theregister.co.uk. To make your search phrases look like those
of activists, you need to add phrases from activist sites.

reddit contains many sub-reddits for activists ...

![Reddit BlackLivesMatter Subreddit](/uploads/reddit-blm.png)

... and you can get an RSS feed for any sub-reddit by appending `.rss` to its
URL. E.g.,
[https://www.reddit.com/r/BlackLivesMatter/.rss](https://www.reddit.com/r/BlackLivesMatter/.rss)
Copy this URL, open TrackMeNot options ...

![TrackMeNot Options](/uploads/trackmenot-options.png)

... and add it to the RSS Feed.

![TrackMeNot RSS Feed with
BlackLiveMatter](/uploads/trackmenot-rss-feed-blm.png)

* **Note**: Separate your feeds with a `|` character

If there is no sub-reddit for the activist topic, you can get an RSS feed of a
reddit search by appending `.rss` to `/search` before the `?q=` params. E.g.,
[https://www.reddit.com/search.rss?q=dapl](https://www.reddit.com/search.rss?q=dapl)

![TrackMeNot Search Queries](/uploads/trackmenot-queries.png)

Tada! You're now helping to provide online cover for activists' search
activity. You can add as many feeds as you like - just remember to separate
them with a `|` character.
