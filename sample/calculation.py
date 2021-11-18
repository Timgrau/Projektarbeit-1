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
    power_s = np.sum(clean_audio ** 2)
    power_n = np.sum(noise ** 2)
    return clean_audio + np.sqrt(power_s / power_n) * noise


def get_constant(signal, noise, SNR):
    """
    Calculates a constant factor to get 0dB SNR noise
    and mean power of the noise.
    That factor can be multiplied with the noise array.

    :param clean_audio:
    :param noise:
    :return:
    """
    RMS_s = np.sqrt(np.abs(np.mean(signal ** 2)))
    # required RMS of noise
    RMS_n = np.sqrt(RMS_s ** 2 / (pow(10, SNR / 10)))

    # current RMS of noise
    RMS_n_current = np.sqrt(np.abs(np.mean(noise ** 2)))
    return RMS_n / RMS_n_current


def get_noisy_sound(signal, noise, SNR):
    RMS_s = np.sqrt(np.mean((signal ** 2)))
    # required RMS of noise
    RMS_n = np.sqrt(RMS_s ** 2 / (pow(10, SNR / 10)))

    # current RMS of noise
    RMS_n_current = np.sqrt(np.mean(noise ** 2))
    return signal + noise * (RMS_n / RMS_n_current)
