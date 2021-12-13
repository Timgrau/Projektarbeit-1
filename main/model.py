import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model


def unet(pretrained_weights=None, input_size=(256, 128, 1)):
    # size filter input
    size_filter_in = 16
    # normal initialization of weights
    kernel_init = 'he_normal'
    # To apply leaky relu after the conv layer
    activation_layer = None
    inputs = layers.Input(input_size)
    conv1 = layers.Conv2D(size_filter_in, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(inputs)
    conv1 = layers.LeakyReLU()(conv1)
    conv1 = layers.Conv2D(size_filter_in, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv1)
    conv1 = layers.LeakyReLU()(conv1)

    pool1 = layers.MaxPooling2D(pool_size=(2, 2))(conv1)

    conv2 = layers.Conv2D(size_filter_in * 2, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(pool1)
    conv2 = layers.LeakyReLU()(conv2)
    conv2 = layers.Conv2D(size_filter_in * 2, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv2)
    conv2 = layers.LeakyReLU()(conv2)

    pool2 = layers.MaxPooling2D(pool_size=(2, 2))(conv2)

    conv3 = layers.Conv2D(size_filter_in * 4, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(pool2)
    conv3 = layers.LeakyReLU()(conv3)
    conv3 = layers.Conv2D(size_filter_in * 4, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv3)
    conv3 = layers.LeakyReLU()(conv3)

    pool3 = layers.MaxPooling2D(pool_size=(2, 2))(conv3)

    conv4 = layers.Conv2D(size_filter_in * 8, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(pool3)
    conv4 = layers.LeakyReLU()(conv4)
    conv4 = layers.Conv2D(size_filter_in * 8, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv4)
    conv4 = layers.LeakyReLU()(conv4)

    drop4 = layers.Dropout(0.5)(conv4)
    pool4 = layers.MaxPooling2D(pool_size=(2, 2))(drop4)

    """conv5 = layers.Conv2D(size_filter_in*16, 3, activation = activation_layer, padding = 'same', kernel_initializer = kernel_init)(pool3)
    conv5 = layers.LeakyReLU()(conv5)
    conv5 = layers.Conv2D(size_filter_in*16, 3, activation = activation_layer, padding = 'same', kernel_initializer = kernel_init)(conv5)
    conv5 = layers.LeakyReLU()(conv5)

    drop5 = layers.Dropout(0.5)(conv5)

    up6 = layers.Conv2D(size_filter_in*8, 2, activation = activation_layer, padding = 'same', kernel_initializer = kernel_init)(layers.UpSampling2D(size = (2,2))(drop5))
    up6 = layers.LeakyReLU()(up6)

    merge6 = layers.concatenate([drop4,up6], axis = 3)

    conv6 = layers.Conv2D(size_filter_in*8, 3, activation = activation_layer, padding = 'same', kernel_initializer = kernel_init)(drop5)
    conv6 = layers.LeakyReLU()(conv6)
    conv6 = layers.Conv2D(size_filter_in*8, 3, activation = activation_layer, padding = 'same', kernel_initializer = kernel_init)(conv6)
    conv6 = layers.LeakyReLU()(conv6)"""

    up7 = layers.Conv2D(size_filter_in * 4, 2, activation=activation_layer, padding='same',
                        kernel_initializer=kernel_init)(layers.UpSampling2D(size=(2, 2))(drop4))
    up7 = layers.LeakyReLU()(up7)

    merge7 = layers.concatenate([conv3, up7], axis=3)

    conv7 = layers.Conv2D(size_filter_in * 4, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(merge7)
    conv7 = layers.LeakyReLU()(conv7)
    conv7 = layers.Conv2D(size_filter_in * 4, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv7)
    conv7 = layers.LeakyReLU()(conv7)

    up8 = layers.Conv2D(size_filter_in * 2, 2, activation=activation_layer, padding='same',
                        kernel_initializer=kernel_init)(layers.UpSampling2D(size=(2, 2))(conv7))
    up8 = layers.LeakyReLU()(up8)

    merge8 = layers.concatenate([conv2, up8], axis=3)

    conv8 = layers.Conv2D(size_filter_in * 2, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(merge8)
    conv8 = layers.LeakyReLU()(conv8)
    conv8 = layers.Conv2D(size_filter_in * 2, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv8)
    conv8 = layers.LeakyReLU()(conv8)

    up9 = layers.Conv2D(size_filter_in, 2, activation=activation_layer, padding='same', kernel_initializer=kernel_init)(
        layers.UpSampling2D(size=(2, 2))(conv8))
    up9 = layers.LeakyReLU()(up9)

    merge9 = layers.concatenate([conv1, up9], axis=3)

    conv9 = layers.Conv2D(size_filter_in, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(merge9)
    conv9 = layers.LeakyReLU()(conv9)
    conv9 = layers.Conv2D(size_filter_in, 3, activation=activation_layer, padding='same',
                          kernel_initializer=kernel_init)(conv9)
    conv9 = layers.LeakyReLU()(conv9)
    conv9 = layers.Conv2D(2, 3, activation=activation_layer, padding='same', kernel_initializer=kernel_init)(conv9)
    conv9 = layers.LeakyReLU()(conv9)

    conv10 = layers.Conv2D(1, 1, activation='tanh')(conv9)

    model = Model(inputs, conv10)

    model.compile(optimizer='adam', loss="mse")

    return model
