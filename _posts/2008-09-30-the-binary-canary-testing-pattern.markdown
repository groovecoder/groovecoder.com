---
layout: post
status: publish
published: true
title: the binary canary testing pattern
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 189
wordpress_url: http://groovecoder.com/2008/09/30/the-binary-canary-testing-pattern/
date: '2008-09-30 17:06:00 -0500'
date_gmt: '2008-09-30 22:06:00 -0500'
categories:
- Uncategorized
tags:
- php
- agile
- sourceforge
comments: []
---
<p><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://4.bp.blogspot.com/_Fa_U5q7fBBY/SOKz6Lj7UTI/AAAAAAAAABA/BOQGrVtVFic/s1600-h/canary_coal_mine_0.gif"><img style="cursor:pointer; cursor:hand;" src="http://4.bp.blogspot.com/_Fa_U5q7fBBY/SOKz6Lj7UTI/AAAAAAAAABA/BOQGrVtVFic/s320/canary_coal_mine_0.gif" border="0" alt=""id="BLOGGER_PHOTO_ID_5251957927584682290" /></a></p>
<p>I think I just invented a new testing pattern - The Binary Canary.</p>
<p>Basically, I was grouping my PHPUnit tests into a test suite and I realized that my TestCase super-classes were "failing" because they had no tests in them. Obviously this is intentional - only the specific sub-classes would have tests.</p>
<p>I guess I could have made the TestCase super-classes abstract, but instead I added this to the highest-level TestCase class:
<pre><br />/*<br /> * global test plumbing here<br /> */<br />class Sfx_TestCase extends PHPUnit_Framework_TestCase<br />{<br /> public function setUp()<br /> {<br />  // more global test plumbing here<br /> }<br /> public function test_Binary_Canary()<br /> {<br />  $this->assertEquals(<br />         "Binary Canary says test plumbing is working.", <br />         "Binary Canary says test plumbing is working."<br />        );<br /> }<br />}<br /></pre>
<p>My little binary canary serves two purposes:
<ol>
<li>It adds an "always-pass" test to each of my TestCase classes so they don't throw up any more PHPUnit warnings.</li>
<p>
<li>Because my TestCase classes set up context-specific test plumbing, the binary canary test inherited by each of them now alerts me if I screw up any of my test plumbing - and tells me the specific area.</li>
<p></ol>
<p>For example:
<pre><br />class Sfx_Db_TestCase extends Sfx_TestCase<br />{<br /> public function setUp()<br /> {<br />  parent::setUp();<br />  // Db-specific test plumbing<br /> }<br />}<br /></pre>
<p>And:
<pre><br />class Sfx_Controller_TestCase extends Sfx_TestCase<br />{<br /> public function setUp()<br /> {<br />  parent::setUp();<br />  // Controller-specific test plumbing<br /> }<br />}<br /></pre>
<p>Just like the coal-miner canaries of old, this mechanism gives me a simple yes/no signal as to whether or not my test plumbing will soon kill me, <strong>and</strong> which plumbing code is the culprit.</p>
