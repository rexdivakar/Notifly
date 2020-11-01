from notifly import discord
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
token = 'https://discord.com/api/webhooks/771253998313144321/5FNBsAi8-exyc-3rxLOYudQdQqMdpcaCOqCh6z1IX4ledG1oGyaONeIY1HDUns6qBZhW'
x = discord.Notifier(token)

import inspect


class NotifierCallback:

    @staticmethod
    def notify_on_epoch_end(platform, epoch_interval, graph_interval, training_end_message, monitor='all'):

        def inner(func_to_call):
            def wrapper(*args, **kwargs):

                # get parameter values
                parameter_values = []
                for i in args:
                    parameter_values.append(i)
                for i in kwargs.values():
                    parameter_values.append(i)

                # get arguments names from the function signature
                sig = inspect.signature(func_to_call)
                parameter_names = sig.parameters.keys()

                # parameter mapping with names to values
                parameter_mapping = dict(zip(parameter_names, parameter_values))
                print(parameter_mapping)

                # get model instance
                model_instance = parameter_mapping.get('self').model

                # get current epoch because epoch starts from 0
                current_epoch = parameter_mapping.get('epoch') + 1

                # get current epoch logs
                current_epoch_logs = parameter_mapping.get('logs')

                # notify if current_epoch is divisible by epoch_interval
                if current_epoch % epoch_interval == 0:
                    message = f"epoch: {current_epoch},"
                    for k, v in current_epoch_logs.items():
                        message += " {}: {:.4f},".format(k, v)
                    x.send(message, print_message=False)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    x.send(f"{current_epoch}. {model_instance.history.history}", print_message=False)

                # if training is ended in between by some callback
                if model_instance.stop_training:
                    x.send(f"Hooray! Training has ended by callback", print_message=False)

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

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
    @NotifierCallback.notify_on_epoch_end(
        platform='discord', epoch_interval=1, graph_interval=10, training_end_message=True, monitor='all')
    def on_epoch_end(self, epoch, logs=None):
        pass


model.fit(train_images, train_labels, epochs=5, callbacks=[testCallback()])

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)

print('\nTest accuracy:', test_acc)
