import sys
import view.mainView
import classes.util

from PySide.QtGui import *
from pyhooked import hook

__author__ = 'Alex Libório Caranha'


class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.app.setWindowIcon(QIcon('ico/tool.png'))

        self.__config_menu__()
        self.__config_tray__()
        self.__config_main_window__()

        self.hk = hook()
        self.hk.Hotkey(["LCtrl", "LAlt", "Space"], self.show)

    def __del__(self):
        self.hk.RemHotKey(self.show)

    def __config_menu__(self):
        self.menu = QMenu()

        show_action = self.menu.addAction("&Show")
        show_action.setShortcut('Ctrl+2')
        show_action.triggered.connect(self.show)

        setting_action = self.menu.addAction("setting")
        # setting_action.triggered.connect(self.setting)

        exit_action = self.menu.addAction("exit")
        exit_action.triggered.connect(self.quit)

    def __config_tray__(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon('ico/tool.png'))
        self.tray.setContextMenu(self.menu)
        self.tray.show()
        self.show_short_message("Begin")

    def __config_main_window__(self):
        center_x, center_y, monitor_width, monitor_height = classes.util.get_center_of_current_monitor()
        window_width = int(monitor_width/3)
        window_height = int(monitor_height/5)

        self.main_window = view.mainView.MainWindow(self)
        self.main_window.setMinimumSize(window_width, window_height)
        self.main_window.adjustSize()
        self.main_window.move(center_x - int(window_width/2), center_y - int(window_height/2))

    def run(self):
        self.app.exec_()

    def quit(self):
        self.show_short_message("End")
        sys.exit()

    def show(self):
        self.main_window.show()

    def show_short_message(self, message="", ico=QSystemTrayIcon.Information, time_in_seconds=1):
        self.tray.showMessage(
            "Instrumenta",
            message,
            ico,
            time_in_seconds * 10)

if __name__ == "__main__":
    app = App()
    app.run()
