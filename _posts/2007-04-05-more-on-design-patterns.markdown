---
layout: post
status: publish
published: true
title: More on design patterns
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 172
wordpress_url: http://groovecoder.com/2007/04/05/more-on-design-patterns/
date: '2007-04-05 12:01:00 -0500'
date_gmt: '2007-04-05 18:01:00 -0500'
categories:
- Uncategorized
tags: []
comments: []
---
<p>Design patterns in the context of frameworks is a nice opportunity for me to take a break from my framework posts. I've been reading a bit on design patterns as a result of that previous post, and <a href="http://tech.groups.yahoo.com/group/tulsaphp/surveys?id=2474898">the poll activity on the Tulsa PHP Users Group</a>.</p>
<p>In my readings, I came across <a href="http://www.loudthinking.com/arc/000485.html">this old post from the Loud Thinking blog re: Patterns & Practices over languages</a>. Good stuff, and I'll recall my related personal experience.</p>
<p>Before joining SourceForge, I was <span style="font-style: italic;">okay</span> in a few languages - Java, ColdFusion, WebMethods (<span style="font-style: italic;">shudder</span>), Javascript, SQL, XSL/XPATH - and I was <span style="font-style: italic;">pretty good</span> in one language - PHP. The first couple months at SourceForge were simply LOTS of PHP with a bit more architecture than I was used to - caching, entity objects, a Smarty view layer - but not much different than the PHP coding I had always done.</p>
<p>I was exposed to a pretty sophisticated Java architecture when I joined the Marketplace engineering team. But, my main task initially was to build a few simple wrapper classes that would allow our PHP scripts to communicate with the Java backend over <a href="http://stomp.codehaus.org/">STOMP</a> to a message queue system (ActiveMQ, specifically). This would let us continue to write simple (display-oriented) PHP scripts which relied on the sophisticated Java backend for most logic. I still like that idea, and think it can work well if given proper time and attention.</p>
<p>But as we faced mounting time constraint pressure, and in the interest of leveraging our available talent pool, we stepped away from using STOMP and took out most of the PHP code - save for a proxy-type controller which speaks to the Java app server and some helper classes. We started using the Web MVC module of the Spring framework (in addition to the Core, Testing, Transaction, and Hibernate modules we were already using), and were therefore implementing everything, including display via JSP, in Java. So I poured over <a href="http://static.springframework.org/spring/docs/2.0.x/reference/index.html">Spring reference material</a>. (<a href="http://www.amazon.com/Spring-Action-Craig-Walls/dp/1932394354/ref=pd_bbs_2/002-1640040-5981604?ie=UTF8&s=books&amp;qid=1175816990&sr=8-2">Highly recommended book</a>)</p>
<p>It was quite a (beneficial) learning experience for me. As I learned (and accepted) the Spring approach, I found that I started to care less and less about Java - it just happened to be the language in which Spring is written - and I cared more and more about the <em>ways</em> in which Spring worked.</p>
<p>Those "ways" are, of course, design patterns. Inversion of Control, Object-Relational Mapping and Active Record, MVC, Front Controller, Command Controllers ... these are all just "ways" of doing certain things, solving certain problems, that are common to many systems. As I said, in learning Spring, I'm appreciating these patterns more than the Java language.</p>
<p>This is what lessened my resistance to frameworks, so much so that I became a fan of (some of) them! But, still having fondness for PHP, I started looking for PHP frameworks which work in the same <em>ways</em> that Spring does. But, it has really changed my perspective from analyzing languages based on syntax, (or types, or whatever) to analyzing languages based on the availability of design pattern implementations.</p>
<p>In this respect, and from my searching, I still think (though it may still be simple bias) that PHP is the best language available for the web. There are <a href="http://www.mustap.com/phpzone_post_73_top-10-php-mvc-frameworks">many PHP MVC frameworks</a> (look at all the ones in the comments as well) which implement nearly all the best proven design patterns for the web. There's enough choice out there that PHP engineers can choose not only the design patterns to use, but also between many different <em>styles</em> of each design pattern. And of course, because PHP is so easy, it doesn't take an "architect" to craft their own style implementation of a favorite design pattern. (like <a href="http://www.phparch.com/issue.php?mid=100">the Active Record implementation</a> I referenced in my last post.)</p>
<p>It was a big step for me to stop focusing on certain languages and instead focus on design patterns. I think it's been a big step upwards in my engineering aptitude/skill/whatever. And the more design patterns I learn, the more I realize there are so many others I <span style="font-style: italic;">don't</span> know that could make my programming even easier. Sadly, I'm nowhere near the competence needed to recognize the "informal patterns" (i.e., unnecessary repetition/duplication) in my own code, but hopefully I'll get there.</p>
<p>For now, I'm still just learning my way into the topic and very glad I have an opportunity to do so.</p>
