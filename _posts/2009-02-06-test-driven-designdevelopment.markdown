---
layout: post
status: publish
published: true
title: Test-Driven [Design|Development]
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 201
wordpress_url: http://groovecoder.com/2009/02/06/test-driven-designdevelopment/
date: '2009-02-06 16:04:00 -0600'
date_gmt: '2009-02-06 22:04:00 -0600'
categories:
- dev
tags:
- agile
comments:
- id: 133
  author: rozydesouza
  author_email: ''
  author_url: ''
  date: '2009-08-12 01:09:44 -0500'
  date_gmt: '2009-08-12 07:09:44 -0500'
  content: I have been in search of such interesting Articles, I am on a holiday its
    good to see that everyone are trying their best to keep up the Spirit by having
    such great articles posted.<br /><br />Cheers, Keep it up.<br />___________________<br
    />rozy<br /><a href="http://iwaayinternetmarketing.blogspot.com/" rel="nofollow">We
    do your Marketing for best sales</a>
---
<p>Today I learned to appreciate Test-Driven <span style="font-weight: bold;">Design</span> a little bit more. Here's the story.</p>
<p>I'm writing some RSS feeds that will contain extensions and other non-RSS elements using XML Namespaces. I'm using Zend_View and Zend_Feed and I thought the best place to put the namespace would of course be at the top of my default.rss.phtml template file - that way I can register all the namespaces at once at the top of the feed. Instead of writing the test first, I wrote the code first. Took maybe 10-20m and seems to work fine:
<pre name="code" class="xml"><br />&lt;rss content=&quot;http://purl.org/rss/1.0/modules/content/&quot; <br />doap=&quot;http://usefulinc.com/ns/doap#&quot; <br />sf=&quot;http://sf.net/api/sfelements.rdf#&quot; <br />foaf=&quot;http://xmlns.com/foaf/0.1/&quot; <br />rdf=&quot;http://www.w3.org/1999/02/22-rdf-syntax-ns#&quot; <br />version=&quot;2.0&quot;&gt;<br />....<br />&lt;/rss&gt;<br /></pre>
<p>Then I go to write the test. Lo and behold - it's a big pain in the ass to consume the feed using SimpleXML.</p>
<p>It's easy enough to create a SimpleXML element out of the feed, but I can't create SimpleXML elements from the content:encoded XML data:
<pre name="code" class="xml"><br />&lt;content:encoded&gt;<br />&lt;!--[CDATA[&lt;doap:version&gt;<br />&lt;doap:name&gt;Project 1.1 - Foobaj&lt;/doap:name&gt;<br />&lt;doap:created&gt;1202221896&lt;/doap:created&gt;<br />&lt;doap:helper&gt;<br />&lt;foaf:person&gt;<br />&lt;foaf:name&gt;admin1&lt;/foaf:name&gt;<br />&lt;foaf:homepage resource=&quot;http://lcrouch-703.sb.sf.net/users/admin1&quot;&gt;<br />&lt;foaf:mbox_sha1sum&gt;6dd817a0f71590a68131a5e83b1bd73944654e8d&lt;/foaf:mbox_sha1sum&gt;<br />&lt;/foaf:Person&gt;<br />&lt;/doap:helper&gt;<br />&lt;doap:file-release&gt;proj1.file1.tgz&lt;/doap:file-release&gt;<br />&lt;sf:download-count&gt;0&lt;/sf:download-count&gt;<br />&lt;/doap:Version&gt;]]--&gt;<br />&lt;/content:encoded&gt;<br /></pre>
<p>Because all the namespaces used in the DOAP class aren't in the content. Argh! My first thought is to screw SimpleXML and do a raw string search/parse in the test. But then I had my epiphany: "If I were an actual client of this feed, I would want to be able to parse it easily with SimpleXML or with any other XML library."</p>
<p>I ended up pushing the xml namespace declarations right down into the appropriate elements - where I now think they are *supposed* to be:
<pre name="code" class="xml"><br />&lt;content:encoded&gt;<br />&lt;!--[CDATA[&lt;doap:version <br />doap=&quot;http://usefulinc.com/ns/doap#&quot; <br />sf=&quot;http://lcrouch-703.sb.sf.net/api/sfelements.rdf#&quot;&gt;<br />&lt;doap:name&gt;Project 1.1 - Foobaj&lt;/doap:name&gt;<br />&lt;doap:created&gt;1202221896&lt;/doap:created&gt;<br />&lt;doap:helper&gt;<br />&lt;foaf:person <br />foaf=&quot;http://xmlns.com/foaf/0.1/&quot; <br />rdf=&quot;http://www.w3.org/1999/02/22-rdf-syntax-ns#&quot;&gt;<br />&lt;foaf:name&gt;admin1&lt;/foaf:name&gt;<br />&lt;foaf:homepage resource=&quot;http://lcrouch-703.sb.sf.net/users/admin1&quot;&gt;<br />&lt;foaf:mbox_sha1sum&gt;6dd817a0f71590a68131a5e83b1bd73944654e8d&lt;/foaf:mbox_sha1sum&gt;<br />&lt;/foaf:Person&gt;<br />&lt;/doap:helper&gt;<br />&lt;doap:file-release&gt;proj1.file1.tgz&lt;/doap:file-release&gt;<br />&lt;sf:download-count&gt;0&lt;/sf:download-count&gt;<br />&lt;/doap:Version&gt;]]--&gt;<br />&lt;/content:encoded&gt;<br /></pre>
<p>Voila - SimpleXML starts parsing everything very easily.</p>
<p>This is one of the biggest boons for Test-Driven Development - the effects it has on the way you <span style="font-weight:bold;">design</span> your code. If I had not tested my code as an actual client would use it, I would have produced some pretty shoddy feeds with useless XML namespacing.</p>
