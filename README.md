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

#### Rauschen numerisch laden ```len(type)```x5*22050 :
```python
from sample import loadData

noise_type = loadData.processedNoise(type)
audio = loadData.processedData()
# type := {aircon, dishwasher, vacuuming, street, washer} {type == None -> all}
```

#### Einem Audiosignal additiv ein Störgeräusch hinzufügen:
 ```python
path = "path/to/audiofile.wav" # sampled in 22KHz
data = load(path)
noisyData = helpers.addNoise(data, noise_type)
```

#### Verrauschtes Signal darstellen:
```python
specData = package.calcSpec(noisyData)
mfccData = package.calcMfcc(noisyData)
...
```

* __Implementierte Funktionalitäten siehe [hier](noise_data/README.md)__.

---

## Usage/Import:

```python
from sample import loadData, helpers
```
