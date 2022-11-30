import numpy as np
from masspoint import MassPoint
from softbody import Softbody
from spring import Spring

def genCuboid(width, height, gap, rigidity=1, offset=np.array([0., 0.]), mass=1, stiffness=100, dampingFactor=10):
    """Generate a cuboid softbody.
    
    Args:
        width (int): Width of the cuboid.
        height (int): Height of the cuboid.
        gap (int): Gap between each mass point.
    
    Returns:
        [
            list: List of mass points,
            list: List of springs,
        ]"""
    
    # Generate columns
    columns = []
    for x in range(width):
        column = []
        for y in range(height):
            position = np.array([x * gap, y * gap], dtype=float) + offset
            column.append(MassPoint(position, mass))
        
        columns.append(column)
    
    # Generate springs
    springs = []
    for colIndex, column in enumerate(columns):
        # Generate springs between mass points in the same column
        for i in range(len(columns)):
            try:
                springs.append(Spring(column[i], column[i + 1], stiffness, dampingFactor))
            except IndexError:
                pass
        
        # Generate springs between up to 3 closest mass points in the next column
        if colIndex < len(columns) - 1:
            # Next column
            nextColumn = columns[colIndex + 1]

            for j in range(len(column)):
                # Find the closest mass points in the next column
                closestMassPoints = []
                for k in range(len(nextColumn)):
                    if len(closestMassPoints) >= rigidity + 2:
                        break
                    if abs(nextColumn[k].position[1] - column[j].position[1]) <= gap * rigidity:
                        closestMassPoints.append(nextColumn[k])
                
                # Generate springs between the closest mass points
                for l in range(len(closestMassPoints)):
                    springs.append(Spring(column[j], closestMassPoints[l], stiffness, dampingFactor))

    points = [point for column in columns for point in column]

    # Print all points
    for point in points:
        print(f"Point {point.id}: {point.position}")
    
    # Print all springs
    for spring in springs:
        print(f"Spring {spring.id}: {spring.masspoint1.id} - {spring.masspoint2.id}")

    return Softbody(points=points, springs=springs)