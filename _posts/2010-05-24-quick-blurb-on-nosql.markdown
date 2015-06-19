---
layout: post
status: publish
published: true
title: quick blurb on NoSQL
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 204
wordpress_url: http://groovecoder.com/2010/05/24/quick-blurb-on-nosql/
date: '2010-05-24 12:08:00 -0500'
date_gmt: '2010-05-24 18:08:00 -0500'
categories:
- dev
tags: []
comments: []
---
<p>I've spent about as much time thinking about this as NoSQL developers spend thinking about their schema, but here it is anyway.</p>
<p>At SourceForge I'm presently developing and maintaining a few different systems using all kinds of web tech's and languages - PHP, python, solr, Postgres, MySQL, and mongo. One thing I'm noticing is that the mongo systems are something of a breeze to write, and then a real challenge to maintain - especially debugging. Our mongo experts mostly say that the tooling for mongo is just 'immature.' I'm sure they're right, but that also points toward what I think might be a fundamental difference in the two modes of development.</p>
<p>AFAIK, there aren't any "old" NoSQL systems around? Mongo is only out since 2007, and Cassandra since 2008? We started using mongo early 2009, and even just one year out it feels so much more painful to maintain than our Postgres or MySQL systems that have been around since 1999! My theory is that NoSQL sacrifices maintenance and future development effort for the sake of startup development. I even made a neat drawing:</p>
<p><a onblur="try {parent.deselectBloggerImageGracefully();} catch(e) {}" href="http://1.bp.blogspot.com/_Fa_U5q7fBBY/S_rDEmp6JtI/AAAAAAAAAHA/HzWpTb8kA5U/s1600/schema_vs_nosql.png"><img style="display:block; margin:0px auto 10px; text-align:center;cursor:pointer; cursor:hand;width: 600px; height: 200px;" src="http://1.bp.blogspot.com/_Fa_U5q7fBBY/S_rDEmp6JtI/AAAAAAAAAHA/HzWpTb8kA5U/s400/schema_vs_nosql.png" border="0" alt=""id="BLOGGER_PHOTO_ID_5474902780885477074" /></a></p>
<p>Initially mongo seems to save on effort until the first valley - initial launch. At this point, the system launches and typically starts interacting with other systems and with users - data requirements change towards reality, which means <span style="font-weight:bold;">code</span> - i.e., function and logic - changes, not just model. In our environment, all other systems that use the data must also change their code which seems harder than the originating code. The code and the data are so intermixed that seemingly any and every change in either domain makes knock-on effects that have to be addressed.</p>
<p>In a typical schema data system, we front-load a bit of data modeling effort. After launch, when we get new and changing data requirements we typically address the schema changes that might be involved, and may have to write a data migration/transformation script. But beyond that, it seems we don't have to worry about data integrity or any other knock-on effects. We can change some data-access or model classes and be on our way.</p>
<p>So, am I just an old crusty developer shouting at these NoSQL kids to "get off my lawn!" ? Or has anyone else noticed this too? Maybe it's just the heterogeneous mix of NoSQL + schema that's killing me. Just seems like such a pain for not enough benefit?</p>
