import tkinter as tk
import random
import time
import threading 
from tkinter import *

window = Tk()

window.title("S.A.R.A.H")

window.geometry("1920x1080")

    
image = tk.PhotoImage(file="C:\\Users\\qadada\\Videos\\Hibernation.png")
smaller_image = image.subsample(5, 5)  
panel = tk.Label(window, image = smaller_image)


panel.pack(side = "bottom", fill = "both", expand = "yes")
panel.configure(background="black")

def callback():  
    img2 = tk.PhotoImage(file="C:\\Users\\qadada\\Videos\\Online.png")
    smaller_image = img2.subsample(5, 5)  
    panel.configure(background = "black", image=smaller_image)
    panel.image = smaller_image

def callback2():  
    img2 = tk.PhotoImage(file="C:\\Users\\qadada\\Videos\\Talking.png")
    smaller_image = img2.subsample(5, 5)  
    panel.configure(background = "black", image=smaller_image)
    panel.image = smaller_image

timer = threading.Timer(2.0, callback) 
timer.start() 
timer = threading.Timer(4.0, callback) 
timer.start() 

window.mainloop()


