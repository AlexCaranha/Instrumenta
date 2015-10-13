# pip3 install screeninfo
# pip3 install pyuserinput
# pip3 install clipboard
# pip3 install pyhooked

import pymouse
from screeninfo import get_monitors

__author__ = 'lual'


def get_center_of_current_monitor():
    mouse = pymouse.PyMouse()
    mouse_x, mouse_y = mouse.position()

    # print("mouse.x: {0}, mouse.y: {1}".format(mouse_x, mouse_y))

    monitors = get_monitors()

    for iMonitor in range(0, len(monitors)):
        monitor = monitors[iMonitor]

        monitor_left = monitor.x
        monitor_right = monitor.x + monitor.width
        monitor_bottom = monitor.y
        monitor_top = monitor.y + monitor.height

        # print("monitor: {0}, width: {1}".format(iMonitor, monitor.width))
        # print("left: {0}, right: {1}".format(monitor_left, monitor_right))

        if monitor_left <= mouse_x < monitor_right and monitor_bottom <= monitor.y < monitor_top:
            x = int((monitor_left + monitor_right)/2)
            y = int((monitor.y + monitor.height)/2)
            return x, y, monitor.width, monitor.height

    return None, None, None, None
