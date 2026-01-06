import tkinter as tk
import os, sys

def snake():
    os.system("start games/snake.py")
def space_inveders():
    os.system("start games/space_invaders.py")
def return_func():
    os.system("start main.py")
    sys.exit()

window = tk.Tk()
height, width = 640, 480
window.geometry(str(height)+"x"+str(width))
window.resizable(False, False)
window.title("TempleOS - Games Menù")

pady = tk.Label(window, text="")
pady.pack(pady=50)
invaders_button = tk.Button(window, text="Space Invaders", font=("Fixedsys", 24), width=width, bg="blue", fg="white", command=space_inveders)
invaders_button.pack(pady=0)
snake_button = tk.Button(window, text="Snake", font=("Fixedsys", 24), width=width, bg="blue", fg="white", command=snake)
snake_button.pack(pady=15)
return_button = tk.Button(window, text="Return", font=("Fixedsys", 16), width=width, bg="blue", fg="white", command=return_func)
return_button.pack(pady=75)

window.mainloop()