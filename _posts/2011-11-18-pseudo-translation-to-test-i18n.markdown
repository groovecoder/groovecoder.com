---
layout: post
status: publish
published: true
title: pseudo-translation to test i18n
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 610
wordpress_url: http://groovecoder.com/?p=610
date: '2011-11-18 16:00:12 -0600'
date_gmt: '2011-11-18 22:00:12 -0600'
categories:
- mdn
- dev
tags:
- i18n
comments:
- id: 1868
  author: F Wolff
  author_email: friedel@translate.org.za
  author_url: http://translate.org.za/blogs/friedel/
  date: '2011-12-29 08:27:13 -0600'
  date_gmt: '2011-12-29 14:27:13 -0600'
  content: "Great to see you use pofilter to improve things for translators!\r\n\r\nTo
    avoid the translation of the new python variables, we need to add support for
    them in the Translate Toolkit to recognise it and skip it in pofilter. It already
    detects HTML, printf variables, etc. so it should be quite feasible, I guess."
- id: 2012
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2012-01-03 08:59:11 -0600'
  date_gmt: '2012-01-03 14:59:11 -0600'
  content: If I knew any C I would offer to help. Where is the relevant profilter
    code?
- id: 2035
  author: F Wolff
  author_email: friedel@translate.org.za
  author_url: http://translate.org.za/blogs/friedel/
  date: '2012-01-04 08:36:15 -0600'
  date_gmt: '2012-01-04 14:36:15 -0600'
  content: "It is all in Python. \r\n\r\nPofilter:\r\nhttps://translate.svn.sourceforge.net/svnroot/translate/src/trunk/translate/tools/pogrep.py\r\n\r\nThe
    code to recognise variables:\r\nhttps://translate.svn.sourceforge.net/svnroot/translate/src/trunk/translate/storage/placeables/general.py"
---
<p><a href="https://developer-stage9.mozilla.org/x-testing/"><img class="aligncenter" title="MDN Unicode Banner" src="http://content.screencast.com/users/groovecoder/folders/Jing/media/300a9678-07ae-4709-94ff-3a71fbf836e7/00000032.png" alt="MDN Unicode Banner" width="448" height="83" /></a>I really like that Mozilla has a strong <a href="https://wiki.mozilla.org/L10n:Localization_Teams">L10n team</a> made up of both employees and community volunteers. Months ago we made some cool <a title="good day for mozillians" href="http://groovecoder.com/2011/03/04/good-day-for-mozillians/">localization changes to MDN</a>, and I learned a lot about <a href="https://docs.djangoproject.com/en/dev/topics/i18n/">django localization</a>, <a href="http://www.gnu.org/software/gettext/">gettext</a>, <a href="http://translate.sourceforge.net/wiki/">pootle, and translate toolkit</a>.</p>
<p>Back then <a href="https://twitter.com/#!/teo951">Leszek</a>, a localization volunteer and <a href="https://addons.mozilla.org/en-US/firefox/user/54957/">add-on developer</a>, filed a <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=664330">bug</a> about a bunch of un-localized MDN strings, and then found <a href="https://bugzilla.mozilla.org/show_bug.cgi?id=698435">a bunch more un-localized strings</a> again recently. I remembered I had read about <a href="http://msdn.microsoft.com/en-us/goglobal/bb688150">using pseudo-translations for localizability testing</a>, and thought I'd try it for MDN.</p>
<p><a href="http://mozweb.readthedocs.org/en/latest/l10n.html">MDN, like (almost?) all Mozilla webdev projects, uses gettext</a> message files (<a href="http://svn.mozilla.org/projects/mdn/trunk/locale/">svn</a>), so we can use <a href="http://translate.sourceforge.net/wiki/toolkit/index">translate toolkit</a>. (woo! SourceForge project!) We also use a product_details repository (<a href="http://svn.mozilla.org/libs/product-details/">svn</a>)  to closely track the same language and country codes used by other Mozilla  products. I needed to add the new test locale, but Pike pointed out  we have to use a single-character subtag (x-testing) to indicate a  privately-defined language code (per <a href="http://tools.ietf.org/html/bcp47#section-2.2.1">ietf bcp47</a>), while Stas pointed out that pootle requires a two-character subtag. So, we added 'x-testing' language to the product_details (<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=668841">bug</a>), then I added  xx_testing in locale/ for pootle, along with a x_testing -&gt;  xx_testing symlink so django uses the xx_testing files for the x-testing  locale.</p>
<p>I installed toolkit and ran <a href="http://translate.sourceforge.net/wiki/toolkit/podebug">podebug</a> on our message.pot file:</p>
<pre>cd locale/
mkdir -p xx_testing/LC_MESSAGES
podebug --rewrite=bracket templates/LC_MESSAGES/messages.pot \
    xx_testing/LC_MESSAGES/messages.po
./compile-mo.sh .</pre>
<p>Which gave me a pseudo-translated messages.po file and a compiled .mo file.</p>
<p style="text-align: center;"><img class="aligncenter" title="Testing Messages PO file" src="https://farm7.staticflickr.com/6234/6389595029_4b7952fe46_z.jpg" alt="Testing Messages PO file" width="374" height="589" /></p>
<p>I changed MDN to use the environment-specific language-loading snippet (found in <del>playdoh</del> <a href="https://github.com/mozilla/funfactory/blob/master/funfactory/settings_base.py#L67">funfactory</a>) to keep the test locale from showing up in production.  (We have to add the 'x-testing' locale to linux on our staging servers  so gettext can use it there, which proves to be quite a chore.)</p>
<p>Voilà - a new pseudo-translated locale for MDN development. It shows which strings we forgot to mark for localization:</p>
<p style="text-align: center;"><img class="aligncenter" title="MDN strings missing 18n" src="https://farm7.staticflickr.com/6097/6389595317_a75003151f_z.jpg" alt="MDN strings missing 18n" width="531" height="297" /></p>
<p>Couple of items I'd like help with:</p>
<ul>
<li>Find out how to exclude jinja template variable names so that
{% raw %}
<pre>{{ _('Welcome back, {username}]) }}</pre>
{% endraw %}
<p>doesn't create</p>
<pre>#: templates/includes/login.html:3
msgid "Welcome back, {username}"
msgstr "Ẇḗŀƈǿḿḗ ƀȧƈķ, {ŭşḗřƞȧḿḗ}"</pre>
</li>
<li>Put all this into <a href="https://github.com/clouserw/tower">tower</a></li>
</ul>
