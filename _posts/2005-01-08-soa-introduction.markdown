---
layout: post
status: publish
published: true
title: SOA introduction
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 242
wordpress_url: http://groovecoder.com/2005/01/08/soa-introduction/
date: '2005-01-08 15:17:00 -0600'
date_gmt: '2005-01-08 21:17:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;">since SOA is basically the buzzword-de-jour, I'm glad <a href="http://www.informit.com/articles/article.asp?p=357691">this piece</a> goes into a good amount of detail as to just why SOA seems so promising to the IT industry. software vendors and enterprise IT departments all have high hopes for SOA via Web Services, but I think rightly retain a good amount of healthy skepticism in their implementation, following the .com "just sell it online" craze and the subsequent bust.</p>
<p>the article gives a good distinction between Service-Oriented and Object-Oriented design - where Object-Oriented design focuses all code around method signatures, Service-Oriented design is focused on the messages exchanged by services. I've done this in our webmethods work at Red Man. I start out designing a process by breaking down the process into the different messages that are involved. Then I create the steps of the process as services that have specific input and output messages, and then fill in the guts.</p>
<p>What it means is that a service I write for, say, creating PIDX 1.0 XML OrderCreate documents, can run for any other service that can provide it with the necessary FixedOrder documents from our own system. Input: FixedOrder documents, Output: PIDX 1.0 XML OrderCreate documents. Since these services are all exposable via WSDL, I could write a ColdFusion or a Java or PHP app that supplies FixedOrder documents and passes them via SOAP to the webmethods service, and get back PIDX 1.0 XML OrderCreate documents every single time.</p>
<p>And if something changes in the way FixedOrders are turned into PIDX orders, I change it in the single service, and all the calling services are fine, as long as the inputs/outputs remain the same. Even if the inputs/outputs change, since they are XML documents, the changes can be made in a way such that the new XML format is backwards-compatible with the old.</p>
<p>Read the introduction though, because I've been bitten by the SOA bug and I hope others will be, too.<br />
</div>
