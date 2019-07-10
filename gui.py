import tkinter as tk
from tkinter import Tk, Label, Button, ttk, PhotoImage
from planter import *

window = Tk()
window.geometry("400x500")
window.title("Auto Cookie Clicker")
window.iconbitmap('images/favicon.ico')
window.resizable(False, False)
background_image = PhotoImage(file='images/background.png')
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


bakers_wheat_icon = PhotoImage(file=bakers_wheat)
thumbcorn_icon = PhotoImage(file=thumbcorn)
cronerice_icon = PhotoImage(file=cronerice)
gildmillet_icon = PhotoImage(file=gildmillet)
ordinary_clover_icon = PhotoImage(file=ordinary_clover)
golden_clover_icon = 0
shimmerlily_icon = PhotoImage(file=shimmerlily)
elderwort_icon = PhotoImage(file=elderwort)
bakeberry_icon = PhotoImage(file=bakeberry)
chocoroot_icon = PhotoImage(file=chocoroot)
white_chocoroot_icon = PhotoImage(file=white_chocoroot)
white_mildew_icon = PhotoImage(file=white_mildew)
brown_mold_icon = PhotoImage(file=brown_mold)
meddleweed_icon = PhotoImage(file=meddleweed)
whiskerbloom_icon = PhotoImage(file=whiskerbloom)
chimerose_icon = PhotoImage(file=chimerose)
nursetulip_icon = PhotoImage(file=nursetulip)
drowsyfern_icon = PhotoImage(file=drowsyfern)
wardlichen_icon = PhotoImage(file=wardlichen)
keenmoss_icon = PhotoImage(file=keenmoss)
queenbeat_icon = PhotoImage(file=queenbeat)
juicy_queenbeat_icon = 0
duketater_icon = 0
crumbspore_icon = PhotoImage(file=crumbspore)
doughshroom_icon = PhotoImage(file=doughshroom)
glovemorel_icon = PhotoImage(file=glovemorel)
cheapcap_icon = PhotoImage(file=cheapcap)
fools_bolete_icon = PhotoImage(file=fools_bolete)
wrinklegill_icon = PhotoImage(file=wrinklegill)
green_rot_icon = PhotoImage(file=green_rot)
shriekbulb_icon = PhotoImage(file=shriekbulb)
tidygrass_icon = PhotoImage(file=tidygrass)
everdaisy_icon = 0
ichorpuff_icon = PhotoImage(file=ichorpuff)


try_thumbcorn_button = tk.Button(window,
                                 image=thumbcorn_icon,
                                 compound="left",
                                 text="Thumbcorn",
                                 command=try_thumbcorn)
try_cronerice_button = tk.Button(window,
                                 image=cronerice_icon,
                                 compound="left",
                                 text="Cronerice",
                                 command=try_cronerice)
try_shimmerlily_button = tk.Button(window,
                                   image=shimmerlily_icon,
                                   compound="left",
                                   text="Shimmerlily",
                                   command=try_shimmerlily)
try_bakeberry_button = tk.Button(window,
                                 image=bakeberry_icon,
                                 compound="left",
                                 text="Bakeberry",
                                 command=try_bakeberry)
try_chocoroot_button = tk.Button(window,
                                 image=chocoroot_icon,
                                 compound="left",
                                 text="Chocoroot",
                                 command=try_chocoroot)
try_white_chocoroot_button = tk.Button(window,
                                       image=white_chocoroot_icon,
                                       compound="left",
                                       text="White Chocoroot",
                                       command=try_white_chocoroot)
try_whiskerbloom_button = tk.Button(window,
                                    image=whiskerbloom_icon,
                                    compound="left",
                                    text="Whiskerbloom",
                                    command=try_whiskerbloom)
try_nursetulip_button = tk.Button(window,
                                  image=nursetulip_icon,
                                  compound="left",
                                  text="Nursetulip",
                                  command=try_nursetulip)
try_drowsyfern_button = tk.Button(window,
                                  image=drowsyfern_icon,
                                  compound="left",
                                  text="Drowsyfern",
                                  command=try_drowsyfern)
try_keenmoss_button = tk.Button(window,
                                image=keenmoss_icon,
                                compound="left",
                                text="Keenmoss",
                                command=try_keenmoss)
try_juicy_queenbeat_button = tk.Button(window,
                                       image=queenbeat_icon,
                                       compound="left",
                                       text="Juicy Queenbeat",
                                       command=try_juicy_queenbeat)
try_tidygrass_button = tk.Button(window,
                                 image=tidygrass_icon,
                                 compound="left",
                                 text="Tidygrass",
                                 command=try_tidygrass)
try_everdaisy_button = tk.Button(window,
                                 compound="left",
                                 text="Everdaisy",
                                 command=try_everdaisy)
try_thumbcorn_button.pack()
try_cronerice_button.pack()
try_shimmerlily_button.pack()
try_bakeberry_button.pack()
try_chocoroot_button.pack()
try_white_chocoroot_button.pack()
try_whiskerbloom_button.pack()
try_nursetulip_button.pack()
try_drowsyfern_button.pack()
try_keenmoss_button.pack()
try_juicy_queenbeat_button.pack()
try_tidygrass_button.pack()
try_everdaisy_button.pack()










window.mainloop()
