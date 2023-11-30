from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#################### Mid point line and circle algorithm:




#####################################
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #glColor3f(1.0, 1.0, 0.0) 
    #call the draw methods here

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(800, 800) #window size
glutInitWindowPosition(700, 25)
wind = glutCreateWindow(b"CSE423 project") #window name
glutDisplayFunc(showScreen)

glutMainLoop()