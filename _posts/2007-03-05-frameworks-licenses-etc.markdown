---
layout: post
status: publish
published: true
title: frameworks, licenses, etc.
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 170
wordpress_url: http://groovecoder.com/2007/03/05/frameworks-licenses-etc/
date: '2007-03-05 21:51:00 -0600'
date_gmt: '2007-03-06 03:51:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<p>I came across this interesting and relevant blurb from <a href="http://weblog.infoworld.com/openresource/archives/2007/03/perspective_on.html">a Dave Rosenberg post on not using GPL for open source projects</a>:<br /><span class="artText"><br />
<blockquote>Spring as GPL wouldn't make a lot of sense, just like SugarCRM as Apache wouldn't make sense. (A very dumbed-down explanation being Apache is for ubiquity whereas GPL is for commercial.)</p></blockquote>
<p></span><span class="artText"></span>I'll take a stab at the fully-fleshed explanation.</p>
<p>The reason Apache is for ubiquity is because, as a permissive license, it allows the licensee to do more with the software. Most relevant, it allows the licensee to build new software on top of the licensed software - a derivative work - but close-source the new software. This makes Apache-covered (or more generally, permissively-covered) software a suitable selection for a wider audience - those that won't (or can't) return their own contributions to the community AND those that will.</p>
<p>The reason GPL can be said to be a more commercial-friendly license (from a project admin perspective) is because, as a viral license, it requires that any modifications made by anyone must be returned as open-source software as well. So a potential competitor cannot "steal" your code (it is free for use anyway), but even furthermore, they cannot improve upon your offering without returning those improvements to you as well - competitors will actually help you.</p>
<p>Now, back to frameworks. Spring, Struts, Tapestry, Google Web Toolkit, Zend Framework, CakePHP, Symfony, Ruby on Rails - all of these use permissive licenses. The reason, of course, is that frameworks are intended to build other software. And that other software won't always be open-source. But it's important for any framework to have a strong and active community in order to enhance the framework itself, so you want ubiquity and popularity over "purity".</p>
<p>If Spring, or any other framework, were licensed under the GPL, then all software built on top of the framework would also have to be GPL. I won't say that this never makes sense - it could be the framework author's intention that the framework only be used to create more free software. It wouldn't make sense if the author intends for the framework to be used in as many software projects as possible.</p>
<p>However, most of the frameworks I mentioned are licensed under Apache License, Version 2.0 (or other similar licenses), and apparently <a href="http://www.fsf.org/licensing/licenses/index_html#GPLIncompatibleLicenses">incompatible with GNU GPL</a>. This is just another GPL annoyance to me. These frameworks are clearly good free software, and have adopted a widely-used permissive license in order to foster popularity and community participation. I'm all for free software, but when I use any of these frameworks in a free software project, I'll be using a BSD license.</p>
