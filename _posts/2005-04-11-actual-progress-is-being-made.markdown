---
layout: post
status: publish
published: true
title: actual progress is being made
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 265
wordpress_url: http://groovecoder.com/2005/04/11/actual-progress-is-being-made/
date: '2005-04-11 21:03:00 -0500'
date_gmt: '2005-04-12 03:03:00 -0500'
categories:
- Uncategorized
tags: []
comments:
- id: 165
  author: Richard Veryard
  author_email: ''
  author_url: ''
  date: '2005-04-14 04:17:00 -0500'
  date_gmt: '2005-04-14 10:17:00 -0500'
  content: Luke<br/><br/>I don't understand what value-add you can offer. To what
    extent are you transforming the services rather than simply passing them "straight-through"?
    How are you going to create a viable brand? <br/><br/>If you succeed I am very
    interested to know more, but I think you have a hard task ahead. (The software
    is the easy bit.)<br/><br/>cheers, Richard<br/>http://www.veryard.com/so/soapbox.htm
- id: 166
  author: luke
  author_email: ''
  author_url: ''
  date: '2005-04-14 08:36:00 -0500'
  date_gmt: '2005-04-14 14:36:00 -0500'
  content: hey Richard. thanks for coming by...I'm interested to find out how you
    ended up here, as I'm basically aware of NO readers of this blog...<br/><br/>in
    any case, there are a few value adds that exist in this model. these values do
    not necessarily apply to the entire courrier-services market - they may only apply
    to certain niches. but I think they are valuable enough to make customers in those
    niche markets.<br/><br/>aggregation. the first response to <a HREF="http://billburnham.blogs.com/burnhamsbeat/2005/04/are_online_reta.html"
    REL="nofollow" rel="nofollow">this post</a>, which you have linked to from <a
    HREF="http://www.veryard.com/so/2005/04/straight-through-processing-2.htm" REL="nofollow"
    rel="nofollow">your post</a>, addresses the value of aggregating products from
    multiple manufacturers. there is value in the sense that you can go to the store,
    and buy products from many different vendors thru a single channel. you make a
    single aggregated order which will trickle to many vendors, you pay a single bill,
    which will trickle to many vendors - you interact with a single merchant, who
    will trickle out the interactions to many vendors.<br/><br/>this same value can
    exist for services. in even just a medium-sized business, there can be an entire
    logistics department. it is valuable for end users of logistics (store clerks,
    field sales, customers, etc.) to have a single place to go to for all logistical
    needs. it may just be a number of employees who spend their entire day calling
    up different carriers to find out what's going on with different shipments. they
    are only providing services to the company, but they still have value.<br/><br/>buying
    consolidated services via a single channel thru an <i>external</i> company merely
    out-sources that value-production. it lets you focus on your core business and
    lets the service-provider handle, to whatever extent possible, your logistics.
    in my case, the project will handle all the technical, and hopefully most of the
    administrative, tasks of integrating your carriers' services into your business
    model.<br/><br/>this may seem like a small piece of the over-all pie, but it's
    still an important piece. and especially when we're talking about solid SOA architecture
    built with exposure via standardized Web Services itself, it makes this particular
    brand of intermediation pluggable into any other software models you have going,
    or may get in the future. (assumming, of course, they drank the same WS koolaid
    as the rest of us)<br/><br/>usability. extending the theme of aggregation making
    logistics-handling <i>easier</i> for companies - a brand can be built around the
    goal of making logistics extremely easy-to-use. both for an end-user, or for a
    technical integrator. the aggregated services are available to customer via a
    nice, clean, crisp, simple web interface (ala Google), and are also available
    via nice, clean, crisp, simple, web SERVICES.<br/><br/>rather than jump around
    X number of carriers' websites, end users can go to a single, clean interface
    to manage shipments for all carriers.<br/><br/>or, if they have their own resources
    (IT staff, consultants, etc), they can integrate the aggregated services into
    their own end-user applications - both existing and new.<br/><br/>extending this
    last capability a bit further...<br/><br/>freelance programmers are getting more
    and more work from traditional small business that are in need of various online
    capabilities (and not just online retail). if an open-source framework exists
    that makes it even that much easier for programmers to consume these kinds of
    services, it means that even very small businesses will be possible consumers
    of services like these, and since location is moot, the potential exists that
    every small business in the country is a possible customer.<br/><br/>I'd like
    to also bring up a somewhat local brand in my area (Midwest USA) that has been
    doing <b>very</b> well. QuikTrip is a convenience store. they're not run by an
    oil company - in fact, I don't even know which company supplies them. they don't
    have anything really that's exclusive to QuikTrip that you can't  get at any other
    convenience store. but their facilities are always clean, they always greet you
    at the door, they never sweat pennies of change, their soda machines are never
    broken, etc.<br/><br/>their brand is not built on value that they add to products
    they sell, or on value that they add to services they pass-thru. their brand is
    built on a set of consistent circumstances that you experience when you buy those
    products and services. and they're doing very well on that premise alone.
- id: 167
  author: Anonymous
  author_email: ''
  author_url: ''
  date: '2005-04-14 13:42:00 -0500'
  date_gmt: '2005-04-14 19:42:00 -0500'
  content: Keep us posted on your progress. I'd like to see what this product looks
    like when you're done. <br/><br/>- Hart, FedEx Services
---
<div style="text-align: justify;">I am in communication with UPS, USPS, FedEx, and DHL in regards to re-selling their online services, bundled and branded together in a single interface. FedEx's registration even asked which other carriers' services would be offered along with theirs, so they have obviously worked with ISV's that build shipping management solutions before.</p>
<p>mine has a few key differentiating factors, which I think will make it a great service.</p>
<p>1. built on top of a solid SOA. this is still in progress, but with a proper SOA, keeping up with all the different carriers' online functionality should not be a problem, and developers can be assigned to certain carriers, and to implement the carriers' functionality into the larger shipping management product that we are building. In addition, SOA based on WS-* standards will allow our offering to be incorporated into BPEL processes, which many larger companies will undoubtedly be using in the future.</p>
<p>2. low cost. we use open-source technologies, which makes our software costs approx. 0. I'm almost positive, should demand go as high as I'd like it to, to deploy on Zend Platform, or ActiveGrid, and to use commercial licenses of MySQL, Linux, etc. besides just the software licensing, the popularity of the OS technologies means there will be a huge number of developers as potential employees.</p>
<p>3. relating to a project Matt has going, I will also work on a RAD framework with him that will, hopefully, be built with consideration of allowing developers to quickly and easily set up communications with services such as the one we'll be offering. if that really is the case, then popularity of that framework will only help to accellerate the demand for our service.</p>
<p>4. federated identity. I don't know a LOT about this (yet), but the concept sounds great, and it's one of the differentiating factor that the Rearden group uses. hopefully Rearden will eventually be one of our customers. =)</div>
