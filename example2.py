#!python3

# A basic canvas drawing using some geometric shapes

import tkinter as tk
import random
import time

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


#Placing blocks by coordinates assuming all blacks are the same size and 20x20 pixels
map = [ (0,1) , (3,4) , (5,10) , (9,0) , (10,3)]
walls = []
for i in map:
    x1 = i[0]*20 + 5
    y1 = i[1]*20 + 5
    x2 = x1+20
    y2 = y1+20
    walls.append( c.create_rectangle(x1,y1,x2,y2,fill="#aa00aa"))




w.mainloop()