import pygame
import matplotlib.path as mplPath

class Polygon:
    def __init__(self, points):
        self.points = points
        self.path = mplPath.Path(points)
    
    def draw(self, surface):
        """Draw the polygon"""
        pygame.draw.polygon(surface, pygame.Color("white"), self.points)
    
    def contains(self, point):
        """Check if the polygon contains the point"""
        return self.path.contains_point(point)