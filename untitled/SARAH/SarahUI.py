import tkinter as tk
import random
import time

window = tk.Tk()

window.title("S.A.R.A.H")

window.geometry("500x500")

def updaterofsorts():
    rand = random.randint(1,4)
    x = rand
    return(x)

def updatershow():
    print("test")
    greeting = updaterofsorts()
    n_o_display = tk.Text(master=window, height=10,width=30)
    n_o_display.grid(column=0, row = 3)
    n_o_display.insert(tk.END,(greeting))

image = tk.PhotoImage(file="volume2.png")
label = tk.Label(image=image, height=100, width =100)
label.grid(column=3,row=3)

title = tk.Label(text ="Kill me")
title.grid(column = 0, row = 0)

button1 = tk.Button(text="Click me", command=updatershow)
button1.grid(column = 0, row = 1)


window.mainloop()

