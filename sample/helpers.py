from sample.constants import *
import librosa as lr
import os
import glob
import shutil


def getAllSampleRates(mainPath):
    """Returns the sample rate of all providing noise_data data

    TODO: @test -> test for path that has no data or wrong file
    :param mainPath:
    :return:
    """
    ret = []
    for files in os.listdir(mainPath):
        ret.append(lr.get_samplerate(mainPath + files))
    return ret


def getSampleRates(path, type):
    """Returns the sample rate of the selected type of noise_data data
    TODO: doc for availabe types

    :param path: Following types available: `NOISE_RAW`, `NOISE_PRO`
    :param type: Following types available: `NOISE_TYPES`
    :return: array of sample rates
    """
    ret = []
    if type in NOISE_TYPES:
        for file in glob.glob(path + type + "_?" + AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
        return ret
    else:
        raise KeyError("Type not found in %s" % path)


def getDuration(mainPath):
    ret = []
    for files in os.listdir(mainPath):
        ret.append(lr.get_duration(filename=mainPath + files))
        print(files)
    return ret


def copyRawData(safePath):
    """
    Function will be called in function resampledNoise to copy noise_data/raw/*.wav
    Do not abuse this function !!
    TODO: Function can just be called in loadData.resampledNoise()
    :param safePath:
    :return:
    """
    if os.path.exists(safePath):
        for files in os.listdir(NOISE_RAW):
            shutil.copy(NOISE_RAW + files, safePath + files)
    else:
        raise FileNotFoundError("No such directory: %s" % safePath)


def copyUseData(safePath):
    """ Function will be called in function resampledNoise to copy use_data/raw/*.wav
    Do not abuse this function !!
    TODO: Function can just be called in loadData.resampledData()
    :param safePath:
    :return:
    """
    if os.path.exists(safePath):
        for files in os.listdir(DATA_RAW):
            shutil.copy(DATA_RAW + files, safePath + files)
    else:
        raise FileNotFoundError("No such directory: %s" % safePath)
