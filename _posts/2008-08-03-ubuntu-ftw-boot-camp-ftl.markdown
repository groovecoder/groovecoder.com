---
layout: post
status: publish
published: true
title: Ubuntu FTW; Boot Camp FTL?
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 185
wordpress_url: http://groovecoder.com/2008/08/03/ubuntu-ftw-boot-camp-ftl/
date: '2008-08-03 13:16:00 -0500'
date_gmt: '2008-08-03 19:16:00 -0500'
categories:
- Uncategorized
tags: []
comments: []
---
<p>quick update on my ubuntu experience ...</p>
<p>webex went fine. linux client seamlessly downloaded and allowed me to join a webex conference. joined the teleconference via skype with just a small hiccup - took me a couple minutes of tweaking with various sound levels to get my mac's built-in mic going. but iSight camera was working with Skype straight away, so that was nice.</p>
<p>but, near the start of my first full day, I needed to investigate an IE bug, so I tried booting up into my Windows partition. epic fail. blue screen immediately upon boot. :( tried fixing my mbr via the Windows XP install CD, but no luck with that either.</p>
<p>I remembered that the <a href="https://help.ubuntu.com/community/MacBookPro#Preparing%20to%20Install%20Ubuntu%20alongside%20OS%20X%20&amp;%20Windows%20XP%20%28Triple%20Boot%29">ubuntu instructions for triple-booting</a> suggested installing GRUB on the partition with ubuntu, and I also remembered that I had missed that step. so, I decided to reset and start all over again. I booted into Mac OS (no probs there - in all of this experimentation I never once had a problem booting into Mac OS), and used disk utility to destroy both my ubuntu and windows partitions.</p>
<p>this time, I tried <a href="https://help.ubuntu.com/community/MacBookPro#Easiest%20Triple%20Boot%20%28Boot%20Camp%29">the other (easy) approach</a> and after installing Windows, I ran ubuntu installer. this time I remembered to install GRUB on the ubuntu partition, rather than defaulting to the mbr. however, when I booted up again, I had the same experience - Mac and Ubuntu would start up fine, but Windows failed to start again. :(</p>
<p>because I constantly need to test in IE every day, I sadly decided that I needed to stop with all the experimentation and just resign to using Ubuntu on my secondary computers. :(</p>
<p>it's too bad - I would love to have a triple-booting MacBook Pro, especially if I could fire up both my Windows and my Ubuntu systems inside a parallels or fusion vm.</p>
