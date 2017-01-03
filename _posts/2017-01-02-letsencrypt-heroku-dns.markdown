---
layout: post
status: publish
published: true
title: Let's Encrypt on Heroku with DNS Domain Validation
author:
  display_name: groovecoder
  login: groovecoder
  email: luke.crouch@gmail.com
  url: http://groovecoder.com
author_login: groovecoder
author_email: luke.crouch@gmail.com
author_url: http://groovecoder.com
date: '2017-01-02 21:00:00 -0600'
date_gmt: '2017-01-02 21:00:00'
tags:
- security
- letsencrypt
- heroku
---
We needed to renew and update our certificate for
[www.codesy.io](https://www.codesy.io), and I've
been wanting to use [Let's Encrypt](https://letsencrypt.org/) for a while. I
had read and tried some other guides for using Let's Encrypt on Heroku, but
none of them cover DNS domain validation. The steps are roughly:

1. Install `certbot`
2. Use `certbot` to generate a manual cert
3. Deploy a TXT record to your DNS
4. Upload signed certificate to Heroku
5. Update your DNS Target

### Install certbot

First, you'll need <a href="https://certbot.eff.org/"
target="_blank"><code>certbot</code></a>:

    brew install certbot

Note: The <a href="https://certbot.eff.org/" target="_blank">certbot site</a>
contains install instructions for other systems.

### Use certbot to generate a manual cert
With `certbot` you will need to generate a cert to manually install to the
Heroku server, and specify DNS as your preferred challenge:

    sudo certbot certonly --manual --preferred-challenges dns

Note: `certbot` needs `sudo` to put resulting files into `/etc/`

`certbot` will ask you the domain for which you want a certificate ... 

![Certbot Domain Prompt Screenshot](/uploads/certbot-domain-prompt.png)

... and if you're OK with your IP being logged as having requested the
certificate ...

![Certbot IP Prompt Screenshot](/uploads/certbot-ip-prompt.png)

... and will finally tell you what DNS TXT record to deploy:

    Please deploy a DNS TXT record under the name
    _acme-challenge.www.codesy.io with the following value:

    CxYdvM...5WvXR0

    Once this is deployed,
    Press ENTER to continue

Note: Don't press ENTER until you have deployed your TXT record

### Deploy a TXT record to your DNS

Your domain registrar likely has its own docs for adding a TXT record. Here are
some links to a few:

* <a href="https://www.godaddy.com/help/add-a-txt-record-19232" target="_blank">GoDaddy</a>
* <a href="https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-CNAME-MX-TXT-and-SRV-Updated-Aug-2015-" target="_blank">Hover</a>
* <a href="https://support.office.com/en-us/article/Create-DNS-records-at-Google-Domains-for-Office-365-0db29490-2612-48bc-9b77-1862e7a41a8c#bkmk_verify" target="_blank">Google Domains</a> (docs by Microsoft!)
* <a href="https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-creating.html" target="_blank">Amazon Route 53</a> (See Basic Resource Record Sets)

### Upload signed certificate to Heroku

Go back to `certbot` and press `ENTER`. It will create signed certificate files
in your `/etc/letsencrypt` directory.

<a href="https://blog.heroku.com/ssl-is-now-included-on-all-paid-dynos"
target="_blank">SSL is now included on all paid dynos on Heroku</a>. The $7/mo.
for a hobby dyno is still cheaper than $20/mo. for the old SSL Endpoint add-on.
So, to change to a hobby dyno, go to your app's Resources panel and click
"Change..."

![Heroku Dyno Resources Screenshot](/uploads/heroku-app-resources.png)

Then, use `heroku certs:add` to add your Let's Encrypt `fullchain` and `privkey`
files.

    sudo heroku certs:add --type=sni /etc/letsencrypt/live/www.codesy.io/fullchain.pem /etc/letsencrypt/live/www.codesy.io/privkey.pem

Note: Again, `heroku` needs `sudo` to access files in `/etc/`

You can also copy+paste your certificates' contents in your app's settings
dashboard - under "Domains and certificates", click "Configure SSL".

### Update your DNS Target

Finally, update your DNS CNAME record for your domain to point to the
`certificate-domain.herokudns.com`. In our case, it was
`www.codesy.io.herokudns.com`

![Hover DNS Screenshot](/uploads/hover-dns-cname-herokudns.png)

### Enjoy your Let's Encrypt-verified site!

![Codesy Verified Screenshot](/uploads/codesy-verified-by-letsencrypt.png)
