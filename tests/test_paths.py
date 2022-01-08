from main.constants import DATA_RAW, DATA_PROCESSED, NOISE_PROCESSED, NOISE_RAW

"""

Changes on relative paths to run unittest
from the terminal.

python3 -m unittest

NOTE: Tests do no longer run in an IDE with this paths.
-> Use paths from main.constants

TODO: Write a separate local testfile for the IDE.
"""

TEST_DIR = "/home/timo/unittest/"
TEST_DATA_RAW = DATA_RAW.replace("../", "")
TEST_DATA_PROCESSED = DATA_PROCESSED.replace("../", "")
TEST_NOISE_RAW = NOISE_RAW.replace("../", "")
TEST_NOISE_PROCESSED = NOISE_PROCESSED.replace("../", "")
