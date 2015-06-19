---
layout: post
status: publish
published: true
title: Editing MDN with VIM
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
wordpress_id: 830
wordpress_url: http://groovecoder.com/?p=830
date: '2012-03-02 12:02:04 -0600'
date_gmt: '2012-03-02 18:02:04 -0600'
categories:
- mdn
- dev
tags:
- mdn
- vim
comments:
- id: 3025
  author: Screwtape
  author_email: thristian@gmail.com
  author_url: ''
  date: '2012-03-03 00:43:36 -0600'
  date_gmt: '2012-03-03 06:43:36 -0600'
  content: "Looks like you should also add to your .vimrc:\r\n\r\nautocmd BufNewFile,BufRead
    developer.mozilla.org.*.txt setlocal filetype=html\r\n\r\n(assuming that 'html'
    is the most appropriate filetype for Deki's wiki markup; it looks like raw HTML
    in that screenshot, but if not, you can probably find or create a more appropriate
    filetype plugin)"
- id: 3032
  author: groovecoder
  author_email: luke.crouch@gmail.com
  author_url: http://groovecoder.com
  date: '2012-03-04 09:24:17 -0600'
  date_gmt: '2012-03-04 15:24:17 -0600'
  content: Great tip! updated screenshot!
- id: 5017
  author: Rod Knowlton
  author_email: codelahoma@gmail.com
  author_url: http://codelahoma.com
  date: '2012-04-17 16:04:39 -0500'
  date_gmt: '2012-04-17 21:04:39 -0500'
  content: Ha! I googled for the autocmd you told me about at the Hackathon, and this
    is where I found it!
---
<p><span style="color: #339966;">UPDATED</span>: New screenshot with html filetype! Thanks Screwtape for the tip in the comments!</p>
<p>Yes, it's possible! If you're like me you want to spend as much time in vim as possible. While I appreciate CKEditor on MDN, I personally prefer to edit text in vim, and I think many developers might agree. And since MDN should include content written by developers for developers, here's a way to edit your favorite web developer docs (that would be MDN), using vim. (In my case, MacVim)<br />
<img class="alignright" title="It's All Text Preferences" src="http://dl.dropbox.com/u/21969365/images/iat_preferences.png" alt="It's All Text Preferences" width="300" height="199" /></p>
<ol>
<li>Install the <a href="https://addons.mozilla.org/en-US/firefox/addon/its-all-text/">It's All Text Firefox addon</a>.</li>
<li>Go to the IAT preferences</li>
<li>set your editor to vim (MacVim.app in my case)</li>
<li>set your hotkey. (alt+command+e in my case, now that I'm used to <a href="http://www.andismith.com/blog/2012/02/firefox-developer-tools/">Firefox Dev Tools</a> "Inspect" and "Console" keyboard hotkeys)</li>
<li>Go to the MDN article you want to edit. (<a href="https://developer.mozilla.org/en/Apps/Getting_Started">Apps/Getting Started</a> in my case)</li>
<li>Click Edit (duh)</li>
<li>Click Source</li>
<li>Type your hotkey!</li>
<li>Drink beer and edit away!*</li>
<li>:wq</li>
</ol>
<p><small>* groovecoder is not responsible for whatever Sheppy might do to you if you actually edit MDN while intoxicated.</small></p>
<p><img class="alignleft" title="MacVim Quite on Close" src="http://dl.dropbox.com/u/21969365/images/macvim_quit_on_close.png" alt="MacVim Quite on Close" width="290" height="221" />Note: For MacVim you may need to set the "After last window closes: Quit MacVim" preference so it puts you right back to Firefox when you :wq.</p>
<p style="text-align: center;"><a href="http://dl.dropbox.com/u/21969365/images/apps_gettings_started_vim.png"><img class="aligncenter" title="Apps/Getting Started in vim" src="http://dl.dropbox.com/u/21969365/images/apps_gettings_started_vim.png" alt="Apps/Getting Started in vim" width="578" height="697" /></a></p>
