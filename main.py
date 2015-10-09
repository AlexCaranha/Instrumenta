import sys
import view.mainView

import pymouse
from screeninfo import get_monitors

from PySide.QtGui import *

def get_center_of_actual_monitor():
	mouse = pymouse.PyMouse()
	mouse_x, mouse_y = mouse.position()
	actual_monitor = None
	
	print("mouse.x: {0}, mouse.y: {1}".format(mouse_x, mouse_y))
	
	monitors = get_monitors()
	
	center_x = 0
	center_y = 0
	
	for iMonitor in range(0, len(monitors)):
		monitor = monitors[iMonitor]
		
		jMonitor = iMonitor
				
		monitor_left = monitor.x
		monitor_right = monitor.x + monitor.width
		
		print("\nmonitor: {0}, width: {1}".format(iMonitor, monitor.width))
		print("left: {0}, right: {1}".format(monitor_left, monitor_right))
		
		if monitor_left <= mouse_x and mouse_x < monitor_right:
			print("found")
			
			actual_monitor = monitor						
			
			center_x = int((monitor_left + monitor_right)/2)
			center_y = int((actual_monitor.y + actual_monitor.height)/2)
		
			break
			
	if actual_monitor == None:
		print("not found")
		return None, None, None, None
	
	return center_x, center_y, actual_monitor.width, actual_monitor.height

app = QApplication(sys.argv)
screen = app.desktop().screen()

#window = view.mainView.MainWindow(screen.rect().width()/3, screen.rect().height()/5)
#window.show()
#window.adjustSize()
#window.move(app.desktop().screen().rect().center() - window.rect().center())

center_x, center_y, monitor_width, monitor_height = get_center_of_actual_monitor()

if not center_x == None and not center_y == None:
	print("------")
	print("monitor.width: {0}, monitor.height: {1}".format(monitor_width, monitor_height))
	print("center_x: {0}, center_y: {1}".format(center_x, center_y))
	print("------")
	
	window_width = int(monitor_width/3)
	window_height = int(monitor_height/5)
	
	window = view.mainView.MainWindow(window_width, window_height)
	window.show()
	window.adjustSize()
	window.move(center_x - int(window_width/2), center_y - int(window_height/2))

	sys.exit(app.exec_())

#pip3 install screeninfo
#pip3 install pyuserinput
