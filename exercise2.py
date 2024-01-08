import time
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

move = 0.01

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    render_scene()
    glutSwapBuffers()

def idle():
    global move
    glTranslatef(move, 0, 0)
    # Check if the triangle has reached the right edge
    if move > 1.0:
        # Reset the position to the left
        glLoadIdentity()
        move = 0.01
    time.sleep(0.02)
    glutPostRedisplay()

def render_scene():
    glColor3f(1, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, -0.1, 0.1)
    glVertex3f(0.3, -0.1, 0.0)
    glVertex3f(0, 0.3, -0.2)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutCreateWindow("Animating a triangle")
glutInitWindowPosition(50, 50)
glutDisplayFunc(display)
glutIdleFunc(idle)
glutMainLoop()
