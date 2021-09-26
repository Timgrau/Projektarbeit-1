from sample.helpers import *
import os
import soundfile


def resampledNoise(safePath):
    """
    Function to safe resampled noise Data to 16KHz
    :param safePath: Path you want your data to be stored
    :return: None
    """
    copyRawData(safePath)
    i = 0
    for files in os.listdir(safePath):
        data, sr = soundfile.read(safePath + files)
        soundfile.write(safePath + files, data, SAMPLE_RATE)
        i += 1
    print("%s noise files from %s copied and resampled to %s Hz" % (i, NOISE_LENGTH, SAMPLE_RATE))


def resampledData(safePath):
    copyUseData(safePath)
    i = 0
    for files in os.listdir(safePath):
        data, sr = soundfile.read(safePath + files)
        soundfile.write(safePath + files, data, SAMPLE_RATE)
        i += 1
    print("%s data files from %s copied and resampled to %s Hz" % (i, DATA_LENGTH, SAMPLE_RATE))
