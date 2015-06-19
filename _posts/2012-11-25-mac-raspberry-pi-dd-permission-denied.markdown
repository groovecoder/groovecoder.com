---
layout: post
status: publish
published: true
title: mac raspberry pi dd permission denied
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 960
wordpress_url: http://groovecoder.com/?p=960
date: '2012-11-25 10:43:50 -0600'
date_gmt: '2012-11-25 16:43:50 -0600'
categories:
- tech
tags:
- raspberry pi
- mac
comments:
- id: 41427
  author: Russ
  author_email: rfmcmillan@gmail.com
  author_url: ''
  date: '2013-01-03 20:06:45 -0600'
  date_gmt: '2013-01-04 02:06:45 -0600'
  content: Incredible. I just did like you said and blew out the SD card slot on my
    iMac and it worked! Thanks!
- id: 51946
  author: Ed Daw
  author_email: eddaw1@gmail.com
  author_url: ''
  date: '2013-01-21 04:36:30 -0600'
  date_gmt: '2013-01-21 10:36:30 -0600'
  content: I had the same problem. In my case the memory card I bought had a lock
    tab on it that was getting pushed over into the lock position when I inserted
    the memory card into the receptacle on the pi. Once I realised this and inserted
    the card more carefully - no more problems. A blob of superglue might be heading
    in the direction of that lock tab soon!
- id: 58455
  author: DUSTIN REEVES
  author_email: dustin.reeves@gmail.com
  author_url: ''
  date: '2013-02-03 23:06:33 -0600'
  date_gmt: '2013-02-04 05:06:33 -0600'
  content: "i cant believe this, i couldnt figure out for the life of me why i was
    getting permission errors, my though process \"im running root ?, ive unmounted
    the disk?, wtf?\"\r\n\r\nthank you for this helpful post."
- id: 61705
  author: Kevin K
  author_email: kkuhl05@gmail.com
  author_url: ''
  date: '2013-02-15 19:47:59 -0600'
  date_gmt: '2013-02-16 01:47:59 -0600'
  content: If you ordered through CanaKit, be sure to try the "locked" position of
    your SD card. I thought the above was my issue but apparently, the lock switch
    was put in backwards in the card shipped with my kit!
- id: 74202
  author: Ronnie H
  author_email: ronhashjr@gmail.com
  author_url: ''
  date: '2013-05-18 13:14:37 -0500'
  date_gmt: '2013-05-18 18:14:37 -0500'
  content: Hah, blowing the dust out of the SD card slot worked for me also. Thanks
    for the tip! And thanks for the flashback of the Nintendo days :)
---
<p><strong><img class="alignleft" title="Raspberry Pi Grayscale Logo" src="http://www.adafruit.com/adablog/wp-content/uploads/2012/10/OccidentalisLogo.png" alt="Raspberry Pi Grayscale Logo" width="281" height="358" />tl;dr</strong> - <em>If you get "permission denied" errors while trying to dd a raspberry pi disk image on your macbook pro, try blowing out your sd card slot to unset its "disk lock" switch. Seriously</em>.</p>
<p>I love Mac's for the almost-linux environment coupled with a nice, rich, high-performance GUI. But every once in a while we Mac users have to search a couple extra error messages when we try to do more "linuxy" stuff - e.g., preparing a raspberry pi sd card.</p>
<p>This morning I got my HDMI cord for my pi, so I went thru the <a href="http://www.raspberrypi.org/quick-start-guide">raspberry pi quick start guide</a> including the <a href="http://elinux.org/RPi_Easy_SD_Card_Setup">easy sd card setup</a>. But, even though I unmounted the disk and ran `dd` with `sudo` I still got "Permission denied"</p>
<p>I googled for this blog post title and found <a href="http://www.raspberrypi.org/phpBB3/viewtopic.php?f=5&amp;t=5561">a topic on the Raspberry Pi forums</a>, but the answer that seemed to work for most people was down at the bottom of the thread. So I'm re-posting it here, because it's funny, and so someone else having the same problem might fix it faster.</p>
<p>Apparently, 15" 2010 MacBook Pro's built-in SD card reader's get stuck in the write-locked position. So bust out your old Nintendo skills and give it a blow to clear it out. If you never had an NES, your weak under-trained lungs might need you to use a compressed air can instead. Pansy.</p>
