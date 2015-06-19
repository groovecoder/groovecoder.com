---
layout: post
status: publish
published: true
title: bugzilla-agile
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 646
wordpress_url: http://groovecoder.com/?p=646
date: '2011-07-18 09:59:17 -0500'
date_gmt: '2011-07-18 14:59:17 -0500'
categories:
- mozilla
- mdn
- greatest-hits
tags:
- mozilla
- agile
comments:
- id: 526
  author: Kumar McMillan
  author_email: kumar.mcmillan@gmail.com
  author_url: http://farmdev.com
  date: '2011-07-18 16:25:22 -0500'
  date_gmt: '2011-07-18 22:25:22 -0500'
  content: "At my previous job we did XP (when it was the hotness), then Scrum, and
    we used all sorts of tools.  So I've been doing Agile with a capital A since 2004
    then stopped at Mozilla.  The latest tool I used was Pivotal Tracker and I liked
    it a lot.  There are a lot of rules to Scrum and I don't think it's very useful
    for remotely distributed teams (although there are published adjustments you can
    make).  However, I think the best concept that everyone should adopt from Agile/Scrum
    is this:\r\n\r\nTime does not slip. Ever. If you always release at the *same time*
    then you guarantee new features to your users.\r\n\r\nThe idea is that you release
    every week or at some regular interval (called a sprint).  The features you actually
    release depend on what you were able to get done in that sprint.  If a feature
    was not ready for release then you don't release it but all other finished features
    go out.  Another powerful lesson you learn from working like this is that you
    are forced to *cut* unnecessary features.  Cutting features is the secret to doing
    more work with fewer resources.\r\n\r\naddons.mozilla.org is in the early stages
    of moving to continuous deployment.  We would essentially release a feature as
    soon as it's ready and any feature still in development would be hidden behind
    a feature flag.  This would have a similar affect of delivering value to users
    at a rapid pace but it wouldn't help to force feature cutting.  Pivotal Tracker
    has a really interesting UI where it shows you how many features you'll be able
    to release at the end of the current sprint to facilitate feature cutting.  If
    a project manager gets ambitious and piles *more* features on  the current sprint
    then features at the bottom of the list will roll off.  You cannot bend time!\r\n\r\nThis
    is implemented using a point system; the backend estimates how many points the
    team will complete based on a running average calculated over the last two to
    three sprints.  This would be a nice feature in bugzillaJS and I think all each
    team would need to do is diligently adopt a whiteboard value like points=N (or
    p=N if you insist).  The rest of the effort would be in tallying up previous point
    values, logging time based milestones, and actually building the UI that showed
    a projection of what features will go out next.\r\n\r\nThere is probably a way
    to apply a similar radar for feature cutting to a continuous deployment model
    but I'm not sure it would look the same.  Even without a UI, this is a concept
    all developers can apply in their daily lives.  That is, whenever you're assigned
    a bug be sure that bug has a clear indication of what value it provides to the
    user of your product.  If it does not explain user value then the bug is either
    missing information or isn't valid at all."
- id: 63510
  author: Lincoln
  author_email: lincolnsherman@gmail.com
  author_url: http://chigaavpli1.edublogs.org
  date: '2013-02-24 17:00:26 -0600'
  date_gmt: '2013-02-24 23:00:26 -0600'
  content: "Hey! Quick question that's entirely off topic. Do you know how to make
    your site mobile friendly? My website looks weird when viewing from my apple iphone.
    I'm trying to \r\nfind a theme or plugin that might be able to correct this problem.\r\n\r\nIf
    you have any suggestions, please share. Appreciate it!"
---
<p><img class="alignleft" title="Agile Bugzilla" src="http://www.qa-testing.eu/static/images/bugzilla_logo.jpg" alt="Bugzilla is cute but deadly." width="252" height="147" />I'm not a pure Agilista™ but we're always trying to improve our development process for MDN. John and I like Scrum and XP stuff, but every team does Agile™ a little differently - as they should. A while back we shopped around for tracker tools and stuck (as Mozillians always do) with <a href="https://bugzilla.mozilla.org/describecomponents.cgi?product=Mozilla%20Developer%20Network">bugzilla</a>. We - i.e., mostly John and Jay - also looked at <a href="http://acunote.com">acunote</a>, <a href="http://planbox.com">planbox</a>, <a href="http://scrumdo.com">scrumdo</a>, <a href="http://agilezen.com">agilezen</a>, <a href="http://pivotaltracker.com">pivotal</a>, and <a href="http://agilebench.com">agilebench</a>.</p>
<p style="clear: both;">What we most like about Bugzilla:</p>
<ul>
<li>Bugzilla is Mozillian - it channels the work of tens of thousands of Mozillians; we can cc anyone in the community on a bug</li>
<li>Bugzilla is open - we can link anyone in the world to a bug</li>
<li>Bugzilla is versatile - as Jonath says in <a href="http://blog.johnath.com/2010/02/04/bugzilla-for-humans/">Bugzilla for Humans</a>, it's the devil we know</li>
</ul>
<p>On the latter point, I've forked some agile features onto <a href="https://github.com/gkoberger/BugzillaJS">Greg's BugzillaJS</a> to help us work more Scrummy™. Our most pressing issue is managing releases - our scope keeps bloating and our releases keep slipping. So we're starting to use the Agile/XP concept of "points" to estimate bugs, track our team velocity, and hopefully improve our release rhythm and reliability. Behold our improved "sprint backlog":</p>
<p><a href="http://screencast.com/t/Fk1kKKOu"><img class="size-full wp-image-652 aligncenter" title="mdn_099" src="http://groovecoder.com/wp-content/uploads/2011/07/mdn_099.png" alt="MDN™ 0.9.9 Sprint™ Backlog™" width="360" height="440" /></a></p>
<p>There's a few new things going on here. Here's a summary of how we're doing what we're doing:</p>
<p><img class="alignright" src="http://content.screencast.com/users/groovecoder/folders/Jing/media/61eeb577-8754-4f79-aca9-6a9bcab74002/00000043.png" alt="Bugzilla Agile Target Milestone" /><br />
<strong>Milestone releases</strong> - We use the milestone field of bugzilla for our releases. Next up is 0.9.9 scheduled for August 2nd release. As we move to a more continuous development and release cycle, the milestone version numbers lose meaning (just like Firefox), but we want to track releases. (Sorry James, we're not deploying every check-in just yet).</p>
<p><img class="alignright" src="http://content.screencast.com/users/groovecoder/folders/Jing/media/670e353b-4a0d-4f48-a380-cb1b2d897ab7/00000042.png" alt="Bugzilla Whiteboard" /><br />
<strong>Whiteboard overloading</strong> - We're using a tag=value pattern in the whiteboard to add new "fields" because adding fields and values to bugzilla requires IT changes and they're over-worked as it is. In our case,</p>
<ul>
<li>'u' - the primary user of the feature/bug (faster and more programmable than writing "As a ___, I want ___" every time</li>
<li>'c' - the component that the feature/bug modifies</li>
<li>'p' - points</li>
</ul>
<p><img class="alignright" title="bugzilla agile story points" src="http://content.screencast.com/users/groovecoder/folders/Jing/media/5aa5f192-1a4f-4361-96fe-c68bc5b4cfef/00000040.png" alt="bugzilla agile story points" width="123" height="73" /></p>
<p><strong>Calculating points and stories</strong> - For any search that includes the "whiteboard" column with the specified tokens, the addon sums the number of "Open" and "Closed" stories and points for the release.</p>
<p><img class="alignright" style="clear: both;" src="http://content.screencast.com/users/groovecoder/folders/Jing/media/027c427a-08f3-4d0b-bbf0-04c3851eadfa/00000041.png" alt="MDN Components Graph" width="187" height="162" /><br />
<strong>Pretty graphs</strong> - data visualization FTW. Seriously, graphs give us a quick snapshot of the open v. closed bugs, and in which component we're spending our effort. This is important for MDN because we want to re-write the wiki while continuing to deploy site enhancements and changes. Now we can see exactly how much of our effort is going to the wiki as compared to other components.</p>
<p style="clear: both;">I really hope this improves our releases and makes life easier for devs. Points by release and components are our most pressing needs so we can set realistic release and product expectations, and keep ourselves honest about where we're spending our effort. We'll probably add velocity and burndown charts once we finish a few point-based releases. </p>
<p>If anyone else wants to use it, <a href="https://github.com/groovecoder/BugzillaJS">my fork of BugzillaJS is up on github</a>; download the .xpi file and open it with Firefox to install the addon. Feedback and pull requests are very welcome!</p>
<p><strong>Edit</strong>: I should point out we're inspired by other agile Bugzilla tools - the <a href="http://blog.songbirdnest.com/2008/12/15/songbird-path-to-agility-part-iii/#">Songbird team has wrestled bugzilla into their Agile process</a>, and <a href="https://github.com/fligtar/moxie">fligtar created moxie to help AMO product management</a>.</p>
