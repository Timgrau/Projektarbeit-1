from sample.helpers import *
import os
import soundfile
from pydub import AudioSegment

def resampledNoise(safePath):
    """
    Function to safe resampled noise_data to 16KHz
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
    """
    Function to safe resampled use_data to 16KHz
    :param safePath: Path you want your data to be stored
    :return: None
    """
    copyUseData(safePath)
    i = 0
    for files in os.listdir(safePath):
        data, sr = soundfile.read(safePath + files)
        soundfile.write(safePath + files, data, SAMPLE_RATE)
        i += 1
    print("%s data files from %s copied and resampled to %s Hz" % (i, DATA_LENGTH, SAMPLE_RATE))


def sliceRawData(safePath, path=DATA_RAW, duration=DURATION):
    """ Test
    :param safePath: path your sliced data to be stored
    :param path: Path the audio you want to be sliced is stored
    :param duration: Duration of chunk's can be changed in constants : `DURATION`
    :return:
    """
    for file in os.listdir(path):
        data = AudioSegment.from_file(path + file)
        for i, chunk in enumerate(data[::DURATION]):
            if len(chunk) == DURATION:
                with open(safePath + file.replace(AUDIOFORMAT, "") + "_%s" % i + ".wav", "wb") as f:
                    chunk.export(f, format="wav")
            else:
                print("Duration of last chunk is %s sec file will be ignored" % (len(chunk) / 1000))
