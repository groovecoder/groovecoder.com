---
layout: post
status: publish
published: true
title: Virtual Machines and Real Humans
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 688
wordpress_url: http://groovecoder.com/?p=688
date: '2011-10-11 16:28:19 -0500'
date_gmt: '2011-10-11 21:28:19 -0500'
categories:
- dev
- community
tags:
- mozilla
- community
comments:
- id: 954
  author: Buddy Lindsey
  author_email: percent20@gmail.com
  author_url: http://buddylindsey.com
  date: '2011-10-11 20:40:55 -0500'
  date_gmt: '2011-10-12 02:40:55 -0500'
  content: "Great post and breakdown. Also I wouldn't say I was an exception on the
    commitment level. I just hate having problems I can't solve, especially when it
    is something as \"trivial\" as setting up an application, I call it stubbornness.
    \r\n\r\nI have mentioned to you I think in the long run it might be time better
    spent to spend a few minutes every so often to make sure installation instructions
    still work over spending hours and hours and hours getting some automated VM up
    and running. The risk reward scenario, as you point out, is just too high and
    time consuming. \r\n\r\nAlso, as you point out in another post, getting started
    is easier on potential devs, after initial setup, when it is local. I have kuma
    installed locally and not in a VM so all I have to do is cd my terminal over and
    I am ready to start testing. However, if i was using a VM i would have to boot
    it up and spend a lot of time waiting just to get started. By the time I am ready
    to start coding I might be out of motivation to start.\r\n\r\nIt is a fun discussion
    to say the least. Community contribution and interaction has always been an interesting
    subject to discuss and problem to crack. I am curios to see how well Mozilla can
    crack this particular nut."
- id: 960
  author: David Boswell
  author_email: dboswell@mozilla.com
  author_url: http://davidwboswell.wordpress.com/
  date: '2011-10-12 14:05:03 -0500'
  date_gmt: '2011-10-12 20:05:03 -0500'
  content: "Great post.  Very interesting to hear how you helped Buddy get started
    and then to see what he went on to do once he got familiar with things.\r\n\r\nI
    also like this line:\r\n\r\n\"Of course, we can't spend all our time recruiting
    and mentoring community developers to do our work for us.\"\r\n\r\nI think we
    can find a good balance between doing everything ourselves and spending all of
    our time mentoring.\r\n\r\nWithout having a good balance, it seems pretty clear
    that it can be very hard for new people to get involved.  \r\n\r\nAs you point
    out above, there are few webdev contributors that aren't employees, but we have
    a lot of web developers expressing interest in getting involved.  Mentoring seems
    to be one way to fix this disconnect.\r\n\r\nThe trick with mentoring seems to
    be how to use the time available in the best possible way.  It wouldn't scale
    to try to mentor everyone who expressed interest so who do you mentor, what are
    good projects to start with...\r\n\r\nDavid"
- id: 961
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2011-10-12 14:20:39 -0500'
  date_gmt: '2011-10-12 20:20:39 -0500'
  content: David, you have a lot more history in Mozilla than I do - do the other
    product areas of Mozilla (Firefox, Thunderbird, etc.) have full-time mentor types?
    I.e., someone whose full-time paid job is to ramp community contributors onto
    Mozilla projects?
- id: 963
  author: David Boswell
  author_email: dboswell@mozilla.com
  author_url: http://davidwboswell.wordpress.com/
  date: '2011-10-12 15:41:20 -0500'
  date_gmt: '2011-10-12 21:41:20 -0500'
  content: "There haven't been many people who have had bringing community members
    into Mozilla as their full-time job, although that's started to change recently.
    \ For instance, SUMO now has a community manager role.\r\n\r\nAs Mozilla grows
    and problems with scaling become even harder to deal with, I think it definitely
    makes sense to make sure each team has someone with this role (or several people
    who share the role)."
---
<h3>Encouraging contributors to open source website development</h3>
<p>Mozilla, like any good open source project, is a community. 25% of contributions to Mozilla Core, Firefox, Thunderbird, and other products come from the community rather than employees. We, i.e. Mozilla Webdev, <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=688911">want more community web developers to contribute to Mozilla websites</a>. Here are community contribution stats for some Mozilla websites:</p>
<ul>
<li>SUMO<br />
github: <a href="https://github.com/jsocol/kitsune">kitsune</a><br />
ADV*: 357k<br />
community contributors: <a href="https://github.com/api/v2/json/repos/show/jsocol/kitsune/contributors">0</a>†</li>
<li>AMO<br />
github: <a href="https://github.com/jbalogh/zamboni">zamboni</a><br />
ADV*: 736k<br />
community contributors: <a href="https://github.com/api/v2/json/repos/show/jbalogh/zamboni/contributors">3-4</a>†</li>
<li>Socorro<br />
github: <a href="https://github.com/mozilla/socorro">socorro</a><br />
ADV*: ?<br />
community contributors: <a href="https://github.com/api/v2/json/repos/show/mozilla/socorro/contributors">1-2</a>†</li>
<li>MDN<br />
github: <a href="https://github.com/mozilla/kuma">kuma</a><br />
ADV*: 56k<br />
community contributors: <a href="https://github.com/api/v2/json/repos/show/mozilla/kuma/contributors">4</a></li>
</ul>
<p>* Average Daily Visitors<br />
† Guesstimated figures - looked at commit logs and our LDAP phonebook; open to corrections</p>
<p><a href="https://twitter.com/#!/tofumatt">tofumatt</a> wrote a good post about how we're starting to <a href="https://blog.mozilla.com/webdev/2011/10/04/developing-with-vagrant-puppet-and-playdoh/">use vagrant and puppet to give developers easier access to working on Mozilla Webdev sites</a>. <a href="https://twitter.com/lmorchard">lmorchard</a> has a passion for this idea, and he's been extremely patient with all my troubles and questions about Vagrant and Puppet as I've tried to jump on the bandwagon of <a href="http://decafbad.com/blog/2011/10/02/putting-clouds-in-boxes">putting clouds in boxes</a>. I don't want to discredit their work and opinions, but let me offer my own.</p>
<h3>I am slow and make mistakes</h3>
<p><a href="http://groovecoder.com/wp-content/uploads/2011/10/mistakes.png"><img class="size-full wp-image-699 alignleft" title="mistakes" src="http://groovecoder.com/wp-content/uploads/2011/10/mistakes.png" alt="mistakes" width="250" height="217" /></a></p>
<blockquote><p>Instructions for humans are nowhere near as good as instructions for computers. Humans make mistakes, misunderstand, and are generally not as fast as computers when doing this kind of thing.<br />
- tofumatt</p></blockquote>
<p>Amen to that. If you read <a href="http://pastebin.mozilla.org/1348346">some choice excerpts from our #mdn chat log</a>, you'll see how slow I am (and how patient lmorchard is) re: vagrant. Even though I'm slow, I presumably have more "sysadmin" experience than the oft-cited hypothetical design contributor just trying to make a CSS fix, and yet vagrant and puppet make me cringe. So far, vagrant and puppet have only introduced MORE setup pain - and not the regular MySQL setup pain that I (and yes, even designers) have done dozens of times already.</p>
<h3>Making boxes put boxes into clouds for your boxes</h3>
<p><img class="alignright" title="Clouds and Boxes" src="http://farm3.static.flickr.com/2368/1608136608_7572c04f8c.jpg" alt="Clouds and Boxes" width="300" height="200" /></p>
<blockquote><p>I've also started playing with Puppet by itself, to build plain-vanilla VM appliances and to spin up cloud servers on Amazon EC2 and Rackspace Cloud Servers. It's going pretty well, and it's conceivable we could do without Vagrant to script the build of downloadable VM appliances and to spin up disposable cloud servers.<br />
- lmorchard</p></blockquote>
<p>lmorchard is spot on - maybe because he's tired of dragging my slow brain thru vagrant and puppet. Our CI machine should generate vm images with 1-button deploy to Rackspace or Amazon. I think this idea of using VM's to encourage community contribution to website projects is an all-or-nothing deal. If it doesn't work 100%, it's worse than failure. If a community contributor runs into problems with vagrant or puppet, it's much worse than if they run into problems with MySQL or pip. At least there's a bunch of established resources to debug MySQL - I couldn't find much debugging resources for vagrant, besides lmorchard.</p>
<p>At <a title="['Tulsa %s' % e for e in ('Tech Fest', 'Hackathon')]" href="http://sf.net">SourceForge</a> we had this kind of "ideal" setup for years. The Service Operations Group at SourceForge maintains sandbox servers with an admin dashboard for <a href="http://screencast.com/t/QbBnvIJuC">creating</a>, <a href="http://screencast.com/t/K3XR8iXzM">managing, and destroying</a> per-developer sandbox vm's that run instances of SourceForge.net. (Though sadly <a href="https://ctrl.sb.sf.net/sandboxctrl/">it's behind corporate LDAP</a> - only given to employees) I don't know if/how that model could scale from a single site to dozens of sites all with different moving parts. And there are big latency issues developing on a remote vm. Still, it's exactly what we would want for that elusive CSS designer who wants to fix Mozilla sites without setting one up. She clicks "Create MDN Sandbox" and gets an email containing the domain and access credentials to start editing code on her sandbox. Beautiful.</p>
<h3>The virtual machine is us</h3>
<p><object width="420" height="315"><param name="movie" value="http://www.youtube.com/v/NLlGopyXT_g?version=3&amp;hl=en_US" /><param name="allowFullScreen" value="true" /><param name="allowscriptaccess" value="always" /><embed type="application/x-shockwave-flash" width="420" height="315" src="http://www.youtube.com/v/NLlGopyXT_g?version=3&amp;hl=en_US" allowscriptaccess="always" allowfullscreen="true"></embed></object></p>
<blockquote><p>The web is no longer just linking information ... the web is linking <strong>people</strong>. People sharing, trading, and collaborating.</p></blockquote>
<p>In all this technology, we sometimes lose track of the people. I don't want to abandon the idea of using virtual machines to encourage community contribution; the SourceForge sandbox model is, for me, the ideal system for enabling easy contributions from casual community developers. I'll join work for something similar at Mozilla.</p>
<p>I do want to highlight an additional on-ramp for getting community developers involved with Mozilla websites - Mozilla webdev's should get involved with our developer communities!</p>
<p>A couple weeks ago at our Tulsa Web Devs coworking day, <a href="https://twitter.com/#!/buddylindsey">Buddy</a> and I were talking about Mozilla and he asked how he can get a job at Mozilla. I said Mozilla really likes looking at your open-source code, and also likes hiring community contributors. He asked how he should become a contributor. The easy answer is go to the <a href="https://www.mozilla.org/contribute/">Get Involved with Mozilla</a> page, but since I was working on MDN that moment, I showed him <a href="https://github.com/mozilla/kuma">the kuma repository</a> I was working on. He forked it and went thru the "menial and often fragile setup" in our <a href="https://github.com/mozilla/kuma/blob/master/docs/installation.rst">installation.rst</a>; I fielded his questions as he went.</p>
<p>It was incredibly valuable - he filed <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=689001">a kuma setup and installation bug</a> and <a href="https://github.com/buddylindsey/kuma/commits/master/">made the appropriate fixes</a>. Then he went on to fix an <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=690399">easy 1-liner bug</a>, and got comfortable enough to do a significant bug <a href="https://github.com/buddylindsey/kuma/commit/c70b079108bf1023aa9ab380b0f46d9015dff7f6">involving cron, urllib, and json</a> to <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=681124">generate a humans.txt file for MDN</a> - which <a href="https://developer.mozilla.org/humans.txt">now includes him</a> as a community contributor!</p>
<p><img class="aligncenter" title="Shut up and take my code" src="http://blog.mozilla.com/webdev/files/2011/10/shut-up-and-take-my-code-300x168.jpg" alt="" width="300" height="168" />Of course, we can't spend all our time recruiting and mentoring community developers to do our work for us. [Or can we? ;) ] And Buddy is an exception in his level of commitment to contribute. So, yes we should reach out to those developers looking to make a casual CSS fix without wanting to set up a whole website environment (though <a href="https://github.com/mozilla/kuma/commit/99434cd1c2ad79a01fe674ddfbd35d234b4fb53b">we've received those 1-line CSS commits into MDN</a> even without vm's). That's a good reason to pursue turn-key VM's.</p>
<p>But if you're at a conference or an event and someone asks you how to get involved with or fix a bug on Mozilla websites, don't just send them to a page or a virtual machine - pull up a chair and work with the real human sitting next to you.</p>
