import numpy as np

def reflection(points):
    # Reflection about X-axis
    R = np.array([
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 1]
    ])
    return R @ points
# @ because reflection matrix needs to be 3x3 for homogeneous coordinates