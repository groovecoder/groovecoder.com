---
layout: post
status: publish
published: true
title: Tarak Modi wants you to KISS your web services
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 247
wordpress_url: http://groovecoder.com/2005/01/19/tarak-modi-wants-you-to-kiss-your-web-services/
date: '2005-01-19 16:08:00 -0600'
date_gmt: '2005-01-19 22:08:00 -0600'
categories:
- Uncategorized
tags: []
comments:
- id: 156
  author: Tarak Modi
  author_email: ''
  author_url: ''
  date: '2005-01-20 07:20:00 -0600'
  date_gmt: '2005-01-20 13:20:00 -0600'
  content: 'Luke, thanks for your positive comments. <br /><br />I definitely did
    not intend to promote the notion that most WS-* specifications are to be ignored.
    That would be irresponsible of me. And you are correct that a lot of the specifications
    can be used for creating robust distributed systems around Web Services, which
    is why they were created. That is also reason #1 in my article "KISS your Web
    Services". But at the same time not all distributed systems require all of the
    WS-* specifications either. For example, I just rolled off a large project that
    makes heavy use of Web Services in a distributed environment using only basic
    SOAP and WSDL. Of course a lot of design went into the effort (this is key). Security
    and identity info was conveyed thru SOAP headers. I could have used WS-Security,
    but the complexity was not justified for various reasons. Finally, until a core
    set of second generation Web Services specifications are univerally accepted/ratified,
    it''s hard to create systems that will support all possible candidates. So use
    what you need now and leave the future where it should be... in the future.'
- id: 157
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-01-20 10:54:00 -0600'
  date_gmt: '2005-01-20 16:54:00 -0600'
  content: Thanks for coming by, Tarak!<br /><br />The only web services I've done
    have just used basic SOAP and WSDL as well, though I haven't done any mission-critical
    web services projects yet. I think one of the best reasons for NOT going with
    WS-Security or another WS-* standard is indeed the fact that none of the 2nd-generation
    WS specifications are universally accepted.<br /><br />I hope in the near future
    I will be needing some kind of security or other feature so I can seriously look
    at the standards in comparison to a real-world project need. I'll have a much
    better perspective as to the pros and cons of the standard, and a better way to
    look at how WS-I is trying to fix the confusion.<br /><br />Thanks again for stopping
    by.
---
<div style="text-align: justify;"><a href="http://www.teknirvana.com/">Tarak Modi</a> is becoming a favorite of mine. he seems a very astute and pragmatic observer of the WS landscape. his most recent <a href="http://www.javaworld.com/weblogs/javadesign/index.html">blog</a> <a href="http://www.javaworld.com/weblogs/javadesign/archives/000319.html">entry</a> is a good follow up to his <a href="http://www.javaworld.com/weblogs/javadesign/archives/000316.html">previous one</a>, in which he talked about the confusion around the WS-* specifications. in this one, he links to an article he wrote that talks about the reasons for the explosion in standards/specifications.</p>
<p>I agree 100% with his analysis. reading it also encouraged me to pay more attention to <a href="http://www.ws-i.org/">WS-I</a> as its <a href="http://www.ws-i.org/Profiles/BasicProfile-1.0-2004-04-16.html">profile</a>s could evolve into the guiding standards for the 2nd generation WS specifications, like <a href="http://www.w3.org/">W3C</a> is for the <a href="http://www.w3.org/2002/ws/">1st generation</a>.</p>
<p>I know Tarak would agree that although the WS-* standards are confusing, but are, in fact, manageable.  I <span style="font-style: italic;">assume</span> he would also agree that these standards are, in fact, required for <span style="font-style: italic;">some</span> distributed systems. and I do agree with him that keeping Web Services applications as simple as possible is the best way to avoid the confusion and complexity of WS-*. But I would also caution that ignoring a WS-* standard that performs a function you need could mean trouble down the road if/when a large number of other systems are built around the standard, and you'll have to play catch-up to be able to work with them.<br />
</div>
