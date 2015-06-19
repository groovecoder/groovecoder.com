---
layout: post
status: publish
published: true
title: closing [loopholes|business models] in OS licenses
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 161
wordpress_url: http://groovecoder.com/2006/10/13/closing-loopholesbusiness-models-in-os-licenses/
date: '2006-10-13 13:07:00 -0500'
date_gmt: '2006-10-13 19:07:00 -0500'
categories:
- Uncategorized
tags: []
comments:
- id: 114
  author: Crosbie Fitch
  author_email: ''
  author_url: ''
  date: '2006-10-17 07:48:00 -0500'
  date_gmt: '2006-10-17 13:48:00 -0500'
  content: It all results from a misunderstanding over whether freedoms taken away
    by copyright are being restored, or whether a quid pro quo is being enforced in
    support of a misperception that this is the objective of the GPL.<br/><br/>It's
    freedom versus gift economy.<br/><br/>If you removed just the SaaS clause, the
    GPLv3 is 100% freedom based.<br/><br/>The APL, and now HPL, are gift economy licenses  (you
    can't modify our stuff unless you publish your mods). Unfortunately, the EUPL
    has jumped on the gift economy bandwagon and the concept of privacy violation
    has whizzed over its head.
- id: 115
  author: luke
  author_email: ''
  author_url: ''
  date: '2006-10-19 22:43:00 -0500'
  date_gmt: '2006-10-20 04:43:00 -0500'
  content: I'm not so sure I'd say that GPLv3 - SaaS clause = 100% freedom. Like I
    said, I have a freedom problem with GPLv2 in that it would REQUIRE me to REQUIRE
    my users to distribute THEIR enhancements under GPLv2...that's a couple of requirements
    (non-freedoms) and it stretches beyond even me to my users!?<br/><br/>I agree
    it's unfortunate that there's Yet Another Gift-Economy-License (YAGEL), but I
    think I'd modify the relationship of "freedom vs. gift economy" ...<br/><br/>I'd
    say it's more like freedom OVER gift economy. Because the two concepts are not
    necessarily mutually exclusive - a voluntary gift economy is possible. However,
    what's not possible is to ENFORCE a "free" gift economy - the very act of enforcement
    makes it unfree.<br/><br/>Thanks for coming by and for the great comment.
- id: 116
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2006-11-14 10:18:00 -0600'
  date_gmt: '2006-11-14 16:18:00 -0600'
  content: 'Meh. I don''t get it. If you''re uncomfortale ever placing restrictions
    on recipients of yr code, just public-domain it all and be done with it. This
    is what I think when you say "the very act of enforcement makes it unfree"<br/><br/>You
    indicate acceptance of GPL (whatever version) by distributing the software licensed
    thereunder. Nothing else gives you the right to distribute this software, which
    you did not write. That''s because of the copyright laws, not the GPL.<br/><br/>Of
    course the GPL is not freedom. The GPL is a device meant to preserve freedoms.
    Maybe it sucks at that; maybe it rules. That''s a debate worth having.<br/><br/>Thought
    experiment: if software were not copyrightable, and therefore distributable by
    all without restriction. would the FSF be mad, sad, or glad?<br/><br/>I think
    you would find that free-software developers would love it if they didn''t have
    to leverage copyright law to preserve their users'' freedoms.'
---
<p>I started out by reading  <a href="http://weblog.infoworld.com/openresource/archives/2006/10/the_eupl_a_lice.html">Matt Asay's take on the EUPL</a>. And I read just about every article or post to which he linked. Asay says that the GPL, for better or worse, "leaks like a sieve." I can only conclude from his statement, "I really like the way it [EUPL] closes the ASP loophole without closing off everything else, as well" that Matt dislikes at least the ASP "loophole" in the GPL.</p>
<p>(Disclosure: As an employee of SourceForge.net, I am dependent on an ASP model, like Google's or Yahoo's, for my livelihood.)</p>
<p>But I'd fall into the camp which thinks the "leakiness" of the GPL is a positive rather than a negative. In fact, I think even the GPLv2 is a bit too strict for my liking. As I understand it, when you distribute (old-school) any software which you received under a GPLv2 license, <span style="font-style: italic;">you must </span>license your own modifications under GPLv2. Emphasis added to stress this point - any mechanism that sets up a "you must _____" condition places an inhibition on the recipient, not a freedom.</p>
<p>Apparently, the HPL, EUPL, and GPLv3 take this same inhibition and make it even more invasive. Under these, when you "communicate" (new-school) any software which you received, <span style="font-style: italic;">you must</span> license all of your own modifications under the same license. The "communicate" term is defined in every license (or an equivalent principle is established) to prevent a person or corporation from using such licensed software to distrubte services (<a href="http://en.wikipedia.org/wiki/Software_as_a_Service">SaaS</a>) without releasing all their own modifications or enhancements to the software.</p>
<p>I'm fine with these kinds of licenses, I suppose. I just don't happen to share this kind of perspective - feeling betrayed or cheated if someone enhances my software but doesn't give their stuff back to me. IMO, <span style="font-style: italic;">their</span> work and labor went into those enhancements so I'm fine with them licensing <span style="font-style: italic;">their</span> stuff however they want. I rest easy knowing <a href="http://sourceforge.net/projects/ajaxmytop">my stuff</a> will always be LGPL and (theoretically) usable by anyone. I'll admit this a pretty individualistic perspective. But then isn't the open-source community just made up of individuals. Why do we need someone like the EU or FSF to tell us how to feel, or what's best for ourselves?</p>
<p>I think the majority of people in the open-source community don't mind that Google and Yahoo (and SourceForge) modify some open-source software but don't distribute all those modifications when they "communicate" that software via their SaaS websites. Combine that with the fact that some of these extra-invasively-viral(?) licenses prevent other business models besides just the ASP one, and I can't imagine these licenses will be very popular. (Indeed, GPLv3 has already been ranted upon by more than a couple open-source supporters.)</p>
