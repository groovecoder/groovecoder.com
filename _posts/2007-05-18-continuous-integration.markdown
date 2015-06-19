---
layout: post
status: publish
published: true
title: Continuous Integration
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 177
wordpress_url: http://groovecoder.com/2007/05/18/continuous-integration/
date: '2007-05-18 21:24:00 -0500'
date_gmt: '2007-05-19 02:24:00 -0500'
categories:
- Uncategorized
tags:
- agile
comments: []
---
<p>This is another Agile/XP practice with which I'm fairly happy; although I haven't yet seen it live up to its full potential, that potential is great enough to make me a believer.</p>
<p>Continuous Integration is a process that completely builds and tests code frequently. The "process" usually takes the form of a dedicated server running special software that continuously performs a series of tasks similar to the following:<br />(though <a href="http://www.jamesshore.com/Blog/Continuous-Integration-on-a-Dollar-a-Day.html">apparently this process can be un-automated by using a rubber chicken</a>)</p>
<p>1. Perform an update from the code repository<br />2. If changes are found, run a build (compile, test) of the latest code<br />3. a) If successful, package the latest code for deployment or b) If failure, report failure</p>
<p>Although I'm a fan of CI, it seems to be a more complicated practice than TDD. Though my experience may be tainted by bad hardware + software on which our CI depends.</p>
<p>CI requires that you maintain an automated build script. This isn't a tall order amongst Java and other compiled-language developers since projects of any moderate size need an automated build to simply compile and to separate source code from compiled code.</p>
<p>Interpreted languages are a bit different, though, in that they can usually be tested immediately upon edit. As such, automated build scripts are a bit more un-common for software written in interpreted languages. But most interpreted language software projects of any moderate size do have a consistent process for deployment, even if it's as simple as: make db changes, move files - and most interpreted languages have builders to automated this consistent process. In PHP, <a href="http://tulsaphp.net/node/70">I've been looking at Phing</a>.</p>
<p>CI is really most helpful when the build process includes a solid test suite. (Defining "solid test suite" is an exercise left to the reader.) With a solid test suite, CI can help you catch bugs earlier than usual because it typically re-runs all those tests after every check-in.</p>
<p>In addition, CI gives creates a vast sequence of clean builds similar to the "nightly builds" you hear about in open-source projects - a finalized packaged release of the project ready for deployment.</p>
<p>Finally, if you ensure that your CI platform replicates your target production platform(s), you can use it as a reliable measure of your project's production-platform readiness. This can be a double-edged sword, however - if your CI platform is different than your target production platform, it can give you false confidence of production-readiness, and even cause problems that aren't caught until later in QA or worse, actual production.</p>
<p>As with TDD, the benefits are not without drawbacks and you should weigh them for your own project before deciding if/which/how Agile practices are adopted. CI has the above benefits, but it is also a fairly complicated development platform for which engineers will be primarily responsible - it sometimes requires a good deal of time and attention to keep going. You still have to judge for yourself if it fits into your project, goals, and style.</p>
