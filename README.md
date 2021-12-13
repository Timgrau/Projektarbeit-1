# Projektarbeit 1 (Audio Preprocessing)

Dieses Projekt wird im Rahmen der Projektarbeit 1 erstellt und soll zur Unterstützung der Projektarbeit 2 dienen. Indem
Funktionalitäten angeboten werden, um additiv Störgeräusche einem Audiodatensatz hinzuzufügen und diese zu so zu Augmentieren.
[Präsentation](https://git.ikt.fh-dortmund.de:3000/tigra005/Ausarbeitung-PA1/src/branch/master/abgabe_PA1/slides.pdf) und [Ausarbeitung](https://git.ikt.fh-dortmund.de:3000/tigra005/Ausarbeitung-PA1/src/branch/master/abgabe_PA1/ausarbeitung.pdf)

## [Störgeräusche](noise_data/README.md):

* Klimaanlage
* Straße
* Staubsauger
* Spülmaschine

---

## Funktionalität:
#### Resample and slice data into 16KHz and 3 sec Duration:
```python
# Import the Manipulator
from main.manipulate_data import Manipulator

# choose wisely
path = "/raw/data/stored/"
save_path = "/store/clean/data/"

# Create Manipulator object
manipulator = Manipulator(path, save_path, sample_rate=16000, duration=3000)

# resamples the data and overwrites the old ones
manipulator.resample_data()

# Slices the files into chunks and store them in save_path
manipulator.slice_audio()   # path -> save_path

# manipulator can copy data through the dirs
manipulator.copy_data()

# TODO: Create a pipeline and stream data into the pipeline
# TODO: Implement automated denoising for the pipeline
```
#### Audiodaten augmentieren:
```python
# Import the Augmenter object
from main.manipulate_data import Augmenter
from main.helpers import Helper

# First we need numerically audio chunks
path_noise = "/noise/chunks/"
path_audio = "/audio/chunks/"

noise_matrix = Helper(path_noise).get_numpy_data()
audio_matrix = Helper(path_audio).get_numpy_data()

# create Augmenter object
augmenter = Augmenter(audio_matrix, 
                      noise_matrix, 
                      signal_to_noise_ratio=10)

# Augment the data
input_data_noisy = augmenter.get_noise_input()
input_data_clean = augmenter.get_clean_input()

# Could be used to fit a function e.g.
neuralnetwork.fit(input_data_clean, input_data_noisy, epochs=...)

```
#### HDF5-File
You can create your own [HDF5-File](https://www.h5py.org/) or use the [created one](numerical-data.hdf5) containing some prepared audio and
noisy audio spectrogram. Can be pretty handy for an HPC or distributed model learning or just to be portable.


with the groups and datasets: 
* `"chunks/noise"`
* `"chunks/audio"`

Different SNR dB Data should be available:
* `"noisy_chunks/0/"` 
* `"noisy_chunks/5/"`
* `"noisy_chunks/10/"`


```python
from main.write_data import HDF5File

file = "example-file.hdf5"

# create a HDF5-file
h5file = HDF5File(file)
h5file.create()

# write data into the file
h5file.write(audio_matrix, noisy_matrix, 10)

# Writes audio_matrix into file["chunks/audio/"] 
# and noisy_matrix into file[noisy_chunks/10/"]
```
Access the data of the given HDF5-File
```python
import h5py

file = h5py.File("numerical-data.hdf5")

input_data_clean = file["chunks/audio"][:]
input_noisy_10 = file["noisy_chunks/10"][:]
```
* __Implementierte Funktionalitäten siehe [hier](noise_data/README.md)__.

---
