# 6 Rechnen am Schleifprozess

<div class="ziel" markdown="1">

Lernziel · 5 Einheiten

Du rechnest Schnittgeschwindigkeit, Geschwindigkeitsverhältnis, Zeitspanvolumen und **Taktzeit** sicher aus. Du schätzt, bevor du rechnest. Mit der Taktzeit zeigst du einem Kunden, was eine neue Maschine **pro Teil** bringt. In Kapitel 13 wird daraus die Wirtschaftlichkeitsrechnung.

</div>

<div class="einstieg" markdown="1">

Warum ein Verkäufer rechnen muss

Die meisten Wettbewerber zeigen Prospekte. Wer dem Kunden **mit seinen eigenen Teilen** vorrechnet, dass er 40 Sekunden pro Teil spart, verkauft gegen den Preis. Genau das übst du hier.

</div>

## 6.1 Die Formeln

| Größe | Formel | Einheit | Typische Werte (Richtwerte) |
|---|---|---|---|
| Schnittgeschwindigkeit | **v_c = π · d_s · n_s / 60 000** | m/s (d_s in mm, n_s in 1/min) | Korund ca. 25–35 m/s, CBN deutlich höher möglich |
| Werkstück-/Tischgeschwindigkeit | **v_w** | m/min | Pendelschleifen: einige 10 m/min |
| Geschwindigkeitsverhältnis | **q_s = v_c / v_w** (beide in m/s!) | – | Flachschleifen typisch 50–100, unter 50 Rattergefahr |
| Zustellung | **a_e** | mm | Pendeln: 0,005–0,03 mm |
| bezogenes Zeitspanvolumen | **Q'_w = a_e · v_w** (v_w in mm/s) | mm³/(mm·s) | „Wie viel mm³ pro Sekunde und mm Scheibenbreite“ |

<div class="merk" markdown="1">

Merksatz

Die Einheiten sind die häufigste Fehlerquelle. **Rechne alles zuerst in mm und s um.** 1 m/min = 1000 mm / 60 s = **16,67 mm/s**.

</div>

[[LINIEN 2]]

### Beispiel 1: Schnittgeschwindigkeit

Scheibe Ø 355 mm, Drehzahl 1500 1/min:
v_c = π · 355 · 1500 / 60 000 = 1 672 898 / 60 000 = **27,9 m/s**

### Beispiel 2: Geschwindigkeitsverhältnis

v_c = 35 m/s, v_w = 30 m/min = 0,5 m/s → q_s = 35 / 0,5 = **70**. Das liegt im typischen Bereich für das Flachschleifen.

### Beispiel 3: Zeitspanvolumen

a_e = 0,02 mm, v_w = 20 m/min = 333,3 mm/s → Q'_w = 0,02 · 333,3 = **6,7 mm³/(mm·s)**

## 6.2 Taktzeit beim Flachschleifen

<div class="formel">Lagen = Aufmaß / a_e  ·  Hubzeit = (L + Überlauf) / v_w</div>
<div class="formel">Einstechen: t = Lagen · Hubzeit</div>
<div class="formel">Pendeln: t = Lagen · Querschritte · Hubzeit, mit Querschritte = B / f_q (aufrunden)</div>

Dazu kommen **Ausfunkhübe**, **Abrichten** und **Nebenzeiten** (Spannen, Messen, Laden). Reale Maschinen brauchen außerdem Zeit für die Tischumkehr. Deshalb ist eine gerechnete Taktzeit immer eine **Untergrenze**.

### Beispiel 4: Platte im Pendelschleifen, Schruppen und Schlichten

Platte L × B = 400 × 200 mm, Aufmaß 0,30 mm, v_w = 20 m/min = 20 000 mm/min, Überlauf gesamt 50 mm.

| | Schruppen | Schlichten |
|---|---|---|
| Aufmaß | 0,25 mm | 0,05 mm |
| a_e | 0,025 mm | 0,005 mm |
| Lagen | 0,25 / 0,025 = 10 | 0,05 / 0,005 = 10 |
| f_q | 15 mm | 5 mm |
| Querschritte | 200 / 15 = 13,3 → 14 | 200 / 5 = 40 |
| Hubzeit | 450 / 20 000 min = 0,0225 min = 1,35 s | 1,35 s |
| **Zeit** | 10 · 14 · 1,35 = **189 s** | 10 · 40 · 1,35 = **540 s** |

Gesamt: 189 + 540 = **729 s ≈ 12,2 min**, ohne Ausfunken und Nebenzeiten.

<div class="merk" markdown="1">

Erkenntnis

Das **Schlichten** kostet hier fast dreimal so viel Zeit wie das Schruppen, obwohl es nur ein Sechstel des Aufmaßes ist. Wer Taktzeit sparen will, schaut zuerst auf das Schlichten: auf eine feinere Scheibe, einen anderen Zyklus oder ein kleineres Aufmaß vom Härten.

</div>

<div class="vorher" markdown="1">

Erst schätzen, dann prüfen · Aufgabe 6.1

Bevor du weiterrechnest: Was ist wohl schneller, **eine** Leiste 250 × 40 mm einzeln einstechen oder **sechs** Leisten nebeneinander in einer Aufspannung? Und warum könnte die Antwort „kommt darauf an“ sein? Schreib deine Vermutung auf. Du prüfst sie in den Aufgaben 6.6 bis 6.8.

</div>

[[LINIEN 2]]

<div class="rechnen" markdown="1">

Rechnen · Aufgaben 6.2 bis 6.5

**6.2** Scheibe Ø 355 mm, n_s = 1800 1/min. Wie groß ist v_c?

**6.3** Die Scheibe ist auf Ø 300 mm abgerichtet. Die Drehzahl bleibt bei 1800 1/min. Wie groß ist v_c jetzt? Welche Drehzahl brauchst du, um wieder dieselbe v_c wie in 6.2 zu erreichen? Liegt sie im Bereich einer Spindel mit 500–2500 1/min?

**6.4** v_c = 30 m/s, v_w = 18 m/min. Berechne q_s. Liegt der Wert im typischen Bereich?

**6.5** a_e = 0,015 mm, v_w = 24 m/min. Berechne Q'_w.

</div>

[[KARO 80]]

<div class="rechnen" markdown="1">

Rechnen · Aufgaben 6.6 bis 6.8 – Taktzeit

Für alle drei Aufgaben gilt: Leiste L × B = 250 × 40 mm, Scheibenbreite 50 mm, Aufmaß 0,15 mm, a_e = 0,015 mm, v_w = 20 m/min, Überlauf gesamt 50 mm. Spannen und Laden dauern 60 s pro Aufspannung, egal wie viele Teile auf der Platte liegen. Rechne **ohne Ausfunken**.

**6.6** **Eine** Leiste, Einstechschleifen. Wie lange dauert das Schleifen und wie lange dauert es pro Teil mit Spannen?

**6.7** **Sechs** Leisten nebeneinander mit 10 mm Abstand. Wie breit ist die Fläche? Sie wird **gependelt** mit f_q = 20 mm. Berechne die Zeit pro Teil mit Spannen.

**6.8** Dieselben sechs Leisten, aber mit **Mehrpositionsschleifen**: Jede Leiste wird an ihrer Position einzeln eingestochen. Die Fahrzeit zwischen den Positionen vernachlässigst du. Wie groß ist die Zeit pro Teil?

Vergleiche 6.6, 6.7 und 6.8. Welches Argument für eine CNC-Maschine mit Mehrpositionsschleifen ergibt sich daraus?

</div>

[[KARO 95]]

## 6.3 Was passiert, wenn …? Gefühl für die Stellschrauben

| Wenn du … erhöhst | Zeitspanvolumen | Wärme | Rauheit | Risiko |
|---|---|---|---|---|
| Zustellung a_e | steigt | steigt stark | steigt | Brand, Risse |
| Tischgeschwindigkeit v_w | steigt | steigt | steigt | Ratter bei kleinem q_s |
| Schnittgeschwindigkeit v_c | – | steigt | sinkt (feinere Späne) | Grenze der Scheibe |
| Querschritt f_q | Zeit sinkt | – | steigt (Streifen) | sichtbare Spuren |

<div class="vorher" markdown="1">

Erst schätzen, dann prüfen · Aufgabe 6.9

Ein Kunde will die Taktzeit aus Beispiel 4 halbieren und schlägt vor: „Einfach beim Schlichten a_e verdoppeln.“ Schätze, was mit der **Zeit**, der **Oberfläche** und der **Ebenheit** passiert. Rechne dann die neue Schlichtzeit aus.

</div>

[[KARO 40]]

<div class="sprechen" markdown="1">

Laut sprechen · Aufgabe 6.10 (2 Minuten)

Nimm dein Ergebnis aus 6.6 bis 6.8 und präsentiere es einem Fertigungsleiter: „Heute schleifen Sie einzeln, mit Mehrpositionsschleifen sind es … Sekunden pro Teil.“ Rechne die Ersparnis auf **1000 Leisten pro Monat** hoch, in Stunden.

</div>

<div class="begriffe" markdown="1">

Fachbegriffe Deutsch – Englisch

| Deutsch | Englisch | Deutsch | Englisch |
|---|---|---|---|
| Schnittgeschwindigkeit | wheel speed / cutting speed | Taktzeit | cycle time |
| Tischgeschwindigkeit | table speed | Hauptzeit | grinding time |
| Zeitspanvolumen | material removal rate (MRR) | Nebenzeit | non-productive time |
| Schruppen | roughing | Überlauf | overtravel |
| Schlichten | finishing | Mehrpositionsschleifen | multi-position grinding |

</div>

<div class="test" markdown="1">

Kurztest Kapitel 6

1. Schreib die Formel für v_c aus dem Gedächtnis auf und nenne die Einheiten.
2. Rechne 30 m/min in mm/s um.
3. Warum ist eine gerechnete Taktzeit immer nur eine Untergrenze?
4. Was ist beim Flachschleifen meist der größte Zeitfresser?
5. Was passiert mit v_c, wenn die Scheibe kleiner wird und die Drehzahl gleich bleibt?

</div>

[[LINIEN 6]]

Wiederholen am: ________ (morgen) · ________ (in 1 Woche) · ________ (in 1 Monat)
