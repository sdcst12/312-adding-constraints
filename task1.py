import tkinter as tk

w = tk.Tk()
w.geometry("925x475")
w.attributes('-topmost',True)
c = tk.Canvas(height=475,width=900,bg="#ffdddd")
c.pack()
f = open('map1.txt')
tiles = f.read().split('\n')
walls = []
for y in range(len(tiles)):
    for x in range(len(tiles[y])):
        if tiles[y][x] == "*":
            walls.append( c.create_rectangle(x*30+10,y*30+10,x*30+40,y*30+40,fill="#ffffff"))
print(tiles)

w.mainloop()