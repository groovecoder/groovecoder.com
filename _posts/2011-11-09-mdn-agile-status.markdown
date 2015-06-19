---
layout: post
status: publish
published: true
title: MDN Agile and status
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 734
wordpress_url: http://groovecoder.com/?p=734
date: '2011-11-09 16:03:35 -0600'
date_gmt: '2011-11-09 22:03:35 -0600'
categories:
- mdn
tags:
- mdn
- agile
comments: []
---
<p>tl;dr: We're settling into an Agile process for MDN with daily standups and weekly planning. In the last few months we've added and enhanced <a href="https://developer.mozilla.org/profiles/groovecoder/">developer profiles</a>, <a href="https://developer.mozilla.org/events">events</a>, <a href="https://developer.mozilla.org/demos/">demos dev derby</a>, and other MDN features. We've also restored, added, and enhanced drafts, review flags, search, article properties, section editing, and authentication in the <a href="https://kuma-stage.mozilla.org/">new wiki</a>. I'll try to write status posts more frequently - each time we make a release, if possible.</p>
<h2>Agile<img class="alignright" title="Agile" src="https://confessionsofascrummaster.files.wordpress.com/2008/01/agile.jpg" alt="Agile" width="300" height="434" /></h2>
<p>Since <a title="MDN &amp; Kuma progress" href="http://groovecoder.com/2011/06/15/mdn-kuma-progress/">my last MDN &amp; Kuma progress post</a>, we've settled into a regular, yet customized, Agile methodology in the MDN team with our <a title="bugzilla-agile" href="http://groovecoder.com/2011/07/18/bugzilla-agile/">agile Bugzilla JS tool</a>. We've pushed MDN 0.9.8, 0.9.9, 1.0, 1.1, 1.2, 1.3, 1.4, and 1.5 thru it relatively smoothly. We've learned and adapted a few techniques in our Agile process worth noting:</p>
<h3>Daily standups on IRC</h3>
<ol>
<li>What have you done since we last met?</li>
<li>What do you plan to do until we meet next?</li>
<li>Are you blocked by anything?</li>
</ol>
<p>By far the 3rd question here is the most important. The first questions are mostly intended to lead into the 3rd. Our scrum-master (now me) is tasked with removing any and all blockers as much as possible - usually chasing down people in other groups from whom we need something (IT, DevEngage, Legal, Security, etc.)</p>
<h3>(Bi-)Weekly Retro &amp; Planning Poker</h3>
<p>We push code on Tuesdays, so we alternate between post-/pre- and mid-sprint planning meetings. Mid-sprint planning meetings are shorter and faster, little more than a standup. We use an <a href="https://etherpad.mozilla.org/MNIfVpfAgq">etherpad template for a running minutes of our weekly Wednesday meetings</a>. The basic format is:</p>
<ol>
<li>Retro - what's go[(ing)|(ne)] good or bad in the sprint?</li>
<li>Discuss - general items to discuss, usually flowing from Retro</li>
<li>Planning (post/pre-sprint only) - re-assess bugs carried over from previous sprint, use <a href="http://planningpoker.com/">planningpoker.com</a> to estimate the <a href="http://mzl.la/mdn_16">current sprint backlog in bugzilla</a></li>
</ol>
<h2><img class="alignleft" title="Test Chamber Progress" src="http://www.freakified.net/wp-content/uploads/2008/05/testchamber13wthumb.png" alt="Test Chamber Progress" width="309" height="606" />Status</h2>
<p>We're developing major features for both MDN and the upcoming wiki.</p>
<h2>MDN</h2>
<ul>
<li>Developer profiles<br />
My <a href="https://developer.mozilla.org/en-US/profiles/groovecoder/">MDN profile</a> is missing demos because I haven't made any yet. :( We want to hook this up with <a href="http://mozillians.org">Mozillians.org</a> in the (near) future.</li>
<li><a href="https://developer.mozilla.org/events">Events</a><br />
We've tried to make the MDN events page a comprehensive resource to find the events Mozillians attend. Inspired originally by <a href="http://isithackday.com/wheresmozilla/">Christian's site for Mozilla events</a>.</li>
<li><a href="https://developer.mozilla.org/demos/">Demos &amp; Dev Derby</a><br />
We've done significant work on the Dev Derby feature - streamlining the process and clearing out bugs. This is one of my favorite MDN features. When I need to show anyone cool web technology I can open the MDN demo studio and inevitably find <a href="https://developer.mozilla.org/demos/detail/remixing-reality">something way cool with canvas, video, audio, and webgl</a>.</li>
<li>Miscellaneous<br />
We're also finding and squashing bugs as often as we can. We finally restored production server error emails, so we should be much better about squashing bugs that real users are are hitting. And we're trying to add smaller optimizations and fun features as often as we can.</li>
</ul>
<p>I enjoy enhancing MDN in addition to building the new wiki system. The wiki is important and should help us take more control over our docs, but it's still behind-the-scenes; I like shipping code to a production site that helps people, especially developers, immediately.</p>
<h2>Wiki</h2>
<p>We hope to soon (by the end of the year) run the new wiki side-by-side with MindTouch so we can work from a single line of code and allow testers to compare MindTouch with the new wiki on the same server. But so far we've developed the following features on <a href="https://kuma-stage.mozilla.org/">the separate kuma wiki staging server</a>:</p>
<ul>
<li>Drafts<br />
We use localStorage to periodically save the editing session so a writer doesn't lose precious work if their client crashes.</li>
<li>Review Flags<br />
We added review flags for both technical and editorial review.</li>
<li>Search<br />
We restored the Sphinx-powered search backend we inherited from SUMO/kitsune (just in time for them to move on to ElasticSearch). We still need to restore all of the search frontend and ancillary features.</li>
<li>Page Properties<br />
We restored and refactored document properties we inherited from SUMO/kitsune.</li>
<li>Section Editing<br />
We added section editing to the wiki - our first major modification to the wiki functionality we inherited from SUMO/kitsune.</li>
<li>Authentication<br />
We're in the middle of switching MDN user authentication from MindTouch to django. We will run both authentication backends together, first django then falling back to MindTouch and auto-registering and migrating users to django authentication as they log in.</li>
</ul>
<p>The wiki work is going pretty well, but we still have a couple of major hurdles to clear: data migration &amp; user scripting. We are already investigating data migration a bit, and once we start migrating data over it should help direct our work on user scripts. In my opinion, we can see light at the end of the tunnel but we're still watching out to avoid potential train-wrecks.</p>
<h2>The rest</h2>
<p>Outside of MDN, I helped pull together an <a href="http://techfests.com/Tulsa/2011/Tracks/HTML5/default.aspx">HTML5 track for Tulsa Tech Fest</a>, helped organize a <a href="http://tulsahackathon.com/2011/">Tulsa Hackathon</a> with <a href="http://tulsawebdevs.org/">Tulsa Web Devs</a>, and I participated in <a href="http://tulsa.startupweekend.org/">Startup Weekend Tulsa</a>. At SWT we started a quick web app on top of the TRIF project from Hackathon called <a href="http://ottozen.com">OttoZen</a> to send an SMS alert to someone when there's a traffic incident on their commute. It's making us consider building a broader Data/App site for Oklahoma. We'll see.</p>
<p>From now on I'll try to make a status post every time we make an MDN release.</p>
