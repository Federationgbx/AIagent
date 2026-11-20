# 05 — Sistemul de producție pentru clicuri (CTR) și atenție (retenție)

> Scop: fiecare video trebuie să câștige **clicul** (titlu + miniatură) și apoi să **țină omul** până la final.
> Limba documentului: română. Exemplele de titluri, hook-uri și replici sunt în **engleză** (limba canalului).

Termeni pe scurt:
- **CTR** = din 100 de oameni care *văd* miniatura, câți dau click.
- **Retenție** = ce procent din video rămâne omul să vadă (graficul arată unde pleacă).
- **Hook** = primele 5–30 de secunde, care decid dacă omul rămâne.

---

## 1. Lanțul care face un video să meargă

```
PROMISIUNE  →  CONFIRMARE  →  LIVRARE  →  RECOMPENSĂ  →  URMĂTORUL PAS
(titlu+mini)   (0–30 sec)    (structură)  (răspunsul)    (alt video)
```

Regula de aur: **miniatura și titlul fac o promisiune; primele 30 de secunde o confirmă; restul o livrează mai bine decât se aștepta omul.**
Dacă promisiunea e mai mare decât livrarea → CTR mare, retenție mică → YouTube oprește distribuția.
Dacă livrarea e bună, dar promisiunea slabă → nimeni nu află de video.

---

## 2. Filtrul de idei (înainte să scriem un cuvânt)

Fiecare idee primește scor 1–5 la șase criterii. Producem doar idei cu **minim 22/30**.

| Criteriu | Întrebarea | Exemplu bun |
|---|---|---|
| Familiaritate | Toată lumea a plătit pentru asta? | popcorn la cinema, iPhone, bilet de avion |
| Miză pentru portofel | Simte omul că e „jupuit” sau păcălit? | taxe la bilete de concert |
| Golul de curiozitate | Există un „de ce?” pe care nu-l poate răspunde singur? | de ce Costco pierde bani la pui |
| Surpriza | Răspunsul e contraintuitiv? | „companiile aeriene câștigă din carduri, nu din zboruri” |
| Căutare | Oamenii caută deja asta pe YouTube/Google? | „why is X so expensive” |
| Se poate arăta | Putem face un grafic clar „unde merge fiecare dolar”? | defalcarea prețului unui latte |

**Testul de 3 secunde:** dacă nu poți explica ideea în 3 secunde unui prieten („Unde ajung de fapt cei 9 dolari pe popcorn”), ideea e prea complicată pentru miniatură.

---

## 3. Titluri — 10 formule care funcționează în nișa noastră

Reguli:
1. Sub **55 de caractere** (pe telefon se taie restul).
2. Un **obiect familiar** + un **număr concret** sau o **contradicție**.
3. Titlul **nu repetă** miniatura — o completează.
4. Fără minciuni. Fără MAJUSCULE peste tot. Maximum un cuvânt cu majuscule pentru accent.
5. Scriem **10 variante** pentru fiecare video și alegem 3 pentru testul A/B (vezi 06).

| # | Formula | Exemplu |
|---|---|---|
| 1 | Where your $X actually goes | Where Your $9 Popcorn Money Actually Goes |
| 2 | Why X costs $Y (now) | Why Concert Tickets Cost $400 Now |
| 3 | X isn't a [business], it's a [alt business] | Airlines Aren't Airlines. They're Banks. |
| 4 | The real cost of X | The Real Cost of a $1,199 iPhone |
| 5 | How X makes money from you | How Spotify Actually Makes Money From You |
| 6 | Why X loses money on Y (on purpose) | Why Costco Loses Money on Chicken (On Purpose) |
| 7 | The $X trick behind Y | The $1.50 Trick That Built Costco |
| 8 | X is a scam? Let's do the math | Is Extended Warranty a Scam? Let's Do the Math |
| 9 | I followed $1 through X | I Followed $1 Through a Concert Ticket |
| 10 | Nobody talks about why X | Nobody Explains Why Insulin Costs More Here |

Atenție: formula 9 („I followed”) sugerează o persoană. O folosim doar ca stil narativ („We followed…”) — canalul nu se prezintă ca o persoană reală (vezi 11).

---

## 4. Miniaturi — sistemul vizual „autopsie”

Identitatea vizuală (detalii în 02): fundal închis, obiectul familiar decupat curat, o **linie punctată de „incizie”** care taie obiectul și **etichete de preț** care arată în ce se descompune prețul.

**Reguli:**
- Un singur subiect mare (obiectul) care ocupă ~50% din imagine.
- Maximum **3 cuvinte** sau **un număr**. De preferat un număr.
- Contrast puternic: obiect luminos pe fundal închis; o singură culoare de accent (roșu-coral pentru „bani pierduți”, verde pentru „profit”).
- Lizibilă la dimensiunea unui timbru (testează la 160×90 px).
- Fără fețe AI realiste de oameni (riscuri de politică + arată ieftin).

**4 șabloane fixe** (le rotim ca să nu arate repetitiv — important și pentru politica YouTube):

| Șablon | Ce se vede | Când îl folosim |
|---|---|---|
| A — „Chitanța” | Obiectul + o chitanță lungă care iese din el, cu un singur rând încercuit | „Where your $X goes” |
| B — „Feliat” | Obiectul tăiat în felii, fiecare felie cu un procent (ex. 4% / 55% / 41%) | defalcări de cost |
| C — „Două prețuri” | Același obiect, două prețuri: „$0.40” vs „$9.49”, cu săgeată | diferențe uriașe cost vs preț |
| D — „Graficul care cade” | Obiectul + o bară/grafic dramatic (crește sau se prăbușește) | istorie de preț, companii |

Fișiere: specificația fiecărei miniaturi intră în `content/<video>/package.md`; randarea automată se face cu `tools/thumbnail/` (vezi 07).

---

## 5. Hook-ul: primele 30 de secunde

Structura fixă:

| Interval | Sarcina | Exemplu (popcorn) |
|---|---|---|
| 0–5 s | **Confirmă promisiunea vizual**: arată obiectul și prețul din miniatură | „This bucket of popcorn costs $9.49. The corn inside it costs about…” *(număr pe ecran)* |
| 5–15 s | **Miza + răsturnarea**: de ce e ciudat, ce crede omul greșit | „But the theater isn't ripping you off the way you think. It's actually losing money on the thing you came for.” |
| 15–30 s | **Harta + bucla deschisă**: ce vom afla, fără să dăm răspunsul | „By the end, you'll see exactly where every dollar of your movie night goes — and why the bucket is the only thing keeping your local cinema alive.” |

**Interzis în hook:** „Hey guys, welcome back”, logo animat lung, rezumatul canalului, cereri de abonare, explicații de context înainte de miză.

**8 tipuri de hook** (alegem unul per video):
1. **Numărul șoc** — „This $1,199 iPhone costs about $X to build.”
2. **Contradicția** — „Airlines lose money flying you. So how are they worth billions?”
3. **Acuzația falsă** — „You think the theater is ripping you off. It isn't. The studio is.”
4. **Testul** — „Pause the video and guess: how much of your $40 ticket goes to the artist?”
5. **Povestea în mijloc** — „In 2009, Costco built a $450 million chicken empire to protect a $4.99 price tag.” *(se verifică cifra în research)*
6. **Consecința personală** — „If you have a credit card, you're already paying for someone's free flight.”
7. **Secretul public** — „It's in their annual report. Page 38. Almost nobody reads it.”
8. **Comparația absurdă** — „Per ounce, this is more expensive than…” *(doar dacă e verificat)*

---

## 6. Scena de deschidere (cold open)

Prima imagine **nu** e logo. E obiectul, mare, cu prețul real pe ecran, într-un cadru care se mișcă (zoom lent sau „incizia” care se desenează).
Sunet: un efect scurt (casa de marcat / „ding”) la apariția prețului.
Primul cuvânt al naratorului începe în **prima secundă**.

Exemplu de scenă (specificație pentru montaj):
> 0:00 — Close-up găleată de popcorn pe fundal negru. Text: **$9.49**. Sunet „ka-ching”.
> 0:02 — O linie punctată coral taie găleata. Bucata de sus se ridică: eticheta „corn: $0.__”.
> 0:05 — Tăietură la sală de cinema goală (stock). Narațiunea începe răsturnarea.

---

## 7. Structuri narative (alegem una per video)

**A. Autopsia** (formatul de bază al canalului, 60% din video-uri)
1. Hook + prețul pe masă (0–8%)
2. „Incizia”: împărțim prețul în 3–5 „organe” (8–15%)
3. Organ cu organ — fiecare cu un mini-mister și răspuns (15–75%)
4. Cauza reală: *de ce* prețul e așa (75–90%)
5. Verdictul + ce poți face tu ca și consumator (90–100%) → video următor

**B. Detectivul** (pentru „how X really makes money”)
Misterul → indiciul 1 → fundătura → indiciul 2 → răsturnarea → adevărul → implicația.

**C. Urmărește dolarul** (follow the money)
Un dolar animat pleacă din buzunarul privitorului și e urmărit prin fiecare intermediar. Excelent pentru bilete, medicamente, streaming.

**D. Cronologia prețului**
„Acum 20 de ani costa $X. Azi costă $Y. Ce s-a schimbat?” — 3–4 momente-cheie, fiecare cu o cauză.

Lungime țintă: **8–12 minute** (destul pentru timp de vizionare, scurt cât să ținem ritmul). Fiecare capitol: 60–120 de secunde.

---

## 8. Tehnici de menținere a atenției (retenție)

| Tehnică | Cum o aplicăm | Frecvență |
|---|---|---|
| **Chitanța care curge** (semnătura canalului) | O chitanță în colțul ecranului se completează pe măsură ce descompunem prețul. Omul rămâne ca să vadă „totalul”. | tot video-ul |
| Bucle deschise | „We'll get to the popcorn in a minute — but first, the number that surprised me most…” — închidem bucla mai târziu | 1 la fiecare capitol |
| Re-hook la început de capitol | Fiecare capitol începe cu o întrebare, nu cu o explicație | fiecare capitol |
| Schimbare vizuală | Imagine nouă la fiecare 3–6 secunde (grafic, stock, text, hartă) | continuu |
| „Pause and guess” | Întrebăm privitorul o cifră, apoi o dezvăluim pe grafic | 1–2 per video |
| Specificitate | „$0.41” nu „câțiva cenți”; „page 38 of the 10-K” nu „rapoartele” | mereu |
| Ritmul propozițiilor | Fraze scurte. Apoi una mai lungă care explică. Apoi din nou scurt. | mereu |
| Răsturnare la 50–60% | Un fapt care schimbă perspectiva exact unde graficele de retenție scad de obicei | 1 per video |
| Fără „umplutură” | Tăiem orice frază care nu adaugă un fapt, o întrebare sau o emoție | la editare |
| Final fără „outro” lung | Ultimele 20 de secunde trec direct la următorul video recomandat | mereu |

---

## 9. Îndemnuri la acțiune (CTA)

| Moment | Ce cerem | Exemplu |
|---|---|---|
| ~30% din video | Nimic sau comentariu-întrebare | „Quick question before we go on — what's the most overpriced thing you bought this month? I read every comment.” *(la AI: „we read every comment” — scris la plural, canalul e o echipă/marcă)* |
| ~65% din video (după cel mai bun moment) | Abonare **legată de valoare** | „Every week we cut open the price of one thing you pay for. If you want the next one, subscribe — next week it's concert tickets.” |
| Ultimele 15 s | Un singur video următor (end screen) | „The airline trick is even crazier. That one's right here.” |
| Comentariul fixat | Întrebare + sursele | „Sources for every number are in the description. Which price should we dissect next?” |

Reguli: un singur CTA principal pe video-moment; niciodată „like, comment, subscribe, bell” toate odată.

---

## 10. Zece idei dezvoltate complet (titlu, miniatură, hook, de ce merge)

| # | Titlu | Miniatură | Hook (prima frază) | De ce atrage și ține |
|---|---|---|---|---|
| 1 | Where Your $9 Popcorn Money Actually Goes | B — găleată feliată: „3% / 82% profit” *(cifre din research)* | „The corn in this $9.49 bucket costs less than your parking meter's spare change.” | Toată lumea a simțit prețul; răsturnarea „cinema-ul trăiește din popcorn” e surprinzătoare |
| 2 | Airlines Aren't Airlines. They're Banks. | C — avion + card de credit, „$7B” | „Delta made more from a credit card last year than from…” *(cifra din research)* | Contradicție puternică; privitorul are un card și simte că e implicat |
| 3 | The $1.50 Trick That Built Costco | A — hot dog + chitanță cu „MEMBERSHIP” încercuit | „Costco has sold this hot dog for $1.50 since 1985. It's not a hot dog. It's a contract.” | Nostalgie + mister + model de business ușor de înțeles |
| 4 | Why Concert Tickets Cost $400 Now | C — „$89 → $412” | „The band set the price at $89. You paid $412. Let's find the other $323.” | Durere recentă, mulți oameni furioși, structură „urmărește dolarul” |
| 5 | The Real Cost of a $1,199 iPhone | B — iPhone feliat în componente | „Apple pays about $X for the parts inside this phone. The rest isn't profit — not all of it.” | Produs universal; dezvăluirea „marja nu e unde crezi” |
| 6 | Why Insulin Costs 10x More in the US | C — două fiole, steaguri | „The same vial. Two prices. Same factory.” | Miză morală + comparație clară; atenție la acuratețe (temă sensibilă) |
| 7 | How Spotify Pays an Artist $0.003 | A — telefon + chitanță minusculă | „For every 1,000 streams, an artist gets about… pause and guess.” | Interactivitate + nedreptate percepută |
| 8 | Why Your Grocery Bill Doubled (It's Not Inflation) | D — coș + grafic care urcă | „Inflation explains part of this. The rest has a name, and you've never heard it.” | Relevanță zilnică maximă; buclă deschisă puternică |
| 9 | Hidden Fees: Where Your $20 Uber Goes | A — mașină + chitanță lungă | „Your driver got less than half. So who got the rest?” | Simpatie pentru șofer + curiozitate despre platformă |
| 10 | Why Restaurants Lose Money on Steak | B — friptură feliată | „The most expensive thing on the menu is the one they make the least on.” | Contraintuitiv; deschide seria „meniul decodat” |

Toate cifrele marcate „*(din research)*” se completează **numai** din fișierul `research.md` al video-ului. Nicio cifră nu intră în scenariu fără sursă.

---

## 11. Checklist CTR + retenție (înainte de publicare)

- [ ] Ideea are scor ≥ 22/30 la filtrul din secțiunea 2
- [ ] 10 titluri scrise, 3 alese pentru test; cel principal ≤ 55 caractere
- [ ] Miniatura e lizibilă la 160×90 px și nu repetă titlul
- [ ] Prima secundă arată obiectul și prețul din miniatură
- [ ] Hook-ul are miză + răsturnare + buclă deschisă în ≤ 30 s
- [ ] Fiecare capitol începe cu o întrebare
- [ ] Cel puțin un moment „pause and guess” și o răsturnare la ~50–60%
- [ ] Chitanța de pe ecran se completează pe tot parcursul
- [ ] Nicio frază fără un fapt, o întrebare sau o emoție
- [ ] Toate cifrele au sursă în `research.md`
- [ ] Un singur CTA de abonare (după cel mai bun moment), end screen spre un video anume
