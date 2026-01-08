from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# =================== Q4: Line Graph using DDA ===================
def display_line_graph():
    """Display function for line graph using random data"""
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glClear(GL_COLOR_BUFFER_BIT)

    
    # Generate random data points
    n = 8  # Number of points
    margin = 50
    window_width = 500
    x_gap = (window_width - 2 * margin) / (n - 1)
    
    # Generate random y values
    random.seed(42)  # For consistent output
    data = []
    for i in range(n):
        x = margin + i * x_gap
        y = random.randint(100, 400)
        data.append((x, y))
    
    # Draw axes
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(1.0)
    dda_line(40, 50, 40, 450)    # Y-axis
    dda_line(40, 50, 500, 50)    # X-axis
    
    # Draw data points
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(6.0)
    glBegin(GL_POINTS)
    for point in data:
        glVertex2f(point[0], point[1])
    glEnd()
    
    # Connect points with lines using DDA
    glColor3f(0.0, 0.0, 1.0)
    glPointSize(2.0)
    for i in range(len(data) - 1):
        dda_line(int(data[i][0]), int(data[i][1]),
                 int(data[i+1][0]), int(data[i+1][1]))
    
    glFlush()

def dda_line(x1, y1, x2, y2):
    """DDA Line Drawing Algorithm"""
    dx = x2 - x1
    dy = y2 - y1
    
    # Determine number of steps
    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    
    # Calculate increment in x and y
    if steps == 0:
        return
    
    x_inc = dx / steps
    y_inc = dy / steps
    
    # Starting point
    x = x1
    y = y1
    
    glBegin(GL_POINTS)
    for i in range(int(steps) + 1):
        glVertex2f(round(x), round(y))
        x += x_inc
        y += y_inc
    glEnd()

def reshape(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set orthographic projection to match window pixels
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
