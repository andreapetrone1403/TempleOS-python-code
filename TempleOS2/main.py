import tkinter as tk
from tkinter.font import *
import os, sys

def talk():
    os.system("start talk.py")
    sys.exit()
def game():
    os.system("start game_menu.py")
    sys.exit()

window = tk.Tk()
height, width = 640, 480
window.geometry(str(height)+"x"+str(width))
window.resizable(False, False)
window.title("TempleOS")

title_label = tk.Label(window, text="† TempleOS †", font=("Fixedsys", 32, BOLD), fg="#fcba03", bg="#75746f", width=width)
title_label.pack(pady=30)
pady = tk.Label(window, text="")
pady.pack(pady=50)
talk_button = tk.Button(window, text="Talk With God", font=("Fixedsys", 16), fg="#ffffff", bg="#1002d4", width=width, command=talk)
talk_button.pack(pady=0)
games_button = tk.Button(window, text="Game Menù", font=("Fixedsys", 16), fg="#ffffff", bg="#1002d4", width=width, command=game)
games_button.pack(pady=15)

window.mainloop()