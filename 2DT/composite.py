import numpy as np
import math

def composite_transformation(points, tx, ty, sx, sy, angle):
    T = np.array([[1, 0, tx],
                  [0, 1, ty],
                  [0, 0, 1]])
    S = np.array([[sx, 0, 0],
                  [0, sy, 0],
                  [0, 0, 1]])
    theta = math.radians(angle)
    R = np.array([[math.cos(theta), -math.sin(theta), 0],
                  [math.sin(theta), math.cos(theta), 0],
                  [0, 0, 1]])
    C = R @ S @ T
    transformed_points = C @ points
    return transformed_points, C
