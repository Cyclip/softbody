import pygame
import matplotlib.path as mplPath
import constants

class Polygon:
    def __init__(self, points, border=2):
        self.points = points
        self.path = mplPath.Path(points)
        self.border = border
    
    def draw(self, surface):
        """Draw the polygon"""
        if self.border:
            pygame.draw.polygon(surface, pygame.Color("white"), self.points, self.border)
        else:
            pygame.draw.polygon(surface, pygame.Color("white"), self.points)
    
    def contains(self, point):
        """Check if the polygon contains the point"""
        return self.path.contains_point(point)