from pymouse import PyMouse
from pykeyboard import PyKeyboard

import webbrowser
import clipboard
import classes.util as util
import time

__author__ = 'Alex Libório Caranha'


class Command:
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.mouse = PyMouse()
        self.keyboard = PyKeyboard()

        center_x, center_y, self.monitor_width, self.monitor_height = util.get_center_of_current_monitor()

    def execute(self, message):
        message = message.lower()

        if "short message " in message:
            short_message = message[len("short message "):]
            self.mainWindow.app.show_short_message(short_message)

        elif "comando mostrar" == message:
            self.mainWindow.show()

        elif "comando esconder" == message:
            self.mainWindow.hide()

        elif "comando mouse no centro" == message:
            center_x, center_y, monitor_width, monitor_height = util.get_center_of_current_monitor()
            self.mouse.move(center_x, center_y)

        elif "comando mouse direita" == message:
            x, y = self.mouse.position()
            x = x + 1 if x < self.monitor_width else x

            self.mouse.move(x + 1, y)

        elif "comando mouse esquerda" == message:
            x, y = self.mouse.position()
            x = x - 1 if x > 0 else x

            self.mouse.move(x - 1, y)

        elif "comando enter" in message:
            self.keyboard.tap_key(self.keyboard.enter_key)

        elif "comando abrir site" in message:
            text = message.replace("comando abrir site ", "")
            webbrowser.open_new_tab("https://" + text)

        elif "comando fechar aba" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('w')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando nova janela" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('n')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando nova aba" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('t')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando endereço" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('l')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando salvar" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('s')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando significado de" in message:
            text = message.replace("comando significado de ", "")
            caminho = "www.priberam.pt/DLPO/{0}".format(text)
            self.execute("comando abrir site {0}".format(caminho))

        elif "comando texto" in message:
            text = message.replace("comando texto ", "")
            clipboard.copy(text)
            # self.keyboard.type_string(text)
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('v')
            self.keyboard.release_key(self.keyboard.control_key)

        elif "comando sair" == message:
            while not self.mainWindow.thread.isFinished():
                time.sleep(1)

            self.mainWindow.app.quit()
