import tkinter as tk
from tkinter.font import *
import os, sys

#global var
running = True

#function
def root():
    running = False
    os.system("start main.py")
    sys.exit()

#window
height, width = 640, 480
window = tk.Tk()
window.title("TempleOS - ROOT")
window.config(bg="black")
window.geometry(str(height)+"x"+str(width))
window.resizable(False, False)

#widget
root_button = tk.Button(window, text="root", font=("Fixedsys", 32, BOLD), width=width, command=root, fg="#ffffff", bg="#000000",
                        highlightthickness=0, relief='flat')
root_button.pack(pady=200)

#made a mainloop
window.mainloop()