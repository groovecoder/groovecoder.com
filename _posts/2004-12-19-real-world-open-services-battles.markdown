---
layout: post
status: publish
published: true
title: real world &quot;Open Services&quot; battles
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 235
wordpress_url: http://groovecoder.com/2004/12/19/real-world-open-services-battles/
date: '2004-12-19 08:47:00 -0600'
date_gmt: '2004-12-19 14:47:00 -0600'
categories:
- Uncategorized
tags: []
comments:
- id: 159
  author: Jeff Licquia
  author_email: ''
  author_url: ''
  date: '2005-02-26 13:44:00 -0600'
  date_gmt: '2005-02-26 19:44:00 -0600'
  content: Just found your link; don't know if I missed it before.<br /><br />My point
    wasn't necessarily that I don't care about eBay getting compensated, but about
    access.  Windows users of eBay can get programs like TurboLister for free; Linux
    users have to pay $100 to get the same access.<br /><br />Sure, regular users
    in Linux can still use the Web interface.  But tools like TurboLister exist because
    the web interface isn't sufficient for some tasks.  And because of eBay's support
    for TurboLister, Windows users can get some of that goodness for free, while Linux
    users get to pay.  That was my complaint.<br /><br />Of course, eBay has the right
    to support whatever platforms they want, make some platforms second-class, and
    so on.  But Jeff McManus was trying to make out as if eBay was really pro-open-source
    and all keen to support alternative platforms.  At the time, that was manifestly
    untrue.<br /><br />(I note that they seem to have made some changes to their developer
    APIs and program, so they may have fixed all this for all I know.)
---
<div style="text-align: justify;">I remember mentioning Amazon and how I was a big fan of them and their business model. On that subject, most people have compared eBay to them as well, but after I read <a href="http://www.xml.com/pub/a/2004/12/15/deviant.html">this article</a> alluding to <a href="http://www.beatniksoftware.com/blog/index.php?p=9">this post</a> at Alex Graveley's blog, I think eBay's a better example of the need for a compatible Open Source Web Services model (which Amazon may be on!).</p>
<p><a href="http://mcmanus.typepad.com/grind/">Jeffrey McManus</a>, eBay Web Services evangelist said, in response to an accusation that eBay's Web Services were not 'Linux-friendly': "If our API somehow didn’t work with Linux, that would be one thing, but, hello, this is XML we’re talking about."</p>
<p>to which <a href="http://www.licquia.org/">Jeff Licquia</a> responded quite reasonably: "I suppose we in the free software world aren’t used to the idea that we have to pay money for the privilege to access an otherwise free site."</p>
<p>at the risk, or inevitability, of rousing the slumbering OS debating giant that is my brother, this particular example demonstrates some of the misunderstanding of (or unacceptance toward) non-OS business models that I think the majority in the OS community has. Both of the contrasting points are true and to me just signify the importance of getting the Holy Grail of an Open Source Web Services licensing, business, and development model.</p>
<p>Since I completely agree with Licquia's response to McManus, and the debate went in a different direction afterwards, I'll have to go ahead an extend that original topic on my own.</p>
<p>Although Licquia ultimately concludes that it should at least be easier to sign up users into the eBay API program, and I agree with that, I do not agree with a conclusion that eBay is now charging a fee for information which is otherwise free.</p>
<p>The data may be the same, but as we all learned in Information Systems 101, data != information. Data is just raw data, like this:<br />
<br />(0,1,2,1,0,0,0)<br />
<br />and information is more like this:<br />
<br />Readers of Luke's blog last week, by day, in linear order are (0,1,2,1,0,0,0)</p>
<p>Now, the reason that's relevant here is that the way data is presented is what makes it information. So the same data could be used to convey different information to different people, and that is exactly what eBay is doing with their Web Services vs. their website.</p>
<p>When they use their data on their website, they massage the data all up with <a href="http://www.ebay.com/">their site</a>'s features, including a listing of advertisers' logos and links, who no doubt paid money for it. Whereas their Web Services is a more raw form of the data, expressed in a much more generic information set as XML. And that's great for others to work with, but it also means they lose the features of their site, like the paying advertisement links. And eBay is very much different from Amazon in the respect that they do not actually sell products, but rather they sell the services of their site. If they offer a means by which these services could be replicated by anyone else, they are essentially removing the need for themselves. Their value then is only in their data, and to stay solvent, they must recover their costs+ (economic costs, which include profit)</p>
<p>Whether their products, services, and/or prices are reasonable is up to the market to decide, including all the open-source and proprietary developers that will use their product. In this sense, eBay has made their model and is asking the market to figure out how to make it work. If the market can't, then their web services API is doomed. If only the proprietary market can make it work, it will survive in that market.</p>
<p>To make it work for open-sourcerors, a reseller license, or an end-user registration API, or many other things could be tried.</p>
<p>For open-source and web services, it is imperative to find a correct balance of the ease of distribution that open-source carries as its main strength, while still accurately compensating service providers to keep their services active. The freedom of distribution makes it extremely hard to comine the two requirements. There will be many attempts, and it may just be that the models will be as unique as the applications they are applied to. Everyone may need their own.<br />
</div>
