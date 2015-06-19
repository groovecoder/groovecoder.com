---
layout: post
status: publish
published: true
title: Test Driven Development
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 175
wordpress_url: http://groovecoder.com/2007/05/15/test-driven-development/
date: '2007-05-15 07:10:00 -0500'
date_gmt: '2007-05-15 12:10:00 -0500'
categories:
- Uncategorized
tags:
- agile
comments: []
---
<p>I've read a few anti- and pro-Agile rants in the past couple days. Because I'm somewhere in between, I can't really <a href="http://www.answers.com/rant&amp;r=67">rant</a> in either direction. Instead what I might try to do is give my opinion on the actual effects I've noticed from some Agile/XP practices on my own coding. Note that I'm probably only picking out the ones I like, so my posts on the subject will betray a pro-Agile bias. But, the sparse number of posts will hopefully balance the scales in demonstrating that there are only so many Agile/XP practices about which I actually care enough to write.</p>
<p>I'm a fan of Test Driven Development. I don't do TDD 100% of the time, and there are quite a few things I'm not sure how to automatically test (CSS tweaks, anyone?). But I agree with just about all the benefits I read in <a href="http://butunclebob.com/ArticleS.UncleBob.TheThreeRulesOfTdd">this pro-TDD article</a>, though I'll re-arrange their listing by my personal opinion of their importance:</p>
<blockquote><p>When you follow ... TDD, <i>all your code will be testable by definition!</i>  And another word for "testable" is "decoupled".  In order to test a module in isolation, you must decouple it.</p></blockquote>
<p>When I use TDD, it forces me to write "decoupled" code. "Decoupled" is one of those magic words programmer types say to each other in intellectual flexing competitions. But TDD shows what it really means - code that can be isolated. The benefits of isolated/decoupled code are numerous - re-usability, less duplication, more concise, and I'd also say "testability" is a benefit.</p>
<p>This is not to say that you have to use TDD to write decoupled code. There are much smarter and more disciplined developers than myself all over who write excellent code without using TDD. But for me personally, TDD forces me into just enough structure and pre-code analysis to keep me from writing messy code that will need cleaning later. Speaking of which ...</p>
<blockquote><p>Why don't we clean up code that we know is messy? We're afraid we'll break it. But if we have the tests, we can be reasonably sure that the code is not broken, or that we'll detect the breakage immediately. If we have the tests we become fearless about making changes. If we see messy code, or an unclean structure, we can clean it without fear.</p></blockquote>
<p>The "safety net" feeling you get from gradually building up a big suite of automated tests is, like all "feelings", impossible to describe, but I'll try to relay an anecdote which might help.</p>
<p>I still don't consider myself a Java programmer, although I spend at least 50% of my time programming in Java. I don't "feel" comfortable in Java. But, in the course of our development, I made at least one deep and far-stretching re-factoring (more fancy talk for "change the guts of the code without changing its behavior") to maybe 30 different Java source files all over our code-base, with no hesitation before committing. My uncomfortable Java feelings were superseded by my comfort in the fact that all 800+ tests passed after I made the change. So I'm wasn't afraid of making the needed changes, even in a language in which I'm uncomfortable, because all the code was covered.</p>
<p>Again, this doesn't mean someone can't make sweeping changes unless they have tests covering all their code. I've simply noticed myself indeed becoming more fearless when I myself have to make those kinds of sweeping changes.</p>
<blockquote><p>Have you ever integrated a third party library into your project? You got a big manual full of nice documentation. At the end there was a thin appendix of examples. Which of the two did you read? The examples of course! That's what the unit tests are!</p></blockquote>
<p>This particular benefit is quite a distance behind the previous two. Mostly because the kind of example code you find attached to "nice documentation" is a better reference than unit test code. Unit test code is oftentimes performing some superfluous tricks for isolation, and/or hard to understand. It could be argued that if the test code is hard to follow, the tested code's design is to blame. But I think personally I'd rather move extra verbosity into my test code and keep my productive code clean. Could just be a matter of personal preference.</p>
<p>However, unit-tests are useful in understanding the intended use of the tested code. And programmers are more likely to spend their time to write test code that benefits themselves (see above) than they are to "waste" their time writing example code which benefits only others. So, lacking the refined, formal example code, unit tests can act as use-case specifications. (<a href="http://www.agiledata.org/essays/tdd.html#Misconceptions">Though not 100% comprehensive design specs</a>, as some might say.)</p>
<p>There are a few anti-TDD points with which I also agree...</p>
<p>For many, TDD is a new way of programming. As such, it has an associated learning curve, requires new thinking patterns, and takes time before it is comfortable to someone. However, I have found TDD easier and more enjoyable to adopt than Java. Some might say that isn't high praise for TDD, but to those people I would say, "Well, at least it's simpler than Java." TDD can be practiced in the language of your choice, and you will probably find that <a href="http://www.phpunit.de/pocket_guide/3.0/en/test-first-programming.html">TDD resources from within your preferred language</a> can really help to match your existing programming style with TDD.</p>
<p>TDD results in a LOT of code. In the course of <a href="http://tulsaphp.net/node/40">adding tests for the ZF Tutorial app</a>, I realized I was adding verbose testing code to already-verbose MVC code. Indeed, the test code for the controller was more code than the controller code itself. This is a simple fact of TDD - more code. There's no getting around it. You simply have to decide if the benefits of TDD outweigh its drawbacks, such as this one.</p>
<p>We have run into problems where our 800+ test suite takes a significantly long time to run (~10 minutes). This can be a real pain if you're working under strict CI rules in that every change you make, even that pesky css tweak, is supposed to be sent thru that test suite before committing to your source repository. Typically, though, once developers have the hang of TDD, they know what kinds of changes really need the entire test suite, and what kinds of changes can be simply checked-in, or can pass thru only a sub-set of tests. But the pain still exists in that you have an extra step of responsibility between writing your code and committing it. Again, weigh the benefits of TDD against this drawback, maybe come up with a compromise of some kind.</p>
