from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# =================== Q3: Midpoint Circle Drawing Algorithm ===================
def plot_circle_points(xc, yc, x, y):
    """Plot 8 symmetric points of circle"""
    glBegin(GL_POINTS)
    glVertex2f(xc + x, yc + y)
    glVertex2f(xc - x, yc + y)
    glVertex2f(xc + x, yc - y)
    glVertex2f(xc - x, yc - y)
    glVertex2f(xc + y, yc + x)
    glVertex2f(xc - y, yc + x)
    glVertex2f(xc + y, yc - x)
    glVertex2f(xc - y, yc - x)
    glEnd()

def midpoint_circle(xc, yc, r):
    """Midpoint Circle Drawing Algorithm"""
    x = 0
    y = r
    d = 1 - r
    
    plot_circle_points(xc, yc, x, y)
    
    while x < y:
        x += 1
        if d < 0:
            d += 2 * x + 3
        else:
            y -= 1
            d += 2 * (x - y) + 5
        plot_circle_points(xc, yc, x, y)

def display_circle():
    """Display function for circle"""
    glClear(GL_COLOR_BUFFER_BIT)
    # glClearColor(1.0, 1.0, 1.0, 1.0)
    glColor3f(0.0, 1.0, 0.0)
    glPointSize(2.0)
    
    # Draw a single circle
    midpoint_circle(250, 250, 120)
    
    glFlush()

def reshape(window, width, height):
    """
    Handle window resizing
    """
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()