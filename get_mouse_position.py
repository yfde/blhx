import pyautogui
import time


def current_position():
    while(True):
        x, y = pyautogui.position()
        print(x, y, pyautogui.screenshot().getpixel((x, y)))
        time.sleep(0.5)


def fixed_position():
    position = [
        [1260, 818],
        [1498, 820]
        ]
    for p in position:
        print(p[0], p[1], pyautogui.screenshot().getpixel((p[0], p[1])))


if __name__ == '__main__':
    current_position()
