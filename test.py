import win32gui
import win32con
import win32com.client
import time
from ctypes import *


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
        and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_map.update({hwnd: win32gui.GetWindowText(hwnd)})


hwnd_map = {}
win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_map.items():
    if t:
        # h 为想要放到最前面的窗口句柄
        print(t, h)
        # 被其他窗口遮挡，调用后放到最前面
        if t == 'xxx碧蓝航线 - MuMu模拟器':
            win32gui.BringWindowToTop(h)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')

            win32gui.SetForegroundWindow(h)
            # 解决被最小化的情况
            # win32gui.ShowWindow(h, win32con.SW_RESTORE)
            time.sleep(1)


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


x, y = getpos()


print(x, y)
windll.user32.SetCursorPos(1000, 500)
windll.user32.SetCursorPos(x, 500)
windll.user32.SetCursorPos(x, y)
