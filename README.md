# E-Fitek Digital Services — website v2

Static, dependency-free site deployed on Vercel.

## Structure
- `index.html`, `services.html`, `about.html`, `contact.html`, `404.html` — generated pages
- `_src/build.py` — **edit content here** (services, team, FAQs, contact details), then run `python3 _src/build.py`
- `assets/css/main.css` — design system · `assets/js/main.js` — interactions · `assets/icons.svg` — icon sprite
- `assets/img/` — optimised WebP images (≈0.5 MB total, down from ≈25 MB)
- `api/gemini.js` — secure server-side proxy for the AI voice assistant
- `vercel.json` — clean URLs, redirects, caching and security headers
- `sitemap.xml`, `robots.txt`, `site.webmanifest`, `og-image.jpg`

## Deploy
1. Replace the repo contents with this folder (delete the old PNG/MP4 files, `styles.css`, `script.js`, `team.html`, `launch-chatbot-page.html`, `voice-chatbot.html`).
2. In Vercel → Settings → Environment Variables add `GEMINI_API_KEY` (use a **new** key — the old one was public in the repo).
3. Push. Vercel deploys automatically.

## Before you go live
- Set `GA4_ID` and `GSC_TOKEN` in `_src/build.py`, rebuild, push.
- When you buy a domain, change `SITE` in `_src/build.py`, rebuild, and add the domain in Vercel.
