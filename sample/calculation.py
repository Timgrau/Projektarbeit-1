import numpy as np


def meanPower(dataArray):
    """ Calculates the mean power of a signal

    :param dataArray: numerical data
    :return: mean power of data (float)
    """
    return np.mean(np.abs(dataArray) ** 2)


def snr(power_signal, power_noise):
    """ Calculates the signal to noise ratio

    :param power_signal: mean power of signal
    :param power_noise: mean power of noise
    :return: logarithmic snr (float)
    """
    return 10 * np.log10((power_signal / power_noise))


def add_noise_zero_db(clean_audio, noise):
    """
    Add's noise to an clean audio clip (denoised).
    With an signal to noise ration = 0 dB

    :param clean_audio: denoised audio array
    :param noise: stationary noise array
    :return: noisy signal (numpy array)
    """
    power_s = np.sum(clean_audio**2)
    power_n = np.sum(noise**2)
    return clean_audio + np.sqrt(power_s / power_n) * noise

def get_constant(clean_audio, noise):
    """
    Calculates a constant factor to get 0dB SNR noise
    and mean power of the noise.
    That factor can be multiplied with the noise array.

    :param clean_audio:
    :param noise:
    :return:
    """
    power_s = np.sum(clean_audio**2)
    power_n = np.sum(noise**2)
    return np.sqrt(power_s / power_n)
