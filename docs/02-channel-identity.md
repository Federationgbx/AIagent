# 02 — Identitatea canalului și poziționarea

---

## 1. Numele

| | |
|---|---|
| **Nume recomandat** | **Pricewhy** |
| **Handle** | **@Pricewhy** — liber la 20.11.2026 (pagina dădea 404), fără canale cu același nume, fără conflict de marcă găsit |
| **Rezervă** | **Tilltale** — handle-ul @Tilltale e luat (gol), **@TilltaleTV** e liber |
| **De ce nu un nume descriptiv** | „Price Autopsy”, „Behind The Price”, „Itemized”, „Subtotal”, „Sticker Shock”, „Line Item” sunt toate deja folosite de canale-clonă cu voce AI și ~0 vizualizări (01 §4.2). Un nume inventat ne separă de ele |

⚠️ **Acțiune pentru tine, cât mai repede:** creează canalul și rezervă handle-ul @Pricewhy (disponibilitatea se poate schimba oricând). Mărcile înregistrate (USPTO/UKIPO) **nu** au fost verificate.

---

## 2. Poziționarea (o frază)

> **Pricewhy explică de ce lucrurile costă cât costă — dolar cu dolar, cu sursele pe ecran, în SUA, Marea Britanie, Canada și Australia.**

- **Slogan (EN):** *Why things cost what they cost.*
- **Promisiunea repetată în video-uri (EN):** *„Every week, we take one price apart — line by line.”*
- **Diferența față de concurenți:**
  - față de canalele mari (Business Insider, CNBC, Wendover): ne concentrăm pe **chitanța consumatorului**, nu pe fabrică sau pe macroeconomie; și pe **4 țări**, nu doar SUA;
  - față de clone: **analiză originală**, surse pe ecran, grafice proprii, scenarii scrise cu structură, nu „slideshow” cu voce.

---

## 3. Publicul țintă

### Persoana principală — „The Squeezed Curious” (70%)
| | |
|---|---|
| Vârstă | 25–44 |
| Țări | SUA (~50%), Marea Britanie, Canada, Australia |
| Situație | Lucrează, simte că „totul s-a scumpit”, nu e economist |
| Ce vrea | Să **înțeleagă** de ce plătește cât plătește — și să nu fie păcălit |
| Ce nu vrea | Sfaturi de investiții, jargon, prelegeri de 45 de minute |
| Ce mai urmărește | Wendover, Half as Interesting, CNBC, Company Man, How Money Works |
| Când se uită | Seara, în weekend, pe telefon și pe TV |

### Persoana secundară — „The Business Nerd” (30%)
Studenți la business/economie și angajați curioși de modele de afaceri. Vin pentru „How They Make Money” și rămân pentru calcule.

---

## 4. Vocea canalului (cum scriem)

**Personalitate:** detectivul calm și ușor ironic, care a citit raportul anual ca să nu trebuiască să-l citești tu.

| Facem | Nu facem |
|---|---|
| Fraze scurte. Cifre exacte. „$0.41”, nu „câțiva cenți” | Jargon fără explicație („EBITDA” fără traducere) |
| Ironie fină la adresa sistemului, nu a privitorului | Să facem privitorul să se simtă prost |
| „We” (canalul) sau formulări neutre | „I'm Mike, a finance expert” — nicio persoană inventată (11) |
| Recunoaștem nuanța: „Here's the part that doesn't fit the story” | Concluzii conspiraționiste sau acuzații fără sursă |
| Spunem anul fiecărei cifre | Cifre fără dată |
| Terminăm cu ce poate face privitorul (doar ca informație) | Sfaturi financiare personalizate |

**Cuvinte-semnătură (EN):** *line by line · here's the receipt · follow the dollar · the part nobody reads · page X of the annual report.*

**Vocea AI (narațiunea):**
- O singură voce pentru totdeauna (devine identitatea sonoră).
- Profil: caldă, calmă, registru mediu, ritm de documentar, accent nord-american neutru (piața cea mai mare); fără ton de „reclamă”.
- **Alegerea:** la primul video, Claude marchează un paragraf de test; tu generezi 3 voci în ElevenLabs, alegi una și notezi aici numele vocii și setările:
  - Vocea aleasă: `________` · Stabilitate: `____` · Claritate: `____` · Stil: `____`

---

## 5. Identitatea vizuală

### 5.1 Culori (aceleași în `tools/render/render.mjs` → BRAND)
| Rol | Culoare | Cod |
|---|---|---|
| Fundal | Cerneală (aproape negru) | `#0E0F12` |
| Chitanța / text principal | Hârtie | `#F4F1EA` |
| Bani pierduți / taxe / costuri | Coral | `#FF5A4E` |
| Profit | Verde | `#2BD38A` |
| Accent / titluri / săgeți | Galben | `#FFD23F` |
| Neutru secundar | Gri | `#9AA0A6` |
| Al doilea accent (date, hărți) | Albastru | `#4C8DFF` |

### 5.2 Fonturi
- Titluri și cifre mari: **Inter Display Black / ExtraBold**
- Chitanța și sursele: **JetBrains Mono**

### 5.3 Elementele-semnătură
1. **Chitanța** — o chitanță de hârtie pe fundal închis, care se „printează” linie cu linie pe parcursul video-ului. Ultima linie e totalul. (`tools/render` → tipul `receipt`.)
2. **Linia de incizie** — o linie punctată coral care „taie” obiectul, în miniaturi și în cold open.
3. **Obiectul-erou** — ilustrații vectoriale plate, originale (popcorn, avion, hot dog...), nu fotografii stock generice. Consecvente și ușor de recunoscut în feed.
4. **Tabla de prețuri** — prețul aceluiași lucru în SUA / UK / CA / AU, convertit în dolari, cu data cursului (doar când există date comparabile).
5. **Sursa pe ecran** — mereu jos-stânga, în font mono: „Source: AMC 10-K, FY2025”.

### 5.4 Logo și pagina canalului
- **Logo:** semnul „?” desenat ca o chitanță ondulată, coral pe fundal închis (Claude livrează specificația; se poate face în Canva în 10 minute sau îl randăm cu `tools/render`).
- **Banner (EN):** „PRICEWHY — Why things cost what they cost. New breakdown every Tuesday & Friday.”
- **Descriere „About” (EN):**
  > Pricewhy takes one price apart every week — the popcorn, the plane ticket, the hot dog — and shows where every dollar actually goes, with the sources on screen. We compare prices across the US, UK, Canada and Australia. Narration uses a synthetic voice; every number is sourced in the description. Educational content, not financial advice.
- **Trailer pentru vizitatori noi:** cel mai bun video (după primele 8, ales din date).

### 5.5 Ce nu folosim niciodată
- Fețe umane realiste generate AI, siglele altor creatori, clipuri TV, fotografii stock generice „om îngrijorat cu calculator”.
- Mai mult de 3 cuvinte pe miniatură.

---

## 6. Promisiunea pe 12 luni

- Fiecare video: o întrebare de preț, răspunsul complet, sursele.
- Ritm: marți și vineri.
- La 12 luni: cea mai bună bibliotecă de „de ce costă X” din limba engleză pentru 4 țări — și un canal monetizat.
