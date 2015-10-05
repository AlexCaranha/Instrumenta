import sys
import view.mainView

from PySide.QtGui import *

app = QApplication(sys.argv)
screen = app.desktop().screen()

window = view.mainView.MainWindow(screen.rect().width()/3, screen.rect().height()/5)
window.show()
window.adjustSize()
window.move(app.desktop().screen().rect().center() - window.rect().center())

sys.exit(app.exec_())
