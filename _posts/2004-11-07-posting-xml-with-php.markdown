---
layout: post
title: posting XML with PHP
date: '2004-11-07 21:54:00 -0600'
categories:
- Uncategorized
tags: []
comments: []
---
<div style="text-align: justify;">a more technical entry.</p>
<p>for a pilot project involving php web services, I had the task of making an HTTPS post to the UPS Rate Service Selection <a href="http://www.ec.ups.com/ecommerce/gettools/gtools_intro.html">online tool</a>. their online tool requires that you post to them 2 XML documents in the payload of your HTTPS post. I had some problems doing this, but did resolve them...</p>
<p>first, I had a problem using fsockopen function in PHP because, alas, I am developing on a Windows machine now, and didn't want to set up another Linux server just for this...so, I decided to use cURL extension for PHP instead of fsockopen. but again, cURL is a little tricky to <a href="http://www.tonyspencer.com/mt/archives/2003/10/curl_with_php_a.htm">get working on Windows</a>, but it did what I needed.</p>
<p>the resulting code will probably be up at the <a href="http://www.lamp5.net/">lamp5 website</a> in a tutorial sometime soon. and the full pilot project will be posted sometime in December.<br />
</div>
