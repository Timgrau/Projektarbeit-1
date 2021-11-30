import tensorflow as tf
from tensorflow.keras import layers


class Autoencoder(tf.keras.Model):
    def __init__(self):
        super(Autoencoder, self).__init__()
        self.encoder = tf.keras.Sequential([
            layers.Input(shape=(1025, 157, 1)),
            layers.Conv2D(128, (6, 6), activation="relu", padding="same"),
            layers.MaxPool2D(2, padding="same"),
            layers.Conv2D(64, (6, 6), activation="relu", padding="same"),
            layers.MaxPool2D(2, padding="same"),
            layers.Conv2D(32, (6, 6), activation="relu", padding="same"),
            layers.MaxPool2D(2, padding="same")
        ])
        self.decoder = tf.keras.Sequential([
            layers.Conv2D(32, (6, 6), activation="relu", padding="same"),
            layers.UpSampling2D(2),
            layers.Conv2D(64, (6, 6), activation="relu", padding="same"),
            layers.UpSampling2D(2),
            layers.Conv2D(128, (6, 6), activation="relu", padding="same"),
            layers.UpSampling2D(2),
            layers.Conv2D(1, (6, 6), padding='same')
        ])

    def call(self, x):
        encoder = self.encoder(x)
        decoder = self.decoder(encoder)
        return decoder
