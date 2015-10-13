import webbrowser
import time
import re

import classes.commandMouse as cm
import classes.commandKeyboard as ck

__author__ = 'Alex Libório Caranha'


class Command:
    def __init__(self, main_window):
        self.mainWindow = main_window
        self.commandMouse = cm.CommandMouse(main_window)
        self.commandKeyboard = ck.CommandKeyboard(main_window)

    def execute(self, message):
        message = message.lower()

        if self.commandMouse.execute(message):
            return

        if self.commandKeyboard.execute(message):
            return

        if "sair" == message:
            while not self.mainWindow.thread.isFinished() or not self.mainWindow.thread.isClosed():
                time.sleep(1)

            self.mainWindow.app.quit()
            return

        if "mensagem curta" in message:
            short_message = message[len("short message "):]
            self.mainWindow.app.show_short_message(short_message)
            return

        if "mostrar" == message:
            self.mainWindow.show()
            return

        result = re.match("não mostrar|esconder", message)
        if result is not None:
            self.mainWindow.hide()
            return

        if "abrir site" in message:
            text = message.replace("abrir site ", "")
            webbrowser.open_new_tab("https://" + text)
            return

        if "significado de" in message:
            text = message.replace("significado de ", "")
            path = "www.priberam.pt/DLPO/{0}".format(text)
            self.execute("abrir site {0}".format(path))