# 09 — Sistemul de analiză a datelor și optimizare

> Scop: să știm în fiecare săptămână **ce funcționează, ce nu și ce schimbăm** — pe baza cifrelor, nu a impresiei.
> Tu exporți datele (5 minute pe săptămână). Claude face analiza și scrie raportul.

---

## 1. Indicatorii care contează (în ordinea importanței)

| # | Indicator | Unde îl găsești în YouTube Studio | Ce ne spune | Prag „verde” (canal nou, nișa noastră) |
|---|---|---|---|---|
| 1 | **Ore de vizionare** (watch time) | Analytics → Overview | Progresul spre monetizare | creștere lună de lună |
| 2 | **Impresii** | Analytics → Reach | Cât ne arată YouTube | creștere lună de lună |
| 3 | **CTR al impresiilor** | Reach | Puterea titlu + miniatură | ≥ 5% (≥ 8% excelent) |
| 4 | **Durata medie de vizionare** | Engagement | Cât stă omul | ≥ 4:00 la 10 min |
| 5 | **Procent mediu vizionat** | Content → video | Calitatea per video | ≥ 40% |
| 6 | **Retenția la 30 s** | Graficul de retenție | Hook-ul | ≥ 70% |
| 7 | **Abonați câștigați per 1.000 vizualizări** | Content | Dorința de „încă unul” | ≥ 5 |
| 8 | **Spectatori care revin** | Audience | Avem un public fidel? | creștere constantă |
| 9 | **Sursele de trafic** | Reach | Căutare / sugerate / browse / Shorts | vezi 06 §3 |
| 10 | **Like-uri și comentarii per 1.000 vizualizări** | Engagement | Implicarea | ≥ 30 like-uri / 1.000 |
| 11 | **Venituri: RPM** (după monetizare) | Earn / Revenue | Bani per 1.000 vizualizări pentru noi | crește cu publicul US/UK |
| 12 | **Click-uri pe linkuri** (după monetizare) | linkuri cu UTM | Afiliere, newsletter | — |

Pragurile sunt **orientative**. După 10 video-uri, comparăm fiecare video **cu media canalului nostru**, nu cu cifre generale de pe internet.

---

## 2. Cum citim graficul de retenție

| Forma graficului | Ce înseamnă | Ce facem |
|---|---|---|
| Cădere bruscă în primele 30 s | Hook-ul nu confirmă promisiunea sau e lent | Prima secundă = obiectul + prețul; tăiem contextul de la început |
| Coborâre lentă și constantă | Normal — video sănătos | Nimic; doar menținem ritmul |
| „Prăpastie” la un anumit minut | Un segment plictisitor sau confuz | Notăm minutul + ce se spune acolo; evităm acel tip de segment |
| „Cocoașă” (urcare) | Oamenii derulează înapoi = moment foarte interesant | Facem din el un Short + repetăm tipul de moment |
| Cădere mare în ultimele 30–60 s | Outro-ul e simțit ca final | Trecem direct la video-ul recomandat, fără „mulțumim că ați vizionat” |

---

## 3. Arborele de diagnostic pentru video-urile slabe

```
Video-ul are puține vizualizări după 7 zile?
│
├─ Impresii puține?
│   ├─ DA, iar CTR e bun → subiectul are cerere mică sau YouTube încă testează
│   │      → Short care trimite spre el; optimizăm pentru căutare (titlu + descriere)
│   └─ DA, iar CTR e slab → problemă de ambalaj
│          → schimbăm titlul; verificăm rezultatul din Test & Compare
│
└─ Impresii multe, dar CTR slab (< 60% din media canalului)?
    │   → titlul/miniatura nu atrag publicul căruia i se arată
    │   → titlu nou (altă formulă din 05 §3), miniatură alt șablon
    │
    └─ CTR bun, dar retenția la 30 s slabă (< 60%)?
        │   → promisiunea nu se potrivește cu începutul
        │   → ajustăm titlul/miniatura să descrie exact ce se vede în primele secunde
        │
        └─ Retenția bună la început, dar procent vizionat mic?
            │   → structură sau ritm; căutăm „prăpastia” pe grafic
            │   → lecție pentru scenariile următoare (nu putem reface video-ul)
            │
            └─ Totul bun, dar puțini abonați?
                → lipsește promisiunea canalului / seria / CTA-ul după cel mai bun moment
```

---

## 4. Revizuirea săptămânală (luni, ~30 minute în total)

**Tu (5 min):**
1. YouTube Studio → Analytics → **Advanced mode** → tab **Content** → perioada „Last 28 days”.
2. Adaugă coloanele: Views, Watch time (hours), Average view duration, Average percentage viewed, Impressions, Impressions click-through rate, Subscribers.
3. Export → **CSV** → pune fișierul `Table data.csv` în `tracking/exports/AAAA-LL-ZZ/`.
4. Spune-i lui Claude: „fă revizuirea săptămânală”.

**Claude (automat, cu skill-ul `analytics-review`):**
1. Rulează `python3 tools/analytics/review.py tracking/exports/AAAA-LL-ZZ/Table\ data.csv`.
2. Clasează fiecare video:
   - **A (câștigător):** CTR și procent vizionat peste media canalului → facem încă 2 video-uri similare
   - **B (normal):** în jurul mediei → nicio acțiune
   - **C (slab):** sub 60% din medie la CTR sau retenție → aplicăm arborele din §3
3. Completează `templates/weekly-review.md` → salvat ca `tracking/reviews/AAAA-LL-ZZ-weekly.md`.
4. Propune **maximum 3 acțiuni** pentru săptămâna următoare (ex.: „schimbă titlul la #004”, „următorul video: încă o defalcare de bilete”).

---

## 5. Revizuirea lunară (prima luni din lună, ~60 minute)

Întrebarea centrală: **ce tipare au video-urile câștigătoare?**

Fiecare video are etichete în `tracking/video-log.csv`:
- `pillar` (axa de conținut: Cost Autopsy / How They Make Money / Price History / Hidden Fees / Consumer Traps)
- `structure` (Autopsy / Detective / FollowTheMoney / Timeline)
- `hook_type` (1–8 din 05 §5)
- `title_formula` (1–10 din 05 §3)
- `thumb_template` (A / B / C / D)
- `length_min`

Claude calculează media CTR, procent vizionat și abonați/1.000 **pe fiecare etichetă** și răspunde la:
1. Ce axă de conținut aduce cele mai multe ore?
2. Ce formulă de titlu și ce șablon de miniatură au cel mai bun CTR?
3. Ce structură ține oamenii cel mai mult?
4. De unde vine traficul (căutare vs sugerate vs browse) și cum se schimbă?
5. Progresul spre monetizare: abonați și ore de vizionare (ultimele 365 zile) vs pragul.
6. Ce scoatem din lista de idei și ce adăugăm (actualizăm `docs/04`).

Rezultat: `tracking/reviews/AAAA-LL-monthly.md` (șablon: `templates/monthly-review.md`) + lista de idei reordonată.

---

## 6. Îmbunătățirea video-urilor care obțin rezultate slabe

Ce **se poate** schimba după publicare: titlul, miniatura, descrierea, capitolele, end screen-ul, carduri, playlist-ul, comentariul fixat.
Ce **nu se poate** schimba fără reîncărcare: conținutul video (se pot doar tăia bucăți cu editorul YouTube).

Protocol pentru un video „C”:
1. **Ziua 2:** titlu nou (altă formulă).
2. **Ziua 7:** dacă tot e slab → miniatură nouă (alt șablon) sau rezultatul din Test & Compare.
3. **Ziua 28:** dacă primește trafic din căutare → descriere și capitole optimizate pentru acea căutare.
4. **Oricând:** un Short nou care trimite spre el.
5. **Niciodată:** ștergere sau reîncărcare (pierdem istoricul și nu ajută canalul).

Și cel mai important: **lecția intră în skill-uri** (vezi `CLAUDE.md` → bucla de învățare), ca greșeala să nu se repete.

---

## 7. Venituri (după monetizare)

| Indicator | Ce urmărim |
|---|---|
| RPM per video | Ce subiecte aduc bani mai mulți per vizualizare (de obicei: finanțe, tehnologie, asigurări) |
| Venit pe sursă | AdSense vs afiliere vs sponsorizări vs produse (08) |
| Click-uri pe linkuri | Fiecare link din descriere are parametri UTM sau un link de afiliat separat per video |
| Abonați la newsletter per video | Ce video-uri aduc oameni pe lista de e-mail |

---

## 8. Instrumentul de analiză

`tools/analytics/review.py` — citește exportul CSV din YouTube Studio, calculează mediile canalului, clasează video-urile A/B/C și scrie un raport Markdown. Funcționează fără biblioteci externe (doar Python 3).
Test: `python3 tools/analytics/test_review.py` (folosește date de **exemplu**, marcate clar ca fictive, doar ca să verifice calculul).
