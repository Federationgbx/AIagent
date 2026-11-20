# 12 — Testul skill-urilor pe cazuri reale

> Fiecare skill a fost rulat pe un caz real (nu pe exemple inventate). Pentru 001 și 002, skill-urile au fost urmate de **agenți separați** care au avut doar fișierele `SKILL.md` și documentele — un test cinstit că instrucțiunile sunt suficiente singure.
> „Fără skill” = ce iese de obicei când cineva face pasul fără procedură (cum fac canalele-clonă din 01 §4.2).

---

## Rezultate

| Skill | Caz real | Rezultat | Fără skill (comparație) | Ce am corectat în skill |
|---|---|---|---|---|
| **research-brief** | 001 popcorn, 002 companii aeriene, 003 Costco | 3 fișe cu fiecare cifră sursată, perioadă și nivel de încredere; verdict pentru fiecare teză | Primele rezultate Google repetă miturile: „studiourile iau 90%”, „marja la popcorn e 85%”, „abonamentul = 70% din profitul Costco”. Toate trei sunt **false sau exagerate** — skill-ul le-a prins și le-a pus la „Do NOT claim” | Pasul 8 (verdictul tezei) și regula „nu rotunji ca să schimbi povestea” |
| **script-writer** | 003 (scris direct), 001 și 002 (agenți separați) | 3 scenarii de 1.492 / 1.605 / 1.840 cuvinte, 3 structuri diferite (Detectiv, Urmărește dolarul, Autopsie), tabel de verificare a cifrelor (până la 41 de rânduri) | Intro „Hey guys, welcome back”, cerere de abonare la început, cifre fără sursă (vezi exemplul rău din SKILL.md) | Lista de scene trimite la ¶ în loc să repete textul; plafon ferm de 1.900 cuvinte |
| **packaging** | 001, 002, 003 | 30 de titluri, 9 miniaturi, 76 de imagini randate și verificate vizual, descrieri cu surse sub limitele YouTube | ~45–60 min în Canva per video; titluri care promit ce video-ul nu arată | Limitele YouTube; corecturi în generatorul de imagini (etichete, total ascuns, sigla de card eliminată) |
| **shorts-repurpose** | 001, 002, 003 | 15 Shorts, câte unul pe capitol, date de publicare eșalonate 1–16 decembrie | Rezumatul întregului video în 55 de secunde — oamenii dau swipe | Notat: lipsesc graficele native 9:16 (în lista „NEXT”) |
| **analytics-review** | Date de **exemplu** (fictive, marcate SAMPLE) — canalul nu are încă date reale | 7 teste trec; clasare A/B/C corectă și diagnostic pe semnalul care a picat | „Algoritmul nu mă iubește” — fără semnal numit, fără acțiune măsurabilă | Primul test real: prima luni după lansare (7 decembrie 2026) |

---

## Verificarea finală (provocarea pe care mi-ai cerut-o)

**1. Care două skill-uri se suprapun?**
`script-writer` și `packaging` ating amândouă imaginile: primul decide **ce** apare pe ecran (lista de scene), al doilea **creează** fișierele. Granița e acum scrisă explicit în ambele (scriptul numește fișierul, ambalajul îl randează). A doua suprapunere mică: `script-writer` și `shorts-repurpose` scriu amândouă narațiune — Shorts-urile au voie să folosească **doar** fapte deja din scenariu.

**2. Ce descriere era prea vagă?**
`research-brief` se declanșa la „start video N”, care se confunda cu comanda săptămânală „start week N”. Corectat: comanda săptămânală e definită în `CLAUDE.md` și apelează skill-urile în ordine; `research-brief` se declanșează la „research #N”.

**3. Ce mai explici încă de mână?**
- Ce video-uri urmează săptămâna asta → rezolvat cu comanda **„start week N”** din `CLAUDE.md` (citește calendarul singur).
- Cum vrei să primești fișierele → rezolvat: ZIP-uri trimise direct în chat (`tools/export/bundle.py`), fără GitHub.
- **Montajul în CapCut** → încă manual. E cea mai mare parte din timpul tău — primul pe lista de mai jos.

---

## NEXT 3 SKILLS TO BUILD (ordonate după orele economisite pe săptămână)

| # | Skill | Ce face | Ore economisite / săptămână |
|---|---|---|---|
| 1 | **rough-cut** | Din vocea generată + lista de scene + imaginile randate → o primă variantă de montaj (MP4) cu zoom lent pe grafice, chitanța pe pași, muzică sub voce. Tu doar verifici și încarci. Varianta completă: dacă îmi dai o cheie ElevenLabs prin formularul securizat (niciodată în chat), generez și vocea în cloud și îți trimit video-ul gata | **~2–3 h** |
| 2 | **subtitles-and-chapters** | Subtitrări .srt și timpii reali ai capitolelor, calculați din fișierul de voce; versiuni 9:16 ale graficelor pentru Shorts | **~1 h** |
| 3 | **newsletter-community** | Newsletterul săptămânal „The Receipt”, 2–3 postări Community și răspunsuri pregătite la comentarii, din cercetarea existentă | **~45 min** (de la etapa 1, 100+ abonați) |
