# Haushaltsrauschen

Momentan sind 30 Daten mit unterschiedlicher Dauer und Abtastrate verfügbar.   
Die Rauschdaten sind in dem Ordner ``` /noise_data/..``` zu finden, unterteilt in Rohdaten ```/noise_data/raw/```
und aufbereitete Daten ```/noise_data/processed/```.

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
from sample import loadData

# -- Implemented --
path = "path/to/store/noisy_data"
loadData.resampledNoise(path)
loadData.resampledData(path)
# ---            

# TODO: [Duration] Work on cutting sound files in 5 sec pieces
noise = helpers.scaleDuration(path, Duration)

noise = helpers.scaleVolume(path, volume)
```

### Vorverarbeitet

Die vorverarbeiteten __Rauschdaten__ sollten in gleicher Abtastrate wie __Nutzdaten__ (16 KHz) vorliegen. Skaliert auf
eine passende Lautstärke sowie Dauer in Bezug zu den __Nutzdaten__ (5 sec).

## Datenbeschaffung

Ein Teil der Daten wurde von mir selbst aufgenommen, der andere Teil wurde von [Freesound.org](https://freesound.org/)
beschafft/heruntergeladen und unterliegen der [zero(cc0)](http://creativecommons.org/publicdomain/zero/1.0/) license.

