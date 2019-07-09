import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = True


def click_loop():
    last_gc = 0
    while True:
        if keyboard.is_pressed('F4'):
            main_loop()
        else:
            pyautogui.click(204, 367)
            if (time.time() - last_gc) > 135:
                gc = pyautogui.locateOnScreen('gc2.png', confidence=0.93)
                if gc is not None:
                    pyautogui.click(pyautogui.center(gc))
                    time.sleep(1.3)
                    last_gc = time.time()


def main_loop():
    while True:
        if keyboard.is_pressed('F2'):
            click_loop()


time.sleep(0.5)
main_loop()
