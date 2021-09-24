import unittest
from sample import settings as st
from sample import helpers


##### Unit Tests #####
# TODO: Implement downsample() function in helpers
# TODO: check import stuff

class TestHelpers(unittest.TestCase):

    def test_downSampled(self):
        for i in range(0, len(st.NOISE_TYPES)):
            self.assertEqual(
                helpers.downSample(st.NOISE_RAW + st.NOISE_TYPES[i] + st.AUDIOFORMAT, st.SAMPLE_RATE)
            )

    def test_samplerate_Exception(self):
        self.assertRaises(KeyError, helpers.getSampleRates(st.NOISE_RAW, "test"))
        self.assertRaises(KeyError, helpers.getSampleRates(st.NOISE_PRO, "test"))


if __name__ == "__main__":
    unittest.main()
