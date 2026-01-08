import numpy as np

def translation(points, tx, ty):
    T = np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

    ones = np.ones((1, points.shape[1]))
    homogeneous = np.vstack((points, ones))

    result = T @ homogeneous
    return result[:2]
