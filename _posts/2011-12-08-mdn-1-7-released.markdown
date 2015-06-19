---
layout: post
status: publish
published: true
title: MDN 1.7 Released
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 762
wordpress_url: http://groovecoder.com/?p=762
date: '2011-12-08 23:27:46 -0600'
date_gmt: '2011-12-09 05:27:46 -0600'
categories:
- mozilla
- mdn
tags:
- mdn
comments: []
---
<p><img class="alignnone" title="17" src="http://www.portalprelude.com/images/chambers/challenge_17.jpg" alt="17" width="162" height="90" />We released MDN 1.7 today. Included in this release:</p>
<h3>MDN</h3>
<ul>
<li>Developer Profile CTA on <a href="https://developer.mozilla.org/en-US/demos/submit">demo submit page</a>. (<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=696260">bug 696260</a>)</li>
<li>Geolocation on <a href="https://developer.mozilla.org/en-US/events">the events page</a>. (<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=700778">bug 700778</a>)</li>
<li>Fix bug editing derby demos. (<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=704196">bug 704196</a>)</li>
<li><a href="http://mzl.la/mdn_17">Various other bug fixes, additions, improvements</a></li>
<li>Continue to support the Apps developer launch on MDN</li>
</ul>
<h3>Wiki</h3>
<ul>
<li>Switch auth from MindTouch to django (big <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=674635">bug 674635</a>)</li>
</ul>
<h3>MDN 1.8</h3>
<p>The major themes of <a href="http://mzl.la/mdn_18">MDN 1.8</a> are:</p>
<ul>
<li>Merge our separate mdn &amp; wiki branches so we can develop and deploy both with a sane release process.<br />
It also lets run the new wiki on the production site, controlled by <a href="https://github.com/jsocol/django-waffle">waffle</a>, so we can get feedback from MDN users on the new wiki.</li>
<li>Clean up and polish the django auth.</li>
<li>Define UX and mockups for BrowserID.</li>
<li>Continue to support the Apps developer launch on MDN.</li>
</ul>
<h3>It's gonna be the future soon</h3>
<p><a href="https://blog.mozilla.com/jay/2011/11/29/its-been-an-amazing-ride/">Jay is leaving Mozilla</a>! :( I'm going to miss him and his war stories from the good ol' days of Netscape. He brought a lot of insight and perspective to MDN and drove the efforts to make it more than "just" a documentation wiki. Until someone else takes over product management, we're going to put our heads down to work on the big components of the MindTouch-django wiki migration:</p>
<ol>
<li>Migrate MindTouch wiki data.<br />
It's nice that MindTouch stores HTML and our django wiki also stores HTML. Much better than having to parse and translate wiki markup.</li>
<li>Implement an alternative to DekiScript<br />
MindTouch's DekiScript is a LuaScript subset for making dynamic content snippets in wiki pages. We're planning to implement an equivalent system based on JavaScript with a library to work with the django wiki.</li>
</ol>
<p>I'll probably run product <del>management</del> interference for any urgent MDN features (e.g., apps) until we have a dedicated product manager.</p>
<p>Right now <a href="http://www.b-list.org/">James</a> and <a href="http://decafbad.com/blog/">Les</a> and I are in Toronto with #sumo and #sumodev talking about the future of the newly-amalgamating "Platforms" Webdev team. We want to open <a title="pseudo-translation to test i18n" href="https://developer.mozilla.org/">MDN</a>, <a href="http://support.mozilla.org/">SUMO</a>, <a href="http://mozillians.org/">Mozillians.org</a>, and <a href="https://input.mozilla.com/">Input</a> sites as community "platforms" over the next year. Stay tuned for more ...</p>
