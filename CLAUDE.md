# CLAUDE.md — Pricewhy (memoria proiectului)

> Acest fișier se încarcă automat în fiecare sesiune Claude Code din acest repository. Conține tot ce trebuie știut ca utilizatorul să **nu explice nimic de două ori**.

## Ce este proiectul

- Un canal YouTube **nou, în limba engleză**, construit de la zero până la monetizare. Nume: **Pricewhy**, handle **@PricewhyTV** — canal creat de utilizator pe 20.11.2026 (canal de marcă pe contul lui Google; @Pricewhy era indisponibil).
- **Proiect separat.** Nu are legătură cu „millionaireagent” sau cu alte proiecte ale utilizatorului. Nu amesteca contexte.
- Briefingul original, cuvânt cu cuvânt: `docs/00-brief-original.md`.
- **Utilizatorul mai are un canal, separat:** „Christina” — @deutschfuerrumaenen (germană pentru români, DE→RO; 7 abonați, 8 Shorts la 20.11.2026). **Nu** îl folosim pentru Pricewhy și nu amestecăm conținutul. Recomandarea dată (20.11.2026): Pricewhy = **canal nou** (canal de marcă pe același cont Google; același cont AdSense poate primi ambele canale).

## Cine face ce (decis de utilizator, 20.11.2026)

- **Claude creează tot conținutul**: cercetare, scenarii, titluri, miniaturi, grafice, descrieri, Shorts, analize.
- **Utilizatorul publică**: generează vocea, asamblează în CapCut, încarcă și programează, exportă datele din Studio.
- Utilizatorul scrie în **română**. Documentele pentru el: în română, limbaj simplu, fără jargon (termenii YouTube se explică pe scurt). Conținutul canalului: în **engleză**.

## Deciziile luate (nu le relua fără motiv nou)

| Decizie | Valoare | Unde e justificată |
|---|---|---|
| Domeniu | Economia prețurilor de zi cu zi: „de ce costă X cât costă”, „cum câștigă firma X” | docs/01 |
| Diferențiere | Chitanța pe ecran + surse vizibile + **4 țări** (SUA, UK, Canada, Australia) + nume inventat | docs/01 §5, docs/02 |
| Format | Fără față, **voce AI** (ales de utilizator). Plan B: voce umană dacă retenția e slabă după 12 video-uri | docs/01 §8–9 |
| Piață | Engleză; public 25–44 ani | docs/02 §3 |
| Ritm | 2 video-uri lungi/săpt. (marți, vineri, 15:00 New York) + 5–7 Shorts | docs/06 §4, docs/10 |
| Ținta | 1.000 abonați + **8.000 ore** în 365 zile (pragul YPP pentru aplicanți noi de la 1 feb 2027) | docs/08 §1 |
| Lansare | Primul video marți 1 decembrie 2026 | docs/10 |

## Harta fișierelor

- `docs/01`–`11` — planul complet (piață, identitate, conținut, 100 de idei, CTR/retenție, algoritm, producție AI, monetizare, analiză, foaie de parcurs, reguli).
- `content/<NNN>-<slug>/` — un video: `research.md` → `script.md` → `package.md` → `shorts.md` → `visuals/` (specs.json + out/*.png).
- `.claude/skills/` — cele 5 skill-uri (mai jos), fiecare cu `CHANGELOG.md`.
- `templates/` — șabloanele pe care le folosesc skill-urile.
- `tracking/` — `video-log.csv`, `content-calendar.csv`, `exports/` (CSV-uri din Studio), `reviews/`.
- `tools/render/` — miniaturi, grafice, logo, banner (Node + Playwright). `tools/analytics/` — revizuirea A/B/C (Python, fără dependențe).
- `brand/` — logo și banner.

## Fluxul pentru fiecare video (ordinea skill-urilor)

1. `research-brief` → `research.md` (fiecare cifră cu sursă, perioadă, nivel de încredere)
2. `script-writer` → `script.md` (narațiune VOICE-READY pe ¶ + listă de scene + verificarea cifrelor)
3. `packaging` → `package.md` + `visuals/` randate și **verificate vizual**
4. `shorts-repurpose` → `shorts.md`
Săptămânal/lunar: `analytics-review` (după ce utilizatorul pune exportul în `tracking/exports/`).

**Comanda săptămânală — „start week N” / „next videos”** (ca utilizatorul să nu explice de fiecare dată):
1. Dacă există un export nou în `tracking/exports/` → rulează întâi `analytics-review`.
2. Ia din `tracking/content-calendar.csv` următoarele 2 rânduri cu status `planned`.
3. Pentru fiecare: `research-brief` → `script-writer` → `packaging` → `shorts-repurpose` (în ordine; se pot rula în paralel cele două video-uri).
4. Actualizează statusul în calendar (`ready`) și rândul din `tracking/video-log.csv` (structură, hook, formulă de titlu, șablon de miniatură).
5. Raportează utilizatorului, în română, în maximum 10 rânduri: ce e gata, ce trebuie să facă el, orice cifră incertă.

**Livrarea către utilizator (preferința lui, 20.11.2026):** nu vrea să ia fișiere din GitHub. După ce un video e gata, rulează `python3 tools/export/bundle.py <scratchpad>/send` și trimite-i direct în chat (SendUserFile) ZIP-ul video-ului (voice.txt, description.txt, scenariu, titluri, Shorts, images/) — iar logo-ul/miniaturile ca imagini când le cere.

Comenzi:
- `node tools/render/render.mjs content/<NNN>/visuals/specs.json`
- `python3 tools/export/bundle.py <dosar-de-ieșire>` — ZIP-uri pentru telefon
- `python3 tools/analytics/review.py "tracking/exports/<data>/Table data.csv" [--log tracking/video-log.csv]`
- Teste: `python3 tools/analytics/test_review.py`

## Reguli care nu se negociază

1. **Nicio cifră fără sursă** în `research.md`. Respectă lista „Do NOT claim”. Nu rotunji ca să schimbi povestea (51% = „about half”, nu „most”).
2. **Nicio persoană inventată** („I'm Mike, an analyst”) și **niciun sfat financiar**. Vocea = marca, la plural („we”).
3. **„AI use: Yes”** la fiecare încărcare (vocea sintetică) — docs/11 §3.
4. Variație obligatorie: alte structuri, alte șabloane de miniatură, altă muzică de la un video la altul (politica „inauthentic content”).
5. Fără fețe umane realiste generate AI, fără sigle ale altor firme/rețele de carduri ca element principal, fără clipuri TV sau de la alți creatori.
6. **Claude nu publică, nu trimite, nu șterge și nu plătește nimic.** Pregătește; utilizatorul apasă butonul. Niciun skill nu face asta fără aprobare explicită.
7. **Nicio parolă sau cheie API** în repository.
8. Dacă nu știi ceva despre munca utilizatorului: **întreabă, nu inventa.**

## Bucla de învățare (obligatorie)

Când utilizatorul corectează ceva:
1. Întreabă-te: **ce skill trebuia să prevină asta?**
2. Propune modificarea exactă a acelui `SKILL.md` ca **diff**.
3. Aplic-o **doar după OK-ul utilizatorului**.
4. Notează schimbarea în `CHANGELOG.md` din folderul skill-ului (data, ce, de ce).
Aceeași regulă pentru pragurile din `tools/analytics/review.py` și pentru documentele din `docs/`.

## Starea la 20.11.2026

- Gata: planul complet (docs 01–12), 5 skill-uri testate pe cazuri reale, șabloane, unelte, logo, banner, video-urile 001–003 complete (cercetare + scenariu + ambalaj + Shorts + grafice) și trimise utilizatorului ca ZIP. Canalul @PricewhyTV e creat.
- Utilizatorul trebuie să facă: lista din docs/10 §2 (canal, handle, ElevenLabs, CapCut) înainte de 1 decembrie.
- Următorul pas Claude: pachetele 004–008 din `tracking/content-calendar.csv`, câte două pe săptămână, cu o săptămână înainte de publicare.
