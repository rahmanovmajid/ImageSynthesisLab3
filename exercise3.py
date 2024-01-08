from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def render_Scene():
    # Perform a translation to shift the first/red triangle to the bottom
    glTranslated(0.0, -0.1, 0)
    
    # Push the current matrix stack
    glPushMatrix()
    
    # Replace the current matrix with the identity matrix
    glLoadIdentity()
    
    # Draw first/red triangle in Red
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, -0.1, -0.8)
    glVertex3f(0.3, -0.1, -1)
    glVertex3f(0, 0.3, -0.9)
    glEnd()
    
    # Pop the current matrix stack
    glPopMatrix()
    
    # Perform a translation to shift the second/yellow triangle to the top
    glTranslated(0.0, 0.2, 0)
    
    # Draw second/yellow triangle in Yellow
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.3, 0.2, 0.0)
    glVertex3f(-0.7, 0.5, 0.0)
    glVertex3f(-0.5, 0.7, 0.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render_Scene()
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Shift Triangles in Window")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
