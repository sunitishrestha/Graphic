import numpy as np
import matplotlib.pyplot as plt

from translation import translation
from rotation import rotation
from scaling import scaling
from reflection import reflection
from shearing import shearing
from composite import composite_transformation

# Original square
x = np.array([1, 3, 3, 1, 1])
y = np.array([1, 1, 3, 3, 1])
h=np.array([1, 1, 1, 1, 1])  # Homogeneous coordinate
points = np.array([x, y,h])

# Line endpoints A(1,1) and B(4,1) in homogeneous coordinates


# Transformation parameters
tx, ty = 2, 1        # Translation
sx, sy = 2, 2        # Scaling
angle = 45           # Rotation (degrees)

# Apply composite transformation
transformed_points, composite_matrix = composite_transformation(
    points, tx, ty, sx, sy, angle
)

def plot(original, transformed, title):
    plt.plot(original[0], original[1], 'bo-', label="Original")
    plt.plot(transformed[0], transformed[1], 'ro-', label="Transformed")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.axis("equal")
    plt.show()

# Translation
translated = translation(points, 2, 1)
plot(points, translated, "2D Translation")

#Rotation
rotated = rotation(points, 45)
plot(points, rotated, "2D Rotation")

#Scaling
scaled = scaling(points, 2, 1.5)
plot(points, scaled, "2D Scaling")

# Reflection
reflected = reflection(points)
plot(points, reflected, "2D Reflection")

# Shearing
sheared = shearing(points, 0,1)
plot(points, sheared, "2D Shearing")

plot(points, transformed_points, "Composite Transformation (T + S + R)")

print("Original Points:\n", points)
print("\nComposite Transformation Matrix:\n", composite_matrix)
print("\nTransformed Points:\n", transformed_points)