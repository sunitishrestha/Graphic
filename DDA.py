from OpenGL.GL import *

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = int(abs(dx) if abs(dx) > abs(dy) else abs(dy))
    if steps == 0:
        glBegin(GL_POINTS)
        glVertex2f(x1, y1)
        glEnd()
        return

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1

    glBegin(GL_LINE_STRIP)  # <-- Connect points into a solid line
    for _ in range(steps + 1):
        glVertex2f(x, y)
        x += x_inc
        y += y_inc
    glEnd()



def display_dda():
    """
    Display function for DDA line
    """
   # glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)  # Red line
    glPointSize(5.0)

    # Draw the line from bottom-left to top-right
    dda_line(-0.9, -0.9, 0.9, 0.9)

    glFlush()


def reshape(window, width, height):
    """
    Handle window resizing
    """
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
