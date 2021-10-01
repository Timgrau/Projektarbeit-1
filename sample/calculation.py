import numpy as np


def meanPower(dataArray):
    """ Calculates the mean power of a signal

    :param dataArray: numerical data
    :return: mean power of data (float)
    """
    return np.mean(np.abs(dataArray)**2)

def snr(power_signal, power_noise):
    """ Calculates the signal to noise ratio

    :param power_signal: mean power of signal
    :param power_noise: mean power of noise
    :return: logarithmic snr (float)
    """
    return 10 * np.log10((power_signal / power_noise))

def constant(power_signal, power_noise, snr):
    """
    Calculates a constant factor based on wanted signal to noise ratio
    and mean power of the noise.
    That factor can be multiplied with the noise array.

    :param power_signal:
    :param power_noise:
    :param snr:
    :return:
    """
    power_required = power_signal*np.power(10, -snr/10)
    return power_noise / power_required