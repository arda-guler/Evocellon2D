import tkinter as tk
import keyboard as kbd
import time

from autorules import *
from cell2d import *
from space2d import *
from graphics import *

def init(size_x=50, size_y=50, update_func=game_of_life, init_func=rand_init, cell_size=10):
    cells = []
    
    for y in range(size_y):
        cells.append([])
        for x in range(size_x):
            new_cell = cell_bool([x, y], init_func())
            cells[y].append(new_cell)
            
    space = space2d(update_func, cells)

    root = tk.Tk()
    root.title("Evocellon2D")
    root.geometry(str(size_x*cell_size) + "x" + str(size_y*cell_size))

    cvs = tk.Canvas(root, width=size_x*cell_size, height=size_y*cell_size, bg="black")
    cvs.pack()
    
    return space, root, cvs, cell_size

def main():
            
    space, root, cvs, cell_size = init(150, 100, game_of_life, rand_init, 5)

    while True:
        if kbd.is_pressed("Enter"):
            space.update()
        render_space(cvs, space, cell_size, space.time)
        root.update()

    root.mainloop()

main()
