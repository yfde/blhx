import pyautogui
import time
import win32gui
import win32com.client
from ctypes import *


hwnd_map = {}
front_window_index = 2


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
        and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})


class PointAPI(Structure):
    #PointAPI类型,用于获取鼠标坐标
    _fields_ = [("x", c_ulong), ("y", c_ulong)]


def getpos():
    "获取当前鼠标位置。"
    po = PointAPI()
    windll.user32.GetCursorPos(byref(po))  # 传递数据类型的引用
    x = po.x
    y = po.y
    if x > pow(2, 16):
        x -= pow(2, 32)
    if y > pow(2, 16):
        y -= pow(2, 32)
    return x, y


def click(p):
    global hwnd_map
    time.sleep(1.5)
    x, y = getpos()
    print("mouse: ", x, y)
    hwnd_map = {}
    win32gui.EnumWindows(get_all_hwnd, 0)
    i = 1
    for h, t in hwnd_map.items():
        if t:
            if i == front_window_index:
                print("windows: ", t)
                fw = h
                break
            i += 1

    pyautogui.click(p[0], p[1], duration=0.01)
    # time.sleep(0.01)

    win32gui.EnumWindows(get_all_hwnd, 0)
    for h, t in hwnd_map.items():
        if t:
            if h == fw:
                win32gui.BringWindowToTop(h)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.SendKeys('%')
                win32gui.SetForegroundWindow(h)
    windll.user32.SetCursorPos(x, 500)
    windll.user32.SetCursorPos(x, y)
    time.sleep(1.5)


def check(p, color):
    current_color = pyautogui.screenshot().getpixel((p[0], p[1]))
    if (current_color[0] == color[0]) and (current_color[1] == color[1]) \
            and (current_color[2] == color[2]):
        return True
    return False


def until(p, color, refresh=[0, 0], stop=60):
    i = 0
    while True:
        if check(p, color):
            break
        if refresh[0] != 0 and refresh[1] != 0:
            click(refresh)
        if i == stop:
            break
        i += 1
        time.sleep(3)


def click_area(img, dx=0, dy=0):
    location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    if location is not None:
        click([location.x + dx, location.y + dy])
    else:
        print('clicking_failed')


def check_area(img):
    time.sleep(0.5)
    location = pyautogui.locateCenterOnScreen(img, confidence=0.8)
    if location is not None:
        print(location.x, location.y)
        time.sleep(1)
        return True
    time.sleep(1)
    return False


def until_area(img, stop=6):
    i = 0
    while True:
        if check_area(img):
            break
        if i == stop:
            break
        i += 1
