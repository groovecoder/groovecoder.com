---
layout: post
status: publish
published: true
title: (Microsoft != Web Services &amp;&amp; Web Services != SOA)
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 278
wordpress_url: http://groovecoder.com/2005/09/27/microsoft-web-services-web-services-soa/
date: '2005-09-27 07:39:00 -0500'
date_gmt: '2005-09-27 13:39:00 -0500'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;">I'm trying a new tactic with the blog. I've added <a href="http://btetc.blogspot.com/">my brother Matt</a> to make this a team blog. hopefully he can help me in keeping posts pretty regular. I think I've first thought about having him make posts about web services, but we may end up just co-blogging on web services and open source.</p>
<p>now, I read an <a href="http://webservices.sys-con.com/read/133763.htm">interesting opinion</a>. I'm all for healthy skepticism and realism, but Fergesun isn't offering a good deal of either. the "tone" of his writing seems more like whining than real criticism.</p>
<p>he first shows his Microsoft fanboy side with this whopper:</p>
<p>"Web services are great! If you have to interoperate with non-Microsoft systems, they may be your only option."</p>
<p>now, even if one doesn't hate Microsoft, one would have to have their head buried pretty far into the sand to ignore the growing interest among enterprises in running platform-neutral software systems. hell, Java's popularity is largely a result of that single capability. I think it's a pretty safe assumption that if you're building software that will handle any meaningful amount of a company's business, you're going to need (or at least want) to interoperate with other systems in the company - be they non-Microsoft, non-.Net, non-Windows, non-American, non-Expensive, non-UnderYourTotalProprietaryControl, etc.</p>
<p>and his last direct quote I'd like to deal with:</p>
<p>"What I do <em>not</em> buy into is the idea that all systems should be seen either as services that expose their functionality only via unidirectional XML messaging or as clients of such systems."</p>
<p>well, <a href="http://www.computerworld.com/developmenttopics/development/webservices/story/0,10801,95053,00.html">news flash</a> to Mr. Fergesun, "unidirectional XML messaging" is not SOA. what you've described is Web Services, though even web services are growing out of the <span style="font-style: italic;">unidirectional</span> phase. while most SOA proponents think Web Services are the best means to achieving SOA, the two terms are not synonymous. so I'll be sure to make note when Fregesun is criticizing a technical aspect of Web Services that is not intrinsic in every SOA architecture.</p>
<p>Fergesun's problems listed are the "change in thinking" that comes along with asynchronous system operations, versioning, and reliability. in all of these cases, he mistakes Web Services as the only means to SOA, and furthermore, his Microsoft-centric perspective keeps him from seeing how these problems are actually addressed by web services.</p>
<p>in mentioning asynchronous operations, Fergesun ignores the fact that SOA != Web Services. it is entirely plausible to build service-oriented software that communicates via synchronous protocols. however, there is a very good <a href="http://www.ics.uci.edu/%7Efielding/pubs/dissertation/top.htm">case already made</a>(by someone much smarter than myself) that asynchronous architecture is more appropriate for modern systems - that is, highly networked systems using the internet as their core platform. but Fergesun does not mention any of the merits of asynchronous architecture; he only laments the need of a "change in thinking." perhaps if Microsoft had written a white-paper on the subject and released Microsoft Change-In-Thinking XP, he would be more willing to buy...er, <span style="font-style: italic;">accept</span> change.</p>
<p>as far as versioning goes, the .NET CLR approach does not alleviate versioning problems, it only changes them to be more like Java-on-Windows (other platforms, if you're <a href="http://www.mono-project.com/Mono:About">crafty</a>). for example, if your program requires functionality that is in 1.1 of the .NET framework and not in 1.0, you have to upgrade your .NET CLR to 1.1. (note: I came across <a href="http://support.microsoft.com/default.aspx?scid=kb;en-us;817267">this gem</a> while searching for 'web services versioning' and literally laughed out loud.) the CLR approach might avoid "DLL Hell" but is that really of huge benefit? I know one of the things I like about Lx (and php, to a lesser extent) is being able to upgrade only certain components to enable new features, rather than having to buy/download/upgrade to the latest version of dozens of packages all at once that may or may not break my other code relying on them.</p>
<p>but back to the world of Web Services (again remembering SOA could actually be achieved without Web Services, even with completely proprietary .NET system architecture)...</p>
<p>UDDI is the (open-standards-based, non-proprietary) means to address the versioning and deployment of web services, and there are already a <a href="http://www.developer.com/services/article.php/3374631">good</a> <a href="http://www.webservicesarchitect.com/content/articles/irani04.asp">deal</a> of <a href="http://www-128.ibm.com/developerworks/webservices/library/ws-version/">introductory</a> <a href="http://www.dogcaught.com/dpack/index.php?p=89">methods</a> for the practice. so we find that UDDI <span style="font-style: italic;">is</span> the out-of-the-box standard for versioning web services. perhaps if Microsoft isn't on the ball with it, there's a problem with Microsoft. it typically happens that they will try to create an out-of-the-box <span style="font-style: italic;">tool</span> instead of a standard - perhaps a nice little .NET Deployment Wizard that will be released in late 20X6.</p>
<p>since Fergesun makes only passing mention of the reliability "problem" with web services (again, not equivalent to SOA), I'll only make <a href="http://www.oasis-open.org/committees/tc_home.php?wg_abbrev=wsrm">this</a> link as my passing rebuttal.</p>
<p>Finally, I will close, mirror of Fergesun, with the eternal <span style="font-style: italic;">benefits</span> of all new software technologies - revolutionary new productivity, nearly-infinite opportunity, vast new markets for new products, and perhaps most importantly, independence from proprietary legacy vendors.</p>
<p>I may be giving Derek too hard of a time, because I've not read up on his other posts. but my guess is that this editorial post was meant to kick up controversy and "pick a fight." in that he has succeeded. but in providing real criticism or insightful analysis of SOA's "problems," he has failed - largely because he has only criticized web services, and only web services development from a Microsoft perspective.</div>
