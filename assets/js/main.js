/* E-Fitek Digital Services — site behaviour (no dependencies) */
(function () {
  "use strict";
  document.documentElement.classList.remove("no-js");

  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => Array.from(c.querySelectorAll(s));

  /* Header: solid on scroll + mobile menu */
  const header = $(".site-header");
  const toggle = $(".nav-toggle");
  const topBtn = $(".fab-top");
  const onScroll = () => {
    const y = window.scrollY;
    if (header) header.classList.toggle("is-scrolled", y > 12);
    if (topBtn) topBtn.classList.toggle("show", y > 700);
  };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (toggle && header) {
    toggle.addEventListener("click", () => {
      const open = header.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    });
    $$(".nav-links a").forEach((a) =>
      a.addEventListener("click", () => {
        header.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
        document.body.style.overflow = "";
      })
    );
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && header.classList.contains("is-open")) toggle.click();
    });
  }

  if (topBtn) topBtn.addEventListener("click", () => window.scrollTo({ top: 0, behavior: "smooth" }));

  /* Hero word rotator */
  const rot = $(".rotator");
  if (rot) {
    const words = $$("span", rot);
    let i = 0;
    if (words.length > 1 && !matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setInterval(() => {
        const cur = words[i];
        cur.classList.remove("is-active");
        cur.classList.add("is-leaving");
        setTimeout(() => cur.classList.remove("is-leaving"), 500);
        i = (i + 1) % words.length;
        words[i].classList.add("is-active");
      }, 2400);
    }
  }

  /* Reveal on scroll */
  const reveals = $$(".reveal");
  if ("IntersectionObserver" in window) {
    const io = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      }),
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    reveals.forEach((el) => io.observe(el));
  } else {
    reveals.forEach((el) => el.classList.add("in"));
  }

  /* Remote images: swap to a local fallback if the CDN is unreachable */
  $$("img[data-fallback]").forEach((img) => {
    const swap = () => { if (img.src.indexOf(img.dataset.fallback) === -1) { img.removeAttribute("srcset"); img.src = img.dataset.fallback; } };
    img.addEventListener("error", swap, { once: true });
    if (img.complete && img.naturalWidth === 0) swap();
  });

  /* Services page: sticky sub-nav scrollspy */
  const svcLinks = $$(".svc-nav a");
  if (svcLinks.length && "IntersectionObserver" in window) {
    const map = new Map(svcLinks.map((a) => [a.getAttribute("href").slice(1), a]));
    const spy = new IntersectionObserver(
      (entries) => entries.forEach((e) => {
        if (e.isIntersecting) {
          svcLinks.forEach((a) => a.classList.remove("is-active"));
          const a = map.get(e.target.id);
          if (a) { a.classList.add("is-active"); a.scrollIntoView({ block: "nearest", inline: "center" }); }
        }
      }),
      { rootMargin: "-45% 0px -50% 0px" }
    );
    map.forEach((_, id) => { const s = document.getElementById(id); if (s) spy.observe(s); });
  }

  /* Contact form: pre-select service from ?service=, submit via fetch */
  const form = $("#contact-form-el");
  if (form) {
    const want = new URLSearchParams(location.search).get("service");
    if (want) {
      const box = form.querySelector(`input[name="services"][value="${CSS.escape(want)}"]`);
      if (box) box.checked = true;
    }
    const status = $(".form-status", form);
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const btn = form.querySelector("button[type=submit]");
      const label = btn.innerHTML;
      btn.disabled = true; btn.textContent = "Sending…";
      status.className = "form-status";
      try {
        const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
        if (!res.ok) throw new Error("Request failed");
        form.reset();
        status.textContent = "Thank you — your message is in. We reply within one business day.";
        status.classList.add("ok");
        if (window.gtag) window.gtag("event", "generate_lead", { method: "contact_form" });
      } catch (err) {
        status.innerHTML = 'Something went wrong. Please WhatsApp us on <a href="https://wa.me/2348167712361" style="text-decoration:underline">+234 816 771 2361</a>.';
        status.classList.add("err");
      } finally {
        btn.disabled = false; btn.innerHTML = label;
      }
    });
  }

  /* Track WhatsApp / phone / email clicks as conversions (if GA4 is installed) */
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href]");
    if (!a || !window.gtag) return;
    const h = a.getAttribute("href");
    if (h.startsWith("https://wa.me")) window.gtag("event", "contact_whatsapp");
    else if (h.startsWith("tel:")) window.gtag("event", "contact_phone");
    else if (h.startsWith("mailto:")) window.gtag("event", "contact_email");
  });

  /* Footer year */
  $$("[data-year]").forEach((el) => (el.textContent = new Date().getFullYear()));

  /* Tawk.to live chat — deferred until the visitor interacts (keeps first load fast) */
  let tawkLoaded = false;
  const loadTawk = () => {
    if (tawkLoaded) return; tawkLoaded = true;
    window.Tawk_API = window.Tawk_API || {}; window.Tawk_LoadStart = new Date();
    const s = document.createElement("script");
    s.async = true; s.src = "https://embed.tawk.to/689e6323ea06af19271e3e5b/1j2lb6hid"; s.charset = "UTF-8"; s.setAttribute("crossorigin", "*");
    document.body.appendChild(s);
    document.body.classList.add("has-tawk");
  };
  ["scroll", "pointerdown", "keydown", "touchstart"].forEach((ev) => window.addEventListener(ev, loadTawk, { once: true, passive: true }));
  setTimeout(loadTawk, 9000);
})();
