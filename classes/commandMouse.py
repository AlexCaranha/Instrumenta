from pymouse import PyMouse
import re
import classes.util as util

__author__ = 'Alex Libório Caranha'


class CommandMouse:
    def __init__(self, main_window):
        self.mainWindow = main_window
        self.mouse = PyMouse()

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

        return False
