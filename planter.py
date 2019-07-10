import pyautogui
import time
import keyboard

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

bakers_wheat = 'images/bakers_wheat.png'
thumbcorn = 'images/thumbcorn.png'
cronerice = 'images/cronerice.png'
gildmillet = 'images/gildmillet.png'
ordinary_clover = 'images/ordinary_clover.png'
golden_clover = 0
shimmerlily = 'images/shimmerlily.png'
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
    print(pyautogui.locateOnScreen(shimmerlily, confidence=0.93))
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


def get_center_pos(image):
    center = pyautogui.center(pyautogui.locateOnScreen(image, confidence=0.9))
    return center


garden_coords = [(780, 308), (820, 308), (860, 308), (900, 308), (940, 308), (980, 308),
                 (780, 352), (820, 352), (860, 352), (900, 352), (940, 352), (980, 352),
                 (780, 384), (820, 384), (860, 384), (900, 384), (940, 384), (980, 384),
                 (780, 433), (820, 433), (860, 433), (900, 433), (940, 433), (980, 433),
                 (780, 468), (820, 468), (860, 468), (900, 468), (940, 468), (980, 468),
                 (780, 512), (820, 512), (860, 512), (900, 512), (940, 512), (980, 512)]

std_coords_plant_1 = [(820, 308), (940, 308), (820, 384), (940, 433), (820, 512), (940, 512)]

std_coords_plant_2 = [(820, 352), (940, 352), (820, 468), (940, 468)]

same_plant_coords = [(820, 308), (940, 308), (820, 352), (940, 352), (820, 384), (940, 384),
                     (820, 468), (940, 468), (820, 512), (940, 512)]

juicy_coords = [(780, 308), (820, 308), (860, 308), (900, 308), (940, 308), (980, 308),
                (780, 352), (860, 352), (900, 352), (980, 352),
                (780, 384), (820, 384), (860, 384), (900, 384), (940, 384), (980, 384),
                (780, 433), (820, 433), (860, 433), (900, 433), (940, 433), (980, 433),
                (780, 468), (860, 468), (900, 468), (980, 468),
                (780, 512), (820, 512), (860, 512), (900, 512), (940, 512), (980, 512)]

everdaisy_coords_plant_1 = [(780, 308), (820, 308), (860, 308), (900, 308), (940, 308), (980, 308),
                            (780, 468), (820, 468), (860, 468), (900, 468), (940, 468), (980, 468)]

everdaisy_coords_plant_2 = [(780, 384), (820, 384), (860, 384), (900, 384), (940, 384), (980, 384)]


def try_thumbcorn():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_cronerice():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(thumbcorn))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_shimmerlily():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(ordinary_clover))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(gildmillet))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_bakeberry():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_chocoroot():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(brown_mold))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_white_chocoroot():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(white_mildew))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    print(get_center_pos(chocoroot))
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(chocoroot))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_whiskerbloom():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(shimmerlily))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(white_chocoroot))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_nursetulip():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(whiskerbloom))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_drowsyfern():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(chocoroot))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(keenmoss))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_keenmoss():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(brown_mold))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(green_rot))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_juicy_queenbeat():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(queenbeat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in juicy_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_tidygrass():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(white_chocoroot))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in std_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')


def try_everdaisy():
    time.sleep(0.5)
    pyautogui.click(get_center_pos(elderwort))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in everdaisy_coords_plant_1:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(tidygrass))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in everdaisy_coords_plant_2:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')

