from notifly import discord
import inspect


class TfNotifier:

    def __init__(self, token, platform):
        if platform == 'discord':
            self.notifier = discord.Notifier(token)

    def notify_on_train_begin(self):

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

                # get starting logs
                starting_logs = parameter_mapping.get('logs')

                self.notifier.send(f':muscle: training started, got log keys: {starting_logs}')

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

        return inner

    def notify_on_train_end(self):

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

                # get starting logs
                ending_logs = parameter_mapping.get('logs')

                self.notifier.send(f':tada: training ended, got log keys: {ending_logs}')

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

        return inner

    def notify_on_epoch_begin(self, epoch_interval, graph_interval):

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
                print(current_epoch_logs)

                # notify if current_epoch is divisible by epoch_interval
                if current_epoch % epoch_interval == 0:
                    message = f"epoch: {current_epoch} started, got log keys:"
                    for k, v in current_epoch_logs.items():
                        message += " {}: {:.4f} ".format(k, v)
                    self.notifier.send(message, print_message=False)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    self.notifier.send(f"{current_epoch}. {model_instance.history.history}", print_message=False)

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

        return inner

    def notify_on_epoch_end(self, epoch_interval, graph_interval):

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
                    message = f"epoch: {current_epoch} ended, got log keys:"
                    for k, v in current_epoch_logs.items():
                        message += " {}: {:.4f} ".format(k, v)
                    self.notifier.send(message, print_message=False)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    self.notifier.send(f"{current_epoch}. {model_instance.history.history}", print_message=False)

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

        return inner
