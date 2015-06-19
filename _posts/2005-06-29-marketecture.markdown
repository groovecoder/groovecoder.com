---
layout: post
status: publish
published: true
title: '&quot;marketecture&quot;'
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 269
wordpress_url: http://groovecoder.com/2005/06/29/marketecture/
date: '2005-06-29 07:37:00 -0500'
date_gmt: '2005-06-29 13:37:00 -0500'
categories:
- Uncategorized
tags: []
comments:
- id: 169
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2005-07-19 06:59:00 -0500'
  date_gmt: '2005-07-19 12:59:00 -0500'
  content: Never thought I'd see the day.<br/><br/>>In the case of PHP 5, it mangled
    the XML markup in the header by invoking an http_encode type transformation on
    it, and it also prematurely closed the root element of the SOAP Body, in addition
    to erroneously skipping over the first of the items in the parameter array.<br/><br/>Verify
    that it's an actual error in the implementation, and not something that can be
    solved in P5 config, then let the guys know about it.<br/><br/>F/OSS isn't just
    about giving away yr code, it's also about taking a bit of time to report bugs
    in the right channels and see if others have the same problem.<br/><br/>BTW fascinating
    article on WS-Security:<br/>http://blogs.zdnet.com/BTL/?p=1597
- id: 171
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-07-19 09:32:00 -0500'
  date_gmt: '2005-07-19 15:32:00 -0500'
  content: boy, I must have really irked you with that philosophy comment, eh?<br/><br/>http://bugs.php.net/bug.php?id=33366<br/><br/>I
    did I add my vote to the bug as soon as I found the bug, and contacted the other
    people (Carlos Antunes, who originally posted) experiencing it. as far as we could
    tell, the __soapCall method did not work as documented in 5.0.2. dmitry was assigned
    to the bug and provided some good feedback in short time, then the fix was included
    with lots of other SOAP fixes/modifications in the 5.1.0 cvs code (as I predicted).<br/><br/>your
    comment seems like a reactionary jab at my open-source "loyalty." I not only provided
    feedback and input, I've also directed roughly $500 into Zend's coffers...making
    me a customer and a user that they want to keep happy, and do so quite well by
    the quick response time Dmitry offered.<br/><br/>you're right, being open-source
    opens them up to more criticism, and I tried to criticize as constructively as
    possible in the "right channel."<br/><br/>and my blog is a different channel.
- id: 172
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-07-19 09:48:00 -0500'
  date_gmt: '2005-07-19 15:48:00 -0500'
  content: I should also point out that Macromedia (a proprietary vendor) has been
    completely silent in response to my queries about their similar bug. for me, it's
    very obvious that the open-source vendor being constructively and openly criticized
    leads to results. the proprietary vendor uses your money to buy more lattes.
- id: 173
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2005-07-19 19:22:00 -0500'
  date_gmt: '2005-07-20 01:22:00 -0500'
  content: wasn't jabbing at anything .. tone must've come across wrong 'cause i was
    just saying something I assumed you already knew, but hadn't mentioned.
- id: 174
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2005-07-19 19:24:00 -0500'
  date_gmt: '2005-07-20 01:24:00 -0500'
  content: '"Never thought I''d see the day" referred to your endorsement of ReST.<br/><br/>Did
    you read the Berlind article?'
- id: 175
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-07-19 23:20:00 -0500'
  date_gmt: '2005-07-20 05:20:00 -0500'
  content: yeah. and I made a follow-up post (2 posts in 1 day!) about it...
---
<div style="text-align: justify;">I came across this term <a href="http://webservices.sys-con.com/read/104931.htm">here</a>, and found it mildly amusing. or maybe more than that, amusing enough to make a blog post about it...and you can see I haven't been doing much of that recently. even though I'm an SOA and Web Services fan-boy, I enjoy very much when people put a big wet blanket on the ideas because it keeps us zealots honest and grounded to reality.</p>
<p>Adam Bosworth from Google was probably the first to destabilize my vision of a global information marketplace using only SOAP messages. he talked about REST at the Web 2.0 conference in a discussion panel titled "<a href="http://www.itconversations.com/shows/detail329.html">The Platform Revolution</a>," and what he said really stuck with me. I don't have any quotes or minutes to look up, so listen to the entire discussion (~1 hr.).</p>
<p>essentially, Bosworth asserted that it is human imperfections that encourage innovation and creativity. and he quickly summarized what I'm about to say in more length...</p>
<p>how this relates to REST vs. SOAP is that SOAP is designed to be The Solution - created to faciliate all communication needs for every situation and in such a way as to be completely and totally independed of underlying transport, extensible beyond imagination, etc. however, that also means that SOAP is very complicated. in order to understand the 'why' of SOAP, you have to at least dabble into a large number of example scenarios of usage of each of the features of SOAP before you appreciate the inclusion of all the complexity. <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0131488740/qid=1120053015/sr=8-1/ref=pd_bbs_ur_1/102-4582237-4535300?v=glance&s=books&amp;n=507846">there are</a> (and <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0131858580/qid=1120053166/sr=1-2/ref=sr_1_2/102-4582237-4535300?v=glance&s=books">will be</a>) some <a href="http://www.amazon.com/exec/obidos/tg/detail/-/0131428985/qid=1120053137/sr=8-1/ref=sr_8_xs_ap_i1_xgl14/102-4582237-4535300?v=glance&amp;s=books&n=507846">good books</a> about it, and I've been thru some. I think I now understand most of the "why" of  the complexity of SOAP.</p>
<p>but as I've been learning, knowing the "why" of something is hardly sufficient, even less so when that something is to be used for solving real-world problems. one problem might be the need for cross-communication between system X and system Y by date D. in the purely theoretical world, absent of the date D parameter, you choose SOAP and work until you've got that loosely coupled, platform-independent, extensible solution. but since date D is important in the real world, the below example shows that perfect elegance is not always the best option, and is sometimes no option at all.</p>
<p>I've also done work with REST web services. and I must say that the simplicity and ease of REST is no small convenience. specifically, we consume our current <a href="http://www.ec.ups.com/ecommerce/solutions/c1.html">UPS web serices</a> via REST, and we will likely be expanding the number of services we implement because it was only a matter of a few hours from start to finish on implementation. by contrast, when we explored replacing our in-house, expensively maintained, sales-tax tracking system with a <a href="http://www.strikeiron.com/htmls/pws_taxdata_combined.aspx">StrikeIron web service</a>, we initially had only the WSDL, and therefore SOAP, to work with.</p>
<p>to the discredit of both ColdFusion MX and PHP 5, we found that neither includes built-in, functional support for inclusion of SOAP Headers. In the case of PHP 5, it mangled the XML markup in the header by invoking an http_encode type transformation on it, and it also prematurely closed the root element of the SOAP Body, in addition to erroneously skipping over the first of the items in the parameter array. ColdFusion MX has no support for SOAP Headers, until you download and <a href="http://www.macromedia.com/cfusion/knowledgebase/index.cfm?id=tn_18939">install an update</a>. And even then, we never were able to work with it, because it would just outright <a href="http://groups-beta.google.com/group/macromedia.coldfusion.advanced_techniques/browse_frm/thread/d06a6020cde245a2/3c645fe252ce06bb?q=lukecrouch&amp;rnum=1#3c645fe252ce06bb">fail to parse the WSDL</a> correctly.</p>
<p>however, to the credit of REST, we were able to more simply and easily work with an RPC-type interface by issuing simple HTTP GET (included in both languages) with the two arguments and receive our XML response. bliss.</p>
<p>it can be reasonably assumed that these particular faults will be corrected in future versions of the languages. indeed, it's easy to think back to the days when HTTP was the brand new, complicated transport that had numerous problems and bugs as people were still learning how to use it. but it doesn't change the fact of the matter that as of right now, before date D, REST lets us do what we need.</p>
<p>bringing it back to the idea of human imperfections...</p>
<p>most reasonable system analysts will say that the REST systems we have implemented are imperfect, and they're correct. but, because it is working right now, it enables methods of communication (however "clunky") that foster innovation in other places. ie, the business users of our system who now have more tools available to them.</p>
<p>now, I'm hardly an advocate of inelegance, and I'd love to eventually replace our REST interfaces with SOAP and WSDL interfaces, along with lots of other changes to our current systems. but as an interim measure, or a quick-and-easy solution, take a REST.</div>
