from notifly import gpu_stats
import inspect
import matplotlib.pyplot as plt
import copy
import psutil


class TfNotifier:

    def send_message(self, message):
        return

    def send_file(self, file_path):
        return

    @staticmethod
    def get_hardware_stats():
        """
        Fetches the hardware stats on regular intervals

        Returns:
            The parameters of CPU, GPU, RAM
        Raises:
            Exception
        """
        try:
            cpu_usage = psutil.cpu_percent(interval = 0.2)
            mem_stats = psutil.virtual_memory()
            ram_usage = round((mem_stats.used / mem_stats.total) * 100, 2)
        except Exception as e:
            print('Unable to find system parameters', e)

        x = gpu_stats.gpu()
        if x is None:
            return f"CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%"

        gpu_util = x[2]
        tot_v_ram = x[3]
        v_ram_used = x[4]
        unused_vram = x[5]
        driver_ver = x[6]
        gpu_name = x[7]
        gpu_temp = x[11].strip()
        return f"CPU Usage: {cpu_usage}%, RAM Usage: {ram_usage}%, GPU Usage: {gpu_util}%, GPU Temp: {gpu_temp}," \
               f" GPU Memory: {v_ram_used} MB, GPU Unused Memory: {unused_vram} MB"

    @staticmethod
    def plot_graph(history, current_epoch_logs):
        """
        Plots the graphs on runtime

        Args:
            history (dict): gets the logs of the tensorflow model.train()
            current_epoch_logs (int): Fetches the epochs on runtime event
        Returns:
            Plots the graph on runtime
        """

        # merge history with current epoch logs
        for key, value in current_epoch_logs.items():
            if key not in history:
                history[key] = [value]
            else:
                history[key].append(value)

        plt.figure()
        for key, value in history.items():
            if len(value) != 1:
                plt.plot(range(1, len(value) + 1), value, label = str(key))
            else:
                plt.scatter(range(1, len(value) + 1), value, label = str(key))
            plt.title("Training History")

        plt.xlabel('Epochs')
        plt.legend()
        plt.pause(1e-13)
        file_path = 'fig.png'
        plt.savefig(file_path, bbox_inches = 'tight')
        plt.close()
        return file_path

    def notify_on_train_begin(self):
        """
        Decorator which runs on beginning of the training model.

        Returns:
            Updated function
        """

        def inner(func_to_call):
            def wrapper(*args, **kwargs):
                # get parameter values
                parameter_values = list(args)
                for i in kwargs.values():
                    parameter_values.append(i)

                # get arguments names from the function signature
                sig = inspect.signature(func_to_call)
                parameter_names = sig.parameters.keys()

                # parameter mapping with names to values
                parameter_mapping = dict(zip(parameter_names, parameter_values))

                # get starting logs
                starting_logs = parameter_mapping.get('logs')

                self.send_message(f':muscle: training started, got log keys: {starting_logs}')

                return func_to_call(*args, **kwargs)

            return wrapper

        return inner

    def notify_on_train_end(self):
        """
        Decorator which runs on end of each iteration during training model.

        Returns:
            Updated function
        """
        def inner(func_to_call):
            def wrapper(*args, **kwargs):
                # get parameter values
                parameter_values = list(args)
                for i in kwargs.values():
                    parameter_values.append(i)

                # get arguments names from the function signature
                sig = inspect.signature(func_to_call)
                parameter_names = sig.parameters.keys()

                # parameter mapping with names to values
                parameter_mapping = dict(zip(parameter_names, parameter_values))

                # get starting logs
                ending_logs = parameter_mapping.get('logs')

                self.send_message(f':tada: training ended, got log keys: {ending_logs}')

                return func_to_call(*args, **kwargs)

            return wrapper

        return inner

    def notify_on_epoch_begin(self, epoch_interval, graph_interval, hardware_stats_interval):
        """
        Decorator which runs on beginning of the training model.

        Returns:
            Updated function
        """
        def inner(func_to_call):
            def wrapper(*args, **kwargs):

                # get parameter values
                parameter_values = list(args)
                for i in kwargs.values():
                    parameter_values.append(i)

                # get arguments names from the function signature
                sig = inspect.signature(func_to_call)
                parameter_names = sig.parameters.keys()

                # parameter mapping with names to values
                parameter_mapping = dict(zip(parameter_names, parameter_values))

                # get model instance
                model_instance = parameter_mapping.get('self').model

                # get current epoch because epoch starts from 0
                current_epoch = parameter_mapping.get('epoch') + 1

                # get current epoch logs
                current_epoch_logs = parameter_mapping.get('logs')

                # notify if current_epoch is divisible by epoch_interval
                if current_epoch % epoch_interval == 0:
                    message = f"epoch: {current_epoch} started, got log keys:"
                    for k, v in current_epoch_logs.items():
                        message += " {}: {:.4f} ".format(k, v)
                    self.send_message(message)

                # notify if current_epoch is divisible by hardware_stats_interval
                if current_epoch % hardware_stats_interval == 0:
                    hardware_stats = TfNotifier.get_hardware_stats()
                    self.send_message(hardware_stats)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    history_copy = copy.deepcopy(model_instance.history.history)
                    file_path = TfNotifier.plot_graph(history_copy, current_epoch_logs)
                    # TODO: change this function call
                    self.send_file(file_path)

                return func_to_call(*args, **kwargs)

            return wrapper

        return inner

    def notify_on_epoch_end(self, epoch_interval, graph_interval, hardware_stats_interval):
        """
        Decorator which runs on end of the training model.

        Returns:
            Updated function
        """
        def inner(func_to_call):
            def wrapper(*args, **kwargs):

                # get parameter values
                parameter_values = list(args)
                for i in kwargs.values():
                    parameter_values.append(i)

                # get arguments names from the function signature
                sig = inspect.signature(func_to_call)
                parameter_names = sig.parameters.keys()

                # parameter mapping with names to values
                parameter_mapping = dict(zip(parameter_names, parameter_values))

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
                    self.send_message(message)

                # notify if current_epoch is divisible by hardware_stats_interval
                if current_epoch % hardware_stats_interval == 0:
                    hardware_stats = TfNotifier.get_hardware_stats()
                    self.send_message(hardware_stats)

                # notify graph if current_epoch is divisible by graph_interval
                if current_epoch % graph_interval == 0:
                    history_copy = copy.deepcopy(model_instance.history.history)
                    file_path = TfNotifier.plot_graph(history_copy, current_epoch_logs)
                    # TODO: change this function call
                    self.send_file(file_path)

                return func_to_call(*args, **kwargs)

            return wrapper

        return inner
