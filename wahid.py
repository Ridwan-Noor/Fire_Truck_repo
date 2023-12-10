# Final Project

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time
import numpy as np
import math
import random

def draw_points(x, y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def FindZone(dx, dy):
    zone = 0
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        elif dx > 0 and dy < 0:
            zone = 7
    elif abs(dx) <= abs(dy):
        if dx >= 0 and dy >= 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        elif dx > 0 and dy < 0:
            zone = 6
    return zone


def OriginalZone(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y, x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return y, -x
    elif zone == 7:
        return x, -y


def ConvertToZone0(x1, y1, x2, y2, zone):
    if zone == 0:
        return x1, y1, x2, y2
    elif zone == 1:
        return y1, x1, y2, x2
    elif zone == 2:
        return y1, -x1, y2, -x2
    elif zone == 3:
        return -x1, y1, -x2, y2
    elif zone == 4:
        return -x1, -y1, -x2, -y2
    elif zone == 5:
        return -y1, -x1, -y2, -x1
    elif zone == 6:
        return -y1, x1, -y2, x2
    elif zone == 7:
        return x1, -y1, x2, -y2
    return x1, y1, x2, y2


def MidPointLine(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    zone = FindZone(dx, dy)
    x1, y1, x2, y2 = ConvertToZone0(x1, y1, x2, y2, zone)
    dx = x2 - x1
    dy = y2 - y1
    d_init = 2 * dy - dx
    del_ne = 2 * dy - 2 * dx
    del_e = 2 * dy
    x = x1
    y = y1
    while x <= x2:
        new_x, new_y = OriginalZone(x, y, zone)
        draw_points(new_x, new_y)
        x += 1
        if d_init > 0:
            y += 1
            d_init = d_init + del_ne
        else:
            d_init = d_init + del_e


def circlepoints(center_x, center_y, x, y):
    draw_points(x + center_x, y + center_y)
    draw_points(x + center_x, -y + center_y)
    draw_points(-x + center_x, -y + center_y)
    draw_points(-x + center_x, y + center_y)
    draw_points(y + center_x, x + center_y)
    draw_points(-y + center_x, x + center_y)
    draw_points(-y + center_x, -x + center_y)
    draw_points(y + center_x, -x + center_y)


def MidPointcircle(center_x, center_y, radius):
    x = 0
    y = radius
    d = 1 - radius
    circlepoints(center_x, center_y, x, y)
    while x < y:
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        else:
            d += (2 * x) + 3
            x += 1
        circlepoints(center_x, center_y, x, y)


def circlepoints(center_x, center_y, x, y):
    draw_points(x + center_x, y + center_y)
    draw_points(-x + center_x, y + center_y)
    draw_points(y + center_x, x + center_y)
    draw_points(-y + center_x, x + center_y)


def MidPointcircle(center_x, center_y, radius):
    x = 0
    y = radius
    d = 1 - radius
    circlepoints(center_x, center_y, x, y)
    while x < y:
        if d >= 0:
            d += (2 * x) - (2 * y) + 5
            x += 1
            y -= 1
        else:
            d += (2 * x) + 3
            x += 1
        circlepoints(center_x, center_y, x, y)

def buildings():
    glColor3f(1.0, 1.0, 1.0)  # Set drawing color to white

    # Draw roads
    MidPointLine(0, 70, 250 + 520, 337 + 85)  
    MidPointLine(200, 00, 250 + 620, 337 + 85)  
    MidPointLine(420, 00, 350 + 750, 437 + 75)  

    # Start drawing building 1
    MidPointLine(60, 300, 60, 330) 
    MidPointLine(30, 85, 30, 330)  
    MidPointLine(30, 330, 90, 360) 
    MidPointLine(90, 115, 90, 360)  
    MidPointLine(90, 360, 240, 400)  
    MidPointLine(240, 185, 240, 400)  

    # Adding details to building 1
    for i in range(40):
        MidPointLine(120 + i, 300 + i * .3, 120 + i, 350 + i * .3)  
    for i in range(40):
        MidPointLine(180 + i, 320 + i * .3, 180 + i, 368 + i * .3)  
    
    # Start drawing building 2
    MidPointLine(310, 320, 310, 360)  
    MidPointLine(320, 320, 320, 360)  

    MidPointLine(300, 210, 300, 360)  
    MidPointLine(300, 360, 330, 380)  
    MidPointLine(330, 220, 330, 380)  
    MidPointLine(330, 380, 450, 410)  
    MidPointLine(450, 280, 450, 410)  

    # Adding details to building 2
    for i in range(40):
        MidPointLine(350 + i, 310 + i * .3, 350 + i, 360 + i * .3) 
    for i in range(40):
        MidPointLine(400 + i, 325 + i * .3, 400 + i, 375 + i * .3)  

    # Start drawing building 3
    MidPointLine(30 + 470+10, 370, 30 + 470+10, 400)  
    MidPointLine(30 + 470 + 20, 370, 30 + 470 + 20, 400)  
    MidPointLine(30 + 470 + 30, 370, 30 + 470 + 30, 400)  
    MidPointLine(30 + 470, 305, 30 + 470, 410) 
    MidPointLine(30 + 470, 410, 100 + 450, 430)  
    MidPointLine(100 + 450, 320, 100 + 450, 430)  
    MidPointLine(100 + 450, 430, 250 + 380, 450)  
    MidPointLine(250 + 380, 360, 250 + 380, 450)  

    for i in range(25):
        MidPointLine(565 + i, 370 + i * .3, 565 + i, 400 + i * .3)
    for i in range(25):
        MidPointLine(600 + i, 382 + i * .3, 600 + i, 410 + i * .3)
    
 # Start drawing building 4
    MidPointLine(550, 100, 550, 330)  

   # MidPointLine(500, 55, 500, 300)  
    MidPointLine(552, 325, 580, 370)  
    MidPointLine(580, 120, 580, 370)
    MidPointLine(580, 370, 665, 402)  
    MidPointLine(665, 185, 665, 400) 

    for i in range(40):
        MidPointLine(600 + i, 285 + i * .2, 600 + i, 328 + i * .5) 

    # Start drawing building 5
    MidPointLine(355 + 470, 305, 355 + 470, 410)  
    MidPointLine(355 + 470, 410, 400 + 450, 444)  
    MidPointLine(400 + 450, 325, 400 + 450, 445)
    MidPointLine(400 + 450, 445, 550 + 380, 490)  
    MidPointLine(550 + 380, 386, 550 + 380, 490)  

    # Adding details to building 5
    for i in range(25):
        MidPointLine(900 + i, 420 + i * .2, 900 + i, 450 + i * .4)  
    for i in range(25):
        MidPointLine(870 + i, 405 + i * .2, 870 + i, 435 + i * .4)  

def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    buildings()
    glColor3f(1.0, 0, 0)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1200, 1200)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Fire_Project")
glutDisplayFunc(showScreen)
glutMainLoop()