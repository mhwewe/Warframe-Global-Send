import time
from pynput import mouse
from screeninfo import get_monitors
import pypercliper
from pynput.keyboard import Key, Controller
import keyboard as keyb
from ahk import AHK
import cv2
import pyscreenshot as ImageGrab
import numpy as np

ahk = AHK()

keyboard = Controller()
mousee = mouse.Controller()

got_monitor = get_monitors()

for m in got_monitor:
    if m.is_primary:
        monitor_width = m.width
        monitor_height = m.height
        print(f"{monitor_width}// {monitor_height}")

def ratio_func(width, height):
    mulw = width/2560
    mulh = height/1440
    tup = (int(monitor_width*mulw)+5, int(monitor_height*mulh)+5)
    # print(monitor_height)
    # print(monitor_width)
    print(f"tuple from ratio_func: {tup}")
    return tup

def ratio_func2(x, y, width, height):
    mulw = width / 2560
    mulh = height / 1440

    mulx = x/2560
    muly = y/1440

    tup = (int(monitor_width * mulx), int(monitor_height * muly), int(monitor_width * mulw)+5, int(monitor_height * mulh)+5)
    print(f"tuple from ratio_func2: {tup}")
    return tup


def ratio_funcx(x):
    mulx = x/2560
    return int(mulx * monitor_width)+5

def ratio_funcy(y):
    muly = y/1440
    return int(muly * monitor_height)+5



def press_region():
    im = ImageGrab.grab(bbox=ratio_func2(0, 400, 300, 900))
    # im.show()

    im.save("images\\options_full.png")

    img_rgb = cv2.imread("images\\options_full.png")
    template = cv2.imread(f"images\\{monitor_height}region.png")

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1], loc[0][-1] + ratio_funcy(400))  # Region select


def press_confirm():
    im = ImageGrab.grab(bbox=ratio_func2(1700, 1000, 2560, 1440))
    # im.show()

    im.save("images\\options_full.png")

    img_rgb = cv2.imread("images\\options_full.png")
    template = cv2.imread(f"images\\{monitor_height}confirm.png")

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1] + ratio_funcx(1700), loc[0][-1] + ratio_funcy(1000))  # Confirm



def press_find():
    im = ImageGrab.grab(bbox=ratio_func2(0, 1200, 500, 1440))
    # im.show()

    im.save("images\\options_full.png")

    img_rgb = cv2.imread("images\\options_full.png")
    template = cv2.imread(f"images\\{monitor_height}find.png")

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCORR_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1], loc[0][-1] + ratio_funcy(1200))


def press_system():
    im = ImageGrab.grab(bbox=ratio_func2(0, 0, 860, 400))
    # im.show()

    im.save("images\\options_full.png")

    img_rgb = cv2.imread("images\\options_full.png")
    template = cv2.imread(f"images\\{monitor_height}system.png")

    w, h = template.shape[:-1]

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)

    mousee.position = (loc[1][-1], loc[0][-1])  # chat select bottom

def press_options():
    im = ImageGrab.grab(bbox=(ratio_func2(0, 700, 860, 1340)))
    im.save("images\\options_full.png")

    print(f"images\\{monitor_height}options.png")
    img_rgb = cv2.imread("images\\options_full.png")
    template = cv2.imread(f"images\\{monitor_height}options.png")

    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .8
    loc = np.where(res >= threshold)
    print(loc[1][-1], loc[0][-1])

    mousee.position = (loc[1][-1], loc[0][-1] + ratio_funcy(700))


def change_n_paste():

    press_region()
    time.sleep(0.4)
    ahk.click()

    press_confirm()
    time.sleep(0.2)
    ahk.click()

    keyboard.press(Key.esc)
    keyboard.release(Key.esc) #leave the chat to press options
    time.sleep(3.5)

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

    s = pypercliper.paste()
    keyboard.type(s)  # DO NOT ENABLE IN TESTING (:
    # print(s)
    # keyboard.press(Key.enter); keyboard.release(Key.enter)



while True:
    if keyb.is_pressed('down arrow'):
        s = pypercliper.paste()
        keyboard.type(s)
        time.sleep(0.4)

    if keyb.is_pressed('left arrow'):
        print(mousee.position)
        time.sleep(0.4)

    if keyb.is_pressed('up arrow'):

        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(1)

        press_options()
        time.sleep(0.4)
        ahk.click()
        print("press options done")

        time.sleep(0.5)
        press_system()
        time.sleep(0.2)
        ahk.click()
        print("press system done")

        press_find()
        time.sleep(0.2)
        ahk.click()
        time.sleep(0.2)

        s = pypercliper.paste()
        keyboard.type(s) #DO NOT ENABLE IN TESTING (:
        time.sleep(0.4)
        # keyboard.press(Key.enter); keyboard.release(Key.enter)
        time.sleep(0.4)
        if keyb.is_pressed('up arrow'):
            print("nuh")

        for i in range(0,4):
            change_n_paste()
            time.sleep(0.4)
            if keyb.is_pressed('up arrow'):
                break

        time.sleep(0.4)
    time.sleep(0.1)