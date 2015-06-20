---
layout: post
status: publish
published: true
title: 'Packaged HTML5 Apps: Are we emulating failure?'
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 986
wordpress_url: http://groovecoder.com/?p=986
categories:
- dev
- tech
- greatest-hits
tags:
- html5
comments:
- id: 43799
  author: Wes Johnston
  author_email: wjohnston@mozilla.com
  author_url: ''
  date: '2013-01-08 03:22:22 -0600'
  date_gmt: '2013-01-08 09:22:22 -0600'
  content: "I had a conversation that was very similar to this with my wife last week.
    Despite my conviction that typing a few letters in the urlbar is as easy, if not
    easier than navigating an app store (and I'll only install an app if its something
    I'm really passionate about having handy all the time), she feels the exact opposite.
    Its one of the major things that makes me really hopeful for open web marketplaces.
    i.e. Anything that isn't a highly graphical set of search results with big plush
    install buttons seems doomed to be declared \"too hard\" by a large subset of
    users.\r\n\r\nBut I firmly believe that in 5 years we'll all be looking back and
    saying \"I can't believe people had to install an app just to check their email\"."
- id: 43858
  author: Ian Thomas (@ianmthomasuk)
  author_email: ian@ithomas.name
  author_url: http://ithomas.name/
  date: '2013-01-08 05:33:20 -0600'
  date_gmt: '2013-01-08 11:33:20 -0600'
  content: 'I think you touch on the benefits of an app with your last point: you
    get a free advert in the platform''s app store and, after installation, in the
    list of apps on the phone. With a mobile website you need to type the URL in each
    time. If the mobile vendors could let you do that with an enhanced bookmark thing
    then we might be able to forget about native apps (or at least PhoneGap).'
- id: 43909
  author: Matěj Cepl
  author_email: mcepl@redhat.com
  author_url: http://matej.ceplovi.cz/blog
  date: '2013-01-08 07:15:47 -0600'
  date_gmt: '2013-01-08 13:15:47 -0600'
  content: There is a third reason why people prefer apps/packaged webapps ... some
    fundamental permissions missing. The fact that I cannot create a HTML5-offline-capable
    podcatcher as a webapp (because of single-origin XMLHttpRequest limitation; and
    no, I don’t want to proxy downloads of zillion multimegabyte media files over
    my server) seems to suggest to me that there is something wrong somewhere. I know
    making cross-origin XMLHttpRequest safe enough would be very difficult, but unless
    we are unable to resolve hard issues we are making webapps less functional alternative
    to native apps (http://www.youtube.com/watch?v=32wer_j5soQ).
- id: 43911
  author: Matěj Cepl
  author_email: mcepl@redhat.com
  author_url: http://matej.ceplovi.cz/blog
  date: '2013-01-08 07:17:23 -0600'
  date_gmt: '2013-01-08 13:17:23 -0600'
  content: (BTW, you Persona login is broken ... at least doesn't work for me with
    FF/Nightly).
- id: 43924
  author: Les Orchard
  author_email: me@lmorchard.com
  author_url: http://lmorchard.com
  date: '2013-01-08 07:48:41 -0600'
  date_gmt: '2013-01-08 13:48:41 -0600'
  content: "This also makes me wonder: Why don't mobile browsers have built-in QR
    code readers? (and maybe RFID integration?)\r\n\r\nAs it's one of the great problems
    in computer science, naming things is hard. Having worked at several ad agencies,
    I'll tell you that human-friendly URLs get complicated, especially on large global
    sites. That \"incrediblepizza.com\" URL becomes something like \"incredible-pizza.pizzapalace.info/2013/campaigns/43/?fooid=8675309\"
    because:\r\n\r\n* We couldn't afford incredible pizza.com\r\n* Our content is
    grouped by year, by site policy\r\n* We're running a few dozen campaigns, tailored
    by market\r\n* Metrics told us to put that ?fooid thing on there\r\n\r\nOf course,
    URL shorteners can help here. But, that wasn't even a thing when I was last doing
    a lot of work at agencies. And sometimes, clients demand URLs look a certain way,
    for reasons unexplainable or unquestionable.\r\n\r\nThis is also a spot where
    Facebook and geolocation will trump URLs. If Facebook knows you're at Pizza Palace,
    and Pizza Palace is a client, they can take care of the rest."
- id: 43930
  author: Les Orchard
  author_email: me@lmorchard.com
  author_url: http://lmorchard.com
  date: '2013-01-08 07:55:46 -0600'
  date_gmt: '2013-01-08 13:55:46 -0600'
  content: "But all that said about funky marketing URLs and geolocation - I think
    where app stores win over plain old URLs is discoverability. \r\n\r\nURLs are
    precise, but they're sharp and poky for most people to handle. \r\n\r\nAn app
    store lets you be fuzzy: Just get to this one place, and fat-finger in something
    like an app name (you can even misspell it), and you'll probably find what we
    were trying to get you to find.\r\n\r\nOf course, we already have something like
    this for URLs: it's called a search engine. For HTML5 apps, this just becomes
    a special case search engine where the results are constrained. \r\n\r\nIt's also
    handy to have an app store as a special case, because people understand the UI
    better: I'm not just searching for random info on the web, I'm searching for a
    thing that does stuff and lives semi-permanently on my phone. In implementation,
    that might just also just be a special case of bookmark, but the mental model
    is different enough to be important."
- id: 43958
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 08:56:24 -0600'
  date_gmt: '2013-01-08 14:56:24 -0600'
  content: "IMO, that free advert in the app store is worse than nothing, because\r\n\r\n1.
    “The closest thing I’ve seen to a ‘business model’ for marketing iPhone apps is
    to advertise like crazy until you get into the top 50,” says David Barnard of
    AppCubby. “Once you’re there, the top 50 list will start generating its own buzz...But
    that’s not a business model, that’s like rolling the dice at a casino.” (http://www.fastcompany.com/1792313/striking-it-rich-app-store-developers-its-more-casino-gold-mine)\r\n\r\n2.
    Your users will suffer from the WebView experience. I'd love to see numbers of
    return users between WebView apps and their equivalent mobile web versions."
- id: 43960
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 08:57:22 -0600'
  date_gmt: '2013-01-08 14:57:22 -0600'
  content: I really hope you're right. The way we look back at AOL, CompuServe, and
    Prodigy now. ;)
- id: 43962
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 08:58:14 -0600'
  date_gmt: '2013-01-08 14:58:14 -0600'
  content: I don't think it's difficult to make cross-origin XMLHttpRequest safe?
    https://developer.mozilla.org/docs/HTTP/Access_control_CORS
- id: 43966
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 09:00:21 -0600'
  date_gmt: '2013-01-08 15:00:21 -0600'
  content: "I cringe at the thought of Facebook \"taking care\" of more than they
    already do.\r\n\r\nMore interesting to me would be a geolocation/geofencing extension
    to the sitemaps protocol. i.e., Incredible Pizza can tag their Tulsa pages with
    geofencing metadata to tell search engines which of their pages are most relevant
    to geolocations."
- id: 43968
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 09:01:53 -0600'
  date_gmt: '2013-01-08 15:01:53 -0600'
  content: Again, an App extension to the sitemap protocol could help with app discoverability.
- id: 43970
  author: Keith Gable
  author_email: ziggy@ignition-project.com
  author_url: http://www.ignition-project.com/
  date: '2013-01-08 09:03:00 -0600'
  date_gmt: '2013-01-08 15:03:00 -0600'
  content: "I think the right solution is to make it possible to install HTML5 apps
    from app stores. Just like visiting incrediblepizza.com, except it's in the store.
    It's just a bookmark though, so it's very lightweight to download and keep updated.
    Perhaps also make expanded permissions available.\r\n\r\nClients I work with either
    want an enterprise deployed app or an app in the app store. And if you can't deliver
    because you're trying to talk them out of it, they go somewhere else. But, on
    the other hand, if you were able to say \"yeah, we can get you in the app store
    and get you a website for people who don't want to install the app and it'll be
    the same cost\", people will go for it. But first, the app stores would have to
    allow that. (And unfortunately, just wrapping the site with PhoneGap doesn't work
    on iOS because that's against the rules.)"
- id: 43979
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 09:16:24 -0600'
  date_gmt: '2013-01-08 15:16:24 -0600'
  content: I'd be interested to hear a client's reaction to a purely URL-driven experience.
- id: 43987
  author: Robert Kaiser
  author_email: kairo@kairo.at
  author_url: http://home.kairo.at/blog/
  date: '2013-01-08 09:37:30 -0600'
  date_gmt: '2013-01-08 15:37:30 -0600'
  content: Unfortunately, with Firefox OS, we end up having a large number of apps
    in yet another packaged format, and without that, they don't get permissions to
    more delicate Web APIs. I hope you find that as unfortunate as me and I hope somehow
    a way can be found to make things more "webby" in the future.
- id: 43990
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 09:42:10 -0600'
  date_gmt: '2013-01-08 15:42:10 -0600'
  content: Do you know why we couldn't (re-)use the W3C Packaged Web Apps standard?
- id: 43998
  author: Scott Lowe
  author_email: me@scottdlowe.com
  author_url: http://scottdlowe.com
  date: '2013-01-08 09:56:47 -0600'
  date_gmt: '2013-01-08 15:56:47 -0600'
  content: "The link in this quote is broken: \"... although many brands and creative
    agencies believe that they need to develop iPhone apps, what they need in reality
    is a good mobile site. It costs less to develop, manage and work across all handsets.
    - HTML5 - The End of Apps | Mobile Europe\"\r\n\r\n:)"
- id: 43999
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 09:59:39 -0600'
  date_gmt: '2013-01-08 15:59:39 -0600'
  content: Fixed. Thanks!
- id: 44106
  author: Peter Bengtsson
  author_email: mail@peterbe.com
  author_url: http://www.peterbe.com
  date: '2013-01-08 13:02:30 -0600'
  date_gmt: '2013-01-08 19:02:30 -0600'
  content: "I think you're entering the dark magic realm of marketing. \r\n\r\nHaving
    \"www.incrediblepizza.com\" somewhere in your browser history isn't as sexy as
    an Incredible Pizza app shining in your face."
- id: 44114
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 13:11:23 -0600'
  date_gmt: '2013-01-08 19:11:23 -0600'
  content: Maybe. But how many people have a Facebook app shining in their face on
    their desktop?
- id: 44124
  author: rakkarage
  author_email: rakkarage@gmail.com
  author_url: http://dekogame.ca
  date: '2013-01-08 13:32:55 -0600'
  date_gmt: '2013-01-08 19:32:55 -0600'
  content: google goggles can deal with qr codes btw
- id: 44156
  author: Darren Gibson
  author_email: zarthross@gmail.com
  author_url: ''
  date: '2013-01-08 14:39:25 -0600'
  date_gmt: '2013-01-08 20:39:25 -0600'
  content: "I agree that many of the HTML5 'Apps' in appstores (android or otherwise)
    really don't serve much of a purpose: e.g.  \"Domino's\", \"Papa John's\", \"Incredible
    Pizza\", \"NPR News\" and are better served with fast mobile websites, there are
    some exceptions. \r\n\r\nNotifications.  \r\n\r\nAny app that currently needs
    to be able to notify the user can't use native notifications without doing an
    App.  Facebook, IM and other messaging apps are good examples.  Sure, we can all
    use email notifications instead of native notifications, but many of us do not
    want to clutter our email, and would like real time updates and not have to go
    through our mail to see a facebook update.  \r\n\r\nWhat might be a good idea
    though for future HTML5(6 maybe?) mobile web apps would be to allow web apps to
    do notifications like native apps do."
- id: 44162
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 14:51:15 -0600'
  date_gmt: '2013-01-08 20:51:15 -0600'
  content: "https://dvcs.w3.org/hg/notifications/raw-file/tip/Overview.html is supported
    by desktop Chrome and Safari, and Mobile Firefox, Amazon, and BlackBerry browsers.
    ;)\r\n\r\nWhat do you think about using SMS for mobile notifications?"
- id: 44250
  author: m1879
  author_email: m1879@earthlink.net
  author_url: ''
  date: '2013-01-08 18:04:07 -0600'
  date_gmt: '2013-01-09 00:04:07 -0600'
  content: "You may have seen them, but there have been long discussions on why this
    was done on the dev-webapps email list (and others I think) starting early in
    2012. Much of it was summarized here:\r\n\r\nhttps://wiki.mozilla.org/Apps/Security\r\n\r\nJust
    curious: with a website how would you handle giving access to some of the upcoming
    Web APIs like contacts, camera, phone, etc. etc?\r\n\r\nBy the way I could not
    sign in with Persona until I wrote a comment. Intentional?"
- id: 44265
  author: erose
  author_email: erose@mozilla.com
  author_url: ''
  date: '2013-01-08 18:39:08 -0600'
  date_gmt: '2013-01-09 00:39:08 -0600'
  content: I'm a bit unusual here, but each SMS costs me 20¢.
- id: 44275
  author: Erik Rose
  author_email: erik@mozilla.com
  author_url: https://github.com/erikrose
  date: '2013-01-08 18:57:58 -0600'
  date_gmt: '2013-01-09 00:57:58 -0600'
  content: "I \"live\" on the web less than a lot my fellow Mozillians, not for any
    philosophical reasons but for a few practical ones:\r\n\r\n1. The browser is a
    worse application switcher and window manager than my desktop OS. (Butler, distinctive
    window shapes, spatial positioning, etc.)\r\n2. Web app UIs are inconsistent.
    Standard widgets, nav schemes, and text sizes save my brain for more important
    things.\r\n3. Desktop apps usually have more (and more consistent) keyboard shortcuts,
    letting me work faster.\r\n\r\nSo my use of the web is limited to tasks where
    my primary goal is collaboration or fetching data (Github, Bugzilla, Wikipedia).
    The transparent upgrades are great, and it's handy to be able to pass URLs around.\r\n\r\nInterestingly,
    mobile makes #1 and #3 go poof, so if we can provide the consistency bit on Firefox
    OS (through our examples, guidelines, and dev tools), we might win over even curmudgeons
    like me. :-)"
- id: 44342
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-08 21:57:24 -0600'
  date_gmt: '2013-01-09 03:57:24 -0600'
  content: "I love the way Geolocation and local storage ask for permission as-needed.
    So something like, \"This website wants to access your contacts/camera/phone.
    [Allow] [Deny] [] Always\"\r\n\r\n?"
- id: 44412
  author: fabrice
  author_email: fabrice@desre.org
  author_url: ''
  date: '2013-01-09 01:03:06 -0600'
  date_gmt: '2013-01-09 07:03:06 -0600'
  content: "Asking user to make security-related decisions is a bad idea in general
    because the user only wants things to work and does not understand the implications
    in general.\r\n\r\nGeolocation and local storage are relatively easy to understand,
    but some other permissions much less. Take a look at https://mxr.mozilla.org/mozilla-central/source/dom/apps/src/PermissionsTable.jsm
    to see how diverse and too technical this can be."
- id: 44461
  author: Matěj Cepl
  author_email: mcepl@redhat.com
  author_url: http://matej.ceplovi.cz/blog
  date: '2013-01-09 03:27:51 -0600'
  date_gmt: '2013-01-09 09:27:51 -0600'
  content: Not unless the server-side cooperates. Which is not the case with 99% podcast-serving
    sites.
- id: 44589
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 07:05:21 -0600'
  date_gmt: '2013-01-09 13:05:21 -0600'
  content: I'm not a UX pro, but I don't necessarily agree. When it was first introduced
    - in 2008 - geolocation wasn't easy for the average user to understand. But it
    seems we could group permissions for things like 'settings', 'audio', 'storage'
    and provide an anitial checkbox like []Always allow for this site or []Always
    allow for all sites. Some UX Mozillian wrote a blog post specifically about permissions
    but I can't remember who or where it was. :(
- id: 44591
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 07:11:22 -0600'
  date_gmt: '2013-01-09 13:11:22 -0600'
  content: "I'm right with you on #1 and #3! I love it when webapps provide keyboard
    shortcuts - gmail, github, etc. - but not enough of them do.\r\n\r\nHowever, the
    web gave us the most consistent and universal UI ever conceived - the humble hyperlink.
    Train yourself to use the \"Quick find within link-text only\" firefox key (')
    and you'll get #2 and #3 on the web."
- id: 44730
  author: Matt Galloway
  author_email: matt@architactile.com
  author_url: http://architactile.com
  date: '2013-01-09 11:06:06 -0600'
  date_gmt: '2013-01-09 17:06:06 -0600'
  content: "Grrrr. Damn you, Luke Crouch.\r\n\r\nYes, HTML5 apps are awesome. Yes,
    HTML5 apps could and SHOULD be used more often then they currently are. \r\n\r\nBut
    NO, your Incredible Pizza example is not a good example of why. Why not? Because
    the Incredible Pizza example is a example of why most marketing people suck...not
    why apps suck.\r\n\r\nFirst off, QR codes are so 2010. In the US they were a largely
    failed marketing experiment, partially because of poor usage by marketers as exhibited
    in your example. Markets gets all giddy and self-affirming when they feel like
    they are using technology by putting a QR code on something they it never occurs
    to them what happens when a customer actually tries to use the code. I've seen
    dozens and dozens of examples of QR codes that were in places where they are not
    practical to use (tiny ones on billboards, QR codes on the moving objects like
    buses). It's way to common that QR codes are not accompanied by a human readable
    URL . In most cases a shorted or creative URL is more effective than the QR code.
    But the biggest offense with QR is not designing the experience of where the QR
    code leads. The most common mistake is to take someone to a non-mobile friendly
    web page. Complete. Utter. Failure.\r\n\r\nIn the Incredible Pizza case, if you
    can't engineer a URL to take the user to the actual check-in page, or better yet
    to actually check them in then the QR code should have never been used to begin
    with. Furthermore, most people that know what \"Check-In on Facebook\" means have
    a Facebook app on their phone (Yes. That's right, I said it. AN APP. RIGHT THERE
    ON THEIR PHONE.) and are only distracted, as you were, by the QR code.\r\n\r\nAs
    for discover-ability... in this case, I would argue that it's still a marketing
    mistake, not a technology one. Why on earth would Incredible Pizza direct the
    user to not one, but TWO apps or websites that aren't Incredible Pizza? A huge
    part of the (general) failing of QR was a lack of understanding by the general
    public. If you have to educate people about QR you've already lost.\r\n\r\nSmart
    marketers would have a QR code go to a web page that detected the mobile OS and
    then redirected to their own app in either the App Store or Google Play as appropriate.
    (And of course provide an easy, short human readable URL to the same). This solves
    the discoverability problem (and yes, it also works for HTML5 apps).\r\n\r\nAs
    far as installation. I agree, installation on Android sucks. It doesn't on iOS.
    Meh. \r\n\r\nGeneralized discover on iOS is better than Android (and HTML5 apps)
    because there's only one place to look: the App Store. The key is naming your
    app correctly and out-of-store marketing. \r\n\r\n...bottom line is that the moral
    here is one of poor use of QR, not one of native app vs. HTML5."
- id: 44776
  author: Mark in A2
  author_email: mark@mobyus.com
  author_url: http://mobyus.com/
  date: '2013-01-09 12:38:51 -0600'
  date_gmt: '2013-01-09 18:38:51 -0600'
  content: "Great discussion, and I largely agree with everything you say.  Good timing
    for me as I just built my Sencha app in a native wrapper for the first time yesterday
    and actually noticed that it is a bit more sluggish than the straight mobile web
    version.\r\n\r\nI do think the \"add to homescreen\" is essentially the equivalent
    of a bookmark in the mobile app (native or not) world and is important.  Going
    to the browser and typing in the URL or using a browser-based bookmark just won't
    cut it IMO.\r\n\r\nObviously, most games and anything that provides access to
    the camera and hardware needs to be in a native app.  In my app, the only thing
    I really wasn't able to do in the straight Sencha web app was provide a good OAuth2
    login experience for Facebook (can't redirect to the open instance of my web app
    after completion.)  Was trying to find a solution within the native wrapper.\r\n\r\nThanks."
- id: 44807
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 13:37:24 -0600'
  date_gmt: '2013-01-09 19:37:24 -0600'
  content: "We've talked a bunch about native vs. web, so you know I like sensible
    native apps. \r\n\r\nI'm puzzled here by we <em>web dev's</em> who shoe-horn our
    HTML5 apps into an \"almost-native\" experience. What value are we trying to capture?\r\n\r\nWe
    don't get offline capability, since users have to be online to install new apps
    anyway.\r\n\r\nWe don't get a native in-app experience, since HTML5 apps don't
    match the device UX (and WebViews hurt performance).\r\n\r\nWe don't get discover-ability,
    since we still have to do the out-of-store marketing.\r\n\r\nIt seems we're just
    trying to re-use the \"Go to app store, search, install\" experience. But I argue
    that \"Go to incrediblepizza.com\" is every bit as widely understood and accessible."
- id: 44809
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 13:38:52 -0600'
  date_gmt: '2013-01-09 19:38:52 -0600'
  content: "\"Going to the browser and typing in the URL or using a browser-based
    bookmark just won’t cut it IMO.\"\r\n\r\nWhy not? What is it about \"Tap Browser;
    type url\" that is so scary on a mobile device?"
- id: 44818
  author: m1879
  author_email: m1879@earthlink.net
  author_url: ''
  date: '2013-01-09 14:04:20 -0600'
  date_gmt: '2013-01-09 20:04:20 -0600'
  content: I find it pretty tedious to use my phone's keyboard to type a picky thing
    like a URL. And I have a large screen (Samsung Galaxy s3).
- id: 44819
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 14:05:32 -0600'
  date_gmt: '2013-01-09 20:05:32 -0600'
  content: And yet search for apps in the app store requires the same amount of typing.
- id: 44842
  author: Mark in A2
  author_email: mark@mobyus.com
  author_url: http://mobyus.com
  date: '2013-01-09 15:01:17 -0600'
  date_gmt: '2013-01-09 21:01:17 -0600'
  content: "The first time, maybe.  After that, if it is an app I'm using with any
    kind of regularity I want an icon on my home screen.  It isn't about being scary
    - just about being easy and convenient.\r\n\r\n\r\nOne of the nice things about
    the app store is that I know exactly what I'm searching through (iOS native apps)
    and what to expect.  With URL's, I could end up anywhere being served all kinds
    of things and I'm searching the entire web.\r\n\r\nI've often wondered why there
    isn't an HTML5 web app equivalent of the Apple App Store.  There probably are
    some, but nothing I'm aware of as reaching a critical mass."
- id: 44858
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-09 15:25:47 -0600'
  date_gmt: '2013-01-09 21:25:47 -0600'
  content: "Although it can be improved further, \"Add to home screen\" isn't much
    more than \"Install\" IMO.\r\n\r\nI agree there should be an HTML5 app store.
    But it seems like it would just be an app-aware search engine."
- id: 44862
  author: Mark in A2
  author_email: mark@mobyus.com
  author_url: http://mobyus.com
  date: '2013-01-09 15:35:55 -0600'
  date_gmt: '2013-01-09 21:35:55 -0600'
  content: I agree on "Add to home screen".  Hopefully people get get familiar with
    using that.  If there was a "killer app" that was accessed that way, it would
    help.
- id: 47867
  author: Jarred
  author_email: jarred@sencha.com
  author_url: http://www.sencha.com
  date: '2013-01-14 18:44:03 -0600'
  date_gmt: '2013-01-15 00:44:03 -0600'
  content: Nice article.  Just as an FYI, Sencha Fastbook runs equally fast in a WebView
    as it does in Mobile Safari.  The performance comes from optimized DOM, not from
    JavaScript JIT.
- id: 47935
  author: Robert Kaiser
  author_email: kairo@kairo.at
  author_url: http://home.kairo.at/blog/
  date: '2013-01-14 21:43:46 -0600'
  date_gmt: '2013-01-15 03:43:46 -0600'
  content: "Well, I'm just another person watching things while having an opinion,
    but not someone to make decisions (I'd probably never have decided to let in a
    packaged format into FxOS). Still, for one thing, I didn't know there was such
    a thing as a standard for packaged apps (and that smells funny as web and packaging
    don't go well together IMHO), but I guess m1879 already laid out the reasons why
    packaging was done for FxOS.\r\nThat said, I wrestle to understand appCache, but
    distributing your own packaged app seems to be even harder from what I see now
    with trying it. :("
- id: 48227
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-15 09:16:32 -0600'
  date_gmt: '2013-01-15 15:16:32 -0600'
  content: Thanks for the clarification. I couldn't find anything in the sencha docs
    - does Sencha help register custom URL-handling?
- id: 49077
  author: Mike
  author_email: reinstein.mike@gmail.com
  author_url: ''
  date: '2013-01-16 12:18:51 -0600'
  date_gmt: '2013-01-16 18:18:51 -0600'
  content: '@groovecoder: yes, yes a thousand times yes! Great article. About a year
    ago I decided to ditch this app store nonsense, and I strive to build mobile web
    apps wherever possible.'
- id: 49259
  author: J.L.
  author_email: jlreid@thebentpin.com
  author_url: ''
  date: '2013-01-16 18:53:27 -0600'
  date_gmt: '2013-01-17 00:53:27 -0600'
  content: "One position you're not considering--or if you did, I somehow missed it--is
    the value of an app store for acquiring an audience. \r\n\r\nYour pizza parlor
    example is good in that anyone in the restaurant who might be inclined to use
    its app (or app-like) experience from is a captive audience. So posting a QR code
    or url is an easy task.\r\n\r\nIf you're concerned about your city's tourism,
    or if you run a tourist attraction, then prefering a web app over a native one
    is fine since, again, people using it would be captive. Simply print the link
    in a conveniently seen place, and there you go.\r\n\r\nBut if you're developing
    a non-location specific app, one where a potential user isn't within convenient
    \"eye-shot\" of a url or code to scan, then packaging your web app makes sense.\r\n\r\nI
    can create my html5-based game, say, and rather than have to rely solely on the
    usual search engine--or whatever other methods you use to drive traffic to your
    website--game, I can upload my packaged app in an app store and therefore have
    a smaller hill to climb.\r\n\r\nAlso, the advantage of Sencha, phone gap, et.
    al. is that I can take what would normally require internet access, and develop
    it to work offline. In this case, HTML5, CSS3, and javascript simply comprise
    another framework for developing a native app.  Just because I create a html5
    game doesn't mean I must be tethered to the internet."
- id: 49265
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-01-16 19:06:24 -0600'
  date_gmt: '2013-01-17 01:06:24 -0600'
  content: |-
    Sure, "acquiring an audience" is a commercial app developer concern. But I'm approaching the "discover-ability" issue from the perspective of a business & their customer. But I would be interested to see numbers re: the smaller hill to climb. I.e., compare app download & install metrics with and without out-of-store marketing.

    A Sencha-packaged HTML5 still requires internet access to install. And any HTML5 app at a URL can function completely offline using appCache (https://developer.mozilla.org/en-US/docs/HTML/Using_the_application_cache) and local storage (https://developer.mozilla.org/en-US/docs/DOM/Storage), which Sencha actually uses for Ext.data.proxy.LocalStorage.
- id: 51361
  author: Taras
  author_email: taras@quickblox.com
  author_url: http://quickblox.com/
  date: '2013-01-20 03:50:18 -0600'
  date_gmt: '2013-01-20 09:50:18 -0600'
  content: 'FT has done a great job in packaging their HTML5 app without phonegap
    or any other converters: http://apps.ft.com/ftwebapp/'
- id: 52742
  author: Miguel
  author_email: miguel.jose.lima@gmail.com
  author_url: ''
  date: '2013-01-22 06:31:31 -0600'
  date_gmt: '2013-01-22 12:31:31 -0600'
  content: The market approach it's essential for the purpose of selling something.
    Probably this can be an idea that someone could develop, and build a market for
    html5 apps based in a simple URL. The browsers and the OS should have the possibility
    to encapsulate such type of apps, so they can look like a native app. In windows
    8, the IE app experience it's quite diferent from the traditional browser look
    and feel.
- id: 52994
  author: Erik Rose
  author_email: erik@mozilla.com
  author_url: https://github.com/erikrose
  date: '2013-01-22 14:03:02 -0600'
  date_gmt: '2013-01-22 20:03:02 -0600'
  content: "Oh, I use Quick Find all the time to navigate, but it doesn't make the
    UI any more consistent, any more than \"using the keyboard\" equals \"consistent\".
    What I mean is: how about a common, short keystroke for \"go 'up' in the document
    structure\" (as when reading documentation). I used to have that rigged with iCab
    when people used link rels properly. Remember how the Mac standardized command-Q,
    command-W, command-Z -X -C -V? That sort of thing.\r\n\r\nBy #2, I mean I'd literally
    like every web site to look exactly the same (if I want), apart from its content.
    When I load a new site, my workflow goes like this: hit command-plus or -minus
    several times to get it a reasonable size, then maybe resize the window as well.
    I've tried a slew of auto-resize addons, but none work very well."
- id: 59033
  author: thinsoldier
  author_email: thinsoldier@thinsoldier.com
  author_url: ''
  date: '2013-02-05 15:27:03 -0600'
  date_gmt: '2013-02-05 21:27:03 -0600'
  content: "The UI of the app store \"apps\" sucks. Well google play's app currently
    sucks and my memory of the app store on first generation iphones is just as bad.\r\n\r\nHowever,
    the google play website is much, much better. Best of all, when a friend wants
    to tell me about cool app, they have a url to take me right to it. Even better
    than that, the google play website works perfectly with the browser's back button.
    Going back in the play store app after scrolling past 400 entries is very inaccurate."
- id: 59036
  author: thinsoldier
  author_email: thinsoldier@thinsoldier.com
  author_url: ''
  date: '2013-02-05 15:44:18 -0600'
  date_gmt: '2013-02-05 21:44:18 -0600'
  content: "RSS Reader. But not all sites offer a feeed :(\r\n\r\nAll the sites I
    visit regularly do. That might be why they're the only ones I visit regularly."
- id: 59276
  author: thinsoldier
  author_email: thinsoldier@thinsoldier.com
  author_url: ''
  date: '2013-02-06 08:56:04 -0600'
  date_gmt: '2013-02-06 14:56:04 -0600'
  content: "The same thing that's scary about it on desktop. I know older people who
    can type in facebook.com into the search field and nothing else. Other who type
    facebook.com into the address bar, thinking it's the search field, and are pleasantly
    surprised *every* time that it \"found\" exactly what they wanted. \"Why can't
    it find exactly what I want when I type in Cheapest Hotel in Miami.com?\"\r\n\r\nThey
    get all their news from msn.com because it is the default. They only check their
    email when I come over to their house and type in gmail.com and their username
    and password (that they refuse to remember for themselves).\r\n\r\nThere needs
    to be a 1-touch method for adding a website to a device's main list of app icons.\r\n\r\nI'm
    on a nexus 7 using a stylus and I still have a hard time entering URLs. Thankfully
    I do all my browsing/reading via Google Reader so I usually never need to type
    any urls when on my tablet."
- id: 59279
  author: thinsoldier
  author_email: thinsoldier@thinsoldier.com
  author_url: ''
  date: '2013-02-06 09:04:24 -0600'
  date_gmt: '2013-02-06 15:04:24 -0600'
  content: "My main point is:\r\n\r\nI can get my uncle to type in a url for a site
    or app correctly ONE TIME. He'll never use/visit it again unless I bother to nag
    him and walk him through it again. \r\n\r\nThere needs to be a 1 touch method
    of adding a site to the list of app icons. \r\n\r\nIt needs to be something the
    user touches within the site itself. \r\n\r\nMy uncle refuses to touch browser
    chrome. He fears it for some reason."
- id: 59281
  author: thinsoldier
  author_email: thinsoldier@thinsoldier.com
  author_url: ''
  date: '2013-02-06 09:13:05 -0600'
  date_gmt: '2013-02-06 15:13:05 -0600'
  content: "If you look at the instructions on apps.ft.com/ftwebapp/\r\nthat 1 too
    many steps for some people.\r\n\r\nThe device, browser, and website should be
    able to communicate:\r\n\r\n\r\n- Site asks the browser to ask the OS: Is there
    already a home screen icon for this site?\r\n- OS says no -&gt; Browser says no
    -&gt; Site shows a big green button \"Add us to your home screen!\"\r\n-"
- id: 59291
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-02-06 09:59:07 -0600'
  date_gmt: '2013-02-06 15:59:07 -0600'
  content: "I totally agree. But if we package HTML5 apps to fit into the current
    app stores, there's less pressure on the mobile platform vendors to support a
    1-touch site-to-home-screen feature, isn't there?\r\n\r\nWe should push the \"Add
    to home screen\" method instead of shoehorning HTML5 into the app store distribution
    method."
- id: 59671
  author: Ady
  author_email: ady.touba.ngom@gmail.com
  author_url: http://mashappslabs.com
  date: '2013-02-07 15:58:15 -0600'
  date_gmt: '2013-02-07 21:58:15 -0600'
  content: "I use phonegap and the likes as a last resort if one feature carefully
    picked to enhance the user experience has to be done natively, like taking a picture
    and having access to it right away. If there was an easy way to have access to
    the device file system and such, believe me  that would be the end of packaged
    apps. \r\nI haven't had the chance to keep up with the new trends (so many to
    track) to see if such things are in the works, in the meantime that is going to
    be the unfortunate tradeoff that we as WEB developers (emphasis on web) will have
    to make."
- id: 59742
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-02-07 21:04:52 -0600'
  date_gmt: '2013-02-08 03:04:52 -0600'
  content: Check out http://mobilehtml5.org/ - iOS, Android, BB10, and Firefox Mobile
    all support HTML media capture (http://www.w3.org/TR/html-media-capture/).
- id: 64438
  author: Ronan Lavelle
  author_email: ronan.lavelle@gmail.com
  author_url: http://www.azurati.com
  date: '2013-03-01 05:40:35 -0600'
  date_gmt: '2013-03-01 11:40:35 -0600'
  content: "Groovecoder - this is a REALLY great article.  Nice work.  My company,
    Azurati, has been promoting (sometimes it feels like trying to row upstream) HTML5
    apps for enterprise mobile use.  What we have found is that: \r\n\r\n1. there
    is a general expectation that an app should be launched by selecting an App badge/icon\r\n2.
    typing a URL or even accessing mobile bookmarks are not culturally acceptable
    anymore.\r\n\r\nTo counter this, and to provide a solution that enables BYOD at
    a much lower cost than traditional native apps and MDM solutions, we have come
    up with the concept of the Azurati Mobile Portal - a mobile app container for
    HTML5 web apps.  \r\n\r\nDevelopers can publish web apps to the Mobile Portal,
    allowing users to access web apps securely without having to enter URLs or ID
    credentials.\r\n\r\nFurther information on this can be found at:  http://www.azurati.com/products/azurati-mobile-portal/"
- id: 68411
  author: Ted
  author_email: tedcurran@gmail.com
  author_url: http://trueschool.me
  date: '2013-03-21 09:48:20 -0500'
  date_gmt: '2013-03-21 14:48:20 -0500'
  content: "Hi All--\r\nGreat discussion. One other reason why people prefer apps
    to URLs is related to gestures-- apps can define a set of unique gestures and
    interactions that are specific to the way the app should work and make it easier
    for people to interact with the app. Browser-based apps have keystrokes, gestures,
    and buttons that HAVE TO apply to any app you might like to call up in your browser.
    \r\n\r\nFor example, a two finger pinch on your email app might close a message,
    but in a browser it would close the whole app tab. A swipe to the left might go
    to the next message, but in the browser it opens my browser settings menu. In
    short, <b>your gestures can be optimized for the activities you do in the app</b>.\r\n\r\nI've
    long though that for a browser-based future to work, it would be necessary to
    have site-specific gesture settings that could take over from the browser's settings
    somehow. I imagine this as a browser-plugin where each site could submit a set
    of interactions that override the browser's gestures. This way, you could approach
    native-app-like interactions in a browser. \r\n\r\nI don't have the coding chops
    to create such a thing, but hopefully one of you do?\r\n\r\nTed"
- id: 70710
  author: mws
  author_email: m@hotmail.com
  author_url: ''
  date: '2013-04-04 08:46:33 -0500'
  date_gmt: '2013-04-04 13:46:33 -0500'
  content: who the hell wants to check-in anyways, whats it good for
- id: 73380
  author: Raymond Camden
  author_email: raymondcamden@gmail.com
  author_url: http://www.raymondcamden.com
  date: '2013-05-11 09:47:56 -0500'
  date_gmt: '2013-05-11 14:47:56 -0500'
  content: "Disclaimer - I work for Adobe and am a PhoneGap lover. :) \r\n\r\nI'm
    curious why your two introductory arguments (app discoverabilty and content discoverability)
    are used as a means to argue against PhoneGap? Those arguments apply to native
    apps in general. Is there a reason why you have them here in an argument against
    packaged HTML5 apps when they apply to native apps as well?\r\n\r\nAs to PhoneGap,
    one of their philosophies is to actually *not* exist in the future. The team would
    love to see mobile web get to a point where things like camera access and other
    hardware APIs are opened up to the web. I think that would be great too, but I
    can never see it happening completely."
- id: 73382
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-05-12 09:25:31 -0500'
  date_gmt: '2013-05-12 14:25:31 -0500'
  content: "You're right, of course. My discover-ability arguments are against native
    apps. I extend them to packaged HTML5 apps because I don't understand why web
    developers spend time to support these failures of the native mobile platforms
    - because \"everyone wants an app\"? Is that a good reason? I don't think so,
    and <a href=\"http://blog.forecast.io/its-not-a-web-app-its-an-app-you-install-from-the-web/\"
    rel=\"nofollow\">some web app developers are showing that even consumers are poised
    to repatriate the web on their mobile devices</a>.\r\n\r\nIt makes sense to use
    PhoneGap to use device/hardware features that the mobile browser doesn't support,
    but a mobile web app at an easy URL kills native app stores for discover-ability."
- id: 74563
  author: Rahul
  author_email: est.rahul@gmail.com
  author_url: http://www.techendeavour.com/iphone-application-development
  date: '2013-05-21 06:55:47 -0500'
  date_gmt: '2013-05-21 11:55:47 -0500'
  content: "Very nice discussion. IMO the factor which governs the success/failure
    of html5 apps is not the technology itself but it is going to be evolution of
    the financial model behind these apps that would ensure a proper RoI. Until unless
    we have a sustainable Appstore like the once with native applications this is
    not going to last long. \r\n\r\nWe being a mobile company (http://www.techendeavour.com/mobile-application-development)
    have done all. Native, hybrid as well as Web (HTML5 based) but still the trend
    does not seem to shift towards html5."
- id: 74590
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2013-05-21 09:35:29 -0500'
  date_gmt: '2013-05-21 14:35:29 -0500'
  content: "I'm interested - what's your company's financial model for native, hybrid,
    and web-based apps? \n\nLast I heard, even the \"pure\" native app stores don't
    offer a sustainable financial model for most developers. (http://arstechnica.com/apple/2012/05/ios-app-success-is-a-lottery-and-60-of-developers-dont-break-even/)"
- id: 77062
  author: Wacky
  author_email: wcalderw@gmail.com
  author_url: ''
  date: '2013-08-12 14:38:41 -0500'
  date_gmt: '2013-08-12 19:38:41 -0500'
  content: "All of that web naming crap is fine. I'm just glad that the market has
    moved away from all of that protocol nastiness :)\r\n\r\narchie:\r\ngopher:\r\nhttp:\r\ntelnet:\r\nftp:\r\nfile:\r\n\r\nFor
    me the importance around a web app that is wrapped with something like phone gap
    is that when it's running in a browser I don't have access to certain functionality
    that I have when it's running in it's wrapper. For US that's bluetooth, reminders,
    a more secure version of SQLite etc..."
- id: 77766
  author: Easy Home Noida
  author_email: deetyasoft@gmail.com
  author_url: http://easyhomeshopee.com/
  date: '2014-12-18 04:41:40 -0600'
  date_gmt: '2014-12-18 10:41:40 -0600'
  content: "I would just like to tell that I really liked your blog post. In fact
    I am going to \r\n\r\nbookmark your blog and will regularly visit the site. You
    come up with such an amazing \r\n\r\narticles thank you for sharing this your
    site."
- id: 77767
  author: Virtual Call Tracking
  author_email: deetyasoft@gmail.com
  author_url: http://deetyasoft.com
  date: '2014-12-18 04:42:33 -0600'
  date_gmt: '2014-12-18 10:42:33 -0600'
  content: I would just like to tell that I really liked your blog post. In fact I
    am going to bookmark your blog and will regularly visit the site.
---
<p><strong>tl;dr</strong> - URLs delivered a better experience than native desktop apps; they can do the same for mobile apps.</p>
<p><strong>update:</strong> see my follow-up post - <a href="http://groovecoder.com/2013/01/22/html5-app-stores-dont-go-too-far-enough/">HTML5 App Stores don't go too far enough</a>.</p>
<p><img class="aligncenter" alt="HTML5 in a box" src="http://mugs.mugbug.co.uk/500/mb.html5_badge.boxed.jpg" width="300" height="300" /></p>
<p>When <a href="https://groups.google.com/forum/#!topic/mozilla.engagement.developers/Iop743jIaho/discussion">we discussed Sencha's Fastbook app on the mozilla.engagement.developers list</a> Robert pointed out that Sencha compared their HTML5 app running in mobile web <em>browser</em> to Facebook's HTML5 app running in an <em>iOS WebView</em> - the way Sencha &amp; PhoneGap packaged HTML5 apps actually run. It's widely discussed, as we did with Fastbook, that HTML5 apps perform worse in iOS UIWebView than iOS Safari. There are similar stories about <a href="https://www.google.com/search?q=android+webview+performance&amp;ie=utf-8&amp;oe=utf-8&amp;aq=t&amp;rls=org.mozilla:en-US:unofficial&amp;client=firefox-nightly">Android WebView performance</a>, and Tulsa Web Dev and HTML5 PhoneGap developer Rod just posted <a href="https://www.facebook.com/groups/199713962534/permalink/10151235283912535/">a similar performance-related anecdote about BlackBerry WebWorks</a>.</p>
<p>That made me think, "<strong>PhoneGap is just that - a stop-gap.</strong>" ... "<strong>we should drop this whole PhoneGap App nonsense and go (back) to mobile web at simple URL's" </strong>since:<strong><br />
</strong></p>
<ol>
<li>App discover-ability &amp; installation sucks</li>
<li>App content discover-ability sucks</li>
</ol>
<h3>App discover-ability &amp; installation sucks</h3>
<p>A couple months ago, my wife and I took our daughters to Incredible Pizza. When we sat down, I saw this table-tent:</p>
<p><img alt="Incredible Pizza Table-Tent" src="https://dl.dropbox.com/u/21969365/images/incredible_pizza_app_facebook.jpg" width="1062" height="599" /></p>
<p>I spent a couple minutes trying to make this "check-in" UX work on my wife's phone. The table-tent literally reads: "<em>TIP: A QR-Reader App is necessary to scan QR codes. There are several free ones available. Check your app store.</em>" So, here's what I did to find an app:</p>
<ol>
<li>Connect to Incredible Pizza wifi</li>
<li>Tap "All apps"</li>
<li>Swipe down to "Play Store"</li>
<li><em>Tap "Play Store" </em></li>
<li><em>Tap "Search"</em></li>
<li><em>Type "qr reader"</em></li>
<li><em>Swipe thru a huge list of apps</em></li>
<li><em>Pick one at random (*)<br />
</em></li>
<li><em>Tap "Install"</em></li>
<li><em>Tap "Accept &amp; Download" </em></li>
<li><em>Wait for download &amp; install</em></li>
</ol>
<p>Android prompts me with a wall of permissions that I have to accept in order to install the app. And because app updates with new permissions can't be automatically downloaded &amp; installed, <strong>many app developers just make their app request all permissions</strong>.</p>
<p>* Especially interesting to developers - I picked a free qr reader app at random, verifying that <a href="http://www.fastcompany.com/1792313/striking-it-rich-app-store-developers-its-more-casino-gold-mine">App Stores are more like casinos than gold-mines</a>.</p>
<h3>Content discover-ability sucks</h3>
<p>Once I had the QR reader app, I started to use it to check-in to Incredible Pizza on Facebook:</p>
<ol>
<li>Hold the phone in front of the card</li>
<li>Tap "Visit Link"</li>
<li>Tap "Browser"</li>
<li>Go thru 5 redirects to a prompt to open native Facebook app</li>
<li>Facebook opens</li>
<li>Wonder: "Why am I trying to do this in the first place?"</li>
</ol>
<p>There was no human-readable URL on the card. I had to choose between "Browser" and "VZ Navigator" that came with the phone from Verizon. The redirects took about 20 seconds. Finally, since <strong>they don't deep link into the native app</strong>, I ultimately end up just staring at the Facebook app as if I'd opened it myself - nothing there at all about Incredible Pizza.</p>
<p><strong>This totally obscures the app's content, and value, from the user.</strong> If I package my HTML5 app with PhoneGap I have to also register a custom URL scheme to link to a specific part of it - something PhoneGap doesn't help you to do(?). And even when you do it, <strong>you will need to make and deploy an update to the app</strong> anytime you want to add <em>new</em> URL-driven logic to it, invoking another round of app review.</p>
<h3>The Plain Old URL approach</h3>
<p>Contrast the above experience with a more traditional web approach:</p>
<ol>
<li>Connect to Incredible Pizza wifi</li>
<li>Tap Browser</li>
<li>(<em>Maybe</em>) Type "incrediblepizza.com"</li>
<li>(<em>Maybe</em>) Tap "Yes" at a geolocation prompt</li>
</ol>
<p>Incredible Pizza could <strong>immediately give me the</strong> <a href="http://www.incrediblepizza.com/Locations.html">store-specific web page</a> via captive wifi portal <strong>with big buttons for <a href="http://www.incrediblepizza.com/Oklahoma/Tulsa/Tulsa-Coupons/Eat-and-Play.html">location-and-date-specific coupons</a>, facebook check-in, etc.</strong> Or, if I'm not on their wifi, I type "incrediblepizza.com" to get the same thing via geolocation. In addition to a simpler experience, <strong>deploying new or updated content is as simple as updating the website</strong>.</p>
<h3>So why package HTML5 apps?</h3>
<p>Considering all the above, I usually ask web devs using PhoneGap: "Why are you using PhoneGap instead of just putting an HTML5 app at a URL?" and they often reply "everyone wants an app." <strong>This "everyone wants an app" situation is a problem we developers and designers should address </strong>- but not just technically. <strong>We should work with our clients and customers to consider the full user experience of native vs. web</strong> - especially app installation &amp; content discover-ability.</p>
<blockquote><p>... although many brands and creative agencies believe that they need to develop iPhone apps, what they need in reality is a good mobile site. It costs less to develop, manage and work across all handsets.</p></blockquote>
<p>- <a href="http://www.mobileeurope.co.uk/Blog/html-5-the-end-of-apps/All-Pages">HTML5 - The End of Apps | Mobile Europe</a></p>
<p>If you're making an HTML5 app, consider - <strong>do you want to make a native <em>desktop</em> application</strong>? Why or why not? Then consider if the same reasoning is true for the native mobile application. Consider the URL experience for your customers. Walk your clients thru both native app and URL experiences on mobile devices. <strong>We used web URLs to deliver a better experience than native desktop apps - we should do the same with mobile apps.</strong></p>
<h3>Good HTML5 Packaging - URL Bookmarks</h3>
<p>Vendors like Mozilla (disclaimer: my employer) and Google are also working on manifests to install HTML5 apps on Firefox (OS) and Chrome (OS). Opera and previously(?) Microsoft (via Silverlight) use the <a href="http://www.w3.org/TR/widgets/">W3C Packaged Web Apps (Widgets)</a> standard. I like these efforts if they <strong>contribute towards a consistent "installation" experience that works more like an enhanced bookmark</strong>. I.e., turn this:</p>
<ol>
<li>Visit URL</li>
<li>Tap "Add to ..."</li>
<li>Tap "Add to Home Screen"</li>
<li>Tap "Add"</li>
</ol>
<p>into this:</p>
<ol>
<li>Visit URL</li>
<li>Tap "Add to Home Screen."</li>
</ol>
<p>But next time you make an app, consider the tried-and-true web experience:</p>
<ol>
<li>Tap Browser</li>
<li>Type URL</li>
</ol>
