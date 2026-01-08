import glfw
from OpenGL.GL import *

import glfw
# from suniti import display, reshape
# from DDA import display_dda,reshape
from bresenham import display_bresenham, reshape
# from circle import display_circle, reshape
# from line import display_line_graph, reshape
# from pi import display_pie_chart, reshape

# Main function
def main():
    """Initialize and run the OpenGL window"""
    # Initialize GLFW
    if not glfw.init():
        print("Failed to initialize GLFW")
        return
    
    # Create a windowed mode window and its OpenGL context
    window = glfw.create_window(800, 400, "SUNITI - PyOpenGL", None, None)
    if not window:
        glfw.terminate()
        print("Failed to create GLFW window")
        return
    
    # Make the window's context current
    glfw.make_context_current(window)
    
    # Set the reshape callback
    glfw.set_framebuffer_size_callback(window, reshape)
    
    # Initial reshape
    width, height = glfw.get_framebuffer_size(window)
    reshape(window, width, height)
    
    # Main loop
    while not glfw.window_should_close(window):
        # Render
        # display_dda()
   #display()\
        display_bresenham()
        # display_circle()
        # display_line_graph()
        # display_pie_chart()
        # Swap front and back buffers
        glfw.swap_buffers(window)
        
        # Poll for and process events
        glfw.poll_events()
    
    # Terminate GLFW
    glfw.terminate()

if __name__ == "__main__":
    main()
