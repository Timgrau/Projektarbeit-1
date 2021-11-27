import numpy as np


def mean_power(data_array):
    """ Calculates the mean power of a signal

    :param data_array: numerical discrete signal (numpy array)
    :return: mean power of signal
    """

    return np.mean(np.abs(data_array) ** 2)


def snr(power_signal, power_noise):
    """ Calculates the signal to noise ratio

    :param power_signal: mean power of signal (float)
    :param power_noise: mean power of noise (float)
    :return: logarithmic snr (float)
    """

    return 10 * np.log10((power_signal / power_noise))


def get_constant(signal, noise, signal_to_noise_ratio):
    """ Calculates a constant factor for a given signal and noise
    audio clip for a desired signal to noise ratio. That constant
    factor can be multiplied with the noise signal to obtain the
    desired SNR with regards to the signal.

    :param signal: numerical discrete signal (numpy array)
    :param noise: numerical discrete noise signal (numpy array)
    :param signal_to_noise_ratio: desired SNR (integer) dB
    :return: constant factor (float)
    """

    rms_signal = np.sqrt(np.abs(np.mean(signal ** 2)))

    # required RMS of noise
    rms_noise = np.sqrt(rms_signal ** 2 / (pow(10, signal_to_noise_ratio / 10)))

    # current RMS of noise
    rms_noise_current = np.sqrt(np.abs(np.mean(noise ** 2)))

    return rms_noise / rms_noise_current


def get_noisy_sound(signal, noise, signal_to_noise_ratio):
    """ Adds the passed noise to the passed signal for the
    desired signal to noise ratio.

    :param signal: numerical discrete signal (numpy array)
    :param noise: numerical discrete noise signal (numpy array)
    :param signal_to_noise_ratio: constant factor (float)
    :return: noisy signal with desired signal to noise ratio (array)
    """

    constant_factor = get_constant(signal, noise, signal_to_noise_ratio)

    return signal + noise * constant_factor
