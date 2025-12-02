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

from graphics import Canvas

DISTANCE = 50
THICKNESS = 10
CORNER_GAP = 10


def main():
    canvas = Canvas()
    width = canvas.get_width()
    height = canvas.get_height()

    # Calculate how many lines fit
    count_warp = int((width - (2 * CORNER_GAP)) / (THICKNESS + DISTANCE))
    count_weft = int((height - (2 * CORNER_GAP)) / (THICKNESS + DISTANCE))

    print(f"{count_warp} warps (vertical) and {count_weft} wefts (horizontal).")

    # Colors
    weft_color = '#6DC46D'  # Light Green
    warp_color = '#006400'  # Dark Green

    # 1. Draw all Horizontal lines (Wefts) - Background Layer
    y = CORNER_GAP + DISTANCE
    for i in range(count_weft):
        canvas.create_rectangle(CORNER_GAP, y, width - CORNER_GAP, y + THICKNESS, weft_color)
        y += (THICKNESS + DISTANCE)

    # 2. Draw all Vertical lines (Warps) - Middle Layer
    x = CORNER_GAP + DISTANCE
    for j in range(count_warp):
        canvas.create_rectangle(x, CORNER_GAP, x + THICKNESS, height - CORNER_GAP, warp_color)
        x += (THICKNESS + DISTANCE)

    # 3. Draw Patches - Top Layer
    # This creates the illusion of weaving. Currently, Vertical is on top of everything.
    # We need to draw small squares of Horizontal color ON TOP of Vertical lines
    # in a checkerboard pattern.

    for row in range(count_weft):
        for col in range(count_warp):
            # The logic: If the sum of row and col index is odd, we patch.
            # This creates the checkerboard "Over-Under" effect.
            if (row + col) % 2 != 0:
                # Calculate coordinates for this specific intersection
                x_start = CORNER_GAP + DISTANCE + (col * (THICKNESS + DISTANCE))
                y_start = CORNER_GAP + DISTANCE + (row * (THICKNESS + DISTANCE))
                x_end = x_start + THICKNESS
                y_end = y_start + THICKNESS

                # Draw the patch
                canvas.create_rectangle(x_start, y_start, x_end, y_end, weft_color)

    canvas.mainloop()


if __name__ == '__main__':
    main()