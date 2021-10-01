from sample.constants import *
import librosa as lr
import os
import glob
import shutil


def getAllSampleRates(mainPath):
    """ Returns the sample rate of all providing noise_data data
    :param mainPath:
    :return: Array of sample rates
    """
    ret = []
    for files in os.listdir(mainPath):
        ret.append(lr.get_samplerate(mainPath + files))
    return ret


def getSampleRates(path, type):
    """
    Returns the sample rate of the selected type in given directory/path.
    TODO: docs with example
    :param path: path your audio files are stored
    :param type: name of your starting string
    :return: array of sample rates
    """
    ret = []
    if type in NOISE_TYPES:
        for file in glob.glob(path + type + "_?_?" + AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
    elif type == "usage":
        for file in glob.glob(path + type + "_?_?" + AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
    else:
        raise KeyError("Type not found in %s" % path)
    return ret

def getDuration(mainPath):
    ret = []
    for file in os.listdir(mainPath):
        ret.append(lr.get_duration(filename=mainPath + file))
    return ret

def copyData(path, savePath):
    """
    Copy files from one directory into another.
    Function will be used for resampling data.
    :param path: Path where the data you want to copy is stored
    :param savePath: Path you want to store your copied data
    :return:
    """
    stored = os.path.exists(path)
    safe = os.path.exists(savePath)

    if stored and safe:
        for files in os.listdir(path):
            shutil.copy(path + files, savePath + files)
    else:
        if not stored:
            raise FileNotFoundError("Directory: %s does not exist" % path)
        if not safe:
            raise FileNotFoundError("Directory: %s does not exist" % savePath)

#def concatenateData():
