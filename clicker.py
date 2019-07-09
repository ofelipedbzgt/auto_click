import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True

big_cookie = (204, 367)
fhf_up = (570, 535)
fhf_dn = (570, 671)


def click_gc_loop():
    last_gc = 0
    last_fhf = 0
    while True:
        if keyboard.is_pressed('ctrl+f3'):
            main_loop()
        else:
            pyautogui.click(big_cookie)
            if (time.time() - last_gc) > 135:
                gc = pyautogui.locateOnScreen('images/gc2.png', confidence=0.93)
                if gc is not None:
                    pyautogui.click(pyautogui.center(gc))
                    time.sleep(1)
                    last_gc = time.time()
            if (time.time() - last_fhf) > 1620:
                pyautogui.click(fhf_dn)
                time.sleep(4)
                gc_fhf = pyautogui.locateOnScreen('images/gc2.png', confidence=0.9)
                if gc_fhf is not None:
                    pyautogui.click(pyautogui.center(gc_fhf))
                last_fhf = time.time()
                time.sleep(0.5)


def click_loop():
    while True:
        if keyboard.is_pressed('ctrl+f3'):
            main_loop()
        pyautogui.click(204, 367)


def main_loop():
    while True:
        if keyboard.is_pressed('ctrl+f1'):
            click_loop()
        elif keyboard.is_pressed('ctrl+f2'):
            click_gc_loop()


main_loop()
