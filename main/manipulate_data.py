from main.helpers import Copier
from main.calculation import get_noisy_sound
from main.constants import *
import librosa as lr
import os
import soundfile
from pydub import AudioSegment
import numpy as np


class Manipulator(Copier):
    """ Manipulator Class inherit from Copier """

    def __init__(self, path, save_path, sample_rate=SAMPLE_RATE, duration=DURATION):
        """ Constructor of the Manipulator calls the constructor of the subclass.

        :param path: Path to the data (str)
        :param save_path: Path you want to store your manipulated data (str)
        :param duration: Duration of a piece in milliseconds (int)
        """
        super().__init__(path, save_path)
        self.duration = duration
        self.sample_rate = sample_rate

    def resample_data(self):
        """ Takes all the audio files in the passed path resamples
        them to an constant main rate and stores them in save_path.
        """

        i = 0
        for files in os.listdir(self.path):
            data, _ = lr.load(self.path + files, sr=self.sample_rate, mono=True)
            soundfile.write(self.path + files, data, self.sample_rate)
            i += 1

        print("%s files from %s resampled to %s Hz and written into %s" % (
            i, self.path, self.sample_rate, self.path))

    def slice_audio(self):
        """ Cut audio files into pieces with same duration and save the pieces
        in save_path as a .wav file. Uses AudioSegment from pydub, which uses ffmpeg.
        """

        for file in os.listdir(self.path):
            data = AudioSegment.from_file(self.path + file)

            # Cut first 13 sec and last 5 sec from use_data, cause it does not contain realistic information
            if "usage" in file:
                data = data[13000:len(data)-5000]

            # Iterate over every first 5 seconds of the signal with chunk
            for i, chunk in enumerate(data[::self.duration]):
                if len(chunk) == self.duration:
                    with open(self.save_path + file.replace(AUDIOFORMAT, "") + "_%s" % i + ".wav", "wb") as f:
                        chunk.export(f, format="wav")
                else:
                    print("%s got sliced into %s pieces and exported" % (file, i))
                    print("Duration of last chunk is %s sec file will be ignored" % (len(chunk) / 1000))
                    print("-" * 60)


class Augmenter:
    """Class to create Inputs for a Loss-function or a NN"""

    def __init__(self, audio_matrix, noise_matrix, signal_to_noise_ratio=10):
        """Constructor of the Augmenter
        :param audio_matrix: matrix containing audio signal each row (fixed length)
        :param noise_matrix: matrix containing noise signal each row (fixed length)
        :param signal_to_noise_ratio: desired SNR dB (integer)"""

        self.audio_matrix = audio_matrix
        self.noise_matrix = noise_matrix
        self.signal_to_noise_ratio = signal_to_noise_ratio

    def get_noise_input(self, n_fft=510, win_length=510, hop_length=376):
        """Adds every single noise signal (row) from the noise_matrix to every single
        audio signal (row) from the audio_matrix for a desired signal to noise ratio.
        Returns a 3D-Matrix

        :return: Noisy input data (Tensor)"""

        ret = []

        for i in self.audio_matrix:
            for j in self.noise_matrix:
                noisy_chunk = get_noisy_sound(i, j, self.signal_to_noise_ratio)
                # lr.amplitude_to_db(np.abs())
                ret.append(lr.stft(noisy_chunk, n_fft=n_fft,
                                   win_length=win_length,
                                   hop_length=hop_length))
        return np.array(ret)

    def get_clean_input(self, n_fft=510, win_length=510, hop_length=376):
        """Returns the clean spectrogram output of the audio chunks.
        Each chunk will be contained 100 times in the matrix, could
        be used for the Loss function of a NN.

        :return: Clean input data (Tensor)"""

        ret = []

        for i in self.audio_matrix:
            # lr.amplitude_to_db(np.abs())
            spec = lr.stft(i, n_fft=n_fft,
                           win_length=win_length,
                           hop_length=hop_length)
            for j in range(0, len(self.noise_matrix)):
                ret.append(spec)
        return np.array(ret)
