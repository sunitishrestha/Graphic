import numpy as np

def shearing(points, shx, shy):
    Sh = np.array([
        [1, shx, 0],
        [shy, 1, 0],
        [0, 0, 1]
    ])
    return Sh @ points
