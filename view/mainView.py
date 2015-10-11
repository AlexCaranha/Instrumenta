from PySide.QtCore import *
from PySide.QtGui import *
# from PySide.QtGui import QTextEdit

# import pyautogui
# mouse e teclado: http://pyautogui.readthedocs.org/en/latest/mouse.html


__author__ = 'Alex Libório Caranha'


class MainWindow(QWidget):
    def __init__(self, app, parent=None):
        super(MainWindow, self).__init__(parent)

        self.app = app;
        self.setWindowIcon(QIcon('ico/tool.png'))
        self.setWindowTitle("Instrumenta")

        self.__config_text_edit__()
        self.__config_list_view__()
        self.__config_layout__()

        self.edit.setFocus()

    def __config_text_edit__(self):
        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Input search here..")
        self.edit.installEventFilter(self)

    def __config_list_view__(self):
        self.list = QListView(self)

        model = QStandardItemModel(self.list)
        for i in range(5):
            text = 'Item {0}'.format(i + 1)
            item = QStandardItem(text)
            item.setCheckable(True)
            model.appendRow(item)

        self.list.setModel(model)

    def __config_layout__(self):
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.list)

        self.setLayout(layout)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
        # self.app.show_short_message('Running in the background.')

    def eventFilter(self, widget, event):
        if widget is self.edit and event.type() == QEvent.KeyPress:
            key = event.key()
            text = widget.text()

            if key == Qt.Key_Return:
                self.command(text)

        if widget is self.edit and event.type() == QEvent.KeyRelease:
            key = event.key()
            text = widget.text()

            print("keyPressed: {0}, texto: {1}".format(key, text))

        return False

    def command(self, text):
        if "short message " in text:
            short_message = text[len("short message "):]
            self.app.show_short_message(short_message)
