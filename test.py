import pyautogui
import time

time.sleep(2)


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


def get_locals():
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


std_coords_plant_1 = [(820, 308), (940, 308), (820, 384), (940, 433), (820, 512), (940, 512)]
std_coords_plant_2 = [(820, 352), (940, 352), (820, 468), (940, 468)]
same_plant_coords =  [(820, 308), (940, 308), (820, 352), (940, 352), (820, 384), (940, 384),
                      (820, 468), (940, 468), (820, 512), (940, 512)]

for element in same_plant_coords:
    pyautogui.click(element)
    time.sleep(0.5)
