# Static settings for the Project

SAMPLE_RATE = 16000  # Hz

# Path's to access data
NOISE_RAW = "../noise_data/raw/"
NOISE_PRO = "../noise_data/processed/"
DATA_RAW = "../use_data/raw/"
DATA_PRO = "../use_data/processed/"

AUDIOFORMAT = ".wav"
NOISE_LENGTH = 30
DATA_LENGTH = 3
DURATION = 5000   # millisec

# Types of noise_data
NOISE_TYPES = ["aircon", "dishwasher", "street", "vacuuming", "washer"]

# Path's for specific noise data
AIR_CONDITION = NOISE_RAW + "aircon_%s" + AUDIOFORMAT
DISHWASHER = NOISE_RAW + "dishwasher_%s" + AUDIOFORMAT
VACUUM_CLEANER = NOISE_RAW + "vacuuming_%s" + AUDIOFORMAT
STREET = NOISE_RAW + "street_%s" + AUDIOFORMAT
WASHER_M = NOISE_RAW + "washer_%s" + AUDIOFORMAT
