import unittest
import warnings
from sample import helpers,loadData,calculation
import librosa as lr
import os

##### Unit Tests #####
class Test(unittest.TestCase):

    # Reusable class variables
    test_dir = "/home/timo/unittest/"

    def test_downSample(self):
        # Test passed
        loadData.resampledData(helpers.DATA_RAW, Test.test_dir)
        loadData.resampledData(helpers.NOISE_RAW, Test.test_dir)
        for i in helpers.getAllSampleRates(Test.test_dir):
            self.assertEqual(i, helpers.SAMPLE_RATE)

    def test_wrongPath(self):
        # Test passed
        wrong_dir = "home/timo/unit"
        self.assertRaises(FileNotFoundError, lambda: helpers.getAllSampleRates(wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: helpers.copyData(helpers.NOISE_RAW, wrong_dir))
        self.assertRaises(FileNotFoundError, lambda: loadData.resampledData(wrong_dir, helpers.DATA_PROCESSED))

    def test_samplerate_Exception(self):
        # Test passed
        type = "test"
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_RAW, type))
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_PROCESSED, type))

    def test_slice_data(self):
        # Test passed
        # !!! NOTE: Test directory must be empty !!!

        # Warning for older ffmpeg versions
        warnings.simplefilter("ignore", ResourceWarning)

        # actual test
        loadData.sliceAudio(helpers.DATA_RAW, Test.test_dir)
        for i in helpers.getDuration(Test.test_dir):
            self.assertEqual(i, helpers.DURATION/1000)

    def test_getSampleRate_type(self):
        # Test passed

        # Warning for older ffmpeg version
        warnings.simplefilter("ignore", ResourceWarning)

        loadData.sliceAudio(helpers.NOISE_RAW, Test.test_dir)
        for i in helpers.getSampleRates(Test.test_dir, "aircon"):
            self.assertEqual(44100, i)
        for j in helpers.getSampleRates(Test.test_dir, "dishwasher"):
            self.assertEqual(44100, j)

    def test_zero_dB_calculation(self):
        # Test passed
        for file in os.listdir(helpers.NOISE_PROCESSED):
            noise, _ = lr.load(helpers.NOISE_PROCESSED + file, sr=helpers.SAMPLE_RATE)
            for files in os.listdir(helpers.DATA_PROCESSED):
                audio, _ = lr.load(helpers.DATA_PROCESSED + files, sr=helpers.SAMPLE_RATE)
                power_noise = calculation.meanPower(calculation.get_constant(audio, noise) * noise)
                # print(round(calculation.snr(calculation.meanPower(audio), noisee)))
                self.assertEqual(0, round(calculation.snr(calculation.meanPower(audio), power_noise)))

if __name__ == "__main__":
    unittest.main()
