import numpy as np

def genCircle(pos, radius):
    """Generate a circle polygon"""
    points = []
    for i in range(0, 360, 10):
        points.append(pos + np.array([np.cos(np.radians(i)) * radius, np.sin(np.radians(i)) * radius]))
    
    return points