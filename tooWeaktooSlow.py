# The purpose of this bot is to cick the first black pixel.
# Testing a change here done by Git. 
# changes through branches

import pyautogui
import keyboard
import win32api
import win32con
import time

# click function, with a 0.01 pause inorder to properly run the script


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


# pressing 's' to stop the function

while keyboard.is_pressed('s') == False:

    # If the pixel is black (0), click on that pixel

    if pyautogui.pixel(xPosition, yPosition)[0] == 0:
        click(xPosition, yPosition)
