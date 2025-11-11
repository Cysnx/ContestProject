"""
This is a blank PyCharm project for you to develop in.
Feel free to make any new files that you want to.
"""
from joblib.externals.loky.backend.utils import recursive_terminate
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

WAND_WIDTH = 5
WAND_HEIGHT = 50

SPARKLE_RADIUS = 5
SPARKLE_Y_VEL = 10

DELAY = 1/60


def main():
    canvas = Canvas()
    width = canvas.get_width()
    height = canvas.get_height()
    x,y=0,0

    wand=canvas.create_rectangle(0,height,WAND_WIDTH,height-WAND_HEIGHT)
    sparkles=[]


    while True:
        x = canvas.get_mouse_x()-WAND_WIDTH
        y = canvas.get_mouse_y()-WAND_HEIGHT
        rect = canvas.create_rectangle(x, y, x + SPARKLE_RADIUS, y - SPARKLE_RADIUS, color='yellow')
        canvas.moveto(wand,x,y)
        sparkles.append(rect)
        for rect in sparkles:
            x_1=canvas.get_left_x(rect)
            y_1=canvas.get_top_y(rect)+SPARKLE_RADIUS-SPARKLE_Y_VEL
            canvas.moveto(rect,x_1,y_1)
        canvas.update()
        time.sleep(DELAY)

    canvas.mainloop()

if __name__ == '__main__':
    main()
