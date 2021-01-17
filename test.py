import ssl
from notifly import discord
import tensorflow as tf
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def test():
    ssl._create_default_https_context = ssl._create_unverified_context
    token = os.getenv('TOKEN')
    notifier = discord.Notifier(token)

    class TestCallback(tf.keras.callbacks.Callback):

        @notifier.notify_on_epoch_begin(epoch_interval=1, graph_interval=1, hardware_stats_interval=1)
        def on_epoch_begin(self, epoch, logs=None):
            pass

        @notifier.notify_on_epoch_end(epoch_interval=1, graph_interval=1, hardware_stats_interval=1)
        def on_epoch_end(self, epoch, logs=None):
            pass

        @notifier.notify_on_train_begin()
        def on_train_begin(self, logs=None):
            pass

        @notifier.notify_on_train_end()
        def on_train_end(self, logs=None):
            pass

    fashion_mnist = tf.keras.datasets.fashion_mnist
    (train_images, train_labels), (_, _) = fashion_mnist.load_data()

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(2, activation='relu'),
        tf.keras.layers.Dense(10)
    ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    model.fit(train_images, train_labels, epochs=1, callbacks=[TestCallback()])


test()
