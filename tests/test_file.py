import unittest
import warnings
from sample import helpers
from sample import loadData


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
        self.assertRaises(FileNotFoundError, lambda: loadData.resampledData(wrong_dir, helpers.DATA_PRO))

    def test_samplerate_Exception(self):
        # Test passed
        type = "test"
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_RAW, type))
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_PRO, type))

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

if __name__ == "__main__":
    unittest.main()
