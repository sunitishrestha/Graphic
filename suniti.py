import glfw
from OpenGL.GL import *
from OpenGL.GLU import *


# Helper function to draw a filled rectangle
def drawRect(x, y, width, height):
    """Draw a filled rectangle using GL_POLYGON"""
    glBegin(GL_POLYGON)
    glVertex2f(x, y)
    glVertex2f(x + width, y)
    glVertex2f(x + width, y + height)
    glVertex2f(x, y + height)
    glEnd()

# Function to draw letter S
def drawS(x, y):
    """Draw letter S using rectangles"""
    glColor3f(0.2, 0.6, 1.0)  # Cyan color
    # Top horizontal bar
    drawRect(x, y + 0.7, 0.15, 0.1)
    # Left vertical bar (top part)
    drawRect(x, y + 0.4, 0.05, 0.3)
    # Middle horizontal bar
    drawRect(x, y + 0.35, 0.15, 0.1)
    # Right vertical bar (bottom part)
    drawRect(x + 0.1, y + 0.05, 0.05, 0.3)
    # Bottom horizontal bar
    drawRect(x, y, 0.15, 0.1)

# Function to draw letter U
def drawU(x, y):
    """Draw letter U using rectangles"""
    glColor3f(1.0, 0.5, 0.0)  # Orange color
    # Left vertical bar
    drawRect(x, y, 0.05, 0.8)
    # Right vertical bar
    drawRect(x + 0.15, y, 0.05, 0.8)
    # Bottom horizontal bar
    drawRect(x, y, 0.2, 0.1)

# Function to draw letter N
def drawN(x, y):
    """Draw letter N using rectangles"""
    glColor3f(0.4, 0.8, 0.9)  # Light blue color
    # Left vertical bar
    drawRect(x, y, 0.05, 0.8)
    # Right vertical bar
    drawRect(x + 0.1, y, 0.05, 0.8)
    # Diagonal bar using GL_POLYGON for proper slant
    glBegin(GL_POLYGON)
    glVertex2f(x + 0.05, y + 0.8)  # Top left
    glVertex2f(x + 0.08, y + 0.8)  # Top right
    glVertex2f(x + 0.12, y)        # Bottom right
    glVertex2f(x + 0.1, y)         # Bottom left
    glEnd()

# Function to draw letter I
def drawI(x, y):
    """Draw letter I using rectangles"""
    glColor3f(0.9, 0.3, 0.4)  # Red/Pink color
    # Vertical bar
    drawRect(x, y, 0.05, 0.8)

# Function to draw letter T
def drawT(x, y):
    """Draw letter T using rectangles"""
    glColor3f(0.5, 0.9, 0.3)  # Light green color
    # Top horizontal bar
    drawRect(x, y + 0.7, 0.2, 0.1)
    # Vertical bar (centered)
    drawRect(x + 0.075, y, 0.05, 0.8)

# Display callback function
def display():
    """Main display function to render all letters"""
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0.1, 0.1, 0.15, 1.0)  # Dark background
    
    # Draw each letter with spacing
    drawS(-0.85, -0.4)
    drawU(-0.6, -0.4)
    drawN(-0.35, -0.4)
    drawI(-0.1, -0.4)
    drawT(0.1, -0.4)
    drawI(0.35, -0.4)
    
    glFlush()

# Reshape callback function
def reshape(window, width, height):
    """Handle window resizing"""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()