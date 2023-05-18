#!python3

# A basic canvas drawing using some geometric shapes

import tkinter as tk

w = tk.Tk()
w.geometry("600x400")
w.title("sample")

c = tk.Canvas(width=550,height=450,background="#cccccc",bd="2")
c.pack()


rec = c.create_rectangle(50,50,80,80,fill="#aa0000")
obstacle = c.create_rectangle(250,180,350,220,fill='#000000')

def detectCollision():
    #this will return a True value if the objects overlap
    #return False if the objects do not overlap
    # Canvas.bbox draws a rectangular box around the object as a tuple (x0,y0,x1,y1)
    # where (x0,y0) is the coordiante of the top left corner and
    # (x1,y1) is the coordinate of the bottom right corner
    br = c.bbox(rec)
    print(br)
    bo = c.bbox(obstacle)
    print(bo)

def keyPress(e):
    print(e)
    print(e.keycode, e.keysym, e.x, e.y)
    if detectCollision():
        print("objects overlap")
    else:
        print('objects do not overlap')
    
w.bind("<Left>",keyPress)
w.bind("<Right>",keyPress)
w.bind("<Up>",keyPress)
w.bind("<Down>",keyPress)


w.mainloop()