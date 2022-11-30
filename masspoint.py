import numpy as np
import pygame
from classid import genID

class MassPoint:
    def __init__(self, position, mass, velocity=np.array([0, 0], dtype=float)):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.force = np.array([0, 0], dtype=float)
        self.id = f"Point({genID()})"
        self.color = pygame.Color("red")
    
    def zero_force(self):
        """Set the force to zero"""
        self.force = np.array([0, 0], dtype=float)
    
    def add_force(self, force):
        """Add a force to the mass point after zeroing the force"""
        self.force += force
        print(f"[{self.id}] Force: {self.force} (+{force})")
    
    def check_polygon_collision(self, polygon, dt):
        """Check if the mass point collides with the polygon"""
        if polygon.contains(self.position):
            self.position -= self.velocity * dt
            self.velocity *= -0.2

            return True
        
        return False
    
    def check_polygon_collisions(self, polygons, dt):
        """Check if the mass point collides with the polygons"""
        for polygon in polygons:
            if self.check_polygon_collision(polygon, dt):
                break
    
    def update_velocity(self, dt):
        """Update the velocity of the mass point"""
        self.velocity += self.force / self.mass * dt
    
    def update_position(self, dt):
        """Update the position of the mass point"""
        print(f"[{self.id}] Position({self.position.dtype}), Velocity({self.velocity.dtype})")
        self.position += self.velocity * dt
        print(f"[{self.id}] Position: {self.position} (+{self.velocity * dt})")
    
    def draw(self, surface):
        """Draw the mass point"""
        pygame.draw.circle(surface, self.color, self.position.astype(int), 3)

        # Draw force arrow
        pygame.draw.line(surface, pygame.Color("blue"), self.position.astype(int), (self.position + self.force).astype(int), 1)