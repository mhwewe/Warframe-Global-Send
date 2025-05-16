import os
from os import path
import time
from pynput import mouse
from screeninfo import get_monitors
from pynput.keyboard import Key, Controller
import keyboard as keyb
from ahk import AHK
import cv2
from PIL import ImageGrab
import numpy as np
from tkinter import Tk
from pathlib import Path

ahk = AHK()
keyboard = Controller()
mousee = mouse.Controller()
got_monitor = get_monitors()


def paste():
    s = Tk().clipboard_get()
    keyboard.type(f"{s} (sent using Warframe Global Send, GitHub)")  # DO NOT ENABLE IN TESTING (:
    print("sent the message")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


def pather(pathh):
    return path.abspath(path.join(path.dirname(__file__), pathh))


for m in got_monitor:
    if m.is_primary:
        monitor_width = m.width
        monitor_height = m.height
        # print(f"{monitor_width}// {monitor_height}")
        os.system('cls')
        print("APP STARTED\nCopy the message you want to send like: 'LF/H [axi a5 relic] Rad'\nThen in your orbiter while you can freely move your camera press up arrow key")


def ratio_func(width, height):
    mulw = width/2560
    mulh = height/1440
    tup = (int(monitor_width*mulw)+5, int(monitor_height*mulh)+5)
    # print(monitor_height)
    # print(monitor_width)
    # print(f"tuple from ratio_func: {tup}")
    return tup


def ratio_func2(x, y, width, height):
    # print("entered def ratio_func2")
    mulw = width / 2560
    mulh = height / 1440

    mulx = x/2560
    muly = y/1440
    # print("passed mul*")

    tup = (int(monitor_width * mulx), int(monitor_height * muly), int(monitor_width * mulw)+5, int(monitor_height * mulh)+5)
    # print("made the tuple")
    # print(tup)
    # print(f"tuple from ratio_func2: {tup}")
    return tup


def ratio_funcx(x):
    mulx = x/2560
    return int(mulx * monitor_width)+5


def ratio_funcy(y):
    muly = y/1440
    return int(muly * monitor_height)+5


tried: int = 1

def uhhh(loc):
    # print("using uhhh")
    global tried

    # print(tried)
    try:
        if loc[1][-1]:
            # print("if loc[1][-1]")
            if tried == 1:
                # print("if tried == 1:")
                # print(tried)
                pass
            else:
                # print("else")
                # print(tried)
                tried = 1
                # print("checked")

                press_confirm()
                time.sleep(0.2)
                ahk.click()
                # print("pressed confirm after check NA")

                time.sleep(3)
                press_options()
                time.sleep(0.2)
                ahk.click()

                time.sleep(0.4)
                press_system()
                time.sleep(0.2)
                ahk.click()
    except Exception:
        print("nuh")
        tried += 1
        press_region()
        ahk.click()
        check_na()


def check_na():
    # print("using check_na")
    global tried
    im = ImageGrab.grab(bbox=ratio_func2(0, 0, 1560, 1440))
    im.save(pather("images\\options_full.png"))

    img_rgb = cv2.imread(pather("images\\options_full.png"))
    template = cv2.imread(pather(f"images\\{monitor_height}north.png"))

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCORR_NORMED)
    threshold = .9
    loc = np.where(res >= threshold)

    uhhh(loc)


def press_region():
    im = ImageGrab.grab(bbox=ratio_func2(0, 400, 300, 900))
    # im.show()

    im.save(pather("images\\options_full.png"))

    img_rgb = cv2.imread(pather("images\\options_full.png"))
    template = cv2.imread(pather(f"images\\{monitor_height}region.png"))

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1] + ratio_funcx(170), loc[0][-1] + ratio_funcy(400))  # Region select


def press_confirm():
    im = ImageGrab.grab(bbox=ratio_func2(1700, 1000, 2560, 1440))
    # im.show()

    im.save(pather("images\\options_full.png"))

    img_rgb = cv2.imread(pather("images\\options_full.png"))
    template = cv2.imread(pather(f"images\\{monitor_height}confirm.png"))

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1] + ratio_funcx(1700), loc[0][-1] + ratio_funcy(1000))  # Confirm


def press_find():
    im = ImageGrab.grab(bbox=ratio_func2(0, 1200, 500, 1440))
    # im.show()

    im.save(pather("images\\options_full.png"))

    img_rgb = cv2.imread(pather("images\\options_full.png"))
    template = cv2.imread(pather(f"images\\{monitor_height}find.png"))

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCORR_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1], loc[0][-1] + ratio_funcy(1200))


def press_system():
    im = ImageGrab.grab(bbox=ratio_func2(0, 0, 860, 400))
    # im.show()

    im.save(pather("images\\options_full.png"))

    img_rgb = cv2.imread(pather("images\\options_full.png"))
    template = cv2.imread(pather(f"images\\{monitor_height}system.png"))

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1], loc[0][-1])  # chat select bottom

def press_options():
    # print("now in press_options func")
    # im = ImageGrab.grab(bb`ox=(0, 700, 860, 1340))
    im = ImageGrab.grab(bbox=(ratio_func2(0, 700, 860, 1340)))
    # print("just took the SS")
    im.save(pather("images\\options_full.png"))
    # print("saved the SS")

    # print(f"images\\{monitor_height}options.png")
    img_rgb = cv2.imread(pather("images\\options_full.png"))
    # print("img_rgb imread")
    template = cv2.imread(pather(f"images\\{monitor_height}options.png"))
    # print("template imread")

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCORR_NORMED)
    # print("res")
    threshold = .8
    loc = np.where(res >= threshold)
    # print("loc")

    mousee.position = (loc[1][-1], loc[0][-1] + ratio_funcy(700))
    # print("mouse moved")


def change_n_paste():

    press_region()
    time.sleep(0.4)
    ahk.click()

    press_confirm()
    time.sleep(0.2)
    ahk.click()

    keyboard.press(Key.esc)
    keyboard.release(Key.esc) #leave the chat to press options
    time.sleep(1)
    try:
        press_options()
    except Exception:
        time.sleep(1)
        try:
            press_options()
        except Exception:
            time.sleep(1)
            try:
                press_options()
            except Exception:
                pass

    press_options()
    time.sleep(0.4)
    ahk.click()

    time.sleep(0.5)
    press_system()
    time.sleep(0.2)
    ahk.click()

    press_find()
    time.sleep(0.2)
    ahk.click()
    time.sleep(0.2)

    paste()


while True:
    if keyb.is_pressed('down arrow'):
        s = Tk().clipboard_get()
        keyboard.type(s)
        time.sleep(0.4)

    if keyb.is_pressed('left arrow'):
        print(mousee.position)
        time.sleep(0.4)

    if keyb.is_pressed('up arrow'):

        # print("up pressed")

        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        # print("esc pressed")
        time.sleep(1)

        press_options()
        time.sleep(0.4)
        ahk.click()
        print("pressed options")

        time.sleep(0.5)
        press_system()
        time.sleep(0.2)
        ahk.click()
        print("pressed system")

        time.sleep(0.2)
        check_na()
        print("NA alright")
        time.sleep(0.2)



        press_find()
        time.sleep(0.2)
        ahk.click()
        print("pressed find")
        time.sleep(0.2)

        paste()

        time.sleep(0.4)


        if keyb.is_pressed('up arrow'):
            print("nuhhhh")

        for i in range(0,4):
            change_n_paste()
            time.sleep(0.4)
            if keyb.is_pressed('up arrow'):
                break
        press_region()
        time.sleep(0.2)
        ahk.click()
        time.sleep(0.2)
        ahk.click()
        time.sleep(0.2)
        ahk.click()
        time.sleep(0.2)
        press_confirm()
        time.sleep(0.2)
        ahk.click()

        time.sleep(0.4)
    time.sleep(0.1)