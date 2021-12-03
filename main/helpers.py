import librosa.effects
from main.constants import *
import librosa as lr
import os
import shutil
import numpy as np


class Helper:
    def __init__(self, path, sample_rate=SAMPLE_RATE):
        """Constructor of the Class Helper

        :param path: Path where the data is stored (str)
        :param sample_rate: sample rate you want to resample (int)"""

        if os.path.exists(path):
            self.path = path
        else:
            raise NotADirectoryError(
                "Object can not be created because the"
                " directory %s does not exist" % path)
        self.sample_rate = sample_rate

    def get_all_sample_rates(self):
        """Iterates through the passed path that contains
        the audio files, and returns an array with all existing
        main rates."""

        ret = []
        for files in os.listdir(self.path):
            ret.append(lr.get_samplerate(self.path + files))
        return ret

    def get_duration(self):
        """Iterates over all audio files in the passed path
        and returns their duration."""

        ret = []

        for file in os.listdir(self.path):
            ret.append(lr.get_duration(filename=self.path + file))
        return ret

    def get_numpy_data(self):
        """Iterates through the passed path and loads
        all containing audio files in as a numerical array in
        a matrix.

        :return: numerical matrix (numpy)"""

        ret = []

        for files in os.listdir(self.path):
            data, _ = librosa.load(self.path + files, sr=self.sample_rate, mono=True)
            ret.append(data)
        return np.array(ret)


class Copier:
    def __init__(self, path, save_path):
        """Constructor of the Class Helper

        :param path: Path where the data you want to copy is stored (str)
        :param save_path: Path you want to store your copied data (str)"""

        stored = os.path.exists(path)
        save = os.path.exists(save_path)

        if stored and save:
            self.path = path
            self.save_path = save_path
        else:
            if not stored:
                raise NotADirectoryError(
                    "Object can not be created, because directory %s "
                    "does not exist" % path)
            if not save:
                raise NotADirectoryError(
                    "Object can not be created, because directory %s "
                    "does not exist" % save_path)

    def copy_data(self):
        """Copy files from one directory into another.
        Function will be used for resampling data."""

        for files in os.listdir(self.path):
            shutil.copy(self.path + files, self.save_path + files)


class Zipper:
    def __init__(self):
        def unzip(*args):
            return
