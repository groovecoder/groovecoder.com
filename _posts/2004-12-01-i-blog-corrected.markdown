---
layout: post
status: publish
published: true
title: I blog corrected
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 225
wordpress_url: http://groovecoder.com/2004/12/01/i-blog-corrected/
date: '2004-12-01 17:46:00 -0600'
date_gmt: '2004-12-01 23:46:00 -0600'
categories:
- Uncategorized
tags: []
comments:
- id: 142
  author: Anonymous
  author_email: ''
  author_url: ''
  date: '2004-12-02 10:04:00 -0600'
  date_gmt: '2004-12-02 16:04:00 -0600'
  content: It was quite refreshing to see a bit of humility instead of a flame war
    spring up over my comment. I fully expected dismissive and/or abusive language
    in response and appreciate your ability to focus on the issue.<br /><br />Regarding
    the GPL, you may be right that some WS-specific language may need to be added
    in light of the latest tech developments. But I should point out one thing that
    has long been in the GPL FAQ (http://www.gnu.org/licenses/gpl-faq.html)<br /><br
    />"In what cases is the output of a GPL program covered by the GPL too?<br />-Only
    when the program copies part of itself into the output."<br /><br />Since WS consist
    more or less in requests and responses, the output obviously would never consist
    of the WS's source code, but a simple XML file.<br /><br />Keep in mind I am not
    a licensing expert. The webservicesarchitect article you referenced is out of
    date, but points in the right direction for further research immediately before
    the quote you used:<br /><br />"KDE and Gnome, are developing Web Service hooks
    that will allow those environments to be fully scriptable from a Web Service client."<br
    /><br />It may be worth contacting the desktop developers, or just perusing their
    websites, to see how the WS licensing was worked out.
- id: 143
  author: luke
  author_email: ''
  author_url: ''
  date: '2004-12-02 11:24:00 -0600'
  date_gmt: '2004-12-02 17:24:00 -0600'
  content: the WS-PublicLicense, then, should contain the legal encapsulation of the
    not-strictly-legally-binding fact mentioned in the FAQ.<br /><br />but, in some
    cases, your contention of the input/output of WS may not hold true...<br /><br
    />if you create a web service that executes using BPEL4WS,  the BPEL4WS markup
    can be said to be source code that powers/enables the program to execute. But,
    the BPEL4WS markup will also contain markup that is identical to at least portions
    of the input and output to the service, making the output of the service also
    contain, to a degree, the source code of the service.<br /><br />in that respect,
    I would fear that a legal case could be made that external services using output
    from a GPL-covered service (at least one that used BPEL4WS) could be said to be
    derived off the source code of the GPL service. that would be wholly unacceptable
    by most companies looking to build their own service-oriented architectures which
    they would need to be proprietary for a number of reasons.<br /><br />and I like
    making up spiffy marketing terms like WS-PublicLicense.
- id: 144
  author: Anonymous
  author_email: ''
  author_url: ''
  date: '2004-12-02 12:11:00 -0600'
  date_gmt: '2004-12-02 18:11:00 -0600'
  content: You're really just speculating, and IMO in an almost-paranoid manner. You
    think the GPL is so viral that "external services using output from a GPL-covered
    service...could be said to be derived off the source code of the GPL service".
    That's your opinion.<br /><br />Is there room for a WPL alongside the GPL? Maybe.
    But I think your goals can be accomplished, as I said, by the simple addition
    of clarifying language in the GPL. The advantage is that this license is well-established
    and your WPL would have a lot of explaining to do.<br /><br />Note again that
    the GPL places no restriction on your freedom to run the software; it is only
    when distributing it that 2b applies. It would be far-fetched to think that using
    the output of a WS constitutes distributing that WS.<br /><br />"if a Web Service
    is utilized by another program, that program <b>is said</b> to be derived from
    the Web Service program."<br />(emph added)<br /><br />Said by whom? You? This
    is false. Is my browser derived from the server software it connects to? No. Not
    even if I request and get a page full of information about the server, including
    bits of its source code.<br /><br />Service oriented architecture mandates self-containment.
    You can see the edges of a service. Separation of output and program is well-defined...though
    I can't speak about BPEL4WS.<br /><br />The bare, IMO remote, possibility that
    people will take your incredibly liberal reading of 2b to court is no reason to
    toss the GPL. The possibility that a court would countenance that reading is zero.
- id: 145
  author: luke
  author_email: ''
  author_url: ''
  date: '2004-12-02 17:17:00 -0600'
  date_gmt: '2004-12-02 23:17:00 -0600'
  content: IMO, I think every business looking into open-source software is somewhat
    concerned/"paranoid" about it. whether that concern is justified or not is something
    up for debate, but the existence of that kind of concern towards open-source by
    businesses is just a fact.<br /><br />but <b>it is wrong</b> to assume that a
    program using a web service is automatically deemed as being derived from the
    service. a little clarification in either the GPL license or the WPL license could
    go a long way to diminish the concern, though.<br /><br />the BPEL4WS example
    I mentioned is still a bit of a stretch, but there is enough over-lap and fuzzines
    there to cause a flag to go up in my mind, and I think the same would be true
    for other business people.<br /><br />I probably don't really need to comment
    on the lunacy of our present court system when it comes to IP-related issues.
    think software patents. I would want as much protection from a court battle as
    possible.<br /><br />a followup question, though:<br /><br />is it legal/proper
    to copy the GPL or LGPL word-for-word and then make a few changes to create a
    new license?
- id: 146
  author: Anonymous
  author_email: ''
  author_url: ''
  date: '2004-12-03 13:51:00 -0600'
  date_gmt: '2004-12-03 19:51:00 -0600'
  content: Changing the GPL is not allowed, as per the copyright notice at the top
    of it.<br /><br />Writing your own license that's similar to, but different from,
    the GPL is of course legal and possible, but you should definitely get a copyright
    attorney to review it, or -- more likely -- write it for you.<br /><br />Mr. Crouch,
    I hope you'll forgive my saying it but if "every business looking into open-source
    software is somewhat concerned/'paranoid' about it" then part of the problem is
    the simplistic view that otherwise intelligent persons such as yourself perpetuate.<br
    /><br />In previous postings on this blog I find:<br /><br />-Your "prime example"
    of opensource "madness/drivel/hypocrisy" is not well researched. Again, I appreciate
    the retraction on this.<br /><br />-Condescension toward Eric Raymond as though
    he were some naive basement hacker. I'd be careful with that. Such people make
    the internet work<br /><br />-Your frustration with "communist-style drivel on
    almost every open-source site I've been to thus far". I would love to see a list
    of the sites.<br /><br />-Denigration of the OSI, again as though they are unsophisticated
    idealists. Not so.<br /><br />"Are you guys opposed to intellectual property rights?<br
    /><br />The Open Source Initiative does not have a position on whether ideas can
    be owned, whether patents are good or bad, or any of the related controversies.
    <b>We think the economic self-interest arguments for open source are strong enough
    that nobody needs to go on any moral crusades about it.</b>"<br /><br />This is
    on page 1 of their FAQ. It seems to correspond well to your own, pragmatic approach.
    Yet you seem more or less unaware of it. I can only assume you get your information
    about the OSI from third parties who are averse to it.<br /><br />In short, I
    find a lot of off-the-cuff remarks that generate fear, uncertainty, and doubt
    about open-source software, and then I find the statement that "the existence
    of that kind of concern towards open-source by businesses is just a fact."<br
    /><br />It is an unfortunate and temporary fact, and you are helping delay the
    time when it will go away.
- id: 148
  author: luke
  author_email: ''
  author_url: ''
  date: '2004-12-03 15:20:00 -0600'
  date_gmt: '2004-12-03 21:20:00 -0600'
  content: expecting to be pardoned on over-blown, emotionally-motivated terminology
    I used when discussing certain issues is obviously a judgemental error on my part,
    considering the audience this blog would carry is no doubt very logical, passionate,
    detail-oriented, and argumentative. <br /><br />so, dropping the expectations,
    I extend and expand my apology, formerly directed only towards OSI, to:<br /><br
    />1) all readers of this blog<br />1.b) current anonymous readers<br />1.d) current
    readers who share parents with me<br />1.e) current readers who do not share parents
    with me<br />1.f) all future readers<br />2) Eric S. Raymond<br />3) The OSI<br
    />4) All others not expressly mentioned in this license...I mean apology<br /><br
    />for the un-deserved comments and flaming I have directed towards ESR, the OS-I
    and OS community.<br /><br />now for some deserved comments.<br /><br />my condescension
    toward Raymond is more representative of the condescension I hold toward the work
    he is involved in - shouting from the mountain-tops, as I would describe it. although
    he admits that he put himself into the position on purpose, knowing full well
    the kind of brand he would receive, I still find that kind of 'work' to be basically
    pointless. <br /><br />open-source developers should be working on software that
    is practical and applicable to today's software needs. these software needs are
    still dominated by the needs of working with business information, but business-centric
    analysis/direction is quite often absent <i>from the proclaimations of the OS
    'evangelists'</i>. <br /><br />there is no doubt that the majority of open-source
    <i>software</i> is not only compatible, but influential and beneficial to commercial
    interests, often in a vastly superior way to proprietary software. but I would
    contend that it has not gained that stature <i>from the proclaimations of the
    OS evangelists</i>, and I therefore think their activities are, to that end, pointless.<br
    /><br />it is also evident and renown that the internet has evolved due to the
    efforts of so-called 'basement hackers' and I not only hold no condescension for
    these types, but would be honored to work myself into being considered among them.
    the problem is that I do not see ESR or many other OS evangelists as this type
    anymore, though it is understood that he was at a time.<br /><br />in regards
    to the OSI and its pragmatic, pro-capitalism approach that I've been unable to
    see, that should perhaps be attributed to a marketing failure on the part of OSI
    - that they do not adequately tout their pro-business positions as prominantly
    as their 'for the good of the community' positions, which they state in the first
    sentence on the first page of their site, as their first purpose.<br /><br />and
    maybe that failure to relieve the FUD that us capitalist pigs have towards open-source
    is what causes us to express that FUD. (again, admittedly with wrongly phrased
    assertions)<br /><br />in any case, if the proclaiming of the concern is the <i>only
    thing</i> that keeps that concern alive, the solution is just silence. but if
    there are still efforts needing to be made in order to remove the concern, expressions
    of the concern will help to come up with a solution.
---
<div align="justify">the astute (and probably solitary) reader who corrected <a href="http://lukecrouch.blogspot.com/2004/11/example-of-open-source-madness.html">my erroneous assumptions</a> regarding the <a href="http://www.opensource.org/docs/definition.php">Open Source Definition</a> sent me on a much deeper research tangent that is very much vital to the subject of open source web services. but I will first address and correct my statements.</p>
<p>the primary source of my confusion and ill-founded assumptions was my reliance on <a href="http://www.onlamp.com/pub/a/onlamp/2004/11/18/licenses.html"><span style="FONT-STYLE: italic">the article's</span></a> summarization of the definition, rather than the definition as outlined by <a href="http://www.opensource.org">OSI</a>. I therefore had an incomplete perspective of the open source definition, and lambasted a straw-man that had no real resemblance of the real Open Source Definition &amp; Licensing body. I owe OSI an apology, although they never knew it, and I offer it, although probably only to an empty blogosphere.</p>
<p>with my more fully-developed perspective, in regards to my comments about OSI 'zealots' and its 'dream-world', I will withdraw the 'dream-world' accusation, in recognition of the fact that the the OSI definitions and licenses (and specific concepts therein) are not only reasonable, but beneficial and conducive to advancing commercial software.</p>
<p>however, I still retain my, perhaps stereotypical, slant that the majority of open-sourcerors(tm) are ordinarily highly committed to, and evangelical of, open-source for ethical, or moralistic reasons more than techincal or (especially) commercial reasons.</p>
<p>but rather than try to offer up my own argument for the still small, though deeply important, point of contention I have with OS at large, I'm glad I can reference the opinions of somewhat more respected and established OS advocates. Namely, Michael Tiemann:</p>
<p>"...the freedom to use, distribute, and modify software will prevail against any model that attempts to limit that freedom. It will prevail not for ethical reasons, but for competitive, market-driven reasons."</p>
<p>now, for a more productive topic of discussion, I would contend that it is impossible to license Web Services under the GPL and here's way...</p>
<p>GPL, 2.b:</p>
<p>"You must cause any work that you distribute or publish, that in whole or in part contains <span style="FONT-STYLE: italic">or is derived from the Program or any part thereof</span>, to be licensed as a whole at no charge to all third parties under the terms of this License."</p>
<p>Web Services are Programs that will be utilized by countless numbers of other programs, and if a Web Service is utilized by another program, that program is said to be derived from the Web Service program. So the GPL is out for commercial Web Services.</p>
<p>The LGPL is more attractive....LGPL, 2.d:</p>
<p>"If identifiable sections of that work are not derived from the Library, and can be <span style="FONT-STYLE: italic">reasonably considered independent and separate works</span> in themselves, then this License, and its terms, <span style="FONT-STYLE: italic">do not apply to those sections</span> when you distribute them as separate works."</p>
<p>For me, and probably for other commercial firms looking to make profit from Open Source Web Services, the fuzziness of the 'reasonably considered independent works' is way too open for discussion, especially considering the very next part of the license goes on to state:</p>
<p>"But when you distribute the same sections as part of a whole which is a work based on the Library, the distribution of the whole must be on the terms of this License..."</p>
<p>There is no real way, without getting more detailed and technical in the license, to determine where a proprietary program that uses a Web Service can be considered an independent or seperate work. And if a proprietary program were to use many Web Services, all under LGPL, the nightmare of working out the boundaries that the license applies to could hinder the adoption/consumption/embrace of OS Web Services.</p>
<p>I think a Web Services-specific open source license needs to be made, fashioned after the LGPL, but specifically stating that programs utilizing only standardized output of the licensed program are not themselves derivative works of the program, but are considered reasonably independent, recognizing that the standardized output could be replaced by a different program with no detriment.</p>
<p>I hope open-sourcerors catch the Web Services bug, though there are <a href="http://lukecrouch.blogspot.com/2004/11/this-somewhat-old-article-makes-great.html">reasons why they wouldn't</a>, and some progress is made in this important area of WS and OS licensing. </div>
