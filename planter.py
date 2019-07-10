import pyautogui
import time

pyautogui.PAUSE = 0.2
pyautogui.FAILSAFE = True

bakers_wheat = 'C:/Users/Felipe/PycharmProjects/auto_click/images/bakers_wheat.png'
thumbcorn = 'C:/Users/Felipe/PycharmProjects/auto_click/images/thumbcorn.png'
cronerice = 'C:/Users/Felipe/PycharmProjects/auto_click/images/cronerice.png'
gildmillet = 'C:/Users/Felipe/PycharmProjects/auto_click/images/gildmillet.png'
ordinary_clover = 'C:/Users/Felipe/PycharmProjects/auto_click/images/ordinary_clover.png'
golden_clover = 0
shimmerlily = 'C:/Users/Felipe/PycharmProjects/auto_click/images/shimmerlily.png'
elderwort = 'C:/Users/Felipe/PycharmProjects/auto_click/images/elderwort.png'
bakeberry = 'C:/Users/Felipe/PycharmProjects/auto_click/images/bakeberry.png'
chocoroot = 'C:/Users/Felipe/PycharmProjects/auto_click/images/chocoroot.png'
white_chocoroot = 'C:/Users/Felipe/PycharmProjects/auto_click/images/white_chocoroot.png'
white_mildew = 'C:/Users/Felipe/PycharmProjects/auto_click/images/white_mildew.png'
brown_mold = 'C:/Users/Felipe/PycharmProjects/auto_click/images/brown_mold.png'
meddleweed = 'C:/Users/Felipe/PycharmProjects/auto_click/images/meddleweed.png'
whiskerbloom = 'C:/Users/Felipe/PycharmProjects/auto_click/images/whiskerbloom.png'
chimerose = 'C:/Users/Felipe/PycharmProjects/auto_click/images/chimerose.png'
nursetulip = 'C:/Users/Felipe/PycharmProjects/auto_click/images/nursetulip.png'
drowsyfern = 'C:/Users/Felipe/PycharmProjects/auto_click/images/drowsyfern.png'
wardlichen = 'C:/Users/Felipe/PycharmProjects/auto_click/images/wardlichen.png'
keenmoss = 'C:/Users/Felipe/PycharmProjects/auto_click/images/keenmoss.png'
queenbeat = 'C:/Users/Felipe/PycharmProjects/auto_click/images/queenbeat.png'
juicy_queenbeat = 0
duketater = 0
crumbspore = 'C:/Users/Felipe/PycharmProjects/auto_click/images/crumbspore.png'
doughshroom = 'C:/Users/Felipe/PycharmProjects/auto_click/images/doughshroom.png'
glovemorel = 'C:/Users/Felipe/PycharmProjects/auto_click/images/glovemorel.png'
cheapcap = 'C:/Users/Felipe/PycharmProjects/auto_click/images/cheapcap.png'
fools_bolete = 'C:/Users/Felipe/PycharmProjects/auto_click/images/fools_bolete.png'
wrinklegill = 'C:/Users/Felipe/PycharmProjects/auto_click/images/wrinklegill.png'
green_rot = 'C:/Users/Felipe/PycharmProjects/auto_click/images/green_rot.png'
shriekbulb = 'C:/Users/Felipe/PycharmProjects/auto_click/images/shriekbulb.png'
tidygrass = 'C:/Users/Felipe/PycharmProjects/auto_click/images/tidygrass.png'
everdaisy = 0
ichorpuff = 'C:/Users/Felipe/PycharmProjects/auto_click/images/ichorpuff.png'


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
    pyautogui.hotkey('altleft', 'tab')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    pyautogui.press('esc', 1)


def try_cronerice():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_shimmerlily():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_bakeberry():
    pyautogui.hotkey('altleft', 'tab')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(bakers_wheat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    pyautogui.press('esc', 1)


def try_chocoroot():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_white_chocoroot():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_whiskerbloom():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_nursetulip():
    pyautogui.hotkey('altleft', 'tab')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(whiskerbloom))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in same_plant_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    pyautogui.press('esc', 1)


def try_drowsyfern():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_keenmoss():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_juicy_queenbeat():
    pyautogui.hotkey('altleft', 'tab')
    time.sleep(0.5)
    pyautogui.click(get_center_pos(queenbeat))
    pyautogui.keyDown('shift')
    time.sleep(0.5)
    for coord in juicy_coords:
        pyautogui.click(coord)
    pyautogui.keyUp('shift')
    pyautogui.press('esc', 1)


def try_tidygrass():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)


def try_everdaisy():
    pyautogui.hotkey('altleft', 'tab')
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
    pyautogui.press('esc', 1)
