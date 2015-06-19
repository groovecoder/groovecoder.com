---
layout: post
status: publish
published: true
title: Reynolds's SOA definition
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 279
wordpress_url: http://groovecoder.com/2005/10/03/reynoldss-soa-definition/
date: '2005-10-03 17:39:00 -0500'
date_gmt: '2005-10-03 23:39:00 -0500'
categories:
- Uncategorized
tags: []
comments:
- id: 187
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2005-10-04 09:40:00 -0500'
  date_gmt: '2005-10-04 15:40:00 -0500'
  content: '>with WS-based SOA, the interface is described using a standardized format
    so that the services implementing the interface can be in any language on any
    platform.<br/><br/>>so the good news is that it is indeed another attempt at creating
    modularity and re-usability in software. the bad news is that if you work under
    the assumption that that''s ALL it is, you won''t really be capturing the benefits
    of SOA.<br/><br/>I envision it like this: the networked/SOA application is analogous
    to a well-designed operating system, like UNIX or GNU/Linux. Modularity is encouraged
    by having processes generally be small, and good at one thing.<br/><br/>Inerop
    is encouraged by having the vast majority of these processes pipe boring ole ASCII
    To each other.<br/><br/>When I think about it this way, the benefits of SOA seem
    kinda obvious, and I wonder why it took so long for this kind of thinking to get
    hot.<br/><br/>Well, your CF guy -- god bless him -- didn''t actually separate
    into routines. Sticking with my analogy, all he did was write 11 shell scripts
    containing a line, then one shell script that called all those lines in succession.<br/><br/>Actual
    routines would be snippets that require an input (or react to an event) and generate
    an output (or trigger an event)'
- id: 188
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-10-04 13:00:00 -0500'
  date_gmt: '2005-10-04 19:00:00 -0500'
  content: I think you've mentioned the Lx analogy before and I like it.<br/><br/>but
    there's still a danger of over-simplifying it with this analogy unless we emphasize
    that for good SOA, the <b>interface descriptions</b> are the basis of the system
    design.<br/><br/>so to extend the Lx analogy to be more accurate, I'd say:<br/><br/>modularity
    thru small processes that are good at one thing. interoperability thru standardized
    input/output exchanges. <b>and really good man pages describing every process</b>.<br/><br/>then
    good (Lx) SOA is achieved by designing the architecture of the system based on
    the <b>interfaces</b> of the utility processes, as <b>described in the man pages</b>
    - not the internals of each program involved.<br/><br/>ie, if you write a perl
    program or shell script that merely executes a series of lower-level utility programs,
    you decide how to structure your program by looking at the man pages. you don't
    look at the source code of the utility programs, although you could.<br/><br/>in
    that way, you capture the biggest SOA benefits - re-usability (of the many small
    processes), flexibility (by re-arranging existsing processes interactions), and
    modularity (by removing context from the small processes, and the composite larger
    processes).
- id: 189
  author: Matt Crouch
  author_email: ''
  author_url: ''
  date: '2005-10-04 14:29:00 -0500'
  date_gmt: '2005-10-04 20:29:00 -0500'
  content: 'excellent point. WSDL et al. remind me of phpDoc and programs like that
    ... generate man pages automatically if your code is up to snuff, properly commented,
    etc.<br/><br/>I have a confession, though: I never got into this habit. I deserve
    Bad Things (like always being behind deadlines) as a result.'
- id: 190
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-10-04 14:56:00 -0500'
  date_gmt: '2005-10-04 20:56:00 -0500'
  content: interestingly, when I asked Andi about how PHP plans to support the automatic
    creation of WSDL that describes PHP functions, he said it would be implemented
    using certain comment syntax before the function. then a PHP class would interrogate
    the code for the comments and create WSDL based on the input/output of a function
    specified to be a web service.<br/><br/>IMHO, ColdFusion does it just about the
    coolest way possible. you don't even have to include special comments. just make
    your CFC and then hit it in a browser with a ?WSDL at the end of the URL and it
    will interrogate the methods in the CFC and create proper WSDL for it automatically.
    so all code changes are reflected in the WSDL as soon as the change is made. nice.<br/><br/>I
    know PHP5 has object introspection features, so I think that'd be the best way
    to accomplish it. but comment syntax is a good first step.<br/><br/>I also never
    document well. see you in hell.
---
<div style="text-align: justify;">in response to <a href="http://btetc.blogspot.com/2005/09/wikfisk.html">Matt's post</a>, which was a response to <a href="http://btetc.blogspot.com/2005/09/wikfisk.html">Reynolds's post</a>, I would say the following...</p>
<p>cajo's response sounds nice to developers, because it's what they want to hear - we don't need to change the way we do things; SOA is just new buzz-hype on what we already do. but it would not be "honest" to say "that SOA means nothing more than separating business functions into routines, just as they have <i>always</i> done."</p>
<p>for example: one of our developers separated his business functions into routines: he made 11 .cfm pages of ColdFusion code, and then 1 page of ColdFusion code with 12 cfinclude tags. even if the only thing you've read is the senseless marketing trash that vendors are putting out about SOA, you know this cfm approach is not SOA, even though it is separating business functions.</p>
<p>Reynolds includes the key distinction at the end of his definition (a smart place for it):</p>
<p>"Each service provides an interface-based service description to support flexible and dynamically re-configurable processes"</p>
<p>the interface-based service description is mandatory. it's what makes an SOA different. the architecture is not based on identification of objects in the system, as with OOP. rather, objects come about from the descriptions of the services that need to be performed. neither is the architecture based on run-time context as the case with procedural includes of multiple script files.</p>
<p>the service descriptions come first, and are arranged into composite, higher-level services with their own descriptions. this is the key between SOA and other approaches to modularity.</p>
<p>I first encountered this in Erl's first book when he talked about the similarity between OOP and SOA - code to the interface. but with WS-based SOA, the interface is described using a standardized format so that the services implementing the interface can be in any language on any platform.</p>
<p>so the good news is that it is indeed another attempt at creating modularity and re-usability in software. the bad news is that if you work under the assumption that that's ALL it is, you won't really be capturing the benefits of SOA.</div>
