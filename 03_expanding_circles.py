"""
This is a blank PyCharm project for you to develop in.
Feel free to make any new files that you want to.
"""
from shapely.constructive import boundary

import graphics
from graphics import Canvas             # graphics library
from simpleimage import SimpleImage     # images library
import tkinter as tk

def main():
    # Uncomment the line "tkinter.mainloop()" below if you are using a
    # graphics canvas to draw graphics, so that graphics window appears.
    # You can delete these lines if you are not using a drawing canvas.
    # tkinter.mainloop()
    pass

from graphics import Canvas
import time

STARTING_RADIUS = 10
GROWTH_RATE = 5
DELAY = 1/60

def main():
    canvas = Canvas()
    width = canvas.get_width()
    height = canvas.get_height()
    boundary=0
    canvas.set_canvas_background_color(color='gray')
    for i in range(4):
        while boundary+GROWTH_RATE<width/2:
            canvas.create_oval(width/2-(STARTING_RADIUS+boundary), height/2-(STARTING_RADIUS+boundary), width/2+(STARTING_RADIUS+boundary), height/2+(STARTING_RADIUS+boundary),color='black')
            time.sleep(DELAY)
            boundary=boundary+GROWTH_RATE
            canvas.update()
        boundary = 0
        while boundary+GROWTH_RATE<width/2:
            canvas.create_oval(width/2-(STARTING_RADIUS+boundary), height/2-(STARTING_RADIUS+boundary), width/2+(STARTING_RADIUS+boundary), height/2+(STARTING_RADIUS+boundary),color='white')
            time.sleep(DELAY)
            boundary=boundary+GROWTH_RATE
            canvas.update()
        boundary = 0


    canvas.mainloop()

if __name__ == '__main__':
    main()
