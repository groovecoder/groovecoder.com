---
layout: post
status: publish
published: true
title: Take 5 minutes to help web developers and earn Stack Overflow rep
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 1223
wordpress_url: http://groovecoder.com/?p=1223
date: '2014-02-26 11:15:45 -0600'
date_gmt: '2014-02-26 17:15:45 -0600'
categories:
- mdn
tags: []
comments:
- id: 77712
  author: Ted Mielczarek
  author_email: ted@mielczarek.org
  author_url: http://ted.mielczarek.org/
  date: '2014-02-27 07:32:19 -0600'
  date_gmt: '2014-02-27 13:32:19 -0600'
  content: Did we change something in MDN such that we caused old links to not work,
    or is this just the result of documentation being shuffled around? Either way
    it feels like we're shooting ourselves in the foot by not keeping old links working
    by default.
- id: 77713
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2014-02-28 14:22:36 -0600'
  date_gmt: '2014-02-28 20:22:36 -0600'
  content: We do move content around. When we move pages, we leave behind re-directs.
    But many of these old links are from our MindTouch and/or MediaWiki days when
    that feature was less reliable.
---
<p><strong>Update 2014-02-28: </strong>Gareth helped me make <a href="https://docs.google.com/spreadsheet/ccc?key=0ApeHsuEebcoRdHVZZUNqYkFtTVY0UUZ4UUpGblNPZHc#gid=20">this dynamic spreadsheet</a> that auto-updates from Google Analytics every night.</p>
<h3><strong>tl;dr</strong> - go thru <a href="https://docs.google.com/a/mozilla.com/spreadsheet/ccc?key=0ApeHsuEebcoRdHVZZUNqYkFtTVY0UUZ4UUpGblNPZHc#gid=20">Today's stackoverflow MDN links to fix</a> and fix them in the StackOverflow answers.</h3>
<p><img class="aligncenter size-full wp-image-1225" alt="Stack Overflow Rep" src="/uploads/2014/02/stacko_rep.png" width="744" height="224" /></p>
<p>Helping developers is my professional and personal passion (See Exhibits <a href="https://sourceforge.net/blog/meet-the-crew-luke-crouch/">A</a>, <a href="https://blog.mozilla.org/webdev/2012/03/09/better-know-a-webdev-luke-crouch-aka-groovecoder/">B</a>, <a href="http://tulsawebdevs.org/">C</a>, and <a href="http://codefortulsa.org/">D</a>). MDN and Stack Overflow are both great resources for web developers. But <strong>following a Stack Overflow answer link to a 404 page is frustrating</strong> and dis-heartening.</p>
<p><a href="http://xkcd.com/979/"><img class="aligncenter" alt="xkcd: Wisdom of the Ancients" src="http://imgs.xkcd.com/comics/wisdom_of_the_ancients.png" width="485" height="270" /></a>I <a href="https://github.com/mozilla/kuma/pull/2042">added GA event tracking for 404's on MDN</a>. I <strong>originally wanted to help writers decide which wiki pages to prioritize</strong>, based on how many times an MDN reader clicks <em>an internal link</em> that results in a 404. But when you record metrics and analyze them, you <strong>find the unknown unknowns</strong>, and "<a href="http://leananalyticsbook.com/behind-the-scenes-of-a-book-launch/">it’s the unknown unknowns that really matter, because that’s where the magic comes from.</a>"</p>
<p>So, <strong>I learned that the vast majority of 404's on MDN are from external links</strong>. (Duh!) And <strong>the biggest single source of those are old Stack Overflow links</strong>. Luckily, Stack Overflow allows us to edit those answers to update the links to MDN. There's even a special <a href="https://stackoverflow.com/help/badges/1287/excavator">"Excavator" badge</a> for editing a post that's been inactive for 6 months.</p>
<p>So, if you've got a few minutes, you could help clean some of these links up:</p>
<ol>
<li><strong>Look thru <a href="https://docs.google.com/a/mozilla.com/spreadsheet/ccc?key=0ApeHsuEebcoRdGxTS0hMa000MjlqcFhfQ2tXYnY1TGc#gid=0">the Google Spreadsheet</a></strong>; there's a long tail of links to fix</li>
<li>Use <a href="https://developer.mozilla.org/search">our excellent new MDN search system</a> to find the right doc for the link</li>
<li>Edit the answer and earn +2 rep!</li>
</ol>
<p>Note: Sometimes we may want to create REDIRECTs for the 404 pages to help other visitors, so if you fix some links, please mention it to us on <a href="https://groups.google.com/forum/#!msg/mozilla.dev.mdn/q9VcXIb46SU/vCTG4Tb4d_MJ">this thread</a>.</p>
