import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

def load_mnist(plot=False, n_steps=30):
    (train_images, train_labels), (test_images, test_labels) = (
        tf.keras.datasets.mnist.load_data())

    # flatten images
    train_images = train_images.reshape((train_images.shape[0], -1))
    test_images = test_images.reshape((test_images.shape[0], -1))

    if plot:
        for i in range(3):
            plt.figure()
            plt.imshow(np.reshape(train_images[i], (28, 28)),
                       cmap="gray")
            plt.axis('off')
            plt.title(str(train_labels[i]));

    # add single timestep to training data
    train_images = train_images[:, None, :]
    train_labels = train_labels[:, None, None]

    # when testing our network with spiking neurons we will need to run it
    # over time, so we repeat the input/target data for a number of timesteps.
    test_images = np.tile(test_images[:, None, :], (1, n_steps, 1))
    test_labels = np.tile(test_labels[:, None, None], (1, n_steps, 1))

    return train_images, train_labels, test_images, test_labels