# Haushaltsrauschen

Momentan sind 12 Daten mit unterschiedlicher Dauer und einer Abtastrate von 44 KHz verfügbar. 
Das Rauschen ist in dem Ordner ``` /noise_data/..``` zu finden, unterteilt in Rohdaten ```/noise_data/raw/```
und aufbereitete Daten ```/noise_data/processed/```.

## Datenseparierung

* 3x Klimaanlage
* 4x Spülmaschine
* 2x Straßenlärm
* 3x Staubsauger


### Vorverarbeitet

Das vorverarbeitete __Rauschen__ sollte in gleicher Abtastrate wie __Nutzdaten__ (16 KHz) vorliegen. Skaliert auf
eine passende Lautstärke (SNR) 0dB sowie Dauer in Bezug zu den __Nutzdaten__ (5 sec). Die ersten 8 sec der __Nutzdaten__ 
werden durch die Funktion entfernt, da diese unrealistische Informationen erhalten.

## Datenbeschaffung

Ein Teil der Daten wurde von mir selbst aufgenommen, der andere Teil wurde von [Freesound.org](https://freesound.org/)
beschafft/heruntergeladen und unterliegen der [zero(cc0)](http://creativecommons.org/publicdomain/zero/1.0/) license.
