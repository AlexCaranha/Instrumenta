from PySide.QtCore import *
from PySide.QtGui import *
# from PySide.QtGui import QTextEdit

# import pyautogui
# mouse e teclado: http://pyautogui.readthedocs.org/en/latest/mouse.html


__author__ = 'lual'


class MainWindow(QWidget):
    def __init__(self, width, height, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("Instrumenta")
        self.setMinimumSize(width, height)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("Input search here..")
        self.edit.installEventFilter(self)

        self.list = QListView(self)

        model = QStandardItemModel(self.list)
        for i in range(10):
            text = 'Item {0}'.format(i + 1)
            item = QStandardItem(text)
            item.setCheckable(True)
            model.appendRow(item)

        self.list.setModel(model)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.list)
        self.setLayout(layout)

        self.edit.setFocus()

    def eventFilter(self, widget, event):
        if widget is self.edit and event.type() == QEvent.KeyRelease:
            #print("keyPressed: {0}".format(event.key()))
            print("texto: {0}".format(widget.text()))

        return False
