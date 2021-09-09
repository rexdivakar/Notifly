import ssl
from notifly import tf_notifier
import tensorflow as tf
from dotenv import load_dotenv
import os


load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context
token = os.getenv('TOKEN')
notifier = tf_notifier.TfNotifier(token=token, platform='discord')


class TestCallback(tf.keras.callbacks.Callback):

    @notifier.notify_on_epoch_begin(epoch_interval=1, graph_interval=10)
    def on_epoch_begin(self, epoch, logs=None):
        pass

    @notifier.notify_on_epoch_end(epoch_interval=1, graph_interval=10)
    def on_epoch_end(self, epoch, logs=None):
        pass

    @notifier.notify_on_train_begin()
    def on_train_begin(self, logs=None):
        pass

    @notifier.notify_on_train_end()
    def on_train_end(self, logs=None):
        pass


fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, callbacks=[TestCallback()])

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
