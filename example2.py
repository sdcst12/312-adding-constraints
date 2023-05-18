#!python3

# A basic canvas drawing using some geometric shapes

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


rec = c.create_rectangle(50,50,80,80,fill="#aa0000")


def leftKey(e):
    print(e)
    x=-5
    y=0
    c.move(rec,x,y)

def rightKey(e):
    print(e)
    x=5
    y=0
    c.move(rec,x,y)

def upKey(e):
    print(e)
    x=0
    y=-5
    c.move(rec,x,y)

def downKey(e):
    print(e)
    x=0
    y=5
    c.move(rec,x,y)
    
w.bind("<Left>",leftKey)
w.bind("<Right>",rightKey)
w.bind("<Up>",upKey)
w.bind("<Down>",downKey)


w.mainloop()