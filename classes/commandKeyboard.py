from pykeyboard import PyKeyboard
import clipboard

__author__ = 'Alex Libório Caranha'


class CommandKeyboard:
    def __init__(self, main_window):
        self.mainWindow = main_window
        self.keyboard = PyKeyboard()

    def execute(self, message):
        if "entrar" in message:
            self.keyboard.tap_key(self.keyboard.enter_key)
            return True

        if "fechar aba" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('w')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "nova janela" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('n')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "nova aba" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('t')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "endereço" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('l')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "salvar" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('s')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "imprimir" == message:
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('p')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        if "texto" in message:
            text = message.replace("texto ", "")
            clipboard.copy(text)
            # self.keyboard.type_string(text)
            self.keyboard.press_key(self.keyboard.control_key)
            self.keyboard.tap_key('v')
            self.keyboard.release_key(self.keyboard.control_key)
            return True

        return False
