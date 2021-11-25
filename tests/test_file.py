import glob
import unittest
import warnings
from sample import helpers, load_data, calculation
from tests.test_paths import *
import librosa as lr
import os


##### Unit Tests #####
class Test(unittest.TestCase):

    def test_down_sample(self):
        load_data.resampled_data(TEST_DATA_RAW, TEST_DIR)
        load_data.resampled_data(TEST_NOISE_RAW, TEST_DIR)

        for i in helpers.get_all_sample_rates(TEST_DIR):
            self.assertEqual(i, helpers.SAMPLE_RATE)

    def test_wrong_path(self):
        wrong_dir = "/home/unit"

        self.assertRaises(FileNotFoundError, lambda: helpers.get_all_sample_rates(wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: helpers.copy_data(TEST_NOISE_RAW, wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: load_data.resampled_data(wrong_dir, TEST_DATA_PROCESSED))

    def test_samplerate_Exception(self):
        test_type = "test"

        self.assertRaises(KeyError, lambda: helpers.get_specific_sample_rates(TEST_NOISE_RAW, test_type))
        self.assertRaises(KeyError, lambda: helpers.get_specific_sample_rates(TEST_NOISE_PROCESSED, test_type))

    def test_slice_data(self):
        # Warning for older ffmpeg versions
        warnings.simplefilter("ignore", ResourceWarning)

        # Directory should be empty
        if (os.listdir(TEST_DIR)) != 0:
            for file in (glob.glob(TEST_DIR + "*")):
                os.remove(file)

        # Slice audio files and safe them in test directory
        load_data.slice_audio(TEST_DATA_RAW, TEST_DIR)
        load_data.slice_audio(TEST_NOISE_RAW, TEST_DIR)

        # actual test
        for i in helpers.get_duration(TEST_DIR):
            self.assertEqual(i, helpers.DURATION / 1000)

    def test_get_sample_rate_type(self):
        # Warning for older ffmpeg version
        warnings.simplefilter("ignore", ResourceWarning)

        load_data.slice_audio(TEST_NOISE_RAW, TEST_DIR)

        for i in helpers.get_specific_sample_rates(TEST_DIR, "aircon"):
            self.assertEqual(44100, i)

        for j in helpers.get_specific_sample_rates(TEST_DIR, "dishwasher"):
            self.assertEqual(44100, j)

    def test_zero_dB_calculation(self):
        for file in os.listdir(TEST_NOISE_PROCESSED):
            noise, _ = lr.load(TEST_NOISE_PROCESSED + file, sr=helpers.SAMPLE_RATE)

            for files in os.listdir(TEST_DATA_PROCESSED):
                audio, _ = lr.load(TEST_DATA_PROCESSED + files, sr=helpers.SAMPLE_RATE)
                power_noise = calculation.mean_power(calculation.get_constant(audio, noise, 0) * noise)
                self.assertEqual(0, round(calculation.snr(calculation.mean_power(audio), power_noise)))


if __name__ == "__main__":
    unittest.main()
