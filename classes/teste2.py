from Xlib.display import Display
from Xlib import X
# import oss

# custom keys from my dell D400 Laptop

vol_plus  = 176
vol_moins = 174

keys = [vol_plus, vol_moins]


def handle_event():
    print("Hello")

def main():
    # current display
    disp = Display()
    root = disp.screen().root

    # we tell the X server we want to catch keyPress event
    root.change_attributes(event_mask = X.KeyPressMask)

    for keycode in keys:
        root.grab_key(keycode, X.AnyModifier, 1,X.GrabModeAsync, X.GrabModeAsync)

    while 1:
        event = root.display.next_event()
        handle_event(event)

if __name__ == '__main__':
    main()