---
layout: post
status: publish
published: true
title: HTML5 App Stores don't go too far enough
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 1075
wordpress_url: http://groovecoder.com/?p=1075
date: '2013-01-22 10:35:06 -0600'
date_gmt: '2013-01-22 16:35:06 -0600'
categories:
- dev
- tech
- greatest-hits
tags:
- html5
comments:
- id: 53017
  author: Ambrose Little
  author_email: ambrogio@gmail.com
  author_url: http://ambroselittle.com
  date: '2013-01-22 14:48:24 -0600'
  date_gmt: '2013-01-22 20:48:24 -0600'
  content: "I replied to your comment on my blog with some more rationale for choosing
    apps.\r\n\r\nI just don't see it, unless the platform vendors do work to make
    the Web app experience better, and it's not really in their best interests to
    do that.  I like your idea of integrated Web app search. I do think Web app dominance
    will be dependent on, to put it simply, user experience of the apps (regardless
    of how you find them). Right now things are still tilted in favor of native from
    an experience perspective, but it doesn't have to stay that way.  Again, it will
    require the platforms continued investment, but they have a chunk of change to
    lose, so I just don't see it happening.\r\n\r\nI also don't think your analogy
    of the shelf works because devices are much more of a closed system than generic
    Web.\r\n\r\nI will say that the thing I don't care for about the phone gap approach
    is that it is somewhat deceptive to users. It sorta puts on this facade of being
    native while it's not, and often times it is obvious that it is not. That's a
    frustrating experience for people."
- id: 53067
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-22 16:56:52 -0600'
  date_gmt: '2013-01-22 22:56:52 -0600'
  content: "That's why Firefox OS - or something like it - is so important. The entrenched
    devices and platforms won't embrace an open (i.e., web) approach to mobile unless
    or until we - designers, developers, and our users - make it awesome.\r\n\r\nEmulating
    and copying their closed systems is a waste.\r\n\r\nCurious - you like integrated
    web app search? What if that search could deep-link into the web apps' content
    that is most relevant? Because that's basically what the web is. :)"
- id: 53651
  author: Les Orchard
  author_email: me@lmorchard.com
  author_url: http://blog.lmorchard.com/
  date: '2013-01-23 12:03:00 -0600'
  date_gmt: '2013-01-23 18:03:00 -0600'
  content: "Have you seen or used Google Now on Android? It kind of works the way
    you want, contextually speaking.\r\n\r\nIt's early days yet, but it often delightfully
    surprises me by offering up directions on my phone to a place I looked for on
    my desktop 20 minutes ago. It knows what restaurants are nearby and often shows
    them when it's mealtime.\r\n\r\nThere's no technical reason why, given the kind
    of metadata you've laid out, that something like Google Now couldn't spider it
    and tell you about \"pages and apps for places near you\" and just automatically
    surface the pizza place's site and its app. (Which, really, could be the same
    thing)\r\n\r\nI know we (mozilla) are building a nice though rather bog standard
    marketplace right now, but I wonder if 2.0 or 3.0 of that product could be something
    more webby and extend the whole OWA JSON manifest concept in exactly the way you
    say?"
- id: 53681
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-23 12:51:32 -0600'
  date_gmt: '2013-01-23 18:51:32 -0600'
  content: "You mean Google Now only on Android 4.1+ ? ;) That's part of the problem!!\r\n\r\nBut
    yeah - I really hope we push thru and past the whole app/store model and into
    contextual data delivered via the open web."
---
<p><strong>tl;dr</strong> - HTML5 app stores don't leverage the web as much as we should.</p>
<p style="text-align: center;"><img class="aligncenter" alt="Futurama Political Debate" src="http://www.mememaker.net/static/images/memes/854247.jpg" width="400" height="266" /></p>
<p> I'm convinced that <a href="http://groovecoder.com/2013/01/07/packaged-html5-apps-are-we-emulating-failure">packaging HTML5 apps for stores is emulating failure</a>. There are lots of reactions. Among the comments here, <a href="http://blog.lmorchard.com/">Les</a> made the opposite assertion of mine - "<strong>where app stores win over plain old URLs is discoverability. ...</strong> <strong>URLs are precise, but they’re sharp and pokey for most people to handle.</strong>"</p>
<h3>HTML5 App search engine &gt; Pokey URLs</h3>
<p>Les made his own counter-point that we fixed pokey URL's with search engines. So,<strong> do we need "a special case search engine where the results are constrained [to HTML5 apps]"? </strong></p>
<p>Maybe.</p>
<p>The "webby" approach is to crawl the web to build an index of all <a href="http://www.brucelawson.co.uk/2011/installable-web-apps-and-interoperability/">app manifests.</a> But how can we discover the manifests? <strong>None of the HTML5 app stores document a way to hyperlink manifests.</strong><strong><br />
</strong></p>
<p>But maybe we can use <a href="http://schema.org/SoftwareApplication">schema.org SoftwareApplication type, with its convenient installUrl property</a>. We can even use the WebApplication sub-type's 'browserRequirements' property to designate a Firefox, Chrome, or W3C manifest. So Incredible Pizza could expose their HTML5 app like so:</p>
<pre>&lt;div itemscope itemtype="http://schema.org/WebApplication"&gt;
  &lt;a itemprop="installUrl" href="http://app.incrediblepizza.com/incrediblepizza.webapp"&gt;&lt;span itemprop="name"&gt;Incredible Pizza&lt;/span&gt; for &lt;span itemprop="browserRequirements"&gt;Firefox&lt;/span&gt;&lt;/a&gt;
  &lt;a itemprop="installUrl" href="http://app.incrediblepizza.com/incrediblepizza.crx"&gt;&lt;span itemprop="name"&gt;Incredible Pizza&lt;/span&gt; for &lt;span itemprop="browserRequirements"&gt;Chrome&lt;/span&gt;&lt;/a&gt;
  &lt;a itemprop="installUrl" href="http://app.incrediblepizza.com/incrediblepizza.wgt"&gt;&lt;span itemprop="name"&gt;Incredible Pizza&lt;/span&gt; for &lt;span itemprop="browserRequirements"&gt;Opera, Windows Phone&lt;/span&gt;&lt;/a&gt;
&lt;/div&gt;</pre>
<p>Voilà. We have web technology to make an HTML5 App search engine.<strong> But why are HTML5 app stores making developers manually submit manifest URLs to directories when we could leverage hyperlinks - the central nervous system of the web? </strong>As a bonus, a hyperlink-fueled HTML5 app search engine is complimentary to existing mobile platforms. This could be nice:</p>
<p style="text-align: center;"><a href="https://dl.dropbox.com/u/21969365/images/blogging/ios_search_apps.png"><img class="aligncenter" alt="iOS App Search mockup" src="https://dl.dropbox.com/u/21969365/images/blogging/ios_search_apps.png" width="219" height="429" /></a></p>
<h3>Apps contextualize content</h3>
<p>Still, an HTML5 app search engine doesn't leverage the web as much as we could. <a href="http://ambroselittle.com/2013/01/16/no-packaged-html5-apps-are-we-emulating-failure/">Ambrose Little suggests "discoverability is worse</a> [on the web] because it’s not just apps, it is all kinds of content, much of which is not pertinent nor optimized for your device." This gets to the crux of the issue: outside of pure experience apps like games,<strong> when we say we want apps, what we really want is relevant, contextual, optimized content on our mobile devices</strong>. Can we deliver relevant, contextual, optimized content to mobile devices without apps?</p>
<p>In <a href="http://amzn.com/0596807783">Programming the Mobile Web</a>, Maximiliano Firtman touches on this in his chapter about geolocation:</p>
<blockquote><p>One of the great features of mobile devices is that they can go everywhere with us. That is why the <em>where</em> is very important context to be considered by our websites. Knowing the user's location can help us to show useful contextual information -Firtman</p></blockquote>
<p>Geolocation is a great place to start, since it's so widely supported on existing mobile browsers. I suggested that incrediblepizza.com could return location-specific content using a captive wifi portal or geolocation. But <strong>fuzzy search can also deliver location-specific content</strong>, as Google Maps does; though it could be improved to deep-link into a domains' pages with something like <a href="http://geourl.org/">GeoURL</a> or a <a href="http://en.wikipedia.org/wiki/Geo-fence">geofenced</a> sitemap.</p>
<p>I.e., if incrediblepizza.com added:</p>
<pre>&lt;meta name="geo.position" content="36.05877;-95.8831" /&gt;
&lt;meta name="ICBM" content="36.05877, -95.8831" /&gt;</pre>
<p>to their <a href="http://www.incrediblepizza.com/locations/tulsa">Tulsa store location page</a>, and maybe add a geo point and radius to their sitemap:</p>
<pre>&lt;url xmlns:geo="http://geositemaps.org"&gt;
   &lt;loc&gt;http://www.incrediblepizza.com/locations/tulsa&lt;/loc&gt;
   <em>&lt;lastmod&gt;2013-01-01&lt;/lastmod&gt;
   &lt;changefreq&gt;daily&lt;/changefreq&gt;
   &lt;priority&gt;0.8&lt;/priority&gt;
   &lt;geo-radius&gt;36.05877;-95.8831;30&lt;/geo-radius&gt;</em>
&lt;/url&gt;</pre>
<p>mobile search could do something like this:</p>
<p style="text-align: center;"><a href="https://dl.dropbox.com/u/21969365/images/blogging/ios_search_pizza.png"><img class="aligncenter" alt="iOS Search for Pizza" src="https://dl.dropbox.com/u/21969365/images/blogging/ios_search_pizza.png" width="219" height="429" /></a></p>
<h3>Search already works</h3>
<p>We can search for a pizza place nearby. So what? Foursquare already does that.</p>
<p>But do we have to search for it? As predicted by <a href="http://www.forbes.com/2009/07/29/microsoft-yahoo-merger-opinions-contributors-mike-masnick.html">Mike Masnick back during Yahoo's misguided deal with Microsoft in 2009</a>, "People are discovering that information finds them, rather than them going in search of information. Search already works.<strong> The next interesting challenge is in improving the way information finds you</strong>, rather than the way you find information."</p>
<p><strong>Improving the way information finds you</strong> is how social competes with search, and <strong>it's the way mobile web should compete with app stores</strong>. Location, time, personal information, preferences, friends, actions - all of these create the context in which information should find us. <a href="http://techcrunch.com/2010/05/25/facebook-foursquare-and-google-talk-the-future-of-mobile/">Chris Cox from Facebook</a> summed it up:</p>
<blockquote><p>[Mobile phones] should be contextually aware. Check-in to flights, find deals at grocery stores, etc. These things take a bunch of clicks now — it’s all wasting time. The phone should know what we want.</p></blockquote>
<p>My phone should know:</p>
<ol>
<li>I have 2 kids under the age of 4</li>
<li>We're near south Tulsa</li>
<li>We typically eat out on Tuesday nights</li>
<li>It's almost dinner-time</li>
</ol>
<p>It should query the web. To which incrediblepizza.com replies:</p>
<ol>
<li>Kids 3 and under eat free</li>
<li>We're located in south Tulsa</li>
<li>We have double-play-points specials on Tuesdays</li>
</ol>
<p>incrediblepizza.com and my phone inform me automatically. This touches semantic web stuff; and maybe that's something we mobile web developers <em>should</em> be touching. Because ...</p>
<h3>The only group who can contextualize everything is everyone</h3>
<p><strong>The web will obsolete app stores ... again.</strong> In Scott Jenson's "<a href="http://vimeo.com/33692624">Why Mobile Apps Must Die</a>" talk at BDConf 2011, he longs for a web-based phone, and a discovery service that helps us find the right needles in the needle-stack of connected things. He calls it "a baby step towards this idea of doing just-in-time interaction" and says "I can guarantee you this will not happen thru apps."</p>
<p>Why not?</p>
<p><a href="http://christianheilmann.com/2013/01/15/packaged-apps/">Christian reminds us</a> of<strong> Yahoo's first (failed) attempt at re-creating a categorized directory of the web.</strong> If you don't have time to read <a href="http://www.shirky.com/writings/ontology_overrated.html">Clay Shirky's classic perspective on ontology</a> at least watch this great related 5-minute video:</p>
<p><iframe src="http://www.youtube.com/embed/NLlGopyXT_g" height="480" width="640" allowfullscreen="" frameborder="0"></iframe></p>
<p>Even if you skipped both, here's the crux of the matter (emphasis mine):</p>
<blockquote><p>Yahoo ... <i>added the shelf back</i>. ... The charitable explanation for this is that they thought of this ... as their job, and as something their users would value. The uncharitable explanation is that they thought there was business value in determining the view the user would have to adopt to use the system. Both of those explanations may have been true at different times and in different measures, but <strong>the effect was to override the users' sense of where things ought to be, and to insist on the Yahoo view instead</strong>.</p></blockquote>
<p>You can replace "Yahoo" with "Apple" in the preceding statement and it mirrors the current situation of Apps. The web out-grew Yahoo's shelf; it will out-grow Apple's, Google's, Microsoft's, and Mozilla's shelves. Our sense of where things ought to be and how things ought to find us is better than any vendor's. "The web is going to win again. The web always wins." as Johnath says.</p>
<p>The web will win sooner if we spend less time on the shelves and more time delivering relevant, contextual, optimized content to mobile devices.</p>
