import librosa.effects
from sample.constants import *
import librosa as lr
import os
import glob
import shutil
import numpy as np


def get_all_sample_rates(path):
    """ Iterates through the passed path that contains
    the audio files, and returns an array with all existing
    sample rates.

    :param path: path to the audio files (str)
    :return: sample rates (array)
    """

    ret = []

    for files in os.listdir(path):
        ret.append(lr.get_samplerate(path + files))
    return ret


def get_specific_sample_rates(path, signal_type):
    """ Checks if the passed signal_type exists in
    the passed path, if so, iterates through this path
    and return all existing sample rates for the audio files
    that starts with this specific signal_type.

    e.g.
    path = "<path>/noise_data/processed/"
    signal_type = "dishwasher"

    Returns all "dishwasher_<number>_<number>.wav"
    in "<path>/noise_data/processed/"

    :param path: path to the audio files (str)
    :param signal_type: starting name of the audio signals (str) e.g. ("aircon", "dishwasher", "street", "vacuuming")
    :return: sample rates (array)
    """

    ret = []

    if signal_type in NOISE_TYPES:
        for file in glob.glob(path + signal_type + "_?_?" + AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
    elif signal_type == "usage":
        for file in glob.glob(path + signal_type + "_?_?" + AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
    else:
        raise KeyError("Type not found in %s" % path)
    return ret


def get_duration(path):
    """ Iterates over all audio files in the passed path
    and returns their duration.

    :param path: path to the audio files (str)
    :return: duration time in seconds (array)
    """

    ret = []

    for file in os.listdir(path):
        ret.append(lr.get_duration(filename=path + file))
    return ret


def copy_data(path, save_path):
    """ Copy files from one directory into another.
    Function will be used for resampling data.

    :param path: Path where the data you want to copy is stored (str)
    :param save_path: Path you want to store your copied data (str)
    :raise FileNotFound if one path or both does not exist
    """

    stored = os.path.exists(path)
    safe = os.path.exists(save_path)

    if stored and safe:
        for files in os.listdir(path):
            shutil.copy(path + files, save_path + files)
    else:
        if not stored:
            raise FileNotFoundError("Directory: %s does not exist" % path)
        if not safe:
            raise FileNotFoundError("Directory: %s does not exist" % save_path)


def get_numpy_data(path):
    """ Iterates through the passed path and loads
    all containing audio files in as a numerical array in
    a matrix.

    :param path: path to the audio files (str)
    :return: numerical matrix (numpy)
    """

    ret = []

    for files in os.listdir(path):
        data, _ = librosa.load(path + files, sr=SAMPLE_RATE, mono=True)
        ret.append(data)
    return np.array(ret)
