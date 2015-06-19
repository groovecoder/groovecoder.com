---
layout: post
status: publish
published: true
title: 'if request.META[''HTTP_DNT''] == 1:'
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 46
wordpress_url: http://groovecoder.com/?p=46
date: '2011-02-14 10:08:12 -0600'
date_gmt: '2011-02-14 16:08:12 -0600'
categories:
- mozilla
tags:
- mozilla
comments: []
---
<p><img src="http://groovecoder.com/wp-content/uploads/2011/02/G.jpg" alt="SUMO Release" title="G" width="200" height="150" class="alignright size-full wp-image-48" /></a> Yesterday I sat in on <a href="http://blog.mozilla.com/webdev/">webdev</a> work group - really just a bunch of webdevs sitting in conference room G ("get to da choppa"). I overheard a discussion that showed me the mission of Mozilla permeates the entire organization. Here's an anonymous summary to protect the guilty and innocent:</p>
<p>Dev 1: Check out this 7-line <a href="http://donottrack.us/">DNT</a> implementation for Site A.<br />
Dev 2: You know the B group is going to hate DNT.<br />
Dev 1: Yeah.<br />
Dev 2: I don't know if it's a battle I want to fight.<br />
Dev 1: It's not what we want - it's what our users want.</p>
<p>It's the same attitude and perspective we had when we first discussed Do-Not-Track at a brown-bag - we should do what our users want. We discussed what Google and Microsoft are implementing, but there are <a href="https://www.eff.org/deeplinks/2011/01/mozilla-leads-the-way-on-do-not-track">problems with cookie blacklists, as the EFF pointed out</a>. The one I heard most at our brown bag was that <a href="http://www.networkadvertising.org/managing/opt_out.asp">NAI "opt out"</a> doesn't specify whether a user opts out of <strong>all tracking</strong> or only out of the <strong>behavioral advertising</strong>. The quote I remember from the <a href="https://wiki.mozilla.org/Privacy/Jan2011_DoNotTrack_FAQ">Mozilla Privacy discussion</a> was: "A Do-Not-Track header is the clearest message a user can send to advertisers that they don't want to be tracked."</p>
<p>It's also the most technically elegant solution. Check the <a href="http://www.networkadvertising.org/managing/opt_out.asp">NAI opt-out page</a> with Firecookie and you see the following opt-out cookie: values - TOptOut: 1 (bing, live.com, MSN), optout: 1 (collectivemedia, criteo), id: OPT_OUT (doubleclick), opt: 1 (fetchback), optout: * (invitemedia), qoo: OPT_OUT (quantserve), NETID01: optout and NETOPTOUT: true (revsci), a: cOPT_OUT (rfihub.com), AO: o=1 (yahoo). And that's just from the dozen networks from which I've opted out. The page shows me at least two dozen more networks from which I still need to opt-out. I just did this exercise a couple weeks ago. How often do I need to visit this page to opt out? Where are these new networks coming from?</p>
<p>And a user doesn't have the same cookies between browsers so they have to get the opt-out cookies on every device (think Desktop, phone, tablet, etc. unless they use Firefox Sync of course), and have to get all the new ones on every device too. Google can help you if you clear your cookies - but  that's the only issue <a href="https://chrome.google.com/webstore/detail/hhnjdplhmcnkiecampfdgfjilccfpfoe">Keep My Opt-Outs</a> seems to address.</p>
<p>Compare all this with a header:</p>
<p>DNT: 1</p>
<p>It's efficient (6 bytes), decentralized, permanent, extensible (DNT: 2, 3, 4, 'all', 'behavior', etc.) and if it comes down to it - enforceable. It isn't a perfect solution, but I love working at an organization with top-notch engineering talent AND a pervasive focus on the mission to make the web better for everyone. Mozilla FTW.</p>
