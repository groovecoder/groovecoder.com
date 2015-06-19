---
layout: post
status: publish
published: true
title: php-based J2EE approach?
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 233
wordpress_url: http://groovecoder.com/2004/12/11/php-based-j2ee-approach/
date: '2004-12-11 15:56:00 -0600'
date_gmt: '2004-12-11 21:56:00 -0600'
categories:
- Uncategorized
tags: []
comments:
- id: 154
  author: Lux
  author_email: ''
  author_url: ''
  date: '2004-12-13 23:38:00 -0600'
  date_gmt: '2004-12-14 05:38:00 -0600'
  content: 'Hi Luke, thanks for the post about my new project (I''m the developer
    of phpBeans).  I thought it might help to clarify a couple of things about the
    software, which will hopefully dispell a few fears you and others might have about
    it:<br /><br />First, phpBeans is meant to fill a space that SOAP and XML-RPC
    aren''t completely appropriate for.  This space is much more akin to Java''s RMI
    and OMG''s Corba technologies.  Figuring that people would compare phpBeans most
    often to SOAP and XML-RPC, I wrote an article comparing and contrasting it with
    them, in the hopes of better explaining where each of them is most appropriate:<br
    /><br />http://www.phpbeans.com/index/news-app/story.4<br /><br />Second, what
    I am trying to do primarily is not to create new software but to create a new
    standard.  While this standard is PHP-oriented, it is not at all PHP-only.  In
    fact, there is already a Ruby client library available, and we hope to offer many
    more soon:<br /><br />http://www.phpbeans.com/index/client_for_ruby<br /><br />So
    the only way the phpBeans protocol limits you is in the same way that SOAP limits
    you from using Corba or Java RMI limits you from XML-RPC.<br /><br />Third, what
    phpBeans does is different from ActiveGrid as well (as far as I''ve read about
    ActiveGrid), since phpBeans is intended to sit behind the publishing layer of
    the application.  phpBeans would contain the business logic of an application,
    while an HTTP web server would call the business logic layer then compile it into
    whatever format is requested (HTML, XML, RSS, SOAP, etc.).  In MVC terms, phpBeans
    contains the Model.<br /><br />We''re also planning ways of making phpBeans interoperate
    better with other standards like SOAP (probably via the idea of "connectors"),
    but keep in mind that we''re trying to do so with the emphasis on creative specifications
    first, software second.  As I said in our press release: in order for PHP to gain
    acceptance [at the enterprise level] it needs to increase its focus on web standards.  When
    an existing standard doesn''t adequately cover a certain area, the axiom "the
    right tool for the job" would suggest that we create a new standard or a new tool
    that solves it best.  And SOAP is definitely not a one-size-fits-all solution.
    ;)<br /><br />I hope this helps clarify where our project is coming from, as I
    really do think this is one of the things PHP needs in order to be taken seriously.<br
    /><br />Cheers,<br /><br />Lux'
- id: 155
  author: luke
  author_email: ''
  author_url: ''
  date: '2004-12-14 06:51:00 -0600'
  date_gmt: '2004-12-14 12:51:00 -0600'
  content: thanks for coming by my blog, and thanks for leaving the links and the
    info. I think there is a place for phpBeans and other RMI-style distributed computing,
    and the solution would be very beneficial for distributed computing projects that
    will be written under a controlled architecture.<br /><br />most of my interest
    in Web Services is focused on the B2B integration area, where a person may have
    little or no control over the architecture and language of the systems they'll
    be interacting with. for example, to process an inbound order, we might have to
    hit a 3rd party inventory management program, like GAINS, written in Java, and
    we also need to update our own Informix database, and interact with our custom-built
    credit checking program written in ColdFusion, then use an online currency converter,
    etc, etc.<br /><br />if the interactions between these very heterogenous systems
    can be standardized using a SOAP client that hits all their WSDL's, it's almost
    simple to work with them all.<br /><br />I can see phpBeans architecture being
    very well suited for, as you say, an enterprise looking to take their php scripts
    up a notch to get scalability, reliability, redundancy, and all the benefits that
    come with having a good distributed platform. but I would think they need to have
    a good deal of control over how their code interacts with the phpBeans, which
    is not really possible in the kind of environment I described above.
---
<div style="text-align: justify;">I was a little puzzled by <a href="http://www.linuxpr.com/releases/7414.html">this</a>, after reading and getting excited about the direction of <a href="http://www.activegrid.com/">ActiveGrid</a>,  and the concept of <a href="http://www.lamp5.net/">lamp5</a> and Web Services in general. apparently, Simian is attempting to create a J2EE-like server based on php.</p>
<p>the phpBeans (similar to EJB's - Enterprise Java Beans), the phpBeans Object Server, and phpBeans Client API allow php objects to be encapsulated in such a way that they may invoke one another on remote machines and all that jazz.</p>
<p>what I find particularly puzzling is that Web Services enable the same kind of thing. you wrap up your php classes and expose them with WSDL's, and I use SOAP clients to invoke them from anywhere else in the world. but the use of a phpBean and phpBean Object Server takes that cool concept OFF of standardized protocols like SOAP, HTTP, etc and puts it into a client API.</p>
<p>but exposing your php classes/objects as web services means ANY program on ANY platform can use them. exposing your php classes by making them phpBeans and putting them on a phpBeans Object Server means only other php classes that use the phpBeans Client API can use them.</p>
<p>though both ActiveGrid and phpBeans are in their infancy (though they are more mature than lamp5!), I would like to see developers embrace the ActiveGrid approach more than the phpBeans approach. I think web services are being adopted by enterprises in place of approaches like J2EE and CORBA and other language-oriented integration methods.<br />
</div>
