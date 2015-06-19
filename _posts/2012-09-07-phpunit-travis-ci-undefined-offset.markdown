---
layout: post
status: publish
published: true
title: phpunit travis ci undefined offset
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 932
wordpress_url: http://groovecoder.com/?p=932
date: '2012-09-07 01:26:05 -0500'
date_gmt: '2012-09-07 06:26:05 -0500'
categories:
- dev
tags:
- php
comments:
- id: 14902
  author: Dave Marshall
  author_email: dave.marshall@atstsolutions.co.uk
  author_url: http://www.davedevelopment.co.uk
  date: '2012-09-11 13:55:53 -0500'
  date_gmt: '2012-09-11 18:55:53 -0500'
  content: "I think you can put this in your phpunit.xml, a little nicer than setting
    it somewhere in your test suite\r\n\r\n     \r\n         \r\n     "
- id: 14905
  author: John Kary
  author_email: john@johnkary.net
  author_url: http://johnkary.net
  date: '2012-09-11 14:37:27 -0500'
  date_gmt: '2012-09-11 19:37:27 -0500'
  content: "The PHP Framework Interoperability Group, consisting of lead devs from
    most of the popular PHP frameworks and libraries, currently work together to define
    autoloading standards and coding standards. The framework and library authors
    agree to adopt the standards set forth by the group to increase interoperability
    and collaboration between each others' frameworks and libraries.\r\n\r\nhttp://www.php-fig.org/faq/\r\nhttps://github.com/php-fig/fig-standards\r\n\r\nYour
    post says you were working with WordPress, whose authors were approached about
    joining the FIG group at one time, but to which they declined."
- id: 14911
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2012-09-11 15:30:05 -0500'
  date_gmt: '2012-09-11 20:30:05 -0500'
  content: Ah, I had never heard of php fig. https://github.com/klaussilveira/phpcs-psr
    is a very useful link for that too. ;)
---
<p>or</p>
<h2 class="title">How I learned to stop hating on PHP</h2>
<p><a href="http://travis-ci.org/#!/groovecoder/wp-promote-mdn/jobs/2337280"><img class="alignnone" title="PHPUnit Travis CI Undefined Offset" src="https://dl.dropbox.com/u/21969365/images/phpunit_travis_undefined_offset.png" alt="PHPUnit Travis CI Undefined Offset" width="579" height="100" /></a></p>
<p><strong>TL;DR</strong> - "Undefined offset" is an E_STRICT level PHP error, and travis-ci.org uses E_STRICT+ by default. Put <code lang="php">error_reporting( E_ALL );</code> at the top of your phpunit test suite to find and fix all your warnings and notices to fix Travis builds.</p>
<h3>pHpaters</h3>
<p>Today <a href="http://laurathomson.com/">Laura</a> and I chatted briefly about <a href="https://twitter.com/lxt/status/243779047996420096">djangocon presenters bashing PHP</a>. I mentioned that the <a href="http://wordpress.org/extend/plugins/promote-mdn/">Promote MDN</a> code is some of my favorite code - in any language. As with my Zend_Rest code, the two keys I've found to writing good PHP code are:</p>
<ol>
<li>Use a <strong>coding standard</strong></li>
<li>Write <strong>unit tests</strong></li>
</ol>
<h3>Coding Standard</h3>
<p>I use <a href="https://github.com/mrchrisadams/WordPress-Coding-Standards">Chris Adams WordPress Coding Standards for PHP_CodeSniffer</a> to stick to that. It was <strong>amazing how much nicer the PHP code was when I took just an hour to clean up</strong> what I inherited from SEO Smart Links. The PHP community would do well to embrace, encourage, and even enforce coding standards more - the way the Python community does with PEP8.</p>
<h3>Unit Tests</h3>
<p>I write unit tests for Promote MDN too. My tests/doubles.php is hacky, but it Freaking Works™; I <strong>didn't have to build out a set of fixture data or couple the test suite to a running WordPress instance</strong>. Like WordPress, I just (ab)use the global namespace to (re-)define dependency functions with doubles.</p>
<p>I also took the opportunity to try out <a href="travis-ci.org">Travis CI</a>. After fixing the travis.yaml and phpunit.xml files <em>just right</em> I got a bunch of test errors with the message "Undefined offset: 1" which frustrated me because I didn't see them locally. While we chatted about PHP, Laura reminded me about PHP's error reporting levels, and she was spot-on. I bumped up to E_ALL locally and got the same errors as Travis.</p>
<h3>Error Reporting Level</h3>
<p>I spent the next 10 minutes fixing my warnings and notices and realized - <strong>I should always use a higher error level</strong> in PHP. Python will rightfully gripe at me if I try to access a dictionary element by a key that doesn't exist. But <strong>PHP can be equally strict</strong> if I set my error level to E_STRICT or higher. So, I'm adding it to my list:</p>
<ol>
<li>Use a <strong>coding standard</strong></li>
<li>Write <strong>unit tests</strong></li>
<li>Set <strong>error level</strong> to E_STRICT</li>
</ol>
<p>I really think these 3 practices could make any PHP code into good solid code. Instead of simply bashing on PHP, from now on I'm going to simply advise PHP dev's to stick to these practices - it's good for the developers and good for the community.</p>
