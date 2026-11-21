#!/usr/bin/env node
// Renders thumbnails (1280x720) and on-screen charts (1920x1080) from JSON specs.
//
//   node tools/render/render.mjs content/001-movie-theater-popcorn/visuals/specs.json
//
// Brand assets: node tools/render/render.mjs brand/specs.json  (types: logo, banner)
// A spec file holds {"items": [ ...specs ]}. Every spec has "type" and "out"
// (PNG path relative to the spec file). Types:
//   thumbnail  template A | B | C | D   (see docs/05 section 4)
//   receipt    the channel's signature "receipt" breakdown ("show_total": false hides the total), plus one PNG per
//              revealed line (…-step01.png) so the editor can build the reveal
//   stacked    one horizontal "where your $X goes" bar, plus reveal steps
//   compare    2–5 vertical bars comparing amounts
// Colors and fonts live in BRAND below and mirror docs/02-channel-identity.md.

import { readFile, mkdir } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import path from "node:path";
import { illustration } from "./illustrations.mjs";

// require() honours NODE_PATH / global installs, which ESM `import` does not,
// so Playwright is found whether it is installed locally or globally.
const { chromium } = createRequire(import.meta.url)("playwright");

export const BRAND = {
  ink: "#0E0F12",
  ink2: "#1A1C22",
  paper: "#F4F1EA",
  coral: "#FF5A4E",
  green: "#2BD38A",
  yellow: "#FFD23F",
  blue: "#4C8DFF",
  gray: "#9AA0A6",
  head: "'Inter Display', 'Inter', sans-serif",
  mono: "'JetBrains Mono', monospace",
};

// Local images are inlined as data URIs: pages are loaded with setContent (about:blank),
// where Chromium refuses file:// URLs.
const dataUri = (p) => `data:image/${p.toLowerCase().endsWith(".jpg") ? "jpeg" : "png"};base64,${readFileSync(p).toString("base64")}`;

const esc = (s = "") =>
  String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

const toneColor = (tone) => ({ loss: BRAND.coral, profit: BRAND.green, neutral: BRAND.paper, highlight: BRAND.yellow, blue: BRAND.blue })[tone] || BRAND.paper;

const page = (w, h, body, extraCss = "") => `<!doctype html><html><head><meta charset="utf-8"><style>
*{box-sizing:border-box;margin:0;padding:0}
body{width:${w}px;height:${h}px;background:${BRAND.ink};color:${BRAND.paper};font-family:${BRAND.head};overflow:hidden;position:relative}
.vignette{position:absolute;inset:0;background:radial-gradient(ellipse at 35% 45%, #2A2D36 0%, ${BRAND.ink} 65%)}
.hero svg{width:100%;height:100%;display:block;filter:drop-shadow(0 18px 30px rgba(0,0,0,.55))}
.incision{position:absolute;border-top:7px dashed ${BRAND.coral};transform-origin:left center}
.source{position:absolute;left:64px;bottom:34px;font:500 22px ${BRAND.mono};color:${BRAND.gray}}
.brandtag{position:absolute;right:56px;bottom:30px;font:800 22px ${BRAND.head};letter-spacing:4px;color:${BRAND.gray}}
${extraCss}</style></head><body><div class="vignette"></div>${body}</body></html>`;

// ---------- thumbnails (1280x720) ----------

function heroBlock(spec, css) {
  const inner = spec.image
    ? `<img src="${dataUri(path.resolve(spec._dir, spec.image))}" style="width:100%;height:100%;object-fit:contain">`
    : illustration(spec.object || "coin");
  return `<div class="hero" style="position:absolute;${css}">${inner}</div>`;
}

function thumbA(s) {
  // Receipt coming out of the object; one line circled.
  const lines = (s.receipt_lines || [])
    .map((l) => {
      const circled = l.circle ? `outline:6px solid ${BRAND.coral};outline-offset:6px;border-radius:14px;` : "";
      return `<div style="display:flex;justify-content:space-between;gap:24px;padding:6px 0;${circled}"><span>${esc(l.label)}</span><span>${esc(l.amount)}</span></div>`;
    })
    .join("");
  return page(1280, 720, `
    ${heroBlock(s, "left:60px;top:215px;width:490px;height:490px")}
    <div style="position:absolute;right:70px;top:150px;width:520px;transform:rotate(3deg);background:${BRAND.paper};color:${BRAND.ink};font:700 40px ${BRAND.mono};padding:34px 38px 46px;box-shadow:0 20px 50px rgba(0,0,0,.6);clip-path:polygon(0 0,100% 0,100% 96%,95% 100%,90% 96%,85% 100%,80% 96%,75% 100%,70% 96%,65% 100%,60% 96%,55% 100%,50% 96%,45% 100%,40% 96%,35% 100%,30% 96%,25% 100%,20% 96%,15% 100%,10% 96%,5% 100%,0 96%)">
      <div style="font:900 30px ${BRAND.head};letter-spacing:6px;text-align:center;margin-bottom:18px">${esc(s.receipt_title || "RECEIPT")}</div>
      ${lines}
    </div>
    ${s.headline ? `<div style="position:absolute;left:56px;top:34px;font:900 84px/1 ${BRAND.head};color:${toneColor(s.headline_tone || "highlight")};text-shadow:0 6px 0 #000;max-width:640px;white-space:nowrap">${esc(s.headline)}</div>` : ""}
  `);
}

function thumbB(s) {
  // Object cut by a dashed incision; slices with percentages on the right.
  const slices = (s.slices || [])
    .map(
      (sl) => `<div style="display:flex;align-items:baseline;justify-content:flex-end;gap:22px">
        <span style="font:800 ${sl.big ? 46 : 36}px ${BRAND.head};color:${BRAND.gray};letter-spacing:3px">${esc(sl.label)}</span>
        <span style="font:900 ${sl.big ? 170 : 96}px/0.95 ${BRAND.head};color:${toneColor(sl.tone)};text-shadow:0 8px 0 #000">${esc(sl.value)}</span></div>`
    )
    .join("");
  return page(1280, 720, `
    ${heroBlock(s, "left:60px;top:80px;width:520px;height:600px")}
    <div class="incision" style="left:20px;top:330px;width:640px;transform:rotate(-8deg)"></div>
    <div style="position:absolute;right:70px;top:50%;transform:translateY(-50%);display:flex;flex-direction:column;gap:10px">${slices}</div>
  `);
}

function thumbC(s) {
  // Two prices: what it costs vs what you pay.
  const l = s.left || {}, r = s.right || {};
  return page(1280, 720, `
    ${heroBlock(s, `left:${s.hero_left ?? 400}px;top:${s.hero_top ?? 170}px;width:${s.hero_w ?? 480}px;height:${s.hero_h ?? 340}px`)}
    <div style="position:absolute;left:56px;top:70px;text-align:left">
      <div style="font:800 40px ${BRAND.head};color:${BRAND.gray};letter-spacing:4px">${esc(l.label || "COSTS")}</div>
      <div style="font:900 150px/1 ${BRAND.head};color:${toneColor(l.tone || "profit")};text-shadow:0 8px 0 #000">${esc(l.value)}</div>
    </div>
    <div style="position:absolute;right:56px;bottom:70px;text-align:right">
      <div style="font:800 40px ${BRAND.head};color:${BRAND.gray};letter-spacing:4px">${esc(r.label || "YOU PAY")}</div>
      <div style="font:900 190px/1 ${BRAND.head};color:${toneColor(r.tone || "loss")};text-shadow:0 8px 0 #000">${esc(r.value)}</div>
    </div>
    <svg style="position:absolute;left:0;top:0" width="1280" height="720" viewBox="0 0 1280 720"><path d="M150 300 Q150 600 660 590" fill="none" stroke="${BRAND.yellow}" stroke-width="14" stroke-linecap="round"/><path d="M628 560 L664 590 L626 622" fill="none" stroke="${BRAND.yellow}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/></svg>
  `);
}

function thumbD(s) {
  // Object + one dramatic bar chart.
  const bars = s.bars || [];
  const max = Math.max(...bars.map((b) => b.value), 1);
  const barHtml = bars
    .map(
      (b) => `<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;gap:10px">
        <div style="font:900 ${b.big ? 84 : 56}px ${BRAND.head};color:${toneColor(b.tone)};text-shadow:0 6px 0 #000">${esc(b.display ?? b.value)}</div>
        <div style="width:150px;height:${Math.max(4, (b.value / max) * 420)}px;background:${toneColor(b.tone)};border-radius:12px 12px 0 0"></div>
        <div style="font:800 30px ${BRAND.head};color:${BRAND.gray};letter-spacing:3px">${esc(b.label)}</div></div>`
    )
    .join("");
  return page(1280, 720, `
    ${heroBlock(s, "left:30px;top:150px;width:520px;height:520px")}
    ${s.headline ? `<div style="position:absolute;left:56px;top:40px;font:900 84px/1 ${BRAND.head};color:${toneColor(s.headline_tone || "highlight")};text-shadow:0 6px 0 #000;max-width:620px">${esc(s.headline)}</div>` : ""}
    <div style="position:absolute;right:60px;bottom:50px;height:600px;display:flex;gap:40px;align-items:flex-end">${barHtml}</div>
  `);
}

// ---------- on-screen charts (1920x1080) ----------

function receiptPage(s, upto) {
  const items = s.lines || [];
  const shown = items.slice(0, upto);
  const rows = shown
    .map(
      (l) => `<div style="display:flex;justify-content:space-between;gap:40px;padding:10px 0;color:${l.tone ? toneColor(l.tone) === BRAND.paper ? BRAND.ink : toneColor(l.tone) : BRAND.ink};${l.tone === "profit" || l.tone === "loss" ? "font-weight:800" : ""}">
        <span>${esc(l.label)}${l.note ? `<span style="display:block;font-size:24px;color:#6B6F76;font-weight:500">${esc(l.note)}</span>` : ""}</span><span>${esc(l.amount)}</span></div>`
    )
    .join("");
  // "show_total": false keeps the total hidden (e.g. when the reveal comes later in the video).
  const done = upto >= items.length && s.show_total !== false;
  const total = done && s.total
    ? `<div style="border-top:4px dashed ${BRAND.ink};margin-top:18px;padding-top:18px;display:flex;justify-content:space-between;font-weight:900;font-size:52px"><span>${esc(s.total.label || "TOTAL")}</span><span>${esc(s.total.amount)}</span></div>`
    : "";
  return page(1920, 1080, `
    ${s.object ? heroBlock({ ...s }, "left:120px;top:250px;width:620px;height:620px") : ""}
    <div style="position:absolute;left:120px;top:90px;font:900 72px/1.05 ${BRAND.head};max-width:760px">${esc(s.title || "")}</div>
    <div style="position:absolute;right:160px;top:80px;width:860px;background:${BRAND.paper};color:${BRAND.ink};font:600 40px ${BRAND.mono};padding:48px 56px 64px;box-shadow:0 30px 70px rgba(0,0,0,.6)">
      <div style="font:900 34px ${BRAND.head};letter-spacing:8px;text-align:center;margin-bottom:24px">${esc(s.receipt_title || "RECEIPT")}</div>
      ${rows}${total}
    </div>
    ${s.source ? `<div class="source">Source: ${esc(s.source)}</div>` : ""}
    <div class="brandtag">${esc(s.brand || "")}</div>
  `);
}

function stackedPage(s, upto) {
  const segs = s.segments || [];
  const sum = segs.reduce((a, b) => a + b.value, 0) || 1;
  const width = 1680;
  let x = 0;
  const blocks = segs
    .map((g, i) => {
      const w = (g.value / sum) * width;
      const visible = i < upto;
      const html = `<div style="position:absolute;left:${x}px;top:0;width:${w}px;height:180px;background:${visible ? toneColor(g.tone || "neutral") : "#2A2D36"};border-right:4px solid ${BRAND.ink}"></div>
        ${visible ? `<div style="position:absolute;left:${x}px;top:${i % 2 ? 300 : 200}px;width:${Math.max(w, 220)}px;font:800 34px ${BRAND.head};color:${toneColor(g.tone || "neutral")}">${esc(g.display ?? g.value)}<div style="font:600 26px ${BRAND.head};color:${BRAND.gray}">${esc(g.label)}</div></div>` : ""}`;
      x += w;
      return html;
    })
    .join("");
  return page(1920, 1080, `
    <div style="position:absolute;left:120px;top:110px;font:900 76px/1.05 ${BRAND.head};max-width:1600px">${esc(s.title || "")}</div>
    ${s.subtitle ? `<div style="position:absolute;left:120px;top:280px;font:600 36px ${BRAND.head};color:${BRAND.gray}">${esc(s.subtitle)}</div>` : ""}
    <div style="position:absolute;left:120px;top:420px;width:${width}px;height:420px">${blocks}</div>
    ${s.source ? `<div class="source">Source: ${esc(s.source)}</div>` : ""}
    <div class="brandtag">${esc(s.brand || "")}</div>
  `);
}

function comparePage(s) {
  const bars = s.bars || [];
  const max = Math.max(...bars.map((b) => b.value), 1);
  // Leave room for the subtitle so the tallest bar's label never collides with it.
  const maxBar = s.subtitle ? 440 : 540;
  const areaH = s.subtitle ? 660 : 760;
  const html = bars
    .map(
      (b) => `<div style="display:flex;flex-direction:column;align-items:center;justify-content:flex-end;height:100%;gap:16px;width:260px">
        <div style="font:900 64px ${BRAND.head};color:${toneColor(b.tone)}">${esc(b.display ?? b.value)}</div>
        <div style="width:220px;height:${Math.max(6, (b.value / max) * maxBar)}px;background:${toneColor(b.tone)};border-radius:16px 16px 0 0"></div>
        <div style="font:700 32px/1.3 ${BRAND.head};color:${BRAND.gray};text-align:center;height:84px;overflow:hidden">${esc(b.label)}</div></div>`
    )
    .join("");
  return page(1920, 1080, `
    <div style="position:absolute;left:120px;top:90px;font:900 72px/1.05 ${BRAND.head};max-width:1680px">${esc(s.title || "")}</div>
    ${s.subtitle ? `<div style="position:absolute;left:120px;top:250px;font:600 34px ${BRAND.head};color:${BRAND.gray}">${esc(s.subtitle)}</div>` : ""}
    <div style="position:absolute;left:120px;right:120px;bottom:110px;height:${areaH}px;display:flex;justify-content:center;gap:90px;align-items:flex-end">${html}</div>
    ${s.source ? `<div class="source">Source: ${esc(s.source)}</div>` : ""}
    <div class="brandtag">${esc(s.brand || "")}</div>
  `);
}

// ---------- narration cards (1920x1080), used by tools/video/assemble.py ----------
// style: chapter | stat | quote | text | list | math. Optional "object" (illustration) on the right.

function cardPage(s) {
  const tone = toneColor(s.tone || "highlight");
  const hasObj = Boolean(s.object);
  const textW = hasObj ? 1080 : 1680;
  let body = "";
  switch (s.style) {
    case "chapter":
      body = `<div style="font:800 40px ${BRAND.mono};color:${BRAND.coral};letter-spacing:6px">${esc(s.kicker || "")}</div>
        <div style="font:900 120px/1.02 ${BRAND.head};margin-top:24px">${esc(s.title || "")}</div>
        <div class="incision" style="position:relative;margin-top:44px;width:420px"></div>`;
      break;
    case "stat":
      body = `<div style="font:900 ${s.size || 200}px/1 ${BRAND.head};color:${tone};text-shadow:0 10px 0 #000">${esc(s.value || "")}</div>
        <div style="font:800 60px/1.15 ${BRAND.head};margin-top:30px">${esc(s.label || "")}</div>
        ${s.sub ? `<div style="font:600 38px ${BRAND.head};color:${BRAND.gray};margin-top:18px">${esc(s.sub)}</div>` : ""}`;
      break;
    case "quote":
      body = `<div style="font:900 180px/0.6 ${BRAND.head};color:${BRAND.coral}">“</div>
        <div style="font:700 ${s.size || 64}px/1.25 ${BRAND.head};margin-top:10px">${esc(s.quote || "")}</div>
        <div style="font:700 38px ${BRAND.head};color:${BRAND.yellow};margin-top:40px">— ${esc(s.who || "")}</div>`;
      break;
    case "text":
      body = `<div style="font:900 ${s.size || 110}px/1.08 ${BRAND.head};color:${s.tone ? tone : BRAND.paper}">${esc(s.text || "")}</div>
        ${s.sub ? `<div style="font:600 44px/1.3 ${BRAND.head};color:${BRAND.gray};margin-top:34px">${esc(s.sub)}</div>` : ""}`;
      break;
    case "list":
      body = `${s.title ? `<div style="font:900 72px/1.1 ${BRAND.head};margin-bottom:40px">${esc(s.title)}</div>` : ""}
        ${(s.rows || [])
          .map(
            (r) => `<div style="display:flex;gap:40px;align-items:baseline;padding:16px 0;border-bottom:2px solid #2A2D36">
              <div style="font:800 44px ${BRAND.mono};color:${BRAND.yellow};min-width:${s.left_w || 220}px">${esc(r.left || "")}</div>
              <div style="font:700 48px/1.2 ${BRAND.head};color:${r.tone ? toneColor(r.tone) : BRAND.paper}">${esc(r.right || "")}</div></div>`
          )
          .join("")}`;
      break;
    case "math":
      body = `<div style="font:800 ${s.size || 130}px/1.1 ${BRAND.mono};color:${tone}">${esc(s.expr || "")}</div>
        ${s.sub ? `<div style="font:700 48px/1.3 ${BRAND.head};color:${BRAND.gray};margin-top:40px">${esc(s.sub)}</div>` : ""}`;
      break;
    default:
      throw new Error(`card style must be chapter|stat|quote|text|list|math (got ${s.style})`);
  }
  return page(1920, 1080, `
    <div style="position:absolute;left:120px;top:0;bottom:0;width:${textW}px;display:flex;flex-direction:column;justify-content:center">${body}</div>
    ${hasObj ? heroBlock(s, "right:110px;top:240px;width:600px;height:600px") : ""}
    ${s.source ? `<div class="source">Source: ${esc(s.source)}</div>` : ""}
    <div class="brandtag">PRICEWHY</div>
  `);
}

// ---------- vertical Shorts frame (1080x1920), used by tools/video/shorts.py ----------
// hook (top, fixed for the whole Short) + 16:9 visual (middle) + caption (bottom, one sentence).

function verticalPage(s) {
  const visual = s.img
    ? `<img src="${dataUri(path.resolve(s._dir, s.img))}" style="width:1080px;height:608px;object-fit:cover;display:block">`
    : `<div class="hero" style="width:1080px;height:608px;display:flex;align-items:center;justify-content:center"><div style="width:520px;height:520px">${illustration(s.object || "coin")}</div></div>`;
  return page(1080, 1920, `
    <div style="position:absolute;left:60px;right:60px;top:150px;height:400px;display:flex;align-items:center;justify-content:center;text-align:center;font:900 ${s.hook_size || 92}px/1.05 ${BRAND.head};color:${BRAND.yellow};text-shadow:0 8px 0 #000">${esc(s.hook || "")}</div>
    <div style="position:absolute;left:0;top:600px;width:1080px;height:608px;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,.6)">${visual}</div>
    <div style="position:absolute;left:70px;right:70px;top:1290px;height:420px;display:flex;align-items:flex-start;justify-content:center;text-align:center;font:800 ${s.caption_size || 66}px/1.18 ${BRAND.head};color:${BRAND.paper}">
      <span style="background:rgba(14,15,18,.85);padding:10px 22px;border-radius:18px;-webkit-box-decoration-break:clone;box-decoration-break:clone">${esc(s.caption || "")}</span></div>
    <div style="position:absolute;left:0;right:0;bottom:120px;text-align:center;font:800 34px ${BRAND.head};letter-spacing:6px;color:${BRAND.gray}">PRICE<span style="color:${BRAND.coral}">WHY</span></div>
  `);
}

// ---------- brand assets ----------

const receiptEdge =
  "polygon(0 0,100% 0,100% 94%,92% 100%,84% 94%,76% 100%,68% 94%,60% 100%,52% 94%,44% 100%,36% 94%,28% 100%,20% 94%,12% 100%,4% 94%,0 100%)";

function logoPage() {
  // 800x800; YouTube crops it to a circle, so everything sits in the middle 70%.
  return page(800, 800, `
    <div style="position:absolute;left:50%;top:50%;width:380px;height:470px;transform:translate(-50%,-50%) rotate(-6deg);background:${BRAND.paper};clip-path:${receiptEdge};display:flex;align-items:center;justify-content:center">
      <div style="font:900 400px/1 ${BRAND.head};color:${BRAND.coral};margin-top:-30px">?</div>
    </div>
    <div class="incision" style="left:110px;top:500px;width:580px;transform:rotate(-14deg);border-top-width:10px"></div>
  `);
}

function bannerPage(s) {
  // 2560x1440; the area visible on every device is the centred 1546x423 box.
  return page(2560, 1440, `
    <div style="position:absolute;left:507px;top:508px;width:1546px;height:423px;display:flex;align-items:center;gap:70px">
      <div style="width:250px;height:330px;flex:none;transform:rotate(-6deg);background:${BRAND.paper};clip-path:${receiptEdge};display:flex;align-items:center;justify-content:center">
        <div style="font:900 250px/1 ${BRAND.head};color:${BRAND.coral};margin-top:-20px">?</div>
      </div>
      <div>
        <div style="font:900 150px/1 ${BRAND.head};letter-spacing:2px">PRICE<span style="color:${BRAND.coral}">WHY</span></div>
        <div style="font:700 54px ${BRAND.head};color:${BRAND.yellow};margin-top:18px">${esc(s.tagline || "Why things cost what they cost.")}</div>
        <div style="font:500 34px ${BRAND.mono};color:${BRAND.gray};margin-top:22px">${esc(s.line || "")}</div>
      </div>
    </div>
  `);
}

// ---------- driver ----------

function jobsFor(spec) {
  const base = spec.out.replace(/\.png$/i, "");
  switch (spec.type) {
    case "thumbnail": {
      const t = { A: thumbA, B: thumbB, C: thumbC, D: thumbD }[spec.template];
      if (!t) throw new Error(`thumbnail template must be A, B, C or D (got ${spec.template})`);
      return [{ w: 1280, h: 720, html: t(spec), out: spec.out }];
    }
    case "receipt": {
      const n = (spec.lines || []).length;
      const steps = spec.steps === false ? [] : Array.from({ length: n }, (_, i) => ({ w: 1920, h: 1080, html: receiptPage(spec, i + 1), out: `${base}-step${String(i + 1).padStart(2, "0")}.png` }));
      return [...steps, { w: 1920, h: 1080, html: receiptPage(spec, n), out: spec.out }];
    }
    case "stacked": {
      const n = (spec.segments || []).length;
      const steps = spec.steps === false ? [] : Array.from({ length: n }, (_, i) => ({ w: 1920, h: 1080, html: stackedPage(spec, i + 1), out: `${base}-step${String(i + 1).padStart(2, "0")}.png` }));
      return [...steps, { w: 1920, h: 1080, html: stackedPage(spec, n), out: spec.out }];
    }
    case "compare":
      return [{ w: 1920, h: 1080, html: comparePage(spec), out: spec.out }];
    case "card":
      return [{ w: 1920, h: 1080, html: cardPage(spec), out: spec.out }];
    case "vertical":
      return [{ w: 1080, h: 1920, html: verticalPage(spec), out: spec.out }];
    case "logo":
      return [{ w: 800, h: 800, html: logoPage(spec), out: spec.out }];
    case "banner":
      return [{ w: 2560, h: 1440, html: bannerPage(spec), out: spec.out }];
    default:
      throw new Error(`Unknown spec type "${spec.type}"`);
  }
}

async function main() {
  const files = process.argv.slice(2);
  if (!files.length) {
    console.error("Usage: node tools/render/render.mjs <specs.json> [more.json]");
    process.exit(1);
  }
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: 1 });
  const pg = await ctx.newPage();
  let count = 0;
  for (const file of files) {
    const dir = path.dirname(path.resolve(file));
    const data = JSON.parse(await readFile(file, "utf8"));
    const specs = Array.isArray(data) ? data : data.items;
    for (const spec of specs) {
      spec._dir = dir;
      for (const job of jobsFor(spec)) {
        const out = path.resolve(dir, job.out);
        await mkdir(path.dirname(out), { recursive: true });
        await pg.setViewportSize({ width: job.w, height: job.h });
        await pg.setContent(job.html, { waitUntil: "load" });
        await pg.evaluate(() => document.fonts.ready);
        await pg.screenshot({ path: out, clip: { x: 0, y: 0, width: job.w, height: job.h } });
        count++;
        console.log("wrote", path.relative(process.cwd(), out));
      }
    }
  }
  await browser.close();
  console.log(`${count} image(s) rendered`);
}

main().catch((err) => {
  console.error(err.message || err);
  process.exit(1);
});
