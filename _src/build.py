#!/usr/bin/env python3
"""
E-Fitek static site generator.
Edit content here, then run:  python3 _src/build.py
It writes index.html, services.html, about.html, contact.html, 404.html,
sitemap.xml and robots.txt into the site root. No dependencies.
"""
import json, os, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://e-fitek.vercel.app"   # change to your custom domain when you get one
BRAND = "E-Fitek Digital Services"
PHONE = "+2348167712361"
PHONE_H = "+234 816 771 2361"
EMAIL = "kingsleyokedigwe@gmail.com"
WA = "https://wa.me/2348167712361?text=" + "Hi%20E-Fitek%2C%20I%27d%20like%20to%20discuss%20a%20project."
FORM = "https://formspree.io/f/xanbkdez"
BLOG = "https://efitekblog.blogspot.com"
GA4_ID = ""  # e.g. "G-XXXXXXXXXX" — paste your GA4 measurement ID to enable analytics
GSC_TOKEN = ""  # Google Search Console HTML-tag verification token (content="...")
TODAY = datetime.date.today().isoformat()

SOCIALS = [
    ("facebook", "https://web.facebook.com/efitekk", "Facebook"),
    ("linkedin", "https://www.linkedin.com/company/efitekk/", "LinkedIn"),
    ("instagram", "https://www.instagram.com/e_fitek/", "Instagram"),
    ("youtube", "https://www.youtube.com/@e-fitekk", "YouTube"),
    ("twitter", "https://x.com/e_fitek", "X (Twitter)"),
]


def ic(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="/assets/icons.svg#i-{name}"></use></svg>'


def unsplash(pid, w=1200):
    return f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w={w}&q=78"


def rimg(pid, fallback, alt, w=1200, eager=False, cls=""):
    """Remote Unsplash image with local fallback + responsive srcset."""
    srcset = ", ".join(f"{unsplash(pid, x)} {x}w" for x in (480, 800, 1200, 1600) if x <= max(w, 800) * 1.4)
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{unsplash(pid, w)}" srcset="{srcset}" sizes="(max-width: 900px) 100vw, 50vw" '
            f'alt="{alt}" {load} decoding="async" data-fallback="/assets/img/{fallback}">')


def limg(src, alt, w, h, eager=False, cls=""):
    load = 'fetchpriority="high"' if eager else 'loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return f'<img{c} src="/assets/img/{src}" alt="{alt}" width="{w}" height="{h}" {load} decoding="async">'


# ------------------------------------------------------------------ data
SERVICES = [
    dict(id="web-design", icon="code-xml", name="Web Design & Development",
         short="Fast, conversion-focused websites and online stores that make your brand look world-class on every screen.",
         tags=["Business sites", "E-commerce", "Landing pages"],
         long="We design and build websites that load fast, rank well and turn visitors into enquiries. Every build starts with your customer journey — what they need to see, trust and click — then we craft a responsive interface that reflects your brand and is easy for your team to update.",
         deliver=["UX strategy & wireframes", "Custom UI design", "Mobile-first development", "E-commerce & payments (Paystack, Flutterwave)", "On-page SEO built in", "Analytics & conversion tracking"],
         img=("1487338875411-8880f74114a2", "hero-strategy.webp", "Designer workstation with two monitors showing a website layout"),
         faq=[("How long does a website take?", "A typical business website takes 2–4 weeks from kickoff to launch. Larger e-commerce or custom builds take 4–8 weeks. We agree a timeline before we start."),
              ("Do you offer ongoing maintenance?", "Yes. Our care plans cover updates, security monitoring, backups, uptime checks and content changes so your site keeps performing after launch.")]),
    dict(id="software", icon="workflow", name="Custom Software & SAP Integration",
         short="Web apps, automations and SAP BTP / Integration Suite work that connect your systems and remove manual effort.",
         tags=["SAP BTP", "SAP CPI", "APIs", "Automation"],
         long="Our engineers build custom web applications, dashboards and integrations — including SAP BTP, SAP Integration Suite (CPI) and ABAP work. If your team re-types data between systems or runs the business on spreadsheets, we can automate it.",
         deliver=["Custom web apps & portals", "API design & integration", "SAP BTP & Integration Suite (CPI)", "ABAP development", "Workflow automation", "Dashboards & reporting"],
         img=("1562910859-be83f1df7b56", "dev-coding.webp", "Three developers collaborating on laptops"),
         faq=[("Do you work with existing systems?", "Yes. Most of our software work is connecting what you already have — ERPs, CRMs, payment gateways and spreadsheets — rather than replacing it."),
              ("Can you support SAP projects?", "Our team includes SAP technical and functional consultants covering BTP, CPI, ABAP, FICO and supply chain.")]),
    dict(id="seo", icon="search", name="Search Engine Optimisation",
         short="Get found on Google by the customers already searching for what you sell — and win the clicks that matter.",
         tags=["Technical SEO", "Local SEO", "Content"],
         long="SEO puts your business in front of people who are actively searching for your products or services. We fix the technical foundations, optimise every page for the right keywords, build your Google Business Profile and earn quality backlinks for durable, compounding growth.",
         deliver=["SEO audit & keyword research", "Technical fixes & Core Web Vitals", "On-page optimisation", "Google Business Profile & local SEO", "Content strategy & blog writing", "Monthly ranking & traffic reports"],
         img=("1551288049-bebda4e38f71", "blog-seo.webp", "Analytics dashboard showing website traffic growth"),
         faq=[("What is organic traffic and why does it matter?", "Organic traffic is visitors from unpaid search results. They are actively looking for what you offer, so they tend to convert better — and you don't pay per click."),
              ("How long does SEO take to show results?", "Early improvements often appear in 4–8 weeks; significant ranking and traffic gains usually take 3–6 months of consistent work, depending on competition.")]),
    dict(id="ppc", icon="target", name="Paid Ads (PPC)",
         short="Google, Meta and TikTok campaigns built to generate leads and sales from day one — with every naira tracked.",
         tags=["Google Ads", "Meta Ads", "Retargeting"],
         long="Pay-per-click advertising puts you at the top of Google and in social feeds instantly. We handle keyword and audience research, ad creative, landing pages, bidding and weekly optimisation — and we report on cost per lead and return on ad spend, not vanity metrics.",
         deliver=["Google Search & Performance Max", "Meta (Facebook & Instagram) ads", "Retargeting campaigns", "Landing page optimisation", "Conversion tracking setup", "Weekly optimisation & reporting"],
         img=("1460925895917-afdab827c52f", "hero-workshop.webp", "Laptop showing ad campaign performance charts"),
         faq=[("How is PPC different from SEO?", "With PPC you pay for each click and results start almost immediately. SEO earns free traffic but takes longer. The strongest strategies use both."),
              ("What budget do I need?", "You can start testing with a modest monthly ad budget. We'll recommend a figure based on your market and goals, then scale what works.")]),
    dict(id="email-sms", icon="mail", name="Email & SMS Marketing",
         short="Automated sequences, newsletters and SMS campaigns that nurture leads and bring customers back to buy again.",
         tags=["Automation", "Newsletters", "Bulk SMS"],
         long="Email and SMS remain the highest-return channels you own. We set up your platform, design on-brand templates, write the copy and build automations — welcome series, abandoned-cart reminders, re-engagement — that sell while you sleep.",
         deliver=["Platform setup (Mailchimp, Brevo, etc.)", "Branded email templates", "Welcome & nurture sequences", "Abandoned-cart flows", "Bulk SMS campaigns", "List growth & segmentation"],
         img=("1573164574001-518958d9baa2", "hero-team.webp", "Marketer working on an email campaign on a laptop"),
         faq=[("What is a drip campaign?", "A drip campaign is a series of automated emails sent over time — for example, a welcome series that introduces your brand, shares proof and ends with an offer."),
              ("Will my emails land in spam?", "We configure domain authentication (SPF, DKIM, DMARC) and follow sending best practice to protect your deliverability.")]),
    dict(id="social-media", icon="megaphone", name="Social Media Management",
         short="Scroll-stopping content, community management and paid social that grow a brand people trust and buy from.",
         tags=["Content", "Community", "Strategy"],
         long="We plan, create and publish content that fits each platform — Instagram, Facebook, LinkedIn, TikTok and X — and manage your community so every comment and DM is an opportunity. Monthly reports show reach, engagement and, most importantly, enquiries.",
         deliver=["Social strategy & content calendar", "Graphics, reels & short video", "Copywriting & captions", "Community & DM management", "Influencer collaborations", "Monthly performance reports"],
         img=("1573164574230-db1d5e960238", "hero-strategy.webp", "Social media manager using a smartphone and laptop"),
         faq=[("How do you measure success on social media?", "Engagement rate, reach, follower growth, website clicks and — most importantly — enquiries and sales attributed to social."),
              ("What is a content calendar?", "A planned schedule of posts across platforms, aligned to your campaigns, so you post consistently and strategically.")]),
]
EXTRA = [
    dict(id="hosting", icon="server", name="Web Hosting & Care Plans",
         long="Secure, fast hosting with SSL, daily backups, uptime monitoring and a team on call. We look after the technical side so your website is always online and up to date.",
         deliver=["Managed hosting & SSL", "Domain & business email setup", "Daily backups", "Security & uptime monitoring", "Software & plugin updates", "Priority support"],
         img=("1680992046626-418f7e910589", "circuit.webp", "Server rack in a data centre"),
         faq=[]),
    dict(id="training", icon="graduation-cap", name="Digital Skills Training",
         long="Hands-on training for teams and individuals — digital marketing, website management, SAP fundamentals and practical AI tools — so your people can run and grow your digital presence confidently.",
         deliver=["Digital marketing workshops", "Website & CMS training", "SAP fundamentals", "AI tools for productivity", "Corporate team sessions", "1:1 coaching"],
         img=("1573164574048-f968d7ee9f20", "office.webp", "Two professionals learning together on laptops"),
         faq=[]),
]

TEAM = [
    dict(name="Okedigwe Kingsley", role="Founder · Full-Stack Software Developer", img="team-kingsley.webp", w=600, h=801,
         tags=["SAP BTP", "SAP CPI", "ABAP", "Node.js", "Python"],
         links=[("linkedin", "https://www.linkedin.com/in/kingsleyifeanyi26/"), ("twitter", "https://x.com/OkeDigwe"), ("github", "https://github.com/Okedigwe/")]),
    dict(name="Engr. Majed Juhi", role="Senior SAP Technical Consultant · Front-End Engineer", img="team-majed.webp", w=600, h=867,
         tags=["Integration Suite", "SAP BTP", "React", "Node.js"], links=[]),
    dict(name="Walter Ebuka O.", role="Back-End Software Developer", img="team-walter.webp", w=600, h=770,
         tags=["C#", "Node.js", "SQL", "SAP Support"],
         links=[("linkedin", "https://www.linkedin.com/in/onyekwelu-ebuka-81447423a")]),
    dict(name="Bobai Nuhu", role="SAP Functional Consultant · Sales", img="team-bobai.webp", w=577, h=787,
         tags=["Supply Chain", "FICO", "Sales Cloud", "MBA"],
         links=[("linkedin", "https://www.linkedin.com/in/bobainuhu"), ("twitter", "https://x.com/BobaiNuhu"), ("instagram", "https://www.instagram.com/Bobbynuhu")]),
    dict(name="Nonia Madisa", role="Software Developer Associate · Customer Success", img="team-nonia.webp", w=600, h=768,
         tags=["Client Support", "QA", "Web"],
         links=[("linkedin", "https://www.linkedin.com/in/nonia-madisa-31a653221/"), ("facebook", "https://www.facebook.com/nonia.madisa")]),
    dict(name="Ikechukwu Austin", role="Software Developer Associate", img="team-austin.webp", w=600, h=505,
         tags=["BSc Computer Science", "JavaScript", "Web"], links=[]),
]

HOME_FAQ = [
    ("How much does a website cost?", "It depends on scope — a focused business website costs far less than a custom e-commerce platform. Tell us what you need and we'll send a clear, fixed quote within one business day."),
    ("Do you work with businesses outside Nigeria?", "Yes. We work remotely with clients across Africa, the UK, the US and beyond, using video calls, shared project boards and WhatsApp for quick updates."),
    ("Will my website be mobile-friendly and SEO-ready?", "Always. Every site we build is mobile-first, fast-loading and structured for search engines, with analytics set up from day one."),
    ("Can you manage my marketing after launch?", "Yes. Many clients keep us on for SEO, ads, social media and email so there's one team accountable for growth."),
    ("How do we get started?", "Book a free consultation or send us a WhatsApp message. We'll learn about your goals, recommend an approach and send a proposal — no obligation."),
]


# ------------------------------------------------------------------ layout
def head(title, desc, path, extra_ld=None, og_type="website"):
    url = SITE + path
    org = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "@id": SITE + "/#organization",
        "name": BRAND,
        "alternateName": "E-Fitek",
        "url": SITE + "/",
        "logo": SITE + "/icon-512.png",
        "image": SITE + "/og-image.jpg",
        "description": "Web design, software development, SEO, paid ads, email & SMS and social media marketing for growing businesses.",
        "telephone": PHONE,
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressCountry": "NG"},
        "areaServed": ["Nigeria", "Africa", "Worldwide"],
        "priceRange": "₦₦",
        "sameAs": [s[1] for s in SOCIALS],
        "knowsAbout": ["Web design", "Search engine optimisation", "Pay-per-click advertising", "Social media marketing", "Email marketing", "SAP BTP", "SAP Integration Suite"],
    }
    lds = [org, {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/", "name": BRAND, "publisher": {"@id": SITE + "/#organization"}}]
    if extra_ld:
        lds += extra_ld
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    ga = ""
    if GA4_ID:
        ga = f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>"""
    gsc = f'<meta name="google-site-verification" content="{GSC_TOKEN}">' if GSC_TOKEN else ""
    return f"""<!DOCTYPE html>
<html lang="en-NG" class="no-js">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#060a1f">
{gsc}
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_NG">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@e_fitek">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/og-image.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/assets/fonts/jakarta.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preconnect" href="https://images.unsplash.com">
<link rel="stylesheet" href="/assets/css/main.css?v=2">
{ld}
{ga}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
"""


NAV = [("Home", "/"), ("Services", "/services"), ("About", "/about"), ("Insights", BLOG), ("Contact", "/contact")]


def header(active):
    cur = ' aria-current="page"'
    ext = ' target="_blank" rel="noopener"'
    links = "".join(
        f'<li><a href="{h}"{cur if h == active else ""}{ext if h.startswith("http") else ""}>{n}</a></li>'
        for n, h in NAV)
    return f"""<header class="site-header">
  <div class="container nav">
    <a class="brand" href="/" aria-label="{BRAND} — home">
      <img src="/assets/img/logo-mark-light.png" alt="" width="141" height="156">
      <span class="brand-name">E-FITEK<small>DIGITAL SERVICES</small></span>
    </a>
    <nav aria-label="Main">
      <ul class="nav-links" id="nav-links">{links}
        <li class="mobile-cta"><a class="btn btn-primary" href="/contact">Book a free consultation {ic("arrow-right")}</a></li>
      </ul>
    </nav>
    <div class="nav-cta">
      <a class="btn btn-primary btn-sm" href="/contact">Free consultation {ic("arrow-right")}</a>
      <button class="nav-toggle" aria-label="Open menu" aria-expanded="false" aria-controls="nav-links">
        {ic("menu", "icon i-open")}{ic("x", "icon i-close")}
      </button>
    </div>
  </div>
</header>
"""


def footer():
    socials = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{l}">{ic(i)}</a>' for i, u, l in SOCIALS)
    svc = "".join(f'<li><a href="/services#{s["id"]}">{s["name"]}</a></li>' for s in SERVICES)
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-about">
        <a class="brand" href="/"><img src="/assets/img/logo-mark-light.png" alt="" width="141" height="156"><span class="brand-name">E-FITEK<small>DIGITAL SERVICES</small></span></a>
        <p>A Nigerian digital studio building websites, software and marketing engines that help ambitious businesses grow online.</p>
        <div class="socials">{socials}</div>
      </div>
      <div><h4>Services</h4><ul>{svc}</ul></div>
      <div><h4>Company</h4><ul>
        <li><a href="/about">About us</a></li><li><a href="/about#team">Our team</a></li>
        <li><a href="{BLOG}" target="_blank" rel="noopener">Insights &amp; blog</a></li>
        <li><a href="/contact">Contact</a></li><li><a href="/voice-chatbot-app.html">AI voice assistant</a></li></ul></div>
      <div><h4>Get in touch</h4><ul class="footer-contact">
        <li>{ic("phone")}<a href="tel:{PHONE}">{PHONE_H}</a></li>
        <li>{ic("message-circle")}<a href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></li>
        <li>{ic("mail")}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{ic("clock")}<span>Mon – Fri, 8am – 6pm WAT</span></li></ul></div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> {BRAND}. All rights reserved.</span>
      <span>Designed &amp; built in Nigeria for the world.</span>
    </div>
    <div class="footer-word" aria-hidden="true">E-FITEK</div>
  </div>
</footer>
<div class="fab-stack">
  <button class="fab fab-top" aria-label="Back to top">{ic("arrow-right")}</button>
  <a class="fab fab-voice" href="/voice-chatbot-app.html" target="_blank" rel="noopener" aria-label="Talk to our AI voice assistant">{ic("mic")}<span>Ask our AI</span></a>
  <a class="fab fab-wa" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ic("message-circle")}<span>WhatsApp us</span></a>
</div>
<script src="/assets/js/main.js?v=2" defer></script>
</body>
</html>
"""


def cta_band(title="Ready to grow online?", text="Tell us about your business and goals. We'll reply within one business day with ideas and a clear, no-obligation proposal."):
    return f"""<section class="section cta-section">
  <div class="container">
    <div class="cta-band reveal">
      <div><h2>{title}</h2><p>{text}</p></div>
      <div class="actions">
        <a class="btn btn-primary" href="/contact">Book a free consultation {ic("arrow-right")}</a>
        <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">{ic("message-circle")} WhatsApp</a>
      </div>
    </div>
  </div>
</section>
"""


def faq_block(items):
    return "".join(
        f'<details class="reveal"><summary>{q}{ic("chevron-down")}</summary><div class="answer"><p>{a}</p></div></details>'
        for q, a in items)


def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumbs_ld(name, path):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
        {"@type": "ListItem", "position": 2, "name": name, "item": SITE + path}]}


def page_hero(eyebrow, title, lead, crumb):
    return f"""<section class="page-hero">
  <div class="container">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span aria-hidden="true">/</span><span>{crumb}</span></nav>
    <span class="eyebrow">{eyebrow}</span>
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
  </div>
</section>
"""


# ------------------------------------------------------------------ pages
def page_home():
    cards = ""
    for n, s in enumerate(SERVICES):
        tags = "".join(f'<span class="tag">{t}</span>' for t in s["tags"])
        feat = " featured" if n == 0 else ""
        cards += f"""<article class="svc-card reveal{feat}" data-delay="{n % 3 + 1}">
  <div class="svc-ic">{ic(s["icon"])}</div>
  <h3>{s["name"]}</h3>
  <p>{s["short"]}</p>
  <div class="tags">{tags}</div>
  <a class="link-arrow" href="/services#{s["id"]}">Explore service {ic("arrow-up-right")}</a>
</article>"""
    tech = ["SAP BTP", "SAP Integration Suite", "React", "Node.js", "Python", "Next.js", "WordPress", "Shopify", "Google Ads", "Meta Ads", "Google Analytics 4", "Mailchimp", "Paystack", "Flutterwave", "Vercel"]
    marquee = "".join(f"<span>{t}</span>" for t in tech * 2)

    out = head(
        "Web Design, SEO & Digital Marketing Agency in Nigeria | E-Fitek",
        "E-Fitek builds fast websites, custom software and SEO, ads and social media campaigns that win Nigerian businesses more customers. Free consultation.",
        "/", [faq_ld(HOME_FAQ)])
    out += header("/")
    out += f"""<main id="main">
<section class="hero">
  <div class="container hero-grid">
    <div>
      <span class="badge-pill"><b>NEW</b> Talk to our AI voice assistant — 24/7</span>
      <h1 class="h-display">We build digital <br>experiences that <span class="rotator grad-text" aria-live="polite">
        <span class="is-active">sell.</span><span>scale.</span><span>convert.</span><span>rank.</span><span>inspire.</span></span></h1>
      <p class="lead">Websites, software and marketing that turn attention into revenue. E-Fitek is the Nigerian digital team that designs, builds, hosts and grows your brand — end to end.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="/contact">Book a free consultation {ic("arrow-right")}</a>
        <a class="btn btn-ghost" href="/services">Explore services</a>
      </div>
      <ul class="hero-proof">
        <li>{ic("circle-check-big")} Reply within 1 business day</li>
        <li>{ic("circle-check-big")} Fixed, transparent quotes</li>
        <li>{ic("circle-check-big")} SAP-skilled engineers</li>
      </ul>
    </div>
    <div class="hero-visual">
      <div class="ring"></div>
      <div class="frame f1">{limg("hero-team.webp", "E-Fitek team collaborating on a client strategy", 787, 433, eager=True)}</div>
      <div class="frame f2">{limg("office.webp", "Modern open-plan office workspace", 709, 379)}</div>
      <div class="float-card c1"><div class="ic">{ic("trending-up")}</div><div><b>More leads</b><span>SEO + ads, tracked end-to-end</span></div><div class="spark" aria-hidden="true"><i style="height:40%"></i><i style="height:55%;animation-delay:.2s"></i><i style="height:48%;animation-delay:.4s"></i><i style="height:75%;animation-delay:.6s"></i><i style="height:100%;animation-delay:.8s"></i></div></div>
      <div class="float-card c2"><div class="ic">{ic("gauge")}</div><div><b>Built for speed</b><span>Mobile-first · Core Web Vitals</span></div></div>
    </div>
  </div>
</section>

<div class="marquee-wrap" aria-label="Technologies and platforms we work with">
  <p class="marquee-label">Platforms &amp; technologies we work with</p>
  <div class="marquee"><div class="marquee-track">{marquee}</div></div>
</div>

<section class="section" id="services">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">What we do</span>
      <h2 class="h-1">Everything you need to win online — under one roof.</h2>
      <p class="lead">From your first website to a full-funnel marketing engine and enterprise integrations, one accountable team handles strategy, design, build and growth.</p>
    </div>
    <div class="grid services-grid">{cards}</div>
  </div>
</section>

<section class="section section--tint">
  <div class="container split">
    <div class="media-stack reveal">
      <div class="main">{rimg("1573164574572-cb89e39749b4", "hero-strategy.webp", "Team of professionals planning a digital project around a table with laptops")}</div>
      <div class="inset">{rimg("1531482615713-2afd69097998", "hero-workshop.webp", "Two developers reviewing code on a monitor", 700)}</div>
      <div class="chip">{ic("shield-check")} One accountable team</div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Why E-Fitek</span>
      <h2 class="h-1">Strategy, engineering and marketing that work together.</h2>
      <p class="lead">Most businesses juggle a designer, a developer and a marketer who never talk. We bring them into one team focused on a single number: your growth.</p>
      <ul class="checklist">
        <li><span class="tick">{ic("check")}</span><div><b>Built to convert, not just to look good</b><span>Every page is designed around a clear action — call, WhatsApp, buy or book.</span></div></li>
        <li><span class="tick">{ic("check")}</span><div><b>Enterprise-grade engineering</b><span>Our SAP and full-stack engineers bring corporate-level quality to businesses of every size.</span></div></li>
        <li><span class="tick">{ic("check")}</span><div><b>Measured and transparent</b><span>Analytics and conversion tracking from day one, with plain-English monthly reports.</span></div></li>
        <li><span class="tick">{ic("check")}</span><div><b>Local insight, global standard</b><span>We understand Nigerian customers, payments and platforms — and build to international standards.</span></div></li>
      </ul>
      <a class="btn btn-dark" href="/about">Meet the team {ic("arrow-right")}</a>
    </div>
  </div>
</section>

<section class="section section--dark">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">How we work</span>
      <h2 class="h-1" style="color:#fff">From first call to measurable growth in four steps.</h2>
      <p class="lead">A clear, collaborative process — so you always know what's happening, what's next and what it costs.</p>
    </div>
    <div class="grid process">
      <div class="step reveal" data-delay="1"><h3>Discover</h3><p>A free consultation to understand your business, customers, competitors and goals.</p></div>
      <div class="step reveal" data-delay="2"><h3>Plan &amp; design</h3><p>A fixed proposal, sitemap and design concepts you approve before a line of code is written.</p></div>
      <div class="step reveal" data-delay="3"><h3>Build &amp; launch</h3><p>We develop, test on every device, set up tracking and launch with zero downtime.</p></div>
      <div class="step reveal" data-delay="4"><h3>Grow</h3><p>SEO, ads, social and email campaigns — optimised monthly against real business results.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal" style="display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;max-width:none">
      <div style="max-width:640px"><span class="eyebrow">Insights</span><h2 class="h-1" style="margin:0">Ideas to help your business grow.</h2></div>
      <a class="btn btn-outline" href="{BLOG}" target="_blank" rel="noopener">View all articles {ic("arrow-up-right")}</a>
    </div>
    <div class="grid posts">
      <a class="post reveal" data-delay="1" href="{BLOG}/2025/08/the-future-of-ai-in-web-development.html" target="_blank" rel="noopener">
        <div class="post-img">{limg("blog-ai.webp", "Developer working with AI-assisted coding tools", 800, 800)}</div>
        <div class="post-body"><div class="post-meta"><span class="tag">AI &amp; Development</span></div>
        <h3>The Future of AI in Web Development</h3><p>How artificial intelligence is changing the way software and websites are designed, built and maintained.</p>
        <span class="link-arrow">Read article {ic("arrow-up-right")}</span></div></a>
      <a class="post reveal" data-delay="2" href="{BLOG}/2025/08/essential-seo-tips-for-2025-stay-ahead.html" target="_blank" rel="noopener">
        <div class="post-img">{limg("blog-seo.webp", "Illustration of SEO analytics and search rankings", 800, 800)}</div>
        <div class="post-body"><div class="post-meta"><span class="tag">SEO</span></div>
        <h3>Essential SEO Tips to Stay Ahead</h3><p>Practical, proven steps to help your website rank higher on Google and attract more qualified visitors.</p>
        <span class="link-arrow">Read article {ic("arrow-up-right")}</span></div></a>
      <a class="post reveal" data-delay="3" href="/voice-chatbot-app.html" target="_blank" rel="noopener">
        <div class="post-img">{rimg("1551288049-bebda4e38f71", "dev-coding.webp", "Analytics dashboard on a laptop", 800)}</div>
        <div class="post-body"><div class="post-meta"><span class="tag">Try it</span></div>
        <h3>Meet the E-Fitek AI Voice Assistant</h3><p>Ask questions by voice, text or image and get instant answers about our services — any time of day.</p>
        <span class="link-arrow">Launch assistant {ic("arrow-up-right")}</span></div></a>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">FAQ</span><h2 class="h-1">Questions, answered.</h2></div>
    <div class="faq">{faq_block(HOME_FAQ)}</div>
  </div>
</section>
{cta_band()}
</main>
"""
    out += footer()
    return out


def svc_section(s, i):
    rev = " reverse" if i % 2 else ""
    deliver = "".join(f"<li>{ic('check')}{d}</li>" for d in s["deliver"])
    faq = ""
    if s["faq"]:
        faq = '<div class="mini-faq">' + "".join(
            f'<details><summary>{q}{ic("chevron-down")}</summary><p>{a}</p></details>' for q, a in s["faq"]) + "</div>"
    pid, fb, alt = s["img"]
    return f"""<section class="section svc-detail" id="{s["id"]}">
  <div class="container split{rev}">
    <div class="reveal">
      <div class="svc-media">{rimg(pid, fb, alt)}<span class="label">{ic(s["icon"])}{s["name"]}</span></div>
    </div>
    <div class="reveal" data-delay="1">
      <span class="eyebrow">Service {i + 1:02d}</span>
      <h2 class="h-1">{s["name"]}</h2>
      <p class="lead">{s["long"]}</p>
      <ul class="deliverables">{deliver}</ul>
      <a class="btn btn-dark" href="/contact?service={s["id"]}">Get a free proposal {ic("arrow-right")}</a>
      {faq}
    </div>
  </div>
</section>
"""


def page_services():
    allsvc = SERVICES + EXTRA
    nav = "".join(f'<li><a href="#{s["id"]}">{ic(s["icon"])}{s["name"]}</a></li>' for s in allsvc)
    body = "".join(svc_section(s, i) for i, s in enumerate(allsvc))
    faqs = [q for s in allsvc for q in s["faq"]]
    svc_ld = [{"@context": "https://schema.org", "@type": "Service", "name": s["name"], "description": s["long"],
               "provider": {"@id": SITE + "/#organization"}, "areaServed": "Nigeria",
               "url": f"{SITE}/services#{s['id']}"} for s in allsvc]
    out = head("Web Design, SEO, Ads, Social Media & SAP Services | E-Fitek",
               "Explore E-Fitek's services: website design & development, SEO, Google & Meta ads, email & SMS marketing, social media management, SAP integration, hosting and training.",
               "/services", [crumbs_ld("Services", "/services"), faq_ld(faqs)] + svc_ld)
    out += header("/services")
    out += '<main id="main">' + page_hero("Our services", "Digital services engineered for <span class=\"grad-text\">growth.</span>",
                                            "Choose a single service or combine them into a complete growth engine. Every engagement starts with a free consultation and a clear, fixed proposal.", "Services")
    out += f'<nav class="svc-nav" aria-label="Services"><div class="container"><ul>{nav}</ul></div></nav>'
    out += body + cta_band("Not sure which service you need?", "Tell us your goal — more leads, more sales, less admin — and we'll recommend the right mix for your budget.") + "</main>"
    out += footer()
    return out


def page_about():
    team = ""
    for n, m in enumerate(TEAM):
        tags = "".join(f'<span class="tag">{t}</span>' for t in m["tags"])
        links = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="{m["name"]} on {k.title()}">{ic(k)}</a>' for k, u in m["links"])
        team += f"""<article class="member reveal" data-delay="{n % 3 + 1}">
  <div class="member-photo">{limg(m["img"], "Portrait of " + m["name"], m["w"], m["h"])}<div class="member-socials">{links}</div></div>
  <div class="member-body"><h3>{m["name"]}</h3><p class="member-role">{m["role"]}</p><div class="tags">{tags}</div></div>
</article>"""
    person_ld = [{"@context": "https://schema.org", "@type": "Person", "name": m["name"], "jobTitle": m["role"],
                  "worksFor": {"@id": SITE + "/#organization"}, "sameAs": [u for _, u in m["links"]]} for m in TEAM]
    out = head("About E-Fitek | Meet Our Web, Software & Digital Marketing Team",
               "Meet the E-Fitek team — full-stack developers, SAP consultants and digital marketers helping businesses in Nigeria and beyond grow online.",
               "/about", [crumbs_ld("About", "/about")] + person_ld)
    out += header("/about")
    out += '<main id="main">' + page_hero("About us", "A team of builders obsessed with your <span class=\"grad-text\">growth.</span>",
                                            "E-Fitek Digital Services brings together software engineers, SAP consultants and digital marketers to give growing businesses the digital firepower of a large enterprise — without the overhead.", "About")
    out += f"""
<section class="section">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Our story</span>
      <h2 class="h-1">Enterprise skills, made accessible.</h2>
      <p class="lead">We started E-Fitek because great businesses were being held back by slow websites, disconnected tools and marketing that couldn't prove its value.</p>
      <p style="color:var(--text-2)">Our founders spent years delivering SAP and software projects for large organisations. We bring that same discipline — clear scoping, clean engineering, rigorous testing and measurable outcomes — to entrepreneurs, SMEs and corporates who want a partner that cares about results.</p>
      <p style="color:var(--text-2)">Today we design and build websites, custom software and integrations, host and maintain them, and run the SEO, advertising, social and email campaigns that keep customers coming.</p>
    </div>
    <div class="media-stack reveal" data-delay="1">
      <div class="main">{rimg("1573164574397-dd250bc8a598", "hero-strategy.webp", "Professionals collaborating around a table in a bright office")}</div>
      <div class="inset">{limg("hero-workshop.webp", "E-Fitek team workshop", 711, 387)}</div>
      <div class="chip">{ic("handshake")} Partners, not vendors</div>
    </div>
  </div>
</section>

<section class="section section--tint">
  <div class="container">
    <div class="section-head center reveal"><span class="eyebrow">What we value</span><h2 class="h-1">How we show up for every client.</h2></div>
    <div class="grid values">
      <div class="value reveal" data-delay="1">{ic("target")}<h3>Outcomes over output</h3><p>We measure success by leads, sales and time saved — not pages shipped.</p></div>
      <div class="value reveal" data-delay="2">{ic("lightbulb")}<h3>Clarity</h3><p>Plain-English advice, fixed quotes and no surprise invoices.</p></div>
      <div class="value reveal" data-delay="3">{ic("shield-check")}<h3>Craft &amp; quality</h3><p>Enterprise-grade engineering, tested on real devices and networks.</p></div>
      <div class="value reveal" data-delay="4">{ic("users")}<h3>Partnership</h3><p>We stay with you after launch and grow as your business grows.</p></div>
    </div>
  </div>
</section>

<section class="section" id="team">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Our team</span><h2 class="h-1">The people behind your growth.</h2>
    <p class="lead">Developers, SAP consultants and marketers who combine technical depth with a genuine love for building things that work.</p></div>
    <div class="grid team-grid">{team}</div>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container"><div class="story-img reveal">{limg("office.webp", "Bright, modern office where the E-Fitek team collaborates", 709, 379)}</div></div>
</section>
{cta_band("Let's build something great together.")}
</main>
"""
    out += footer()
    return out


def page_contact():
    chips = "".join(f'<label><input type="checkbox" name="services" value="{s["id"]}"><span>{s["name"]}</span></label>' for s in SERVICES + EXTRA)
    out = head("Contact E-Fitek | Free Website & Marketing Consultation",
               f"Talk to E-Fitek about your website, software or marketing project. Call or WhatsApp {PHONE_H}, email us, or send the form for a free, no-obligation proposal.",
               "/contact", [crumbs_ld("Contact", "/contact"), {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact", "about": {"@id": SITE + "/#organization"}}])
    out += header("/contact")
    out += '<main id="main">' + page_hero("Contact", "Let's talk about your <span class=\"grad-text\">next move.</span>",
                                            "Tell us what you're building or where you want to grow. We reply within one business day — usually much sooner on WhatsApp.", "Contact")
    out += f"""
<section class="section">
  <div class="container contact-grid">
    <div class="reveal">
      <span class="eyebrow">Reach us directly</span>
      <h2 class="h-2" style="font-size:clamp(26px,3vw,34px)">Prefer to talk? We're one tap away.</h2>
      <p style="color:var(--text-2);margin-bottom:28px">Book a free 30-minute consultation. We'll discuss your goals, give honest advice and outline the best next steps — whether or not you work with us.</p>
      <div class="contact-cards">
        <a class="contact-card wa" href="{WA}" target="_blank" rel="noopener"><span class="ic">{ic("message-circle")}</span><span><small>WhatsApp · fastest</small><b>{PHONE_H}</b></span>{ic("arrow-up-right", "icon go")}</a>
        <a class="contact-card" href="tel:{PHONE}"><span class="ic">{ic("phone")}</span><span><small>Call us</small><b>{PHONE_H}</b></span>{ic("arrow-up-right", "icon go")}</a>
        <a class="contact-card" href="mailto:{EMAIL}"><span class="ic">{ic("mail")}</span><span><small>Email</small><b>{EMAIL}</b></span>{ic("arrow-up-right", "icon go")}</a>
        <div class="contact-card"><span class="ic">{ic("clock")}</span><span><small>Hours</small><b>Mon – Fri, 8am – 6pm WAT</b></span></div>
      </div>
      <ul class="checklist" style="margin-top:34px">
        <li><span class="tick">{ic("check")}</span><div><b>Free, no-obligation proposal</b><span>Clear scope, timeline and fixed price.</span></div></li>
        <li><span class="tick">{ic("check")}</span><div><b>Your information stays private</b><span>We never share or sell your details.</span></div></li>
      </ul>
    </div>
    <div class="form-card reveal" data-delay="1" id="contact-form">
      <h2>Tell us about your project</h2>
      <p style="color:var(--text-2)">Fill in a few details and we'll come back with ideas and a proposal.</p>
      <form id="contact-form-el" action="{FORM}" method="POST">
        <input type="hidden" name="_subject" value="New enquiry from e-fitek website">
        <input type="text" name="_gotcha" style="display:none" tabindex="-1" autocomplete="off">
        <div class="form-grid">
          <div class="field"><label for="name">Full name</label><input id="name" name="name" autocomplete="name" required></div>
          <div class="field"><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email" required></div>
          <div class="field"><label for="phone">Phone / WhatsApp <span class="opt">(optional)</span></label><input id="phone" name="phone" type="tel" autocomplete="tel"></div>
          <div class="field"><label for="company">Company <span class="opt">(optional)</span></label><input id="company" name="company" autocomplete="organization"></div>
          <div class="field full"><label>What do you need help with?</label><div class="chips">{chips}</div></div>
          <div class="field full"><label for="budget">Estimated budget <span class="opt">(optional)</span></label>
            <select id="budget" name="budget"><option value="">Select a range</option><option>Under ₦500k</option><option>₦500k – ₦1.5m</option><option>₦1.5m – ₦5m</option><option>₦5m+</option><option>Not sure yet</option></select></div>
          <div class="field full"><label for="message">Project details</label><textarea id="message" name="message" required placeholder="What are you looking to achieve? Any deadlines or examples you like?"></textarea></div>
        </div>
        <button type="submit" class="btn btn-primary btn-block" style="margin-top:22px">Send message {ic("send")}</button>
        <p class="form-note">By sending this form you agree to be contacted about your enquiry.</p>
        <div class="form-status" role="status" aria-live="polite"></div>
      </form>
    </div>
  </div>
</section>
</main>
"""
    out += footer()
    return out


def page_404():
    out = head("Page not found | E-Fitek Digital Services", "The page you are looking for could not be found.", "/404")
    out = out.replace('<meta name="robots" content="index, follow, max-image-preview:large">', '<meta name="robots" content="noindex">')
    out += header("")
    out += f"""<main id="main"><section class="page-hero nf"><div class="container">
<div class="code grad-text">404</div><h1 style="margin-inline:auto">This page took a wrong turn.</h1>
<p class="lead" style="margin-inline:auto">The page you're looking for has moved or no longer exists.</p>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:28px"><a class="btn btn-primary" href="/">Back to home {ic("arrow-right")}</a><a class="btn btn-ghost" href="/contact">Contact us</a></div>
</div></section></main>"""
    out += footer()
    return out


def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)


if __name__ == "__main__":
    write("index.html", page_home())
    write("services.html", page_services())
    write("about.html", page_about())
    write("contact.html", page_contact())
    write("404.html", page_404())
    urls = [("/", "1.0", "weekly"), ("/services", "0.9", "monthly"), ("/about", "0.7", "monthly"), ("/contact", "0.8", "yearly")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{c}</changefreq><priority>{p}</priority></url>\n" for u, p, c in urls)
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /_src/\n\nSitemap: {SITE}/sitemap.xml\n")
