"""
So I wanted to create a screenprint mesh, where I can easily select the mesh size and create something accordingly.
Screenprints have 'waft' and 'weft' geometries and a bit difficult to manage.
I want a program that creates the mesh to my design.
"""
from shapely.constructive import boundary
from torch.distributed.fsdp.wrap import size_based_auto_wrap_policy

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

DISTANCE = 20
MESH_SIZE = 5
THICKNESS = 20
X_1 = 20
Y_1 = X_1
X_2 = X_1
Y_2 = X_1


def main():
    canvas = Canvas()
    width = canvas.get_width()
    height = canvas.get_height()
    size_width = int((width - (2 * X_1)) / (THICKNESS + DISTANCE)) + 1
    size_height = int((height - (2 * Y_1)) / (THICKNESS + DISTANCE)) + 1

    y1 = Y_1
    x1 = X_1
    x1 = x1 + THICKNESS
    y1 = y1 + THICKNESS
    y2 = y1 + DISTANCE
    x2 = x1 + DISTANCE
    color = ''

    # ..............DEFINITIONS...............#
    def weft(X_1, y1, y2, width, color):
        return canvas.create_rectangle(X_1, y1, width - 2 * X_1, y2, color)

    def warp(x1, Y_1, x2, height, color):
        return canvas.create_rectangle(x1, Y_1, x2, height - 2 * Y_1, color)

    def patch(x1, y1, x2, y2, color):
        return canvas.create_rectangle(x1, y1, x2, y2, color)

    wefts = []
    for i in range(0, size_height - 1):
        # weft(X_1,y1,y2,width)
        wefts.append(weft(X_1, y1, y2, width, '#6DC46D'))
        y1 = y2
        y1 = y1 + THICKNESS
        y2 = y1 + DISTANCE

    warps = []
    for j in range(0, size_width - 1):
        # warp(x1,Y_1,x2,height)
        warps.append(warp(x1, Y_1, x2, height, '#006400'))
        x1 = x2
        x1 = x1 + THICKNESS
        x2 = x1 + DISTANCE

    print(f'Size of the Warps: {len(warps)} and size of the Wefts: {len(wefts)}')

    print(f'Warps start from:')
    print(warps)

    print(f'Wefts start from:')
    print(wefts)
    x11 = X_1 + DISTANCE
    y11 = Y_1 + DISTANCE
    x22 = X_2 + DISTANCE + THICKNESS
    y22 = Y_2 + DISTANCE + THICKNESS

    patches = []
    for i in range(0, int(len(warps) / 2 + 1)):
        for j in range(0, int(len(wefts) / 2 + 1)):
            patches.append(patch(x11, y11, x22, y22, color='#6DC46D'))
            x11 = x11 + 2 * (DISTANCE + THICKNESS)
            x22 = x22 + 2 * (DISTANCE + THICKNESS)
        x11 = X_1 + DISTANCE
        x22 = X_2 + DISTANCE + THICKNESS
        y11 = y11 + 2 * (DISTANCE + THICKNESS)
        y22 = y22 + 2 * (DISTANCE + THICKNESS)

    x11 = X_1 + DISTANCE
    y11 = Y_1 + 2 * DISTANCE + THICKNESS
    x22 = X_2 + DISTANCE + THICKNESS
    y22 = Y_2 + 2 * (DISTANCE + THICKNESS)

    for i in range(0, int(len(warps) / 2)):
        x11 = X_1 + THICKNESS + 2 * DISTANCE
        x22 = X_2 + 2 * (THICKNESS + DISTANCE)
        for j in range(0, int(len(wefts) / 2)):
            patches.append(patch(x11, y11, x22, y22, color='#6DC46D'))
            x11 = x11 + 2 * (DISTANCE + THICKNESS)
            x22 = x22 + 2 * (DISTANCE + THICKNESS)
        y11 = y11 + 2 * (DISTANCE + THICKNESS)
        y22 = y22 + 2 * (DISTANCE + THICKNESS)

    canvas.mainloop()

if __name__ == '__main__':
    main()