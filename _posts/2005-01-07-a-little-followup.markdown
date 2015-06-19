---
layout: post
status: publish
published: true
title: a little followup
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 241
wordpress_url: http://groovecoder.com/2005/01/07/a-little-followup/
date: '2005-01-07 10:06:00 -0600'
date_gmt: '2005-01-07 16:06:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;">since I didn't see many good news items today (a couple about IBM's <a href="http://www.internetnews.com/storage/article.php/3455461">DB2 XML features</a>' and its <a href="http://www.net-security.org/vuln.php?id=3963">security vulnerabilities</a>), this may be a good time to follow up on <a href="http://lukecrouch.blogspot.com/2005/01/lots-of-good-ones.html">the previous post</a>, and conjure up some more commentary on WS & EDI.</p>
<p>I've been working for quite some time now (about 8 months) on an EDI team, that should really be, and is turning into, a B2B team. Until recently, for this group, B2B == EDI. until now, when partners are starting to request XML B2B. So when our customers started talking about XML, that's when people took notice. In researching XML, a choice had to be made to either treat XML like a fancy flat file document format and handle it the same way all of the EDI was handled, or to go 'all-out' on XML, and look at the ways it could improve upon our B2B in ways that EDI could not.</p>
<p>The most obvious benefit of XML is its conduciveness to transport over standard internet protocols like HTTP. Doing everything in XML would mean no more VAN, and no more VAN charges. At the same time, we have to now be able to handle various transports like HTTP, HTTPS, FTP, FTPS, SMTP, AS2, SOAP, etc.</p>
<p>The most obvious drawback of XML is the lack of rigid standards describing and restricting the documents into definite formats. This means that when you start claiming you can do XML, you need to make sure you're in a position to handle DTD, Schemas, Namespaces, and all the associated XML technologies that partners may use with their XML.</p>
<p>(As an amateur economist, I must say that all of the benefits and drawbacks are interchangeable...that is, they are not so much 100% positive, or 100% negative, as they are trade-offs)</p>
<p>Skipping over the details of the other technical differences between EDI and XML, I want to say something about the capabilities of XML B2B systems that EDI systems lack. While EDI messages are highly standardized, every organization we encounter has their own slight modifications they've made to the standard. When humans speak with different dialects in the same language, this is no problem, but when machines encounter any differences in their "communique," things break. So the slight modifications may as well negate whatever automated format establishment you have going with EDI.</p>
<p>XML does nothing differently, except that it embraces flexible message formats. But, with that have come the schema definition standards like DTD and XML Schema. These allow businesses to retain message format validation and definition, but stay flexible to their own messages' requirements. Now the standards are being established by vertical industry standards bodies and are more widely adopted by companies. Which just means more businesses are willing/able to get into B2B.</p>
<p>Up to now, XML B2B has been implemented for predominately the typical B2B activities that EDI handled like Procurement and Remittance thru automated delivery and processing of Invoices, Orders, etc. And I think I've noticed that the standards bodies defining the schemas for these documents are starting to head in the wrong direction. Many are attempting to create schemas for messages that are really not business documents, but more like business <span style="font-style: italic;">properties</span> involved in a B2B <span style="font-style: italic;">process</span>. The danger here is that these standards bodies will attempt to make pseudo distributed systems based solely on the request/response methodology of the more mundane B2B activities. In that sense, they would miss out on processes that could run in parallel, or as flows, or across unkown endpoints <span style="font-style: italic;">using a standardized methodology</span>. I emphasis the last part because all of that could be accomplished by coding into the app by the partners involved, but building complex, cross-industry, large-scale distributed systems would mean getting thousands of partner to agree, and that's not possible when you want to talk about detailed methods for doing business.</p>
<p>Enter Web Services. Using SOAP as a standardized communication package, and its extensions via the WS-* standards (BPEL, WS-Reliabl...), business will be able to coordinate their own processes in the way that suits them, but also expose and describe those processes (via WSDL and UDDI) to others, enabling a true architecture of internet-based, wide-scale distributed systems that will let businesses interact with one another in highly complicated business processes.</p>
<p>This is the kind of long-term effect that an XML architecture can give to an enterprise or company. Rather than just wrapping up your data in cute little '<' and '>' characters, you are given an opportunity to standardize your business processes in a way that will let you do new things with your business partners that could never be done before. It's why I'm on the XML/Web Services high.<br />
</div>
