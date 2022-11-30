import numpy as np
from classid import genID

class Softbody:
    def __init__(self, points, springs=[]):
        self.points = points
        self.springs = springs
        self.gravity = np.array([0, 9.81])
        self.id = f"Softbody({genID()})"

        print(f"[{self.id}] Created with points: {[i.id for i in self.points]} and springs {[i.id for i in self.springs]}")
    
    def update(self, dt, polygons):
        """Update the softbody"""
        # Zero the force of the mass points
        for point in self.points:
            point.zero_force()

        # Add gravity to the mass points
        for point in self.points:
            point.add_force(self.gravity * point.mass)

        # Update the springs
        for spring in self.springs:
            spring.update(dt)

        # Update the velocity of the mass points
        for point in self.points:
            point.update_velocity(dt)

        # Update the position of the mass points
        for point in self.points:
            point.update_position(dt)
        
        # Check for collisions
        for point in self.points:
            point.check_polygon_collisions(polygons, dt)

        # print(f"All points: {[i.position for i in self.points]}")
        
    def draw(self, surface):
        """Draw the softbody"""
        for spring in self.springs:
            spring.draw(surface)

        for point in self.points:
            point.draw(surface)