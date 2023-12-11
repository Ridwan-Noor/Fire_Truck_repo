from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

truck = [350, 0, 350, 200]
houseOriginalColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]
houseColors = [[[218/255, 165/255, 32/255], [184/255, 134/255, 30/255]], [[255/255, 0/255, 128/255], [128/255, 0/255, 64/255]], [[191/255, 0/255, 255/255], [115/255, 0/255, 153/255]], [[51/255, 102/255, 255/255], [0/255, 45/255, 179/255]], [[138/255, 138/255, 92/255], [92/255, 92/255, 61/255]], [[117/255, 117/255, 163/255], [71/255, 71/255, 107/255]]]

houseHealth = [[0, 160, 150, 160], [0, 410, 150, 410], [0, 660, 150, 660], [650, 160, 800, 160], [650, 410, 800, 410], [650, 660, 800, 660]]


def showHouseHealth():
    global houseHealth
    for i in range(len(houseHealth)):
        glPointSize(15)
        glColor3f(1, 0, 0)
        MidPointLineAlgorithm(houseHealth[i][0], houseHealth[i][1], houseHealth[i][2], houseHealth[i][3])



def showTruck():
    global truck
    glPointSize(5)
    glColor3f(0, 0, 0)
    MidPointCircleAlgorithm(truck[0], truck[1]+30, 5)
    MidPointCircleAlgorithm(truck[0], truck[1]+15, 5)
    MidPointCircleAlgorithm(truck[0], truck[1]+80, 5)
    MidPointCircleAlgorithm(truck[0], truck[1]+95, 5)
    MidPointCircleAlgorithm(truck[0]+80, truck[1]+30, 5)
    MidPointCircleAlgorithm(truck[0]+80, truck[1]+15, 5)
    MidPointCircleAlgorithm(truck[0]+80, truck[1]+80, 5)
    MidPointCircleAlgorithm(truck[0]+80, truck[1]+95, 5)
    glPointSize(4)
    glColor3f(0, 0, 0)
    MidPointLineAlgorithm(truck[0], truck[1], truck[0], truck[1]+120)
    MidPointLineAlgorithm(truck[0], truck[1]+120, truck[0]+80, truck[1]+120)
    MidPointLineAlgorithm(truck[0]+80, truck[1]+120, truck[0]+80, truck[1])
    MidPointLineAlgorithm(truck[0], truck[1], truck[0]+80, truck[1])


    glColor3f(179/255, 0, 0)
    glPointSize(20)
    MidPointLineAlgorithm(truck[0]+10, truck[1]+130, truck[0]+10, truck[1]+140)
    MidPointLineAlgorithm(truck[0]+30, truck[1]+130, truck[0]+30, truck[1]+140)
    MidPointLineAlgorithm(truck[0]+50, truck[1]+130, truck[0]+50, truck[1]+140)
    MidPointLineAlgorithm(truck[0]+70, truck[1]+130, truck[0]+70, truck[1]+140)
    glPointSize(5)
    glColor3f(0, 0, 0)
    MidPointLineAlgorithm(truck[0], truck[1]+120, truck[0]+80, truck[1]+120)
    MidPointLineAlgorithm(truck[0], truck[1]+150, truck[0]+80, truck[1]+150)
    MidPointLineAlgorithm(truck[0], truck[1]+120, truck[0], truck[1]+150)
    MidPointLineAlgorithm(truck[0]+80, truck[1]+150, truck[0]+80, truck[1]+120)
    glColor3f(204/255, 204/255, 204/255)
    MidPointCircleAlgorithm(truck[0]+10, truck[1]+140, 3)
    MidPointCircleAlgorithm(truck[0]+70, truck[1]+140, 3)

    glPointSize(20)
    glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(truck[0]+10, truck[1]+5, truck[0]+10, truck[1]+105)
    glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(truck[0]+20, truck[1]+5, truck[0]+20, truck[1]+105)
    glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(truck[0]+30, truck[1]+5, truck[0]+30, truck[1]+105)
    glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(truck[0]+40, truck[1]+5, truck[0]+40, truck[1]+105)
    glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(truck[0]+50, truck[1]+5, truck[0]+50, truck[1]+105)
    glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(truck[0]+60, truck[1]+5, truck[0]+60, truck[1]+105)
    glColor3f(200/255, 0, 0)
    MidPointLineAlgorithm(truck[0]+70, truck[1]+5, truck[0]+70, truck[1]+105)
    glColor3f(200/255, 0, 0) #
    MidPointLineAlgorithm(truck[0]+60, truck[1]+5, truck[0]+60, truck[1]+105)
    glPointSize(5)
    glColor3f(200/255, 51/255, 51/255)
    MidPointCircleAlgorithm(truck[0]+40, truck[1]+135, 3)
    glColor3f(0, 0, 0)


    MidPointLineAlgorithm(truck[0]+10, truck[1]+105, truck[0]+10, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+20, truck[1]+105, truck[0]+20, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+30, truck[1]+105, truck[0]+30, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+40, truck[1]+105, truck[0]+40, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+50, truck[1]+105, truck[0]+50, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+60, truck[1]+105, truck[0]+60, truck[1]+10)
    MidPointLineAlgorithm(truck[0]+70, truck[1]+105, truck[0]+70, truck[1]+10)


    




def buildHouse(x1, y1, x2, y2, x3, y3, x4, y4, color1, color2):
    glPointSize(3)
    glColor3f(*color1)
    MidPointLineAlgorithm(x1+25, y1+20, x1+25, y1+135)
    MidPointLineAlgorithm(x1+25, y1+135, x1+135, y1+135)
    MidPointLineAlgorithm(x1+135, y1+135, x1+135, y1+20)
    glPointSize(10)
    MidPointLineAlgorithm(x1+30, y1+130, x1+130, y1+130)
    MidPointLineAlgorithm(x1+30, y1+120, x1+130, y1+120)
    MidPointLineAlgorithm(x1+30, y1+110, x1+30, y1+30)
    MidPointLineAlgorithm(x1+60, y1+110, x1+60, y1+30)
    MidPointLineAlgorithm(x1+70, y1+110, x1+70, y1+30)
    MidPointLineAlgorithm(x1+80, y1+110, x1+80, y1+30)
    MidPointLineAlgorithm(x1+90, y1+110, x1+90, y1+30)
    MidPointLineAlgorithm(x1+100, y1+110, x1+100, y1+30)
    MidPointLineAlgorithm(x1+130, y1+110, x1+130, y1+30)
    MidPointLineAlgorithm(x1+30, y1+90, x1+130, y1+90)
    MidPointLineAlgorithm(x1+30, y1+80, x1+130, y1+80)
    MidPointLineAlgorithm(x1+30, y1+50, x1+130, y1+50)
    MidPointLineAlgorithm(x1+30, y1+20, x1+130, y1+20)
    glPointSize(3)
    glColor3f(*color2)
    MidPointLineAlgorithm(x1+25, y1+135, x1+17, y1+120)
    MidPointLineAlgorithm(x1+17, y1+120, x1+17, y1+25)
    glPointSize(8)
    MidPointLineAlgorithm(x1+19, y1+120, x1+19, y1+25)
    glPointSize(5)
    MidPointLineAlgorithm(x1+25, y1+130, x1+25, y1+20)


def buildHouses():
    global houseHealth
    global houseColors
    # House Serial: Bottom Left to Top Left, then, Bottom Right to Top Right
    # buildHouse(0, 0, 150, 0, 0, 150, 150, 150, [218/255, 165/255, 32/255], [184/255, 134/255, 30/255])
    # buildHouse(0, 250, 150, 250, 0, 400, 150, 400, [255/255, 0/255, 128/255], [128/255, 0/255, 64/255])
    # buildHouse(0, 500, 150, 500, 0, 650, 150, 650, [191/255, 0/255, 255/255], [115/255, 0/255, 153/255])
    # buildHouse(650, 0, 800, 0, 650, 150, 800, 150, [51/255, 102/255, 255/255], [0/255, 45/255, 179/255])
    # buildHouse(650, 250, 800, 250, 650, 400, 800, 400, [117/255, 117/255, 163/255], [71/255, 71/255, 107/255])
    # buildHouse(650, 500, 800, 500, 650, 650, 800, 650, [138/255, 138/255, 92/255], [92/255, 92/255, 61/255])
    buildHouse(0, 0, 150, 0, 0, 150, 150, 150, houseColors[0][0], houseColors[0][1])
    buildHouse(0, 250, 150, 250, 0, 400, 150, 400, houseColors[1][0], houseColors[1][1])
    buildHouse(0, 500, 150, 500, 0, 650, 150, 650, houseColors[2][0], houseColors[2][1])
    buildHouse(650, 0, 800, 0, 650, 150, 800, 150, houseColors[3][0], houseColors[3][1])
    buildHouse(650, 250, 800, 250, 650, 400, 800, 400, houseColors[4][0], houseColors[4][1])
    buildHouse(650, 500, 800, 500, 650, 650, 800, 650, houseColors[5][0], houseColors[5][1])


    # # House 1
    # glPointSize(3)
    # glColor3f(218/255, 165/255, 32/255)
    # MidPointLineAlgorithm(25, 20, 25, 135)
    # MidPointLineAlgorithm(25, 135, 135, 135)
    # MidPointLineAlgorithm(135, 135, 135, 20)
    # glPointSize(10)
    # MidPointLineAlgorithm(30, 130, 130, 130)
    # MidPointLineAlgorithm(30, 120, 130, 120)
    # MidPointLineAlgorithm(30, 110, 30, 30)
    # MidPointLineAlgorithm(60, 110, 60, 30)
    # MidPointLineAlgorithm(70, 110, 70, 30)
    # MidPointLineAlgorithm(80, 110, 80, 30)
    # MidPointLineAlgorithm(90, 110, 90, 30)
    # MidPointLineAlgorithm(100, 110, 100, 30)
    # MidPointLineAlgorithm(130, 110, 130, 30)
    # MidPointLineAlgorithm(30, 90, 130, 90)
    # MidPointLineAlgorithm(30, 80, 130, 80)
    # MidPointLineAlgorithm(30, 50, 130, 50)
    # MidPointLineAlgorithm(30, 20, 130, 20)
    # glPointSize(3)
    # glColor3f(184/255, 134/255, 30/255)
    # MidPointLineAlgorithm(25, 135, 17, 120)
    # MidPointLineAlgorithm(17, 120, 17, 25)
    # glPointSize(8)
    # MidPointLineAlgorithm(19, 120, 19, 25)
    # glPointSize(5)
    # MidPointLineAlgorithm(25, 130, 25, 20)




    # House 2





#################### Mid point line and circle algorithm:
def drawPoint(x, y):
    
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()

def findZone(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) >= abs(dy):
        if dx >= 0 and dy >= 0:
            return 0
        elif dx <= 0 and dy >= 0:
            return 3
        elif dx <= 0 and dy <= 0:
            return 4
        elif dx >= 0 and dy <= 0:
            return 7
    else:
        if dx >= 0 and dy >= 0:
            return 1
        elif dx <= 0 and dy >= 0:
            return 2
        elif dx <= 0 and dy <= 0:
            return 5
        elif dx >= 0 and dy <= 0:
            return 6
        
def convertToZone0(x, y, zone):
    if zone == 0:
        return x, y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return y, -x
    elif zone == 3:
        return -x, y
    elif zone == 4:
        return -x, -y
    elif zone == 5:
        return -y, -x
    elif zone == 6:
        return -y, x
    elif zone == 7:
        return x, -y

def convertToOriginalZone(x, y, zone):
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

def MidPointLineAlgorithm(x1, y1, x2, y2):
    zone = findZone(x1, y1, x2, y2)

    x1, y1 = convertToZone0(x1, y1, zone)
    x2, y2 = convertToZone0(x2, y2, zone)

    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx
    dE = 2 * dy
    dNE = 2 * (dy - dx)
    x = x1
    y = y1
    while(x <= x2):
        x_original, y_original = convertToOriginalZone(x, y, zone)
        drawPoint(x_original, y_original)
        x += 1
        if d > 0:
            d += dNE
            y = y + 1
        else:
            d += dE

def drawPoints(x, y, dx, dy):
    #global circles
    #print(circles)
    #if ((-375 <= x+dx <= 375) and (-375 <= -x+dx <= 375) and (-375 <= y+dx <= 375) and (-375 <= -y+dx <= 375) and (-375 <= y+dy <= 375) and (-375 <= -y+dy <= 375) and (-375 <= -x+dy <= 375) and (-375 <= x+dy <= 375)):
    drawPoint(x+dx, y+dy)
    drawPoint(-x+dx, y+dy)
    drawPoint(-x+dx, -y+dy)
    drawPoint(x+dx, -y+dy)
    drawPoint(y+dx, x+dy)
    drawPoint(-y+dx, x+dy)
    drawPoint(-y+dx, -x+dy)
    drawPoint(y+dx, -x+dy)


def MidPointCircleAlgorithm(x, y, r):
    x0 = 0
    y0 = r
    d = 1-r
    drawPoints(x0, y0, x, y)
    while (x0 < y0):
        if (d < 0):
            d += (2*x0 + 3)
            x0 += 1
        else:
            d += ((2*x0) - (2*y0) + 5)
            x0 += 1
            y0 -= 1
        drawPoints(x0, y0, x, y)


#####################################
def specialKeyListener(key, x, y):
    global truck
    if key == GLUT_KEY_UP:
        if (truck[1] + 150 + 5 <= 800): 
            truck[1] += 5

        
    elif key == GLUT_KEY_DOWN:
        if (truck[1] - 5 >= 0): 
            truck[1] -= 5

    elif key == GLUT_KEY_LEFT:
        if (truck[0] - 10 >= 150): 
            truck[0] -= 10
   


    elif key == GLUT_KEY_RIGHT:
        if (truck[0] + 80 + 10 <= 650): 
            truck[0] += 10

    glutPostRedisplay()




def iterate():
    glViewport(0, 0, 800, 800)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 800, 0.0, 800, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0, 128/255, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) 
    #call the draw methods here
    # glColor3f(1, 1, 1)  
    # x1, y1 = 0, 0
    # x2, y2 = 400, 400
    # MidPointLineAlgorithm(x1, y1, x2, y2)
    # MidPointCircleAlgorithm(400, 400, 50)
    glPointSize(3)
    glColor3f(179/255, 179/255, 179/255)
    MidPointLineAlgorithm(400, 700, 400, 5)
    buildHouses()
    showTruck()
    showHouseHealth()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(700, 25)
wind = glutCreateWindow(b"CSE423 project") #window name
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutMainLoop()
