import glfw
from OpenGL.GL import *
WIDTH, HEIGHT = 800, 400

def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x2 >= x1 else -1
    sy = 1 if y2 >= y1 else -1
    x, y = x1, y1

    glBegin(GL_POINTS)
    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            # Map pixel to NDC
            glVertex2f((x / WIDTH) * 2 - 1, (y / HEIGHT) * 2 - 1)
            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
    else:
        p = 2 * dx - dy
        for _ in range(dy + 1):
            glVertex2f((x / WIDTH) * 2 - 1, (y / HEIGHT) * 2 - 1)
            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx
    glEnd()


# ---------- Display function ----------
def display_bresenham():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)  # Blue line
    glPointSize(5)
    bresenham_line(50, 50, 750, 350)  # Pixel coordinates
    glFlush()


# ---------- Reshape function ----------
def reshape(window, width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1, 1, -1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()