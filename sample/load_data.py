import numpy as np
from sample.helpers import *
from sample.calculation import *
import os
import soundfile
from pydub import AudioSegment


def resampled_data(path, save_path, sample_rate=SAMPLE_RATE):
    """ Takes all the audio files in the passed path resamples
    them to an constant sample rate and stores them in save_path.

    :param path: Path to the audio files (str)
    :param save_path: Path you want to store your copied data (str)
    :param sample_rate: sample rate you want to resample (int)
    """

    copy_data(path, save_path)

    i = 0
    for files in os.listdir(save_path):
        data, _ = lr.load(save_path + files, sr=sample_rate, mono=True)
        soundfile.write(save_path + files, data, sample_rate)
        i += 1

    print("%s files from %s resampled to %s Hz and copied into %s" % (i, path, sample_rate, save_path))


def slice_audio(path, save_path, duration=DURATION):
    """ Cut audio files into pieces with same duration and save the pieces
    in save_path as a .wav file. Uses AudioSegment from pydub, which uses ffmpeg.

    :param path: Path the audio files you want to slice are stored (str)
    :param save_path: Path you want to store your sliced data (str)
    :param duration: Duration of a piece in milliseconds (int)
    """

    for file in os.listdir(path):
        data = AudioSegment.from_file(path + file)

        # Cut first 8 sec from use_data, cause it does not contain realistic information
        if path == DATA_RAW or path == DATA_RESAMPLED:
            data = data[8000:]

        # Iterate over every first 5 seconds of the signal with chunk
        for i, chunk in enumerate(data[::duration]):
            if len(chunk) == duration:
                with open(save_path + file.replace(AUDIOFORMAT, "") + "_%s" % i + ".wav", "wb") as f:
                    chunk.export(f, format="wav")
            else:
                print("%s got sliced into %s pieces and exported" % (file, i + 1))
                print("Duration of last chunk is %s sec file will be ignored" % (len(chunk) / 1000))
                print("-" * 60)


def add_noise_to_audio(audio_matrix, noise_matrix, signal_to_noise_ratio=10):
    """ Adds every single noise signal (row) from the noise_matrix to every single
    audio signal (row) from the audio_matrix for a desired signal to noise ratio.
    Returns a 3D-Matrix

    :param audio_matrix: matrix containing a discrete audio signal ech row
    :param noise_matrix: matrix containing a discrete noise signal ech row
    :param signal_to_noise_ratio: desired SNR dB (integer)
    :return: 3D-Matrix or Tensor
    """

    ret = []
    shape_audio = audio_matrix.shape[0]
    shape_noise = noise_matrix.shape[0]
    shape_samples = DURATION*SAMPLE_RATE

    for i in audio_matrix:
        for j in noise_matrix:
            ret.append(get_noisy_sound(i, j, signal_to_noise_ratio))
    return np.array(ret).reshape((shape_audio, shape_noise, shape_samples))
