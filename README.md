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

#### Rausch-/Audiostücke numerisch laden :

```python
from sample.load_data import add_noise_to_audio
from sample.helpers import get_numpy_data
from sample.constants import DATA_PROCESSED, NOISE_PROCESSED

# 5 second chunks
noise_numpy = get_numpy_data(NOISE_PROCESSED)
audio_numpy = get_numpy_data(DATA_PROCESSED)
```

#### Einem Audiosignal additiv Rauschsignale hinzufügen:
```python

# 3D-Matrix o Tensor
input_data = numericalData(audio_numpy,noise_numpy)
```

#### Transformaieren der Daten mit Librosa:
```python
import librosa as lr

D = lr.amplitude_to_db(np.abs(lr.stft(input_data[6,6])), ref=np.max)
img = lr.display.specshow(D,y_axis="log", x_axis="time",sr=16000,ax=ax[0])
plt.sca(ax[0])
plt.yticks(size=15)
plt.xticks(size=15)
plt.xlabel("Time",size=15)
plt.ylabel("Hz",size=15)
plt.title("Data[6,6]",size=18)

D_a = lr.amplitude_to_db(np.abs(lr.stft(input_data[1,10])), ref=np.max)
img_2 = lr.display.specshow(D_a,y_axis="log", x_axis="time",sr=16000,ax=ax[1])
plt.sca(ax[1])
plt.xticks(size=15)
plt.yticks(size=15)
ax[1].set_yticklabels([])
ax[1].set_ylabel(None)
plt.xlabel("Time",size=15)
plt.title("Data[1,10]",size=18)

# colorbar
cb = fig.colorbar(img,ax=ax,format="%+2.f dB")
for t in cb.ax.get_yticklabels():
    t.set_fontsize(15)
```

* __Implementierte Funktionalitäten siehe [hier](noise_data/README.md)__.

---
