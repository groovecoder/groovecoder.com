---
layout: post
status: publish
published: true
title: Facebook never bet on HTML5
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 948
wordpress_url: http://groovecoder.com/?p=948
date: '2012-09-12 11:33:20 -0500'
date_gmt: '2012-09-12 16:33:20 -0500'
categories:
- dev
- tech
- greatest-hits
tags:
- html5
- facebook
comments:
- id: 14955
  author: Kethinov
  author_email: kethinov@gmail.com
  author_url: ''
  date: '2012-09-12 14:11:36 -0500'
  date_gmt: '2012-09-12 19:11:36 -0500'
  content: They didn't change webkit's rendering logic. All they did was add JS APIs
    so m.facebook.com could make calls to device APIs using a bridge code like PhoneGap
    inside their native apps. There's nothing wrong with that approach at all. Lots
    of apps do it and it works fine. The real problem with Facebook's web efforts
    is their web coders did a shoddy job optimizing for performance. That's all.
- id: 14958
  author: Erik Harrison
  author_email: erikharrison@gmail.com
  author_url: ''
  date: '2012-09-12 15:26:26 -0500'
  date_gmt: '2012-09-12 20:26:26 -0500'
  content: "I'm reading this and it doesn't actually seem as insane as you make it
    sound. Maybe I'm missing something, but it looks like pretty standard progressive
    enhancement. They build m.facebook.com for their lowest end target (feature phones),
    then send a javascript blob to upgrade the functionality of all the bits. The
    weirdness is that they JS blob talks to some native bits of the OS API that is
    bound to JS in the app. That requires an extra round trip to the server to get
    the blob, when it could be exposed in the app itself, but this way they don't
    have to update the binary on the phone as often. \r\n\r\nIt's not \"pure\" HTML5,
    but what is?"
- id: 14959
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2012-09-12 16:25:50 -0500'
  date_gmt: '2012-09-12 21:25:50 -0500'
  content: Good points. Updated post to reflect. It still sounds like shoddy engineering
    unrelated to HTML5. i.e., Facebook bet everything on FaceWeb, not HTML5.
---
<p>I'm going to jump into the mix, but my post is short and sweet. In fact, I wrote it while waiting for tests to run.</p>
<p><strong>Facebook never bet on HTML5.</strong> Anyone remember <a href="http://www.readwriteweb.com/mobile/2011/09/how-facebook-mobile-was-design.php">the convoluted rambling of Dave Fetterman at f8 developer conference last year</a>? I remember being both dumbfounded and confounded by it.</p>
<blockquote><p>So, how does this work? Project FaceWeb is an extension of this progressive enhancement idea. So, instead of the phone saying I am rendering for a WebKit browser, we send an agent that says you are going to be rendering for a WebKit UI WebKit view inside the iPhone app. So, what you have to do is detect that, style a Web code to make that work, build a bridge between the things that you want to write to interact natively with the Objective-C, say in Javascript, then build HTML pages for Facebook in the iPhone. So, you build much smaller native goop instead of having to build over and over again.</p>
<p>...</p>
<p>HTML5 is probably the way that we should have done it.</p></blockquote>
<p>Near as I can tell, Facebook invented their own PhoneGap (i.e., FaceWeb) and sent m.facebook.com to it, <strong>then FaceWeb changed webkit's rendering logic*</strong> to match m.facebook.com instead of changing m.facebook.com to a mobile HTML5 site? That's not HTML5 - that's just stupid.</p>
<p>* UPDATE: as pointed out in comments, this isn't exactly accurate. Faceweb does some funky stuff though, and their engineering manager in charge of the project couldn't even articulate what it is. So it still sounds like bad engineering unrelated to HTML5.</p>
<p>* UPDATE 2: You should read <a href="http://www.theregister.co.uk/2012/09/14/facebook_html_5_vs_native_apps/">Matt Asay's analysis of Facebook's HTML5 fiasco</a>. In fact, you should read everything Matt Asay writes.</p>
