from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def print_modelview_matrix():
    # Get the current modelview matrix
    matrix = glGetDoublev(GL_MODELVIEW_MATRIX)

    # Print the modelview matrix
    print("Modelview Matrix:")
    for i in range(4):
        for j in range(4):
            print(f"{matrix[i][j]:.4f}", end="\t")
        print()

def render_scene():
    # Draw a green triangle
    glColor3f(0, 1, 0)

    # Display the modelview matrix before translation
    print_modelview_matrix()

    # Translate the triangle
    glTranslatef(0.2, -0.4, 0)

    # Display the modelview matrix after translation
    print("\nModelview Matrix (After Translation):")
    print_modelview_matrix()

    # Draw the translated triangle
    glBegin(GL_TRIANGLES)
    glVertex3f(-0.8, -0.3, -0.1)
    glVertex3f(-0.3, 0.5, 0.0)
    glVertex3f(0.2, 0.3, 0.2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render_scene()
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
glutCreateWindow("Translate Triangle and Display Modelview Matrix")
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutMainLoop()
