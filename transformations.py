from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import cos, sin, radians as rad

window_size = 500


def plot_points(points=([-.3,0,.3], [0,.6,0])):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for x, y in zip(points[0], points[1]):
        glVertex2f(x, y)
    glEnd()
    glFlush()
    option = int(input("enter 1-translation 2-rotation 3-reflection 4-scaling  "))
    if option == 1:
        x = float(input("enter x inc")) / window_size
        y = float(input("enter y inc")) / window_size
        for i in range(len(points[0])):
            points[0][i] += x
            points[1][i] += y
    elif option == 2:
        angle = float(input("enter angle"))
        for i in range(len(points[0])):
            points[0][i] = points[0][i] * cos(rad(angle)) + points[1][i] * sin(rad(angle))
            points[1][i] = points[1][i] * cos(rad(angle)) - points[0][i] * sin(rad(angle))
    elif option == 3: 
        axes = input("enter x axis or y axis (x/y) :")
        for i in range(len(points[0])):
            if axes == "x":

                points[1][i] = -points[1][i]
            elif axes == "y":
                points[0][i] = -points[0][i]
    elif option == 4:
        x = float(input("enter x scale"))
        y = float(input("enter y scale"))
        for i in range(len(points[0])):
            points[0][i]=points[0][i]*x
            points[1][i]=points[1][i]* y
    elif option==5:
        glFlush() 

def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("transformations")
    glutIdleFunc(plot_points)
    glutMainLoop()


main()
