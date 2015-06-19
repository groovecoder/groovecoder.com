---
layout: post
status: publish
published: true
title: an open source challenge
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 255
wordpress_url: http://groovecoder.com/2005/02/08/an-open-source-challenge/
date: '2005-02-08 16:42:00 -0600'
date_gmt: '2005-02-08 22:42:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;">I know there are plenty of challenges that open-source, as a community and development model, has come up against, and consistently met and surpassed...but, I think another big one is upon us, and I just don't see enough attention being paid to it.</p>
<p>it's very related to the same things I've been writing about for a few days now - <a href="http://www.microsoft.com/mscorp/execmail/2005/02-03interoperability.asp">the interoperability gauntlet that Gates threw down</a>. although Microsoft spin will always over-hype whatever agenda it's intending to promote, I think the interoperability issue is enormous because we're going to see many large-scale, distributed systems and processes emerging over the next few years, now that internet connectivity is ubiquitous, and Web Services foundations are really solidifying.</p>
<p>more <a href="http://informationweek.com/story/showArticle.jhtml?articleID=59301879">PR</a> and <a href="http://www.businessweek.com/technology/content/feb2005/tc2005028_4104_tc203.htm">hype</a> from MS doesn't mean that I'm a big Microsoft supporter...I'm only using their material because I can't seem to <a href="http://www.google.com/alerts">get news</a> from the open-source vendors or community.</p>
<p>Microsoft's strategy here is very, very good. people rightly criticize them for FUD tactics, bad security, and loss of committment to developers, but their interoperability <span style="font-style: italic;">message</span> is right on. whether or not they will deliver is still up in the air - even if their track record indicates they won't, they appear to have fully grasped the importance of interoperability in this Web Services era of programming, and have more than enough resources to make it happen.</p>
<p>the <a href="http://msdn.microsoft.com/msdnmag/issues/05/02/ExcelWebServices/default.aspx">Web Services features of MS Office 2003</a> is a prime example. the example is to have an Excel spreadsheet, which business users are very comfortable with using, act as a client application to live data provided by a Web Service. we go thru a process of creating Excel .xls files from different reports all the time here, and it's a very "hacky" process, so that we have to write a lot of custom ColdFusion code for things like formatting and calculated values being put into different cells and such.</p>
<p>but the Web Service approach means some extra work in designing the front-end spreadsheet, but it will use a generic Web Service that feeds that data not only to that spreadsheet, but also to a web report, or another service or program, or a fat client, or a batch script, etc.</p>
<p>back to Excel...most of our users in other departments can work their way around an MS spreadsheet pretty well, and are able to do vlookups and the like to create reports and do calculations that they need. right now, we have to deliver a new .xls file each time and they have to copy-paste it into different areas. if we could populate some sheets inside a dynamic, web-service-driven workbook, the users could do their thing with the data and we could do our thing with the data.</p>
<p>we haven't tested this particular feature of Excel yet, but we've got a couple guys lookin' at doing a pilot. I'll keep everyone posted about how well it goes. the example, of course, shows and ASP.NET web service being delivered to the spreadsheet. if Microsoft is really about Web Services based interoperability, Excel should play with ColdFusion WSDL the same as ASP.NET WSDL.</p>
<p>we'll see.</div>
