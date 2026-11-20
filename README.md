# Pricewhy — canal YouTube de la zero la monetizare

**Pricewhy** explică de ce lucrurile costă cât costă — dolar cu dolar, cu sursele pe ecran, în SUA, Marea Britanie, Canada și Australia.
Canal în engleză, fără față, cu voce AI. **Claude creează tot conținutul; tu publici.**

> Memoria proiectului (se încarcă automat la fiecare sesiune): [`CLAUDE.md`](CLAUDE.md)

---

## Ce faci tu acum (înainte de 1 decembrie 2026)

1. Creează canalul și rezervă handle-ul **@Pricewhy** cât mai repede (rezervă: @TilltaleTV).
2. Încarcă logo-ul și bannerul din [`brand/out/`](brand/out/) și textul „About” din [docs/02 §5.4](docs/02-channel-identity.md).
3. Urmează lista completă din [docs/10 §2](docs/10-roadmap-weekly-plan.md) (ElevenLabs, CapCut, playlist-uri, setări de încărcare) — ~3 ore.
4. Când ești gata, scrie-i lui Claude: **„start week 1”**.

Primele 3 video-uri sunt pregătite în [`content/`](content/): cercetare cu surse, scenariu gata de citit de vocea AI, titluri, miniaturi randate, descriere, Shorts.

---

## Planul complet

| # | Document | Ce conține |
|---|---|---|
| 00 | [Brief original](docs/00-brief-original.md) | Cererea ta, salvată exact |
| 01 | [Cercetarea de piață](docs/01-market-research.md) | De ce această nișă, cererea, concurenții, „cimitirul clonelor”, riscuri |
| 02 | [Identitatea canalului](docs/02-channel-identity.md) | Nume, poziționare, public, vocea, culori, logo, „About” |
| 03 | [Strategia de conținut](docs/03-content-strategy.md) | Cele 5 axe, tipuri de video, publicare, interacțiunea cu publicul |
| 04 | [100 de idei](docs/04-video-ideas-100.md) | Ordonate după potențialul de creștere, cu motivul pentru fiecare |
| 05 | [Sistemul CTR + retenție](docs/05-ctr-retention-system.md) | Titluri, miniaturi, hook-uri, structuri, tehnici de atenție, CTA |
| 06 | [Algoritmul și creșterea](docs/06-algorithm-growth.md) | Indicatorii explicați, surse de trafic, frecvență, teste, abonați |
| 07 | [Producția cu AI](docs/07-ai-production-workflow.md) | Cine face ce, unelte, etape, șabloane, liste de verificare |
| 08 | [Monetizarea](docs/08-monetization.md) | Pragurile oficiale, scara veniturilor pe etape |
| 09 | [Analiza datelor](docs/09-analytics-system.md) | Indicatori, diagnostic, revizuiri săptămânale și lunare |
| 10 | [Foaia de parcurs](docs/10-roadmap-weekly-plan.md) | Faze, calendarul primelor 12 săptămâni, programul săptămânal |
| 11 | [Reguli YouTube și AI](docs/11-policy-compliance.md) | Ce cere YouTube (verificat), cele 12 reguli ale canalului |
| 12 | [Testul skill-urilor](docs/12-skills-test-report.md) | Fiecare skill rulat pe un caz real, cu rezultatul |

## Skill-urile (Claude le folosește automat)

| Skill | Ce face | Când |
|---|---|---|
| [research-brief](.claude/skills/research-brief/SKILL.md) | Fișa de fapte cu surse | Primul pas la fiecare video |
| [script-writer](.claude/skills/script-writer/SKILL.md) | Scenariul de 9–12 min, gata pentru voce | După cercetare |
| [packaging](.claude/skills/packaging/SKILL.md) | Titluri, miniaturi, descriere, grafice | După scenariu |
| [shorts-repurpose](.claude/skills/shorts-repurpose/SKILL.md) | 3–5 clipuri verticale | După scenariu |
| [analytics-review](.claude/skills/analytics-review/SKILL.md) | Revizuirea săptămânală/lunară | Lunea, după export |

Fiecare are un `CHANGELOG.md`. Când corectezi ceva, Claude propune modificarea skill-ului care trebuia s-o prevină și o aplică doar după OK-ul tău.

## Uneltele

- `node tools/render/render.mjs <specs.json>` — miniaturi (1280×720), grafice (1920×1080), logo, banner, în stilul canalului.
- `python3 tools/analytics/review.py "<Table data.csv>"` — clasează video-urile A/B/C și spune ce să schimbi. Teste: `python3 tools/analytics/test_review.py`.

## Ritmul săptămânal (pe scurt)

Luni: exporți datele (5 min) și scrii „start week N” → Claude pregătește 2 video-uri complete. Miercuri–joi: vocea + montajul (~3–4 h). Sâmbătă: încarci și programezi (~45 min). Total: ~5–6 ore/săptămână la început. Detalii: [docs/10 §4](docs/10-roadmap-weekly-plan.md).
