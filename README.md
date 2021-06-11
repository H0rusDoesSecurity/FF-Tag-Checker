# FF-Tag-Checker
FF.de uses annoyingly long tags. Here's a script that replaces them and checks for basic errors

## Anleitung
* Python3 installieren 
* Kapitel schreiben und anstatt der langen FF Tags die kurzen nutzen
* Kapitel in inp.txt im gleichen Ordner wie den TagChecker speichern
* TagChecker laufen lassen
* Profit!

# Tag Übersicht!
## Style Tags
Alle Style Tags haben **!!** 

* **Kursiv:** !!i
* **Fett:** !!b
* **Unterstrichen:** !!u
* **Durchgestrichen:** !!s
* **Schließender Tag:** /!!

## Align Tags
Alle Align Tags haben **??**
* **Mittig:** ??c
* **Links:** ??l
* **Rechts:** ??r

## Was es kann
* 3 Character lange Tags durch die FF.de Tags ersetzen
* Zählen, ob es gleich viele öffnende und schließende style/align Tags gibt
* Dir sagen, wo du suchen musst, falls Tags fehlen
* Dir fehlende Klammern, nervige Kämpfe mit dem Editor und endloses Copy-Pasten ersparen

## Was es nicht kann
* Checken, ob die Schachtelung stimmt
* Vernúnftiges Markdown konvertieren
* \[Normal\] Tags entfernen

