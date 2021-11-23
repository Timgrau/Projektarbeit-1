import unittest
import warnings
from sample import helpers, load_data, calculation
import librosa as lr
import os


##### Unit Tests #####
class Test(unittest.TestCase):
    # Reusable class variables
    test_dir = "/home/timo/unittest/"

    def test_down_sample(self):
        # Test passed

        load_data.resampled_data(helpers.DATA_RAW, Test.test_dir)
        load_data.resampled_data(helpers.NOISE_RAW, Test.test_dir)

        for i in helpers.get_all_sample_rates(Test.test_dir):
            self.assertEqual(i, helpers.SAMPLE_RATE)

    def test_wrong_path(self):
        # Test passed

        wrong_dir = "home/timo/unit"
        self.assertRaises(FileNotFoundError, lambda: helpers.get_all_sample_rates(wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: helpers.copy_data(helpers.NOISE_RAW, wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: load_data.resampled_data(wrong_dir, helpers.DATA_PROCESSED))

    def test_samplerate_Exception(self):
        # Test passed

        test_type = "test"
        self.assertRaises(KeyError, lambda: helpers.get_specific_sample_rates(helpers.NOISE_RAW, test_type))
        self.assertRaises(KeyError, lambda: helpers.get_specific_sample_rates(helpers.NOISE_PROCESSED, test_type))

    def test_slice_data(self):
        # Test passed
        # !!! NOTE: Test directory must be empty !!!

        # Warning for older ffmpeg versions
        warnings.simplefilter("ignore", ResourceWarning)

        # actual test
        load_data.slice_audio(helpers.DATA_RAW, Test.test_dir)

        for i in helpers.get_duration(Test.test_dir):
            self.assertEqual(i, helpers.DURATION / 1000)

    def test_get_sample_rate_type(self):
        # Test passed

        # Warning for older ffmpeg version
        warnings.simplefilter("ignore", ResourceWarning)

        load_data.slice_audio(helpers.NOISE_RAW, Test.test_dir)

        for i in helpers.get_specific_sample_rates(Test.test_dir, "aircon"):
            self.assertEqual(44100, i)

        for j in helpers.get_specific_sample_rates(Test.test_dir, "dishwasher"):
            self.assertEqual(44100, j)

    def test_zero_dB_calculation(self):
        # Test passed

        for file in os.listdir(helpers.NOISE_PROCESSED):
            noise, _ = lr.load(helpers.NOISE_PROCESSED + file, sr=helpers.SAMPLE_RATE)

            for files in os.listdir(helpers.DATA_PROCESSED):
                audio, _ = lr.load(helpers.DATA_PROCESSED + files, sr=helpers.SAMPLE_RATE)
                power_noise = calculation.mean_power(calculation.get_constant(audio, noise, 0) * noise)
                self.assertEqual(0, round(calculation.snr(calculation.mean_power(audio), power_noise)))


if __name__ == "__main__":
    unittest.main()
