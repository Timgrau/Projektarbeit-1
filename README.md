# Projektarbeit 1 (Audio Preprocessing)

Dieses Package wird im Rahmen der Projektarbeit 1 erstellt und soll zur Unterstützung der Projektarbeit 2 dienen. Indem
Funktionalitäten angeboten werden, um additiv Störgeräusche einem Audiodatensatz hinzuzufügen und diese zu
Visualisieren. [Präsentation](https://git.ikt.fh-dortmund.de:3000/tigra005/Ausarbeitung-PA1/src/branch/master/abgabe_PA1/slides.pdf) und [Ausarbeitung](https://git.ikt.fh-dortmund.de:3000/tigra005/Ausarbeitung-PA1/src/branch/master/abgabe_PA1/ausarbeitung.pdf)

## [Störgeräusche](noise_data/README.md):

* Klimaanlage
* Straße
* Staubsauger
* Spülmaschine

---

## Funktionalität:

#### Rausch-/Audiostücke numerisch laden:

```python
from main.manipulate_data import add_noise_to_audio
from main.helpers import get_numpy_data
from main.constants import DATA_PROCESSED, NOISE_PROCESSED

# 5 second chunks
noise_numpy = get_numpy_data(NOISE_PROCESSED)
audio_numpy = get_numpy_data(DATA_PROCESSED)
```

#### Einem Audiosignal additiv Rauschsignale hinzufügen:
```python

# 3D-Matrix o Tensor
input_data = add_noise_to_audio(audio_numpy,noise_numpy)
```

#### Transformaieren der Daten mit Librosa:
```python
import librosa as lr
import numpy as np

S = np.abs(lr.stft(input_data[1,1]))
```

* __Implementierte Funktionalitäten siehe [hier](noise_data/README.md)__.

---
