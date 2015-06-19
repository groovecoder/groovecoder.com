---
layout: post
status: publish
published: true
title: Framework Performance according to Rasmus
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 191
wordpress_url: http://groovecoder.com/2008/10/23/framework-performance-according-to-rasmus/
date: '2008-10-23 11:38:00 -0500'
date_gmt: '2008-10-23 17:38:00 -0500'
categories:
- Uncategorized
tags: []
comments:
- id: 130
  author: iBspoof
  author_email: ''
  author_url: ''
  date: '2008-10-24 10:18:00 -0500'
  date_gmt: '2008-10-24 16:18:00 -0500'
  content: Ya CakePHP is slow as an elderly woman with a bad leg crossing a 6 lane
    crosswalk, but dev time is faster and with proper caching it can handle the load.  Wish
    they would do more to make it faster, but tis the life.
- id: 131
  author: Vance
  author_email: ''
  author_url: ''
  date: '2008-10-27 07:14:00 -0500'
  date_gmt: '2008-10-27 13:14:00 -0500'
  content: Nice charts - that's kinda funny that so many talks were about CakePHP
    and it's actually the slowest by far.  I've never really liked it personally,
    but it wasn't really for performance reasons.  It was mainly the fact that it
    still supports PHP4 and has some rather sloppy internal code.  Good followup post
    to OSCON. :)
---
<p>Alright, so invoking Rasmus in the title is a bit provocative, but I stumbled on <a href="http://talks.php.net/show/froscon08/">an interesting talk of his; showing performance benchmarks for a number of popular php frameworks</a>. The first portion of the talk is exactly <a href="http://talks.php.net/show/oscon08">what he presented @ OSCON</a>, but the second half looks to be raw performance numbers. It looks like there are a couple specific, but easy, performance tweaks that he granted to certain frameworks, and I like seeing the data so much I thought I could try my hand at distilling it into Google Docs charts.</p>
<p><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://4.bp.blogspot.com/_Fa_U5q7fBBY/SQC4W_KKKEI/AAAAAAAAABI/YXgaNBS3iOY/s1600-h/framework_performance_(higher_is_better).png"><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;width: 320px; height: 227px;" src="http://4.bp.blogspot.com/_Fa_U5q7fBBY/SQC4W_KKKEI/AAAAAAAAABI/YXgaNBS3iOY/s320/framework_performance_(higher_is_better).png" border="0" alt=""id="BLOGGER_PHOTO_ID_5260407069819414594" /></a></p>
<p><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://3.bp.blogspot.com/_Fa_U5q7fBBY/SQC4jP7k-cI/AAAAAAAAABQ/BN53Z--Vp30/s1600-h/framework_performance_(lower_is_better).png"><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;width: 320px; height: 227px;" src="http://3.bp.blogspot.com/_Fa_U5q7fBBY/SQC4jP7k-cI/AAAAAAAAABQ/BN53Z--Vp30/s320/framework_performance_(lower_is_better).png" border="0" alt=""id="BLOGGER_PHOTO_ID_5260407280480090562" /></a></p>
<p>It's interesting that some <a href="http://tulsaphp.net/">tulsaphp</a> guys and were recently talking about Zend had to be the slowest of all the frameworks, but apparently not so! That honor goes to CakePHP?</p>
