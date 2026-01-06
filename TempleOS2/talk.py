import tkinter as tk
from tkinter.font import *
import os, sys, time

def stage1():
    os.system("start questions/1.py")
def stage2():
    os.system("start questions/2.py")
def stage3():
    os.system("start questions/3.py")
def return_func():
    os.system("start main.py")
    sys.exit()

height, width = 640, 480
window = tk.Tk()
window.resizable(False, False)
window.title("TempleOS - Talk With God")
window.geometry(str(height)+"x"+str(width))

god_text = "Hi im your God, you have question for me?"
god_label = tk.Label(window, text=god_text, font=("Fixedsys", 17), fg="#1002d4")
god_label.pack(pady=50)
pady = tk.Label(window, text="")
pady.pack(pady=30)
question1_button = tk.Button(window, text="What happens after we die?", font=("Fixedsys", 17), fg="#ffffff", bg="#1002d4", width=240,
                             command=stage1)
question1_button.pack(pady=0)
question2_button = tk.Button(window, text="What's your real name?", font=("Fixedsys", 17), fg="#ffffff", bg="#1002d4", width=240,
                             command=stage2)
question2_button.pack(pady=15)
question3_button = tk.Button(window, text="why do I exist?", font=("Fixedsys", 17), fg="#ffffff", bg="#1002d4", width=240,
                             command=stage3)
question3_button.pack(pady=5)
return_button = tk.Button(window, text="Return", font=("Fixedsys", 17), fg="#ffffff", bg="#1002d4", width=240, command=return_func)
return_button.pack(pady=10)

window.mainloop()