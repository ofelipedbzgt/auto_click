import pyautogui
import time
import keyboard

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

bakers_wheat = 'images/bakers_wheat.png'
thumbcorn = 'images/thumbcorn.png'
cronerice = 'images/cronerice.png'
gildmillet = 'images/gildmillet.png'
ordinary_clover = 'images/ordinary_clover.png'
golden_clover = 0
shimerlily = 'images/shimerlily.png'
elderwort = 'images/elderwort.png'
bakeberry = 'images/bakeberry.png'
chocoroot = 'images/chocoroot.png'
white_chocoroot = 'images/white_chocoroot.png'
white_mildew = 'images/white_mildew.png'
brown_mold = 'images/brown_mold.png'
meddleweed = 'images/meddleweed.png'
whiskerbloom = 'images/whiskerbloom.png'
chimerose = 'images/chimerose.png'
nursetulip = 'images/nursetulip.png'
drowsyfern = 'images/drowsyfern.png'
wardlichen = 'images/wardlichen.png'
keenmoss = 'images/keenmoss.png'
queenbeat = 'images/queenbeat.png'
juicy_queenbeat = 0
duketater = 0
crumbspore = 'images/crumbspore.png'
doughshroom = 'images/doughshroom.png'
glovemorel = 'images/glovemorel.png'
cheapcap = 'images/cheapcap.png'
fools_bolete = 'images/fools_bolete.png'
wrinklegill = 'images/wrinklegill.png'
green_rot = 'images/green_rot.png'
shriekbulb = 'images/shriekbulb.png'
tidygrass = 'images/tidygrass.png'
everdaisy = 0
ichorpuff = 'images/ichorpuff.png'


def get_coords():
    print(pyautogui.locateOnScreen(bakers_wheat, confidence=0.93))
    print(pyautogui.locateOnScreen(thumbcorn, confidence=0.93))
    print(pyautogui.locateOnScreen(cronerice, confidence=0.93))
    print(pyautogui.locateOnScreen(gildmillet, confidence=0.93))
    print(pyautogui.locateOnScreen(ordinary_clover, confidence=0.93))
    print(pyautogui.locateOnScreen(shimerlily, confidence=0.93))
    print(pyautogui.locateOnScreen(elderwort, confidence=0.93))
    print(pyautogui.locateOnScreen(bakeberry, confidence=0.93))
    print(pyautogui.locateOnScreen(chocoroot, confidence=0.93))
    print(pyautogui.locateOnScreen(white_chocoroot, confidence=0.93))
    print(pyautogui.locateOnScreen(white_mildew, confidence=0.93))
    print(pyautogui.locateOnScreen(brown_mold, confidence=0.93))
    print(pyautogui.locateOnScreen(meddleweed, confidence=0.93))
    print(pyautogui.locateOnScreen(whiskerbloom, confidence=0.93))
    print(pyautogui.locateOnScreen(chimerose, confidence=0.93))
    print(pyautogui.locateOnScreen(nursetulip, confidence=0.93))
    print(pyautogui.locateOnScreen(drowsyfern, confidence=0.93))
    print(pyautogui.locateOnScreen(wardlichen, confidence=0.93))
    print(pyautogui.locateOnScreen(keenmoss, confidence=0.93))
    print(pyautogui.locateOnScreen(queenbeat, confidence=0.93))
    print(pyautogui.locateOnScreen(crumbspore, confidence=0.93))
    print(pyautogui.locateOnScreen(doughshroom, confidence=0.93))
    print(pyautogui.locateOnScreen(glovemorel, confidence=0.93))
    print(pyautogui.locateOnScreen(cheapcap, confidence=0.93))
    print(pyautogui.locateOnScreen(fools_bolete, confidence=0.93))
    print(pyautogui.locateOnScreen(wrinklegill, confidence=0.93))
    print(pyautogui.locateOnScreen(green_rot, confidence=0.93))
    print(pyautogui.locateOnScreen(shriekbulb, confidence=0.93))
    print(pyautogui.locateOnScreen(tidygrass, confidence=0.93))
    print(pyautogui.locateOnScreen(ichorpuff, confidence=0.93))


garden_coords = [(780, 309), (820, 308), (859, 308), (899, 308), (940, 308), (979, 308),
                 (780, 351), (820, 353), (859, 353), (899, 351), (940, 354), (979, 352),
                 (780, 383), (820, 385), (859, 385), (899, 385), (940, 385), (979, 384),
                 (780, 433), (820, 433), (859, 432), (899, 433), (940, 434), (979, 434),
                 (780, 467), (820, 467), (859, 469), (899, 469), (940, 467), (979, 468),
                 (780, 512), (820, 512), (859, 512), (899, 511), (940, 513), (979, 513)]


while True:
    if keyboard.is_pressed('f2'):
        # (x, y) = garden_coords.append(pyautogui.position())
        x, y = pyautogui.position()
        coords = (x, y)
        garden_coords.append(coords)
        time.sleep(0.5)
    elif keyboard.is_pressed('f3'):
        break

print(garden_coords)
