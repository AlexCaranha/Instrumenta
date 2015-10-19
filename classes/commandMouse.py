from pymouse import PyMouse
import re
import classes.util as util
import threading
import time

__author__ = 'Alex Libório Caranha'


class CommandMouse:
    def __init__(self, main_window):
        self.mainWindow = main_window
        self.mouse = PyMouse()
        self.delay = 50 / 1000
        self.thread = None
        self.new_thread()

    def new_thread(self):
        self.thread = CommandMouseThread(mouse=self.mouse, delay=self.delay, parent=self)     # in miliseconds.

    def execute(self, message):
        center_x, center_y, self.monitor_width, self.monitor_height = util.get_center_of_current_monitor()

        if "mouse no centro" == message:
            center_x, center_y, monitor_width, monitor_height = util.get_center_of_current_monitor()
            self.mouse.move(center_x, center_y)
            return True

        result = re.match("mouse direita em (\d+)", message)
        if result is not None:
            variation_x = int(result.group(1))

            x, y = self.mouse.position()
            x += variation_x

            self.mouse.move(x, y)
            return True

        result = re.match("mouse esquerda em (\d+)", message)
        if result is not None:
            variation_x = int(result.group(1))

            x, y = self.mouse.position()
            x -= variation_x

            self.mouse.move(x, y)
            return True

        result = re.match("mouse em (\d+) e (\d+)", message)
        if result is not None:
            x = int(result.group(1))
            y = int(result.group(2))

            self.mouse.move(x, y)
            return True

        result = re.match("parar|stop", message)
        if result is not None:
            self.thread.set_stop(value=True)

        result = re.match("clique|clicar|click", message)
        if result is not None:
            x, y = self.mouse.position()
            self.mouse.click(x, y, button=1)

        result = re.match("duplo clique|duplo click|clicar duas vezes|click duplo", message)
        if result is not None:
            x, y = self.mouse.position()
            self.mouse.click(x, y, button=1, n=2)

        result = re.match("clique direito|clicar botão direito|click direito", message)
        if result is not None:
            x, y = self.mouse.position()
            self.mouse.click(x, y, button=2)

        if "clicar" == message:
            x, y = self.mouse.position()
            self.mouse.click(x, y, button=1)

        if "mouse para direita" == message:
            self.thread.mouse_right()
            if not self.thread.is_running():
                self.thread.start()

        if "mouse para esquerda" == message:
            self.thread.mouse_left()
            if not self.thread.is_running():
                self.thread.start()

        if "mouse para cima" == message:
            self.thread.mouse_up()
            if not self.thread.is_running():
                self.thread.start()

        if "mouse para baixo" == message:
            self.thread.mouse_down()
            if not self.thread.is_running():
                self.thread.start()

        if "mais rápido" == message:
            self.thread.set_delay(multiple=1/2)

        result = re.match("mais rápido (\d+) (vez|vezes)", message)
        if result is not None:
            value = int(result.group(1))
            self.thread.set_delay(multiple=1/value)

        result = re.match("mais devagar|mais lento", message)
        if result is not None:
            self.thread.set_delay(multiple=2)

        result = re.match("mouse mais lento (\d+) (vez|vezes)", message)
        if result is not None:
            self.thread.set_delay(multiple=result.group(1))

        return False


class CommandMouseThread(threading.Thread):
    def __init__(self, mouse, delay, parent):
        threading.Thread.__init__(self)

        self.mouse = mouse
        self.pixels = 1
        self.delay = delay
        self.stop = False
        self.var_x = 0
        self.var_y = 0
        self.running = False
        self.parent = parent

    def set_stop(self, value):
        self.stop = value

    def set_delay(self, multiple):
        self.delay *= multiple

    def mouse_right(self):
        self.var_x = +self.pixels
        self.var_y = 0

    def mouse_left(self):
        self.var_x = -self.pixels
        self.var_y = 0

    def mouse_up(self):
        self.var_x = 0
        self.var_y = -self.pixels

    def mouse_down(self):
        self.var_x = 0
        self.var_y = +self.pixels

    def is_running(self):
        return self.running

    def run(self):
        self.running = True

        while not self.stop:
            time.sleep(self.delay)

            x, y = self.mouse.position()
            x += self.var_x
            y += self.var_y

            self.mouse.move(x, y)

        self.running = False
        self.parent.new_thread()