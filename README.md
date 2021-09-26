# Projektarbeit 1 (Audio Preprocessing)

Dieses Package wird im Rahmen der Projektarbeit 1 erstellt und soll zur Unterstützung der Projektarbeit 2 dienen. Indem
Funktionalitäten angeboten werden, um additiv Störgeräusche einem Audiodatensatz hinzuzufügen und diese zu
Visualisieren.

## [Störgeräusche](noise_data/README.md):

* Klimaanlage
* Straße
* Staubsauger
* Spülmaschine
* Waschmaschine

---

## Funktionalität:

__*NOTE*__ : Hierbei handelt es sich um eine Richtlinie. 

1. Rauschen numerisch laden 6x5*16k ? :

   ```python
   from sample import loadData, helpers
   
   noise_type = loadData.processedNoise(type)
   # type := {aircon, dishwasher, vacuuming, street, washer}
   ```
   
2. Einem Audiosignal additiv ein Störgeräusch hinzufügen:
   ```python
   path = "path/to/audiofile.wav" # sampled in 16KHz
   data = load(path)
   noisyData = helpers.addNoise(data, noise_type)
   ```
3. Verrauschtes Signal darstellen:
   ```python
   specData = package.calcSpec(noisyData)
   mfccData = package.calcMfcc(noisyData)
   ...
   ```

---

## Usage/Import:

```python
from sample import loadData, helpers
```
