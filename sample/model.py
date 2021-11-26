import keras.layers
import tensorflow as tf

encoder = tf.keras.Sequential([
    keras.layers.Input(shape=(1025, 157)),
    keras.layers.Conv2D(128, 6, activation="relu", padding="same"),
    keras.layers.MaxPool2D(2, padding="same"),
    keras.layers.Conv2D(64, 6, activation="relu", padding="same"),
    keras.layers.MaxPool2D(2, padding="same"),
    keras.layers.Conv2D(32, 6, activation="relu", padding="same"),
    keras.layers.MaxPool2D(2, padding="same")
])

decoder = tf.keras.Sequential([
    keras.layers.Conv2D(32, 6, activation="relu", padding="same"),
    keras.layers.UpSampling2D(2),
    keras.layers.Conv2D(64, 6, activation="relu", padding="same"),
    keras.layers.UpSampling2D(2),
    keras.layers.Conv2D(128, 6, activation="relu", padding="same"),
    keras.layers.UpSampling2D(2),
    keras.layers.Conv2D(1, 6, activation='sigmoid', padding='same')
])

model = tf.keras.Sequential([encoder, decoder])
