import numpy as np

from sample.helpers import *
from sample.calculation import *
import os
import soundfile
from pydub import AudioSegment


def resampledData(path, savePath):
    """
    Takes all the audio files in {path} and resamples them into {savePath}.
    Sample rate can be changed in module constant.py @ {SAMPLE_RATE}.

    :param path: Path where the files you want to resample are stored
    :param savePath: Path where you want to store the resampled files
    :return:
    """
    copyData(path, savePath)
    i = 0
    for files in os.listdir(savePath):
        data, sr = lr.load(savePath + files, sr=SAMPLE_RATE, mono=True)
        soundfile.write(savePath + files, data, SAMPLE_RATE)
        i += 1
    print("%s files from %s resampled to %s Hz and copied into %s" % (i, path, SAMPLE_RATE, savePath))


def sliceAudio(path, savePath, duration=DURATION):
    """
    Cut data into pieces with same duration, uses ffpmeg.

    :param savePath: path your sliced files should to be stored
    :param path: Path the audio files you want to slice are stored
    :param duration: Duration of piece can be changed in module constants.py @ {DURATION}
    :return:
    """
    for file in os.listdir(path):
        data = AudioSegment.from_file(path + file)
        # Cut first 8 sec from use_data, cuz it does mot contain realistic information
        if path == DATA_RAW or path == DATA_RESAMPLED:
            data = data[8000:]
        for i, chunk in enumerate(data[::DURATION]):
            if len(chunk) == DURATION:
                with open(savePath + file.replace(AUDIOFORMAT, "") + "_%s" % i + ".wav", "wb") as f:
                    chunk.export(f, format="wav")
            else:
                print("%s got sliced into %s pieces and exported" % (file, i + 1))
                print("Duration of last chunk is %s sec file will be ignored" % (len(chunk) / 1000))
                print("-" * 60)


def numericalData(audio_matrix, noise_matrix):
    """
    Should provide a matrix maybe (tensors) with the real input data (added noise).
    :param audio_matrix:
    :param noise_matrix:
    :return:
    """
    ret = []
    for i in audio_matrix:
        for j in noise_matrix:
            ret.append(get_noisy_sound(i, j, 10))
    return np.array(ret).reshape((72, 100, 80000))
