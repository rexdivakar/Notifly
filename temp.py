from notifly import discord
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

token = 'https://discord.com/api/webhooks/770164527911534634/BUthlz8AwweN6otan37h3lpZM9kcXgBdO77-M5Zc9GHz9kacL1sCYVK_pLyVBkMq1zkP'
x = discord.Notifier(token)

def test(f):
    def inner(*args, **kwargs):
        args[0].stop_training
        x.send(f"{args[1]}. {args[2]}")
        f(*args, **kwargs)
    return inner


import tensorflow as tf

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# train_images = train_images / 255.0

# test_images = test_images / 255.0




model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])


class testCallback(tf.keras.callbacks.Callback):

    @test(interval=1, )
    def on_epoch_end(self, epoch, logs=None):

        print(tf.keras.optimizers)

model.fit(train_images, train_labels, epochs=5,callbacks=[testCallback()])

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)