import numpy as np
import pygame
from classid import genID

class Spring:
    def __init__(self, masspoint1, masspoint2, stiffness, dampingFactor):
        self.masspoint1 = masspoint1
        self.masspoint2 = masspoint2
        self.restLength = self.length()
        self.stiffness = stiffness
        self.dampingFactor = dampingFactor
        self.id = f"Spring({genID()})"

        # print(f"[{self.id}] Initialised with {self.masspoint1.id} and {self.masspoint2.id}")
    
    def update(self, dt):
        """Update the spring. This will add spring forces to the mass points"""
        # Calculate the force
        force = self.stiffness * (self.restLength - self.length())
        # Calculate the damping force
        dampingForce = self.dampingFactor * self.velocity()
        totalForce = force - dampingForce
        # Add the force to the mass points
        self.masspoint1.add_force(totalForce * self.direction())
        self.masspoint2.add_force(-totalForce * self.direction())
        # print(f"[{self.id}] Force: {force}, Damping Force: {dampingForce}, Direction: {self.direction()}")
    
    def length(self):
        """Calculate the length of the spring"""
        return np.linalg.norm(self.masspoint1.position - self.masspoint2.position)
    
    def velocity(self):
        """Calculate the velocity of the spring
        Equation: v = (v1 - v2) * direction
        """
        return np.dot(self.masspoint1.velocity - self.masspoint2.velocity, self.direction())
    
    def direction(self):
        """Calculate the direction of the spring (normalized)"""
        return (self.masspoint1.position - self.masspoint2.position) / self.length()
    
    def draw(self, surface):
        """Draw the spring"""
        # If mouse is hovering over
        pos = np.array(pygame.mouse.get_pos())
        dist = 5
        if np.linalg.norm(pos - self.masspoint1.position) < dist or np.linalg.norm(pos - self.masspoint2.position) < 10:
            color = pygame.Color("green")
        else:
            color = pygame.Color("white")

        pygame.draw.line(surface, color, self.masspoint1.position.astype(int), self.masspoint2.position.astype(int))