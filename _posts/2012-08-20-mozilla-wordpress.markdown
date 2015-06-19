---
layout: post
status: publish
published: true
title: Mozilla & WordPress
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 912
wordpress_url: http://groovecoder.com/?p=912
date: '2012-08-20 13:36:05 -0500'
date_gmt: '2012-08-20 18:36:05 -0500'
categories:
- mozilla
tags:
- mozilla
- wordpress
- community
comments: []
---
<p><img class="aligncenter" title="Mozilla WordPress" src="https://dl.dropbox.com/u/21969365/images/mozilla_wordpress.png" alt="Mozilla WordPress" width="353" height="353" /></p>
<p>TL;DR - I made the <a href="http://wordpress.org/extend/plugins/promote-mdn/">Promote MDN WordPress plugin</a> and enjoyed it; why isn't(?) there a more intentional relationship between Mozilla &amp; WordPress communities?</p>
<h3>WordPress development</h3>
<p>To make the Promote MDN WordPress plugin these last couple weeks, I've worked with WordPress more than I have in the previous decade. I've run dozens of sites with WordPress, but have never been active as a developer or contributor. Observations:</p>
<ul>
<li><strong>Keep code tidy</strong> - Okay, so there's globals and no MVC. But I copied messy code from SEO Smart Links, ran it thru PHP_CodeSniffer and it was actually easy to follow and work with it, due to the ...</li>
<li><strong>Good docs</strong> - The codex has lots of good info. I Googled for stuff like "wordpress http get", "wordpress cache", and "wordpress i18n" and the codex docs always had what I needed.</li>
<li><strong>Can leverage Verbatim for l10n</strong> - After I made a .pot file for the plugin, I added it to our existing MDN project on verbatim. Within hours it was translated into Dutch, Polish, and German. Then a couple days later Brazilian Portuguese and Spanish too. I love our localization teams so much.</li>
<li><strong>Releasing is painful</strong> - It's exactly <a href="https://github.com/groovecoder/wp-promote-mdn/blob/master/RELEASE.txt">this painful</a>. It makes me really love and appreciate our new chief deployment system on MDN, and heroku for my other sites.</li>
<li><strong>Releasing is cool</strong> - It's cool that the plugin is now just a couple clicks away from millions of users. The appeal of "app stores" I guess.</li>
</ul>
<h3>WordPress development at Mozilla</h3>
<p>I coordinated a <a href="http://www.meetup.com/OKC-WordPress-Users-Group/events/68676562/">"WordPress at Mozilla" talk for an OKC WordPress User's Group meetup</a>. When I asked about WordPress on Yammer, only <a href="https://twitter.com/craigcook">Craig</a> and <a href="https://twitter.com/jake_maul">Jake</a> claimed to have WordPress dev and deployment experience at and for Mozilla. They say we have many dozen - approaching a hundred? - WordPress blogs &amp; sites at Mozilla. In addition to that, we have:</p>
<ul>
<li><a href="http://wordpress.org/extend/plugins/browserid/">Mozilla Persona Plugin</a> - Persona for your WordPress site.</li>
<li><a href="http://wordpress.org/extend/plugins/openattribute-for-wordpress/">Open Attribute Plugin</a> - Add licensing information using <a href="http://openattribute.com/">OpenAttribute</a> from Mozilla Drumbeat</li>
<li><a href="http://wordpress.org/extend/plugins/wpbadger/">WPBadger</a> - Issue badges and add them to a user's <a href="www.openbadges.org">Open Badges</a> backpack.</li>
<li>Promote MDN Plugin - adds links to MDN to your WordPress site content</li>
</ul>
<h3>Mozilla and WordPress</h3>
<p>WordPress runs about <strong>55 million websites</strong> in the world. <strong>332 million people</strong> view over <strong>2.5 billion pages</strong> on WordPress.com's hosted sites alone, where there are also <strong>500k new posts</strong> and <strong>400k new comments</strong> <strong>every day</strong>.</p>
<p>Which makes me wonder - does Mozilla have any official or intentional relationship with WordPress? Should we?</p>
<p>WordPress empowers people to <strong>make and control their own content on the web</strong>. (As opposed to, say, Facebook Pages) It seems like we could combine efforts in some cool ways. At the very least, many of our projects and websites could probably put together a cool and useful WordPress plugin of some kind. It's really not bad at all. :)</p>
