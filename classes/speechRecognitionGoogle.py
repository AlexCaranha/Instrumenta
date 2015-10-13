import speech_recognition as sr

from PySide.QtCore import *

__author__ = 'Alex Libório Caranha'


class MySignal(QObject):
    sig = Signal(str)


class ThreadSpeechRecognition(QThread):

    def __init__(self, parent = None):
        QThread.__init__(self, parent)

        self.signal = MySignal()

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def run(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {0}".format(self.recognizer.energy_threshold))

            message = ""
            while True:
                audio = self.recognizer.listen(source)

                try:
                    message = self.recognizer.recognize_google(audio, language="pt-BR")
                    print(message)

                    if "sair" == message:
                        break

                    self.signal.sig.emit(message)

                except sr.UnknownValueError:
                    self.signal.sig.emit("Não entendi!")

                except sr.RequestError as e:
                    self.signal.sig.emit("Não foi possível obter resultados a partir do serviço de reconhecimento de fala da Google; {0}".format(e))

        self.signal.sig.emit(message)