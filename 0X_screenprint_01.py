"""
So I wanted to create a screenprint mesh, where I can easily select the mesh size and create something accordingly.
Screenprints have 'warp' and 'weft' geometries and a bit difficult to manage.
I want a program that creates the mesh to my design.
"""
from shapely.constructive import boundary
from sklearn.metrics import DistanceMetric
from torch.distributed.fsdp.wrap import size_based_auto_wrap_policy

import graphics
from graphics import Canvas             # graphics library
from simpleimage import SimpleImage     # images library
import tkinter as tk


THICKNESS = 20
DISTANCE = THICKNESS * 2.5
CORNER_GAP= DISTANCE



def main():
    canvas = Canvas()
    width = canvas.get_width()
    height = canvas.get_height()
    count_warp=int((width-(2*CORNER_GAP))/(THICKNESS+DISTANCE))
    count_weft=int((height-(2*CORNER_GAP))/(THICKNESS+DISTANCE))

    print (f"{count_warp} warps and {count_weft} wefts.")


    x1=CORNER_GAP+DISTANCE
    y1=CORNER_GAP+DISTANCE
    y2 = y1 + THICKNESS
    x2 = x1 + THICKNESS
    color = ''
    #..............DEFINITIONS...............#
    def weft(CORNER_GAP,y1,y2,width,color):
        return canvas.create_rectangle(CORNER_GAP, y1, width - CORNER_GAP, y2, color)
    def warp(x1,CORNER_GAP,x2,height,color):
        return canvas.create_rectangle(x1, CORNER_GAP, x2, height - CORNER_GAP, color)
    def patch(x1,y1,x2,y2,color):
        return canvas.create_rectangle(x1, y1, x2, y2, color)

    wefts=[]
    for i in range(0,count_weft):
        wefts.append(weft(CORNER_GAP,y1,y2,width,'#6dc499'))
        y1=y2
        y1 = y1 + DISTANCE
        y2 = y1 + THICKNESS

    warps=[]
    for j in range(0,count_warp):
        warps.append(warp(x1,CORNER_GAP,x2,height,'#006400'))
        x1=x2
        x1 = x1 + DISTANCE
        x2 = x1 + THICKNESS


    x11=CORNER_GAP+DISTANCE
    y11=CORNER_GAP+DISTANCE
    x22=CORNER_GAP+DISTANCE+THICKNESS
    y22=CORNER_GAP+DISTANCE+THICKNESS

    patches=[]
    for i in range(0,int(len(warps)/2)):
        while y22 <= (height-CORNER_GAP):
            for j in range(0, int(len(wefts)/2)):
                while x22 <= (width-CORNER_GAP):
                    patches.append(patch(x11,y11,x22,y22,color='#6dc499'))
                    x11=x11+2*(DISTANCE+THICKNESS)
                    x22=x11 + THICKNESS
                x11=CORNER_GAP + DISTANCE
                x22=CORNER_GAP + DISTANCE + THICKNESS
            y11=y22 + DISTANCE*2 + THICKNESS
            y22=y11 + THICKNESS

    y11=CORNER_GAP+2*DISTANCE+THICKNESS
    y22=CORNER_GAP+2*(DISTANCE+THICKNESS)

    for i in range(0,int(len(warps)/2)+1):
        while y22<=(height-CORNER_GAP):
            x11=CORNER_GAP+2*DISTANCE+THICKNESS
            x22=CORNER_GAP+2*(THICKNESS+DISTANCE)
            for j in range(0, int(len(wefts)/2)+1):
                while x22<=(width-CORNER_GAP):
                    patches.append(patch(x11,y11,x22,y22,color='#6dc499'))
                    x11=x11+2*(DISTANCE+THICKNESS)
                    x22=x22+2*(DISTANCE+THICKNESS)
            y11=y11+2*(DISTANCE+THICKNESS)
            y22=y22+2*(DISTANCE+THICKNESS)

    canvas.mainloop()

    n = (10 + DISTANCE) / (THICKNESS + DISTANCE)

    print(f"You created {n:.2f}T mesh. ")

if __name__ == '__main__':
    main()