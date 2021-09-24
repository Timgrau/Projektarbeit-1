import settings as st
import librosa as lr
import os
import glob


def getAllSampleRates(mainPath):
    """Returns the sample rate of all providing noise data

    TODO: @test -> test for path that has no data or wrong file
    :param mainPath:
    :return:
    """
    for files in os.listdir(mainPath):
        print(lr.get_samplerate(mainPath + files))


def getSampleRates(path, type):
    """Returns the sample rate of the selected type of noise data

    :param path: Following types available `{NOISE.RAW, NOISE.PRO}`
    :param type: Following types available see `st.NOISE_TYPES`
    :return: array of sample rates
    TODO: Doc
    """
    ret = []
    if type in st.NOISE_TYPES:
        for file in glob.glob(path + type + "_?" + st.AUDIOFORMAT):
            ret.append(lr.get_samplerate(file))
        return ret
    else:
        raise KeyError("Type not found in noise-data")


def getSampleRate(dataPath):
    return lr.get_samplerate(dataPath)


data = getSampleRates(st.NOISE_RAW, st.NOISE_TYPES[0])
print(data)