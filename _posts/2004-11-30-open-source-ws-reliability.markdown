---
layout: post
status: publish
published: true
title: open source WS-Reliability
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 224
wordpress_url: http://groovecoder.com/2004/11/30/open-source-ws-reliability/
date: '2004-11-30 10:37:00 -0600'
date_gmt: '2004-11-30 16:37:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;"><a href="http://www.cbronline.com/article_news.asp?guid=36E2475C-CE8F-4305-8B87-02D4E6125A53">you gotta love Japan</a>. the WS-Reliability specification is one of those competing specifications I've been talking about lately. it competes directly with WS-ReliableMessaging developed by IBM and MS. WS-Reliability has been accepted by OASIS, which I usually trust...but none of these advanced 2G WS standards have been accepted by W3C, which I would consider THE standards body.</p>
<p>anyway, the open-source part of <a href="http://www.computerworld.com.au/index.php/id;574904090;fp;16;fpid;0">this article</a> is the link to <a href="http://businessgrid.ipa.go.jp/rm4gs/index-en.html">RM4GS</a>, which is an open-source Java implementation of WS-Reliability, developed by the same companies that drafted the WS-Reliability specification. a thought that has been recurring in my mind is that open-source Web Services software may just be a bit redundant, or as <a href="http://lukecrouch.blogspot.com/2004/11/this-somewhat-old-article-makes-great.html">I said before</a>, the benefits of open-source and Web Services are not complimentary, but are mutually exclusive.</p>
<p>WS-Reliability is very useful to potentially everyone, regardless of programming language, because it enables distributed computing systems to be built using internet-based architecture. that's a fancy way of saying that a software program could potentially utilize any other software program on the internet.</p>
<p>RM4GS is very useful to a few people - Java programmers making web services that need reliable messaging. Java itself already has JMX, but RM4GS allows your Java program to reliably communicate with a .NET service and others.</p>
<p>But it's important to note that the .NET service will make no use of RM4GS. It will have to have<span style="font-style: italic;"> its own implementation of WS-Reliability</span>. and if the .NET service will interface with other services that do WS-ReliableMessaging, or some other standard that pops up, these advanced Web Services are starting to lose their shine of being a totally standardized, internet-based, written-once interactive systems. we will be back to having many different interfaces, and needing to code for each interface.</p>
<p>on the plus side, it means that programmers who understand the interfaces can pull in the dough, so that's good.<br />
</div>
