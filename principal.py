# -*- coding: utf-8 -*-

try:
    from PySide import QtCore
    from PySide import QtWidgets
except:
    from PyQt4.QtCore import pyqtSlot as Slot
    from PyQt4 import QtCore
    from PyQt4 import QtWidgets


class principal(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        pass
