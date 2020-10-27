import inspect
import json
import threading
from urllib.request import urlopen, Request


class Notifier:
    """Discord API webhooks wrapper"""
    def __init__(self, url):
        self.__url = url
        self.__timers = {}
        self.__headers = {
            "Content-Type": "application/json",
            "User-Agent": "webhook"
        }

    def send(self, message, print_message=True):
        data = {
            "content": str(message)
        }
        request = Request(
            self.__url,
            json.dumps(data).encode("utf-8"),
            self.__headers
        )
        urlopen(request)
        if print_message:
            print(message)

    def __message_func_exception(self, message_func):
        """Message Status"""
        if not callable(message_func):
            raise TypeError("message_func is not callable.")
        if len(inspect.signature(message_func).parameters) > 0:
            raise TypeError("message_func must not have any parameters")
        if message_func() is None:
            raise TypeError("message_func must return a value.")

    def __send_repeat(self, message_func, interval, timer_id, print_message, daemon):
        """Repeat sending message_func without adding a new timer_id"""
        self.__message_func_exception(message_func)

        if timer_id in self.__timers:
            self.__timers[timer_id] = threading.Timer(
                interval, 
                self.__send_repeat, 
                args=[message_func, interval, timer_id, print_message, daemon]
            )

        if timer_id in self.__timers:  # timer_id may have been deleted by now
            self.send(message_func(), print_message)

        if timer_id in self.__timers:  # timer_id may have been deleted by now
            self.__timers[timer_id].daemon = daemon
            self.__timers[timer_id].start()

    def send_repeat(self, message_func, interval, print_message=True, daemon=True):
        """Repeatedly executes a webhook on a separate timer thread
        
        Arguments:
            - message_func: A callable that returns a message to send
            - interval (float): The number of seconds to wait between sends
            - print_message (bool): Whether or not the message should be
              printed to the console (default: True)
            - daemon (bool): Whether or not the timer should be a daemon thread 
              that automatically terminates with the main thread (default: True)
        Returns:
            The ID number of the timer thread created
        """
        self.__message_func_exception(message_func)

        if len(self.__timers) == 0:
            timer_id = 0
        else:
            max_timer_id = max(self.__timers.keys())
            timer_id = max_timer_id + 1
            for i in range(max_timer_id + 1):
                if i not in self.__timers:
                    timer_id = i
                    break

        self.__timers[timer_id] = threading.Timer(
            interval, 
            self.__send_repeat, 
            args=[message_func, interval, timer_id, print_message, daemon]
        )
        self.send(message_func(), print_message)
        self.__timers[timer_id].daemon = daemon
        self.__timers[timer_id].start()
        return timer_id

    def stop_repeat(self, timer_id):
        """Stops a timer from repeating webhook execution
        
        Arguments:
            - timer_id: The ID number of the timer to stop
        """
        if timer_id in self.__timers:
            self.__timers[timer_id].cancel()
            del self.__timers[timer_id]