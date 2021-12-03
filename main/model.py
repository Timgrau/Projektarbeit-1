import tensorflow as tf
from tensorflow.keras import layers


class Autoencoder():
    def __init__(self):
        self.encoder = tf.keras.Sequential([
            layers.Conv2D(filters=32, kernel_size=(4, 4), activation="selu", padding="same",
                          input_shape=[264, 312, 1]),
            layers.MaxPool2D(pool_size=(2, 2), padding="same"),
            layers.Conv2D(filters=26, kernel_size=(4, 4), activation="selu", padding="same"),
            layers.MaxPool2D(pool_size=(2, 2), padding="same"),
            layers.Conv2D(filters=20, kernel_size=(2, 2), activation="selu", padding="same"),
            layers.MaxPool2D(pool_size=(2, 2), padding="same"),
            layers.Conv2D(filters=14, kernel_size=(2, 2), activation="selu", padding="same"),
            layers.Dropout(0.5),
            layers.Conv2D(filters=8, kernel_size=(2, 2), activation="selu", padding="same"),

        ])

        self.decoder = tf.keras.Sequential([
            layers.Conv2D(filters=8, kernel_size=(2, 2), activation="selu", padding="same"),
            layers.Dropout(0.5),
            layers.Conv2D(filters=14, kernel_size=(2, 2), activation="selu", padding="same"),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(filters=20, kernel_size=(2, 2), activation="selu", padding="same"),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(filters=26, kernel_size=(4, 4), activation="selu", padding="same"),
            layers.UpSampling2D((2, 2)),
            layers.Conv2D(filters=1, kernel_size=(4, 4), activation="sigmoid", padding='same'),

        ])

    def get_model(self):
        return tf.keras.Sequential([self.encoder, self.decoder])
