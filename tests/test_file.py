import unittest
import warnings
from main.manipulate_data import Manipulator, Augmenter
from main import calculation
from main.helpers import Helper, Copier
from main.write_data import HDF5File
from tests.test_paths import *
import librosa as lr
import os


class Clean:
    def __init__(self):
        self.dir = TEST_DIR

    def clean_dir(self):
        for file in os.listdir(self.dir):
            if file.endswith(".wav") or file.endswith(".hdf5"):
                os.remove(os.path.join(self.dir, file))


##### Unit Tests #####
class Test(unittest.TestCase):
    helper = Helper(TEST_DIR)
    cleaner = Clean()

    def test_down_sample(self):
        Manipulator(DATA_RAW, TEST_DIR).copy_data()

        manipulator_data = Manipulator(TEST_DIR, TEST_DIR)
        manipulator_data.resample_data()

        for i in Test.helper.get_all_sample_rates():
            self.assertEqual(i, 16000)

    def test_wrong_path(self):
        wrong_dir = "/home/unit"

        self.assertRaises(NotADirectoryError, lambda: Helper(wrong_dir))
        self.assertRaises(NotADirectoryError, lambda: Copier(wrong_dir, wrong_dir))
        self.assertRaises(NotADirectoryError, lambda: Manipulator(wrong_dir, wrong_dir))

    def test_slice_data(self):
        # Warning for older ffmpeg versions
        warnings.simplefilter("ignore", ResourceWarning)

        # Directory should be empty
        Test.cleaner.clean_dir()

        # Creating Objects
        manipulator_data = Manipulator(DATA_RAW, TEST_DIR)
        manipulator_noise = Manipulator(NOISE_RAW, TEST_DIR)

        # Slice audio files and safe them in test directory
        manipulator_data.slice_audio()
        manipulator_noise.slice_audio()

        # actual test
        for i in Test.helper.get_duration():
            self.assertEqual(i, 3000 / 1000)

    def test_zero_dB_calculation(self):
        for file in os.listdir(NOISE_PROCESSED):
            noise, _ = lr.load(NOISE_PROCESSED + file, sr=16000)

            for files in os.listdir(DATA_PROCESSED):
                audio, _ = lr.load(DATA_PROCESSED + files, sr=16000)
                power_noise = calculation.mean_power(calculation.get_constant(audio, noise, 10) * noise)
                self.assertEqual(10, round(calculation.snr(calculation.mean_power(audio), power_noise)))

    def test_create_tensor(self):
        noise_matrix = Helper(NOISE_PROCESSED).get_numpy_data()
        audio_matrix = Helper(DATA_PROCESSED).get_numpy_data()
        augmenter = Augmenter(audio_matrix, noise_matrix, 10)
        augmenter.get_noise_input()
        augmenter.get_noise_input()

    def test_HDF5(self):
        HDF5Object = HDF5File(TEST_DIR + "testfile.hdf5")
        HDF5Object.create()
        HDF5Object.write([1, 2], [1, 1, 1, 1, 1], 10)


if __name__ == "__main__":
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', category=ImportWarning)
        warnings.simplefilter('ignore', category=DeprecationWarning)
        warnings.simplefilter('ignore', category=ResourceWarning)
        unittest.main()
        Test.cleaner.clean_dir()
