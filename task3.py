#!python3

# A basic canvas drawing using some geometric shapes

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


rec = c.create_rectangle(50,50,80,80,fill="#aa0000")


def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()