# Projektarbeit 1 (Audio Preprocessing)

Dieses Package wird im Rahmen der Projektarbeit 1 erstellt und soll zur Unterstützung der Projektarbeit 2 dienen. Indem
Funktionalitäten angeboten werden, um additiv Störgeräusche einem Audiodatensatz hinzuzufügen und diese zu
Visualisieren.

## [Störgeräusche](noise/README.md):

* Klimaanlage
* Straße
* Staubsauger
* Spülmaschine
* Waschmaschine

---

## Funktionalität:

1. Einem Audiosignal additiv ein Störgeräusch hinzufügen:
   ```python
   data = "path/to/audiofile.wav"
   noisyData = package.addNoise(data, selectedNoise)
   # selectedNoise := {aircon, dishwasher, vacuuming, street, washer}
   ```
2. Rauschdaten laden:
   ```python
   noisyData = package.aircon.loadNoise()
   noisyData = package.street.loadNoise()
   ...
   ```
3. Verrauschtes Signal darstellen:
   ```python
   specData = package.calcSpec(noisyData)
   mfccData = package.calcMfcc(noisyData)
   ...
   ```

---

## Installation:

...
