import time
import pyautogui
pyautogui.FAILSAFE = False

HOT_CORNER_SIZE = 2

class HotCorner:
    def __init__(self, location, hot_key):
        self.x = location[0]
        self.y = location[1]
        self.right = location[0] + HOT_CORNER_SIZE
        self.bottom = location[1] + HOT_CORNER_SIZE
        self.hot_key = hot_key

    def mouse_inside(self, mouse_x, mouse_y):
        if (mouse_x >= self.x and mouse_x <= self.right
                and mouse_y >= self.y and mouse_y <= self.bottom):
            return True
        return False

hot_corners = [
    # Top left corner - Trigger TaskView
    HotCorner(
        (0,0,),
        ('winleft', 'tab',)
    ),
    # Top left corner (second screen) - Trigger TaskView
    HotCorner(
        (1920,0,),
        ('winleft', 'tab',)
    ),
]

mouse_hot = False
while (True):
    mouse_x, mouse_y = pyautogui.position()
    for hot_corner in hot_corners:
        mouse_in_corner = hot_corner.mouse_inside(mouse_x, mouse_y)
        if not mouse_hot and mouse_in_corner:
            mouse_hot = True
            pyautogui.hotkey(*hot_corner.hot_key)
        elif mouse_hot and not mouse_in_corner:
            mouse_hot = False
    time.sleep(0.1)
