import os
import h5py
from main.constants import *
from main.helpers import get_numpy_data
from main.manipulate_data import add_noise_to_audio


def write_txt_file():
    """ Creates a text file, that will be used to create and
    access groups of an HDF5 File. Writes all possible links
    of audio and noise recording chunks.
    """

    file = open("../noisy-chunks.txt", "w")

    for audio in os.listdir(DATA_PROCESSED):
        for noise in os.listdir(NOISE_PROCESSED):
            file.write(
                audio.replace(".wav", "") +
                noise.replace(".wav", "") +
                "\n")
    file.close()


def create_h5py_file():
    """ Creates a HDF5 File with all desired groups. """

    # a = Read/write if exists, create otherwise
    file = h5py.File("../numerical-data.hdf5", "a")

    data_groups = ["audio", "noise"]
    db_groups = ["10", "15", "20"]

    for subgroup in data_groups:
        file.create_group("raw/" + subgroup)
        file.create_group("chunks/" + subgroup)

    for group in db_groups:
        for subgroup in open("../noisy-chunks.txt"):
            file.create_group("noisy-chunks/" +
                              group + "/" +
                              subgroup.replace("\n", ""))


def write_h5py_file(h5py_file):
    file = h5py_file(h5py_file)
