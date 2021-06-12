# FF-Tag-Checker
FF.de uses annoyingly long tags. Here's a script that replaces them and checks for basic errors

## Anleitung
* Aktuellen Release runterladen
* Ordner entpacken
* Kapitel schreiben und anstatt der langen FF Tags die kurzen nutzen
* Kapitel als inp.txt im entpackten Ordner speichern
* TagChecker.exe ausführen
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
* **Schließender Tag:** /??

## Beispiel
!!i!!b??cHallo Welt!/??/!!/!!

**wird zu**

\[style type="italic"\]\[style type="bold"\]\[align type="center"\]Hallo Welt!\[/align\]\[/style\]\[/style\]

# Was es kann
* 3 Character lange Tags durch die FF.de Tags ersetzen
* Zählen, ob es gleich viele öffnende und schließende style/align Tags gibt
* Dir sagen, wo du suchen musst, falls Tags fehlen
* Dir fehlende Klammern, nervige Kämpfe mit dem Editor und endloses Copy-Pasten ersparen

# Was es nicht kann
* Checken, ob die Schachtelung stimmt
* Vernünftiges Markdown konvertieren
* \[Normal\] Tags entfernen

