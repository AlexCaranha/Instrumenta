import sys
from PyQt5.QtWidgets import *


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edt_search = QLineEdit()
        list_result = QTextEdit()

        edt_search.keyPressEvent(self.keyPressEvent123)

        layout = QVBoxLayout()
        layout.addWidget(edt_search)
        layout.addWidget(list_result)

        self.setLayout(layout)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Instrumenta')
        self.show()

    def keyPressEvent123(self):
        sender = self.sender()
        self.statusBar().showMessage("{0} : {1}".format(sender.text(), event.key()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
