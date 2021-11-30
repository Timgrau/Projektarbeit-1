import os
import h5py
from main.constants import *


def write_txt_file():
    """Creates a text file, that will be used to create and
    access groups of an HDF5 File. Writes all possible links
    of audio and noise recording chunks."""

    file = open("../noisy-chunks.txt", "w")

    for audio in os.listdir(DATA_PROCESSED):
        for noise in os.listdir(NOISE_PROCESSED):
            file.write(
                audio.replace(".wav", "") +
                noise.replace(".wav", "") +
                "\n")
    file.close()


class HDF5File:
    def __init__(self, file_path):
        """Constructor of the Class HDF5File

        :param file_path: Path and filename (str)"""
        self.file_path = file_path
        self.db_groups = ["10", "15", "20"]
        self.chunk_groups = ["noise", "audio"]

    def create(self):
        """Creates a HDF5 File with all desired groups and attributes."""

        # a => Read/write if exists, create otherwise
        file = h5py.File(self.file_path, "a")

        # main groups / sub groups
        chunks_grp = file.create_group("chunks")
        noisy_chunks_grp = file.create_group("noisy_chunks")

        attributes = {
            "sample_rate": SAMPLE_RATE,
            "duration": DURATION,
            "domain": "spectrogram"
        }

        for attr, val in attributes.items():
            noisy_chunks_grp.attrs[attr] = val
            chunks_grp.attrs[attr] = val

    def write(self, audio_matrix, noisy_matrix, db_snr):
        """Creates datasets in the created HDF5 file and
        writes numerical audio content into the file.

        :param audio_matrix: numerical matrix (clean)
        :param noisy_matrix: numerical matrix (noisy)
        :param db_snr: signal to noise ration in dB (int)
        :return:"""

        # r+ => Read/write, file must exist
        file = h5py.File(self.file_path, "r+")

        if str(db_snr) in self.db_groups:
            file["noisy_chunks"].create_dataset(
                str(db_snr),
                data=noisy_matrix)
        else:
            raise KeyError("{} dB not found in db_groups".format(db_snr))

        # write audio chunks into the file
        file["chunks"].create_dataset(
            self.chunk_groups[1],
            data=audio_matrix)
