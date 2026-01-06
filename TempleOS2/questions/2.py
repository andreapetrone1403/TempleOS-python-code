import tkinter as tk
from tkinter.font import *
import os, sys, time

def return_func():
    sys.exit()

height, width = 640, 480
window = tk.Tk()
window.resizable(False, False)
window.title("TempleOS - Talk With God")
window.geometry(str(height)+"x"+str(width))

god_text = "My real name is God the Sir simple"
god_label = tk.Label(window, text=god_text, font=("Fixedsys", 17), fg="#1002d4")
god_label.pack(pady=200)
return_button = tk.Button(window, text="Return", font=("Fixedsys", 16, BOLD), bg="#1002d4", fg="white", width=width, command=return_func)
return_button.pack()

window.mainloop()