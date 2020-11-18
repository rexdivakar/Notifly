from notifly import discord, telegram, slack
import inspect
import matplotlib.pyplot as plt
import copy


class TfNotifier:

    def __init__(self, token, platform, channel= 'general'):
        platform = platform.lower()
        if platform == 'discord':
            self.notifier = discord.Notifier(token)
        elif platform == 'telegram':
            self.notifier = telegram.BotHandler(token)
        elif platform == 'slack':   #TODO Handle slack channel config
            self.notifier = slack.Notifier(token, channel)
        else:
            print('Invalid Platform')
            exit(1)

    @staticmethod
    def plot_graph(history, current_epoch_logs):

        # merge history with current epoch logs
        for key, value in current_epoch_logs.items():
            if key not in history:
                history[key] = [value]
            else:
                history[key].append(value)

        plt.figure()
        for key, value in history.items():
            if len(value) != 1:
                plt.plot(range(1, len(value)+1), value, label=str(key))
            else:
                plt.scatter(range(1, len(value)+1), value, label=str(key))
            plt.title("Training History")

        plt.xlabel('Epochs')
        plt.legend()
        plt.pause(1e-13)
        file_path = 'fig.png'
        plt.savefig(file_path, bbox_inches='tight')
        plt.close()
        return file_path

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

                self.notifier.send_message(f':muscle: training started, got log keys: {starting_logs}')

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

                self.notifier.send_message(f':tada: training ended, got log keys: {ending_logs}')

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
                    self.notifier.send_message(message)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    history_copy = copy.deepcopy(model_instance.history.history)
                    file_path = TfNotifier.plot_graph(history_copy, current_epoch_logs)
                    # TODO: change this function call
                    self.notifier.send_file(file_path)

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
                    self.notifier.send_message(message)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    history_copy = copy.deepcopy(model_instance.history.history)
                    file_path = TfNotifier.plot_graph(history_copy, current_epoch_logs)
                    # TODO: change this function call
                    self.notifier.send_file(file_path)

                return_value = func_to_call(*args, **kwargs)

                return return_value

            return wrapper

        return inner
