# 07 — Fluxul de producție bazat pe AI

> Împărțirea muncii (stabilită de tine): **Claude creează tot conținutul. Tu publici.**
> Ca să fie realist, câțiva pași necesită mâna ta (generarea vocii, asamblarea video-ului, încărcarea). Mai jos e exact ce face fiecare și cât durează.

---

## 1. Harta fluxului (un video lung)

```
 CLAUDE (în sesiuni)                                         TU
 ──────────────────────────────────────────────              ─────────────────────────────
 1. Alegerea subiectului (din 04, scor ≥22)
 2. Cercetare cu surse → research.md
 3. Scenariu → script.md (+ versiune pentru voce)
 4. Ambalaj → package.md (titluri, miniaturi,
    descriere, capitole, comentariu fixat)
 5. Pachet vizual → grafice PNG, miniaturi PNG,
    listă de scene (ce apare pe ecran, secundă
    cu secundă), căutări pentru stock
 6. Shorts → shorts.md (3–5 scenarii verticale)
                                                             7. Vocea: lipești textul în
                                                                ElevenLabs → MP3 (~10 min)
                                                             8. Asamblare în CapCut după lista
                                                                de scene (~60–90 min la început,
                                                                ~40 min după 10 video-uri)
                                                             9. Verificare cu checklist-ul (~10 min)
                                                            10. Încărcare + programare (~15 min)
                                                            11. Shorts: tai clipurile din video-ul
                                                                lung (~30 min) → YT, TikTok, Reels
                                                            12. Export CSV din Studio (5 min/săpt)
 13. Analiză săptămânală + lunară (09)
 14. Ajustăm ideile și șabloanele
```

**Timpul tău estimat:** ~2,5–3 ore per video lung + Shorts la început; ~1,5–2 ore după primele 10 video-uri.
**Următorul pas de automatizare** (o sesiune viitoare): un script care asamblează automat o primă variantă de montaj din lista de scene (vezi „NEXT” în README) — ar reduce pasul 8 la verificare și retușuri.

---

## 2. Instrumentele propuse

Prețurile sunt orientative (noiembrie 2026) — verifică pe site înainte de plată. Planurile gratuite ale uneltelor de voce **nu** dau, de regulă, drept de folosire comercială: pentru un canal monetizat ai nevoie de plan plătit.

| Etapă | Recomandat | Alternativă gratuită / ieftină | De ce |
|---|---|---|---|
| Cercetare, scenarii, ambalaj, analiză | Claude (acest proiect) | — | Totul e deja configurat aici, cu skill-uri |
| Voce AI | **ElevenLabs** (plan care include licență comercială) | voce din CapCut (calitate mai slabă) | Cea mai naturală voce în engleză; aceeași voce = identitate de canal |
| Montaj | **CapCut Desktop** | DaVinci Resolve (gratuit, mai greu) | Ușor, subtitrări automate, format vertical pentru Shorts |
| Stock video | **Pexels / Pixabay** (gratuit) | Storyblocks (abonament) când creștem | Licență clară; NU folosim clipuri de la TV/știri |
| Muzică | **YouTube Audio Library** (gratuit) | Epidemic Sound (abonament) | Fără probleme de drepturi de autor |
| Grafice și diagrame | `tools/charts/` (Python, generat de Claude) | Datawrapper / Flourish | Grafice originale = conținut original (important pentru politica YouTube) |
| Miniaturi | `tools/thumbnail/` (randare automată) + Canva pentru retușuri | Canva gratuit | Stil consecvent, rapid |
| Imagini de produs | Pexels/Unsplash; obiecte generate AI (fără oameni realiști) | remove.bg pentru decupare | Obiectul e eroul miniaturii |
| Cuvinte-cheie | vidIQ sau TubeBuddy (plan gratuit) + sugestiile din bara de căutare YouTube | Google Trends | Validăm cererea înainte de producție |
| Programare Shorts pe alte platforme | Programatorul nativ TikTok / Meta Business Suite | Metricool (plan gratuit) | Gratuit |
| Analiză | YouTube Studio + `tools/analytics/` | — | Revizuiri săptămânale automate |

**Buget minim:** ~25–35 €/lună (doar vocea plătită). **Buget recomandat după primele 3 luni:** ~60–90 €/lună (voce + stock premium + muzică).

---

## 3. Sistemul pentru fiecare etapă

### Etapa 1 — Cercetarea temelor
- Sursa ideilor: `docs/04-video-ideas-100.md` (ordonate după potențial).
- Validare rapidă: căutăm subiectul pe YouTube → există video-uri cu multe vizualizări pe canale mici? (= cerere reală). Notăm 3 video-uri concurente și ce le lipsește.
- Skill: `.claude/skills/research-brief/`.
- Rezultat: `content/<nr>-<subiect>/research.md` — fiecare cifră are sursă, perioadă și nivel de încredere.

### Etapa 2 — Scenariul
- Structura din 05 (Autopsie / Detectiv / Urmărește dolarul / Cronologie).
- 1.400–1.900 de cuvinte = 9–12 minute de narațiune.
- Două versiuni: `script.md` (cu indicații vizuale) și secțiunea „VOICE-READY” (doar textul de citit, cu pauze marcate).
- Skill: `.claude/skills/script-writer/`.

### Etapa 3 — Vocea (comentariul audio)
- O singură voce fixă pentru canal (aceeași de fiecare dată — devine „vocea mărcii”).
- Setări de pornire în ElevenLabs: stabilitate medie, claritate ridicată; se ajustează o dată și se notează în `docs/02-channel-identity.md`.
- Numerele scrise în cuvinte în versiunea VOICE-READY („nine forty-nine”) ca să fie citite corect.
- Verificare: ascultă primele 60 s — dacă un cuvânt e pronunțat greșit, regenerează doar acel paragraf.

### Etapa 4 — Înregistrarea ecranului / materiale
Canalul nu are filmări proprii. Materialele vizuale sunt:
1. **Grafice și animații originale** (minimum 40% din timpul ecranului) — generate de Claude.
2. **Chitanța de pe ecran** (semnătura canalului) — un PNG per capitol.
3. **Stock video** cu licență, pentru atmosferă.
4. **Capturi de documente publice** (ex. o pagină din raportul anual), cu sursa scrisă pe ecran.

### Etapa 5 — Montajul
Lista de scene din `script.md` are, pentru fiecare bloc: textul narat, ce apare pe ecran, fișierul sau căutarea de stock, durata aproximativă.
Reguli de montaj:
- Imagine nouă la fiecare 3–6 secunde.
- Subtitrări arse pe ecran doar la Shorts; la video-ul lung încărcăm fișierul .srt.
- Muzică la −25 / −30 dB sub voce; se oprește la momentele „pause and guess”.
- Efect sonor scurt la apariția fiecărui preț.

### Etapa 6 — Designul miniaturilor
- 3 variante per video (șabloane diferite din 05 §4) → Test & Compare.
- Claude scrie specificația + randează PNG-uri 1280×720 cu `tools/thumbnail/`.
- Tu doar le încarci.

### Etapa 7 — Publicarea
Copiezi din `package.md`: titlu, descriere, capitole, etichete, comentariu fixat. Bifezi lista din §5 de mai jos. Programezi la ora stabilită (06 §4).

### Etapa 8 — Analiza datelor
Săptămânal: exporți din YouTube Studio (Analytics → Advanced mode → Export → CSV) și pui fișierul în `tracking/exports/`. Claude rulează analiza și scrie raportul (09).

### Etapa 9 — Reutilizarea pentru Shorts, TikTok, Instagram Reels
Din fiecare video lung: **3–5 clipuri verticale** de 30–55 s.
- Fiecare clip = un singur „organ” al autopsiei (un fapt surprinzător + răsturnare).
- Structura: hook în prima secundă (text mare pe ecran) → fapt → răsturnare → „full breakdown on the channel”.
- Aceleași clipuri merg pe TikTok și Reels, **fără watermark** de la altă platformă (descarcă din CapCut, nu din TikTok).
- Pe YouTube Shorts: legăm fiecare Short de video-ul lung cu „Related video”.
- Skill: `.claude/skills/shorts-repurpose/`.

Alte reutilizări (mai târziu): un fir pe X/Threads cu graficul principal; un articol scurt în newsletter (08); graficul ca postare în Community.

---

## 4. Șabloanele (în `templates/`)

| Fișier | La ce folosește |
|---|---|
| `templates/research-template.md` | Structura cercetării cu tabel de surse |
| `templates/script-template.md` | Structura scenariului + lista de scene |
| `templates/package-template.md` | Titluri, miniaturi, descriere, capitole, etichete |
| `templates/shorts-template.md` | 3–5 scenarii verticale |
| `templates/weekly-review.md` | Revizuirea săptămânală |
| `templates/monthly-review.md` | Revizuirea lunară |
| `tracking/video-log.csv` | Registrul tuturor video-urilor + rezultatele |
| `tracking/content-calendar.csv` | Calendarul de publicare |

---

## 5. Liste de verificare a calității

### 5.1 Fapte și surse (Claude, înainte să predea scenariul)
- [ ] Fiecare cifră din scenariu apare în tabelul din `research.md` cu sursă
- [ ] Anul / perioada fiecărei cifre e spusă clar în narațiune („in fiscal 2025”)
- [ ] Estimările sunt numite estimări („roughly”, „analysts estimate”)
- [ ] Nicio afirmație din secțiunea „Do NOT claim”
- [ ] Nicio acuzație de ilegalitate la adresa unei firme/persoane fără o sursă oficială (instanță, autoritate)
- [ ] Nu dăm sfaturi de investiții („this is not financial advice” în descriere)

### 5.2 Audio (tu, la asamblare)
- [ ] Vocea e clară, fără cuvinte stâlcite în primele 60 s
- [ ] Muzica nu acoperă vocea
- [ ] Niciun sunet sau muzică fără licență

### 5.3 Imagine (tu, la asamblare)
- [ ] Prima secundă = obiectul + prețul din miniatură
- [ ] Nicio imagine statică mai mult de 6 s
- [ ] Graficele au sursa scrisă jos
- [ ] Niciun clip de la TV, film sau alt YouTuber
- [ ] Nicio față de om generată AI care pare reală

### 5.4 Publicare (tu, în YouTube Studio)
- [ ] Titlu, descriere, capitole, etichete copiate din `package.md`
- [ ] 3 miniaturi în Test & Compare
- [ ] Subtitrări .srt încărcate
- [ ] End screen + card spre video-ul recomandat
- [ ] Setarea **„AI use”** (Details → Attributes) completată conform regulii din 11 §3
- [ ] Playlist-ul seriei setat
- [ ] Comentariul fixat publicat
- [ ] Programat la ora stabilită

### 5.5 Politica YouTube (Claude, lunar)
- [ ] Ultimele 8 video-uri nu arată ca același șablon (structuri, miniaturi, intro-uri variate)
- [ ] Fiecare video are analiză originală (grafice proprii, calcul propriu), nu doar repovestire
