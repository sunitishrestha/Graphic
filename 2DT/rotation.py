import numpy as np
import math

def rotation(points, angle):
    theta = math.radians(angle)

    R = np.array([
        [math.cos(theta), -math.sin(theta),0],
        [math.sin(theta),  math.cos(theta),0],
        [0, 0, 1]
    ])

    return R @ points
