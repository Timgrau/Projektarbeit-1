# Static settings for the Project

SAMPLE_RATE = 16000  # Hz

# Path's to access data
NOISE_RAW = "../noise_data/raw/"
NOISE_PROCESSED = "../noise_data/processed/"

DATA_RAW = "../use_data/raw/"
DATA_RESAMPLED = "../use_data/resampled/"
DATA_PROCESSED = "../use_data/processed/"

AUDIOFORMAT = ".wav"
DURATION = 5000   # millisec

# Types of noise_data
NOISE_TYPES = ["aircon", "dishwasher", "street", "vacuuming"]

# Path's for specific noise data
AIR_CONDITION = NOISE_RAW + "aircon_%s" + AUDIOFORMAT
DISHWASHER = NOISE_RAW + "dishwasher_%s" + AUDIOFORMAT
VACUUM_CLEANER = NOISE_RAW + "vacuuming_%s" + AUDIOFORMAT
STREET = NOISE_RAW + "street_%s" + AUDIOFORMAT
