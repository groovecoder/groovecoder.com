---
layout: post
status: publish
published: true
title: Frameworks - 10 pounds of Design Patterns in a 5 pound bag (hopefully)
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 171
wordpress_url: http://groovecoder.com/2007/04/02/frameworks-10-pounds-of-design-patterns-in-a-5-pound-bag-hopefully/
date: '2007-04-02 22:31:00 -0500'
date_gmt: '2007-04-03 04:31:00 -0500'
categories:
- Uncategorized
tags: []
comments: []
---
<p>I was inspired to write this framework-related post when I read Dirk Merkel's "Practical Active Record in PHP" article from <a href="http://www.phparch.com/issue.php?mid=100">the latest issue of PHP Architect</a>. Ironically, I was inspired because the PHP framework I'm most excited about (Zend Framework) has, AFAIK, chosen to use a <a href="http://www.zendframework.com/manual/en/zend.db.table.html">Table Data Gateway</a> pattern instead of an Active Record pattern, which I think is not quite as intuitive or easy to use. But a comparison of those two patterns is not only off-topic for this post, but well beyond my analytical qualifications.</p>
<p>Instead what I'd like to point out is the fact that all good frameworks should help programmers implement good design patterns. Programmers uncomfortable or unclear about frameworks might also be uncomfortable or unclear about design patterns, but design patterns are just ways of expressing common solutions to common problems, and frameworks can help teach good patterns. The web-proven ones that come to my mind first are MVC, Front-Controller, and Active Record, but there are many many more.</p>
<p>If you want to fully grok the Active Record pattern, you should of course read code &amp; articles - like the article I mentioned above, or perhaps <a href="http://www.devshed.com/c/a/PHP/The-Active-Record-Pattern/">this article</a>, or any <a href="http://en.wikipedia.org/wiki/Active_record">other resource</a> on the subject. But, since design patterns are common solutions to common problems, you don't want to re-write Active Record code every time you use a database in your applications. Instead, once you know how the Active Record pattern works, you can look for a framework which gives you an implementation of the pattern with an interface you like.</p>
<p>This is a much better approach to learning design patterns, IMO, than to learn design patterns outside of a framework. I find that resources covering design patterns without a framework tend to be overly abstract. Pattern implementations inside frameworks tend to constrain their context to the framework's intended use. I.e., you can learn much more about MVC theory by first diving into setting up an example <a href="http://static.springframework.org/spring/docs/2.0.x/reference/mvc.html">Spring Web MVC</a> application than you can by reading <a href="http://java.sun.com/blueprints/patterns/MVC-detailed.html">an abstract MVC blueprints paper</a>.</p>
<p>When writing an application with a framework, you might get the feeling that you're dumbing yourself down - that you're relying on the framework too much and therefore becoming dependent on the way it works, or locking yourself into an architecture you don't fully grok and therefore can't fully debug. While that's entirely possible, it's more likely that, given the framework is reputable and has a solid architecture, you're actually relying upon good implementations of well-proven design patterns, and learning all about them in the process. This is not only good for your application, it's good for you as a programmer.</p>
