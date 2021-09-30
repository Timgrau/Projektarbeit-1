import numpy as np

"""
Class for doing mathematical calculations
"""


def calcRMS(dataArray):
    """ Calculates the Root means square of input Data

    :param dataArray: numerical data
    :return: RMS of data (float)
    """
    return np.sqrt(np.mean(dataArray ** 2))


def calcSNR(RMS_u, RMS_n):
    """ Calculates the Signal to noise ratio

    :param RMS_u: RMS of use_data
    :param RMS_n: RMS of nosie_data
    :return:
    """
    return 10 * np.log10((RMS_u ** 2 / RMS_n ** 2))

