from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math

# =================== Q5: Pie Chart ===================
def display_pie_chart():
    """Display function for pie chart with random slices"""
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(1.0, 1.0, 1.0, 1.0)
    
    # Center coordinates
    cx, cy = 250, 250  # Center coordinates
    radius = 150
    n = 5  # Number of slices
    steps_per_slice = 100
    
    # Generate random slice values
    random.seed(42)
    data = [random.randint(5, 50) for _ in range(n)]
    total = sum(data)
    
    # Convert to angles
    angles = [(360.0 * d / total) for d in data]
    
    # Define colors for each slice
    colors = [
        (1.0, 0.0, 0.0),  # Red
        (0.0, 1.0, 0.0),  # Green
        (0.0, 0.0, 1.0),  # Blue
        (1.0, 1.0, 0.0),  # Yellow
        (1.0, 0.0, 1.0),  # Magenta
        (0.0, 1.0, 1.0)   # Cyan
    ]
    
    start_angle = 0
    
    for i in range(n):
        end_angle = start_angle + angles[i]
        glColor3f(*colors[i])
        
        # Generate points for this slice
        points = [(cx, cy)]  # Start with center
        
        for k in range(steps_per_slice + 1):
            angle = start_angle + (k / steps_per_slice) * (end_angle - start_angle)
            angle_rad = angle * math.pi / 180
            x = cx + radius * math.cos(angle_rad)
            y = cy + radius * math.sin(angle_rad)
            points.append((x, y))
        
        # Draw the slice using GL_TRIANGLE_FAN
        glBegin(GL_TRIANGLE_FAN)
        for point in points:
            glVertex2f(point[0], point[1])
        glEnd()
        
        start_angle = end_angle
    
    # Draw the circle outline
    glColor3f(0.0, 0.0, 0.0)
    glPointSize(2.0)
    midpoint_circle(cx, cy, radius)
    
    glFlush()

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

def reshape(window, width, height):
   
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, width, 0, height, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()