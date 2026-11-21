// Original flat vector illustrations used as the "hero object" in thumbnails
// and charts. Drawn from scratch for this channel (no third-party art).
// Each entry returns an SVG string; size is controlled by the caller via CSS.

const stripes = (x0, x1, y0, y1, w, a, b) => {
  let out = "";
  for (let x = x0, i = 0; x < x1; x += w, i++) {
    out += `<rect x="${x}" y="${y0}" width="${w}" height="${y1 - y0}" fill="${i % 2 ? b : a}"/>`;
  }
  return out;
};

const kernels = (list) =>
  list
    .map(
      ([cx, cy, r, c]) =>
        `<circle cx="${cx}" cy="${cy}" r="${r}" fill="${c}" stroke="#C99A2E" stroke-width="3"/>`
    )
    .join("");

export const illustrations = {
  popcorn: () => `
<svg viewBox="0 0 400 480" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <clipPath id="bucket"><path d="M62 168 L338 168 L296 468 L104 468 Z"/></clipPath>
  </defs>
  ${kernels([
    [110, 150, 38, "#FFF6D6"], [160, 120, 44, "#FFEFB8"], [215, 95, 46, "#FFF6D6"],
    [270, 118, 44, "#FFE7A0"], [318, 150, 38, "#FFF6D6"], [140, 70, 34, "#FFE7A0"],
    [200, 45, 36, "#FFF6D6"], [258, 62, 34, "#FFEFB8"], [182, 150, 40, "#FFF6D6"],
    [240, 150, 40, "#FFEFB8"], [300, 92, 30, "#FFF6D6"], [100, 108, 28, "#FFEFB8"],
  ])}
  <g clip-path="url(#bucket)">${stripes(40, 360, 160, 480, 46, "#E63946", "#F8F4EC")}</g>
  <path d="M62 168 L338 168 L296 468 L104 468 Z" fill="none" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <rect x="48" y="152" width="304" height="30" rx="10" fill="#F8F4EC" stroke="#1B1B1F" stroke-width="6"/>
</svg>`,

  plane: () => `
<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg">
  <path d="M70 150 Q60 120 110 116 L520 116 Q600 120 610 150 Q600 180 520 184 L110 184 Q60 180 70 150 Z" fill="#F4F6FA" stroke="#1B1B1F" stroke-width="6"/>
  <path d="M110 118 L60 30 L130 30 L190 118 Z" fill="#2E6BFF" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M270 170 L380 280 L440 280 L370 170 Z" fill="#DDE3EE" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M290 130 L350 60 L395 60 L360 130 Z" fill="#DDE3EE" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <rect x="330" y="196" width="80" height="34" rx="16" fill="#C9D1DE" stroke="#1B1B1F" stroke-width="6"/>
  ${[200, 240, 280, 320, 360, 400, 440, 480]
    .map((x) => `<rect x="${x}" y="134" width="22" height="18" rx="6" fill="#2E6BFF"/>`)
    .join("")}
  <path d="M560 128 Q590 134 598 150 L560 150 Z" fill="#1B1B1F"/>
  <rect x="70" y="160" width="540" height="10" fill="#2E6BFF" opacity="0.9"/>
</svg>`,

  card: () => `
<svg viewBox="0 0 520 330" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#E9C46A"/><stop offset="1" stop-color="#B9852F"/>
    </linearGradient>
  </defs>
  <rect x="10" y="10" width="500" height="310" rx="28" fill="url(#g)" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="58" y="96" width="78" height="60" rx="10" fill="#F2DFA6" stroke="#1B1B1F" stroke-width="4"/>
  <path d="M58 126 H136 M97 96 V156" stroke="#1B1B1F" stroke-width="3"/>
  ${[0, 1, 2, 3]
    .map((g) =>
      [0, 1, 2, 3]
        .map((d) => `<circle cx="${70 + g * 104 + d * 20}" cy="214" r="7" fill="#1B1B1F"/>`)
        .join("")
    )
    .join("")}
  <rect x="58" y="252" width="160" height="16" rx="8" fill="#1B1B1F" opacity="0.7"/>
  <!-- generic contactless waves, deliberately NOT any card network's logo -->
  <path d="M430 250 Q442 272 430 294 M448 242 Q464 272 448 302 M466 234 Q486 272 466 310" fill="none" stroke="#1B1B1F" stroke-width="7" stroke-linecap="round"/>
</svg>`,

  hotdog: () => `
<svg viewBox="0 0 560 300" xmlns="http://www.w3.org/2000/svg">
  <path d="M40 170 Q40 250 120 256 L440 256 Q520 250 520 170 Z" fill="#E9A35A" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="30" y="118" width="500" height="64" rx="32" fill="#B5432F" stroke="#1B1B1F" stroke-width="6"/>
  <path d="M70 150 Q100 125 130 150 T190 150 T250 150 T310 150 T370 150 T430 150 T490 150" fill="none" stroke="#FFD23F" stroke-width="12" stroke-linecap="round"/>
  <path d="M40 170 Q40 120 120 140 L440 140 Q520 120 520 170" fill="none" stroke="#1B1B1F" stroke-width="0"/>
  <path d="M52 176 Q70 128 140 150" fill="none" stroke="#F3B979" stroke-width="22" stroke-linecap="round"/>
  <path d="M508 176 Q490 128 420 150" fill="none" stroke="#F3B979" stroke-width="22" stroke-linecap="round"/>
</svg>`,

  soda: () => `
<svg viewBox="0 0 220 360" xmlns="http://www.w3.org/2000/svg">
  <rect x="122" y="6" width="16" height="110" rx="6" fill="#F8F4EC" stroke="#1B1B1F" stroke-width="5" transform="rotate(12 130 60)"/>
  <rect x="24" y="78" width="172" height="34" rx="12" fill="#F8F4EC" stroke="#1B1B1F" stroke-width="6"/>
  <path d="M36 112 L184 112 L164 350 L56 350 Z" fill="#E63946" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M46 200 L174 200 L170 250 L50 250 Z" fill="#F8F4EC"/>
</svg>`,

  goldbar: () => `
<svg viewBox="0 0 520 360" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="gb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F6D365"/><stop offset="1" stop-color="#C8902A"/></linearGradient></defs>
  <path d="M110 120 L410 120 L490 300 L30 300 Z" fill="url(#gb)" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
  <path d="M110 120 L150 60 L370 60 L410 120 Z" fill="#FBE29A" stroke="#1B1B1F" stroke-width="7" stroke-linejoin="round"/>
  <path d="M150 200 L370 200" stroke="#9C6B12" stroke-width="10" stroke-linecap="round" opacity="0.6"/>
  <path d="M175 240 L345 240" stroke="#9C6B12" stroke-width="10" stroke-linecap="round" opacity="0.4"/>
</svg>`,

  gift: () => `
<svg viewBox="0 0 420 440" xmlns="http://www.w3.org/2000/svg">
  <rect x="52" y="196" width="316" height="226" rx="10" fill="#E63946" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="300" y="199" width="65" height="220" fill="#C62F3C"/>
  <rect x="183" y="196" width="54" height="226" fill="#FFD23F" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="30" y="146" width="360" height="68" rx="12" fill="#F2545F" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="183" y="146" width="54" height="68" fill="#FFD23F" stroke="#1B1B1F" stroke-width="6"/>
  <path d="M210 146 C160 62 74 82 104 132 C120 158 178 154 210 146 Z" fill="#FFD23F" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M210 146 C260 62 346 82 316 132 C300 158 242 154 210 146 Z" fill="#FFD23F" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M132 118 Q160 112 186 136 M288 118 Q260 112 234 136" fill="none" stroke="#C99A2E" stroke-width="5" stroke-linecap="round"/>
  <ellipse cx="210" cy="144" rx="26" ry="22" fill="#F2B705" stroke="#1B1B1F" stroke-width="6"/>
</svg>`,

  house: () => `
<svg viewBox="0 0 440 420" xmlns="http://www.w3.org/2000/svg">
  <rect x="18" y="392" width="404" height="18" rx="9" fill="#2BD38A" stroke="#1B1B1F" stroke-width="5"/>
  <rect x="292" y="58" width="48" height="110" fill="#B5432F" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="284" y="46" width="64" height="20" rx="4" fill="#8E3324" stroke="#1B1B1F" stroke-width="5"/>
  <rect x="72" y="186" width="296" height="208" fill="#F4F1EA" stroke="#1B1B1F" stroke-width="6"/>
  <rect x="72" y="186" width="296" height="26" fill="#DDD6C8"/>
  <path d="M28 206 L220 52 L412 206 Z" fill="#E63946" stroke="#1B1B1F" stroke-width="6" stroke-linejoin="round"/>
  <path d="M84 196 L220 86 L356 196" fill="none" stroke="#C62F3C" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="186" y="268" width="68" height="126" rx="6" fill="#2E6BFF" stroke="#1B1B1F" stroke-width="6"/>
  <circle cx="240" cy="334" r="6" fill="#FFD23F" stroke="#1B1B1F" stroke-width="3"/>
  ${[100, 280]
    .map((x) => `<rect x="${x}" y="236" width="62" height="58" rx="6" fill="#FFD23F" stroke="#1B1B1F" stroke-width="6"/><path d="M${x + 31} 236 V294 M${x} 265 H${x + 62}" stroke="#1B1B1F" stroke-width="4"/>`)
    .join("")}
  <circle cx="220" cy="150" r="22" fill="#FFD23F" stroke="#1B1B1F" stroke-width="5"/>
</svg>`,

  coin: () => `
<svg viewBox="0 0 300 300" xmlns="http://www.w3.org/2000/svg">
  <circle cx="150" cy="150" r="130" fill="#FFD23F" stroke="#1B1B1F" stroke-width="8"/>
  <circle cx="150" cy="150" r="100" fill="none" stroke="#C99A2E" stroke-width="6"/>
  <text x="150" y="196" font-family="Inter" font-weight="900" font-size="130" text-anchor="middle" fill="#1B1B1F">$</text>
</svg>`,
};

export function illustration(name) {
  const fn = illustrations[name];
  if (!fn) throw new Error(`Unknown illustration "${name}". Known: ${Object.keys(illustrations).join(", ")}`);
  return fn();
}
