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
    """ Creates a HDF5 File with all desired groups and attributes. """

    # a => Read/write if exists, create otherwise
    file = h5py.File("../numerical-data.hdf5", "a")

    # main groups / sub groups
    noise_chunks = file.create_group("chunks/noise")
    audio_chunks = file.create_group("chunks/audio")
    noisy_chunks = file.create_group("noisy_chunks")

    # sub groups
    db_groups = ["10", "15", "20"]

    attributes = {
        "sample_rate": SAMPLE_RATE,
        "duration": DURATION,
        "domain": "spectrogram"
    }

    for data in os.listdir(DATA_PROCESSED):
        audio_chunks.create_group(data.replace(".wav", ""))

    for noise in os.listdir(NOISE_PROCESSED):
        noise_chunks.create_group(noise.replace(".wav", ""))

    for group in db_groups:
        for subgroup in open("../noisy-chunks.txt"):
            noisy_chunks.create_group(group + "/" +
                                      subgroup.replace("\n", ""))

    for attr, val in attributes.items():
        noisy_chunks.attrs[attr] = val
        file["chunks"].attrs[attr] = val


def write_h5py_file(h5py_file="../numerical-data.hdf5"):
    """

    :param h5py_file:
    :return:
    """

    # r+ => Read/write, file must exist
    file = h5py.File(h5py_file, "r+")


