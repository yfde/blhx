from utils import click
from utils import check
from utils import until
from utils import click_area
from utils import check_area
from utils import until_area
import time


# （旧版）活动出击，刷贡献值
def activity_attack():
    pos = [
        [1498, 820],  # 第一点坐标
        [460,  363],  # 第二点坐标
        # [428,  354],  # ex模式
        [1332, 854],  # 第三点坐标
        ]
    until(pos[0], [255, 255, 255])
    click(pos[0])
    until(pos[1], [247, 239, 156])  # 第二点颜色
    # until(pos[1], [247, 247, 173])  # ex模式
    click(pos[1])
    click(pos[1])
    click(pos[1])
    until(pos[2], [255, 255, 255])
    click(pos[2])


# 退役清理船坞
def retire():
    images = [
        "full.png",  # 0
        "retire.png",  # 1
        "confirm.png",  # 2
        "continue.png",  # 3
        "exit_retire.png",  # 4
        "auto_off.png",  # 5
        "confirm_4star.png"  # 6
    ]
    click_area(images[0])
    until_area(images[1])
    click_area(images[1])
    until_area(images[2])
    click_area(images[2])
    if check_area(images[6]):
        click_area(images[6])
    until_area(images[3])
    click_area(images[3])
    until_area(images[2])
    click_area(images[2])
    until_area(images[2])
    click_area(images[2])
    until_area(images[3])
    click_area(images[3])
    until_area(images[4])
    click_area(images[4])
    until_area(images[5])
    click_area(images[5], dy=55)


# 主线出击，单图挂机
def main_attack(auto_retire=True):
    images = [
        "full.png",  # 0
        "play_again.png"  # 1
    ]
    click_area(images[1])
    while(True):
        if check_area(images[0]):
            if auto_retire:
                retire()
        time.sleep(3)
        if check_area(images[1]):
            break
        time.sleep(3)


# 演习出击
def pvp():
    images = [
        "opponent.png",  # 0
        "start.png",  # 1
        "attack.png",  # 2
        "continue2.png",  # 3
        "continue.png",  # 4
        "confirm2.png"  # 5
    ]
    until_area(images[0])
    click_area(images[0])
    until_area(images[1])
    click_area(images[1])
    until_area(images[2])
    click_area(images[2])
    while(True):
        if check_area(images[3]):
            click_area(images[3])
            until_area(images[4])
            click_area(images[4])
            until_area(images[5])
            click_area(images[5])
            break


if __name__ == '__main__':
    mode = input("""
    which mode?
    1:main_attack()
    2:pvp()
    3:activity_attack()
    """)
    i = 0
    while(True):
        print("attacked", i, "times")
        if mode == "1":
            main_attack()
        if mode == "2":
            pvp()
        if mode == "3":
            activity_attack()
        i += 1


# improve:
# 1. after click, move mouse back to its original position
# 2. can this script be done in background?
