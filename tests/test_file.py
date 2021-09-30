import unittest
from sample import helpers
from sample import loadData


##### Unit Tests #####

class TestHelpers(unittest.TestCase):

    def test_downSample_Noise(self):
        # Test passed
        testdir = "/home/timo/Dokumente/"
        loadData.resampledNoise(testdir)
        for i in helpers.getAllSampleRates(testdir):
            self.assertEqual(i, helpers.SAMPLE_RATE)

    def test_downSample_Data(self):
        # Test passed
        testdir = "/home/timo/Dokumente/"
        loadData.resampledData(testdir)
        for i in helpers.getAllSampleRates(testdir):
            self.assertEqual(i, helpers.SAMPLE_RATE)

    def test_wrongPath(self):
        # Test passed
        test_dir = "home/timo/Dokument"
        self.assertRaises(FileNotFoundError, lambda: loadData.resampledNoise(test_dir))
        self.assertRaises(FileNotFoundError, lambda: loadData.resampledData(test_dir))
        self.assertRaises(FileNotFoundError, lambda: helpers.getAllSampleRates(test_dir))

    def test_samplerate_Exception(self):
        # Test passed
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_RAW, "test"))
        self.assertRaises(KeyError, lambda: helpers.getSampleRates(helpers.NOISE_PRO, "test"))

    #def test_slice_data(self):
    #   helpers.sliceData()

if __name__ == "__main__":
    unittest.main()
