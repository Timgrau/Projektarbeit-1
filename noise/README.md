# Haushaltsrauschen

Momentan sind 30 Daten mit unterschiedlicher Dauer und Abtastrate verfügbar.   
Die Rauschdaten sind in dem Ordner ``` /noise/..``` zu finden, unterteilt in Rohdaten ```/noise/raw/```
und aufbereitete Daten ```/noise/processed/```.

## Datenseparierung

* 6x Klimaanlage
* 6x Spülmaschine
* 6x Straßenlärm
* 6x Staubsauger
* 6x Waschmaschine

### Roh

Die __Rauschdaten__ liegen in Unterschiedlicher Dauer, Lautstärke und Abtastrate vor.

Funktionen aus dem Modul ```helpers.py``` sollten diese Daten passend vorverarbeiten:

```python
noise = helpers.sampleData(noise, sample_rate)
noise = helpers.scaleVolume(noise, volume)
noise = helpers.scaleDuration(noise, Duration)
```

### Vorverarbeitet

Die vorverarbeiteten __Rauschdaten__ sollten in gleicher Abtastrate wie __Nutzdaten__ vorliegen. Skaliert auf eine
passende Lautstärke sowie Dauer in Bezug zu den __Nutzdaten__.

## Datenbeschaffung

Ein Teil der Daten wurde von mir selbst aufgenommen, der andere Teil wurde von [Freesound.org](https://freesound.org/)
beschafft/heruntergeladen und unterliegen der [zero(cc0)](http://creativecommons.org/publicdomain/zero/1.0/) license.

