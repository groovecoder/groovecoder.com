---
layout: post
status: publish
published: true
title: MDN & Kuma progress
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 584
wordpress_url: http://groovecoder.com/?p=584
date: '2011-06-15 15:07:14 -0500'
date_gmt: '2011-06-15 20:07:14 -0500'
categories:
- mdn
tags:
- mdn
comments:
- id: 299
  author: Robert Kaiser
  author_email: kairo@kairo.at
  author_url: http://home.kairo.at/blog/
  date: '2011-06-16 08:44:19 -0500'
  date_gmt: '2011-06-16 14:44:19 -0500'
  content: Hrm, so Kuma will use the same editor as Deki? And the editor was the main
    reason why I abandoned editing anything on devmo/MDC/MDN. Well, I guess not much
    is lost by keeping me out, in the end. ;-)
- id: 302
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: ''
  date: '2011-06-16 09:55:22 -0500'
  date_gmt: '2011-06-16 15:55:22 -0500'
  content: It will use ckeditor, yeah. I'm not the biggest fan of ckeditor either,
    but changing that would probably be Too Much Change™ all at once. ;)
- id: 9448
  author: Nelson Kelem
  author_email: nelson@safarista.com
  author_url: http://www.safarista.com
  date: '2012-07-13 05:17:34 -0500'
  date_gmt: '2012-07-13 10:17:34 -0500'
  content: "@groovecoder What were you thinking when you named this wikis Kuma and
    Deki?\r\n\r\nSo, say I go to Nairobi Kenya or anywhere in East Africa. Say am
    speaking at a conference at the iHub Centre in Nairobi. I have to tell the audience
    to find more information and resources at Kuma and Deki on MDC/MDN.\r\n\r\nBasically
    this translates to Kuma =&gt; Vagina, Deki =&gt; Penis/Cock. I know Swahili names
    are easy to use and sound awesome. Like Siri, Safari, Mambo, Jumla/Joomla etc.
    But think before you use them. \r\n\r\nHow does a teacher say that to a class
    of young people without looking like an idiot. \r\n\r\nAmend please.\r\n\r\nNelson
    Kelem"
- id: 9461
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2012-07-13 07:46:34 -0500'
  date_gmt: '2012-07-13 12:46:34 -0500'
  content: "We inherited the \"Kitsune\" code from https://support.mozilla.org. \"Kitsune\"
    means \"Fox\" in Japanese. We picked \"Kuma\" - the Japanese word for \"Bear\".\r\n\r\nIt
    wasn't until later that we discovered the Swahili word. :(\r\n\r\nAt some point
    I think Mozilla Webdev should make our code-names more descriptive. We should
    have MDN, SUMO, and AMO; not Kuma, Kitsune, and Zamboni.\r\n\r\nAnyway, in a situation
    where Swahili is widely-known, just refer to the site as \"MDN\". They are synonymous."
---
<p><img class="alignright" title="Kuma will tear you up with fire attacks" src="http://www.sharewallpapers.org/d/518307-2/Kuma.jpg" alt="Kuma will tear you up with fire attacks" width="250" height="200" />I haven't posted in a while for a couple good reasons - I've learned enough django to write more code than words now, and <a href="https://twitter.com/#!/openjck">our new intern</a> has taken over most of the project management work for <a href="https://developer.mozilla.org">MDN</a>. So, I have time and ability to code and I'm using it! I should still post about *what* we're coding, so here we go.</p>
<p>We've done a lot since <a href="http://groovecoder.com/2011/02/10/init/">my first status post</a> 4 months ago. We released <a href="https://developer.mozilla.org/demos/">Demo Studio</a>, <a href="https://developer.mozilla.org/learn">Learning</a>, and <a href="https://developer.mozilla.org/demos/devderby">Dev Derby</a> from our "mdn" branch. I played some small parts in the Demo Studio work, and I implemented the Learning feature while I myself learned our <a href="https://github.com/jbalogh/jingo">jingo</a> and <a href="https://github.com/clouserw/tower">tower</a> libraries.</p>
<p>I did some important but less-visible work - I copied our mdn code from <a href="https://github.com/fwenzel/mdn">our old mdn repository</a> into <a href="https://github.com/mozilla/kuma">our new kuma repository</a>. We maintain an <a href="https://github.com/mozilla/kuma/tree/mdn">mdn branch in kuma</a> where we do main development to push to the live site. The master branch holds all of the kuma-only features. We frequently merge mdn into master to keep master current. I set up continuous integration projects for both <a href="https://jenkins.mozilla.org/job/kuma/">kuma</a> and <a href="https://jenkins.mozilla.org/job/mdn/">mdn</a> on <a href="https://jenkins.mozilla.org/">the Mozilla jenkins server</a>.</p>
<p>All along I've been fielding bugs on our old MindTouch/DekiWiki system and helped prepare our upgrade from MindTouch 9 to MindTouch 10, currently running on the <a href="https://developer-stage9.mozilla.org/En">MDN staging server</a>.</p>
<p>Finally, just last week, I broke free from MDN features &amp; infrastructure to work on the kuma wiki features. The <a href="https://kuma-stage.mozilla.org/en-US/docs/new">kuma wiki</a> is cloned from the <a href="https://github.com/jsocol/kitsune">kitsune</a> wiki that powers <a href="http://support.mozilla.com/">SUMO</a>. So, we're starting with a large solid wiki foundation already. On Thursday I started changing the kuma wiki templates to match our mdn templates. Along the way, I added <a href="http://ckeditor.com">ckeditor</a> to the wiki app (just like our existing MindTouch), removed and/or hid many fields that SUMO requires that we will not, and restored and refactored over 80 wiki unit tests. (Which gave me a nice bump up <a href="https://jenkins.mozilla.org/cigame/?">the Leader board in our cigame</a>.) Now I'm working on article viewing - our implementation is different since we store HTML content rather than wiki markup, so we need to change the way we <a href="https://github.com/jsocol/bleach">bleach</a> content - and I'll work on article previews next. All of this is continuously pushed to <a href="https://kuma-stage.mozilla.org/">our kuma staging server</a>. Very Soon™ we should be able to invite community testers to the staging server to start banging on kuma wiki and giving us feedback.</p>
<p>Outside of my Mozilla work, I gave a Web Application Security talk for <a href="http://tulsawebdevs.org/presentations/tulsa-school-of-dev-2011/">Tulsa School of Dev 2011</a> along with other members of <a href="http://tulsawebdevs.org/">Tulsa Web Devs</a>. I hacked the crap out of a WordPress site right after our other guys promoted WordPress as a great open-source CMS, which it really is; I feel bad to have hacked it in front of a bunch of Microsoft fanboi's, but oh well. Just please PLEASE keep your WordPress updated and be careful about which plugins you install!</p>
<p>Outside of my tech work, my wife and I had our 2nd baby girl on April 8th - River Daphne. It's been quite a learning experience with 2 kids under the age of 2, but we're starting to adapt. I've also made a couple of trips out to <a href="http://clearcreekmonks.org/">Clear Creek Abbey</a> to help Brother Paul start brewing beer for the monks and guests. This last time I got to sample an American Pale, an English Brown, and a Munich Lager - all of them were great; hard to believe Brother Paul has only been brewing a few months.</p>
<p>Enough words. Time for more code.</p>
