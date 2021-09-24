# Static settings for the Project

SAMPLE_RATE = 16000  # Hz

# Path's to access data
NOISE_RAW = "../noise/raw/"
NOISE_PRO = "../nosie/processed/"
AUDIOFORMAT = ".wav"
LENGTH = 5

# Types of noise
NOISE_TYPES = ["aircon", "dishwasher", "street", "vacuuming", "washer"]

# Path's for specific data
AIR_CONDITION = NOISE_RAW + "aircon_%s" + AUDIOFORMAT
DISHWASHER = NOISE_RAW + "dishwasher_%s" + AUDIOFORMAT
VACUUM_CLEANER = NOISE_RAW + "vacuuming_%s" + AUDIOFORMAT
STREET = NOISE_RAW + "street_%s" + AUDIOFORMAT
WASHER_M = NOISE_RAW + "washer_%s" + AUDIOFORMAT
