---
layout: post
status: publish
published: true
title: Linux (open-source) &amp; Interoperability (again)
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 281
wordpress_url: http://groovecoder.com/2005/10/19/linux-open-source-interoperability-again/
date: '2005-10-19 08:02:00 -0500'
date_gmt: '2005-10-19 14:02:00 -0500'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;"><a href="http://www.silicon.com/research/specialreports/opensource/0,3800004943,39153423,00.htm">Couple</a> of <a href="http://www.silicon.com/research/specialreports/opensource/0,3800004943,39151522,00.htm">articles</a> to read to get the perspective from which I'm writing this.</p>
<p>CSP said their need was "increased integration with other criminal justice agencies," and they deduced, dear Watson, that the key to integration is "a standardised infrastructure."</p>
<p>That seems to play nicely into the first article I cited, which discusses how the usual suspects of open-source "big boys" are going to lend support to the Linux Standard Base project in an effort to "encourage the development of more applications for the Linux platform."</p>
<p>So this is all good, but what does it have to do with Web Services? I'm glad I made you ask.</p>
<p>CSP wants increased integration with other criminal justice agencies, and I'll make a few assumptions...</p>
<p>1. The other agencies they're referring to are not-Linux organizations.<br />2. They don't need to interoperate at technical low-level detail - EBCDIC vs. ASCII, Big-Endian vs. Little-Endian and the like.<br />3. The agencies are not big organizations and do not have big IT budgets.</p>
<p>Looking at everything it's NOT, we can see they're probably talking about Windows interoperability at the application level on a small-to-medium-sized budget. This is important because of <a href="http://www.sitepoint.com/blogs/2005/10/17/zend-and-ibm-to-co-develop-new-php-ide-and-framework/">this</a>.</p>
<p>One of the most alluring ways in which Microsoft is promoting .NET is that it gives developers simplified (though proprietary) framework, methodology, and libraries for developing networked applications. This is a big contrast to J2EE which is very complex, and therefore requires significant time and labor to implement. As such, although open-source, free J2EE products are all over the place, the total cost can indeed be higher than getting a .NET license and hiring one really good .NET programmer.</p>
<p>I am extremely excited about the idea of PHP Collaboration Project (<a href="http://en.wikipedia.org/wiki/Phencyclidine">PCP</a>, hah!) which "will aim to compete with Microsoft’s .NET platform..." Especially if it seeks to do so with an interoperability approach based on WS - another approach that Microsoft boasts, and developers, and businesspeople, are attracted toward.</p>
<p>However, we can probably guess what kind of "interoperability" Microsoft .NET may encourage - .NET Remoting rather than Web Services, C#.NET and ASP.NET and VB.NET apps working together, etc. Basically, Microsoft is still convinced they can own the space and lock everyone into their single platform. But that single platform is very attractive to people like CSP and other small or medium-sized orgs because it reduces complexity.</p>
<p>I would love PCP to do the same thing - reduce development complexity and cost for small to medium businesses. But at the same time, keep those business from the lock-in scenario, and maintain a standardized WS-based interoperability approach.</p>
<p>That would seem to line up with the requirements of orgs like CSP which would keep them from jumping to Windows.</div>
