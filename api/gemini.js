// Vercel Serverless Function: secure proxy for the E-Fitek AI voice assistant.
// Set GEMINI_API_KEY in Vercel → Project → Settings → Environment Variables.
// The key never reaches the browser.

const ALLOWED_MODELS = new Set(["gemini-2.5-flash", "gemini-2.5-flash-preview-tts"]);
const ALLOWED_ORIGINS = [/^https:\/\/e-fitek\.vercel\.app$/, /^https:\/\/(www\.)?efitek\.[a-z.]+$/, /^http:\/\/localhost(:\d+)?$/];

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    return res.status(405).json({ error: { message: "Method not allowed" } });
  }

  const origin = req.headers.origin || "";
  if (origin && !ALLOWED_ORIGINS.some((re) => re.test(origin))) {
    return res.status(403).json({ error: { message: "Origin not allowed" } });
  }

  const key = process.env.GEMINI_API_KEY;
  if (!key) return res.status(500).json({ error: { message: "Assistant is not configured yet." } });

  const { model, payload } = req.body || {};
  if (!ALLOWED_MODELS.has(model) || !payload || !Array.isArray(payload.contents)) {
    return res.status(400).json({ error: { message: "Invalid request" } });
  }
  // Keep conversations bounded to protect your quota
  if (payload.contents.length > 40 || JSON.stringify(payload).length > 6_000_000) {
    return res.status(413).json({ error: { message: "Conversation too long — please refresh to start again." } });
  }

  try {
    const r = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
      method: "POST",
      headers: { "Content-Type": "application/json", "x-goog-api-key": key },
      body: JSON.stringify(payload),
    });
    const data = await r.json();
    return res.status(r.status).json(data);
  } catch (e) {
    return res.status(502).json({ error: { message: "Upstream error" } });
  }
};
