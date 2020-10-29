from notifly import discord
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
token='https://discord.com/api/webhooks/771253998313144321/5FNBsAi8-exyc-3rxLOYudQdQqMdpcaCOqCh6z1IX4ledG1oGyaONeIY1HDUns6qBZhW'
x = discord.Notifier(token)

import inspect

def test(f):
    def inner(*args, **kwargs):
        # combine parameters from the arguments into a single list
        parameter_values = []
        for i in args:
            parameter_values.append(i)

        for i in kwargs.values():
            parameter_values.append(i)
        print(parameter_values)
        print(parameter_values)
        sig = inspect.signature(f)
        parameters = sig.parameters.keys()
        print(parameters)
        d = dict(zip(parameters, parameter_values))
        print(d)
        # TODO: in default parameters we wont get the default value if the value is not passed during the function call

        model_instance = d.get('self').model
        print('\n')
        hist = model_instance.history.history
        print('\n')
        epoch = d.get('epoch')
        logs = d.get('logs')

        x.send(f"{epoch}. {hist}", print_message=False)
        r = f(*args, **kwargs)
        return r
    return inner


import tensorflow as tf

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


class testCallback(tf.keras.callbacks.Callback):
    @test
    def on_epoch_end(self, epoch, logs=None):
        print(tf.keras.optimizers)

model.fit(train_images, train_labels, epochs=5,callbacks=[testCallback()])

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)