Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Fitri Ariska
# 20051397082
# D4 MI 2020B

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-50.0, 50.0, -50.0, 50.0)
    glPointSize(5)


def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glEnd()


def bresenham_drawing_circle(r):

    # contoh soal jika nilai center circle (3,3) dan r = 9
    x_center = 3
    y_center = 3

    r = 9
    x = 0
    y = r

    # parameter keputusan bresenham
    d = 3 - 2 * r

    # membuat titik pada koordinat yang ditentukan
    plot(x + x_center, y + y_center)

    while y > x:

        if d < 0:
            x += 1
            d += 4 * x + 6
        else:
            x += 1
            y -= 1
            d += (4 * (x - y)) + 10 

        # Jika x <= y sudah terpenuhi, maka perulangan akan di hentikan.
        # jika nilai (x,y)sudah didapatkan, lalu membalikan nilai (y, x)

        # Untuk pixel (x, y)

        # Quadrant 1
        plot(x + x_center, y + y_center)

        # Quadrant 2
        plot(x + x_center, -y + y_center)

        # Quadrant 3
        plot(-x + x_center, -y + y_center)

        # Quadrant 4
        plot(-x + x_center, y + y_center)

        # Untuk pixel (y, x)

        # Quadrant 1
        plot(y + x_center, x + y_center)

        # Quadrant 2
        plot(-y + x_center, x + y_center)

        # Quadrant 3
        plot(-y + x_center, -x + y_center)

        # Quadrant 4
        plot(y + x_center, -x + y_center)


def plotpoints():

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 1.0)

    glBegin(GL_LINES)

    glVertex2f(-50, 0)
    glVertex2f(50, 0)

    glVertex2f(0, -50)
    glVertex2f(0, 50)

    glEnd()

    bresenham_drawing_circle(40)

    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Bresenham Circle - Fitri Ariska")
    glutDisplayFunc(plotpoints)

    init()
    glutMainLoop()

main()