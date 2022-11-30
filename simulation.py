import pygame
import numpy as np
import constants

pygame.init()

pygame.display.set_caption("Softbody Simulation")
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface(constants.SIZE)
background.fill(constants.BG_COL)

# ========================== SIMULATION ========================== #
class Simulation:
    def __init__(self, softbodies, polygons, speed=1):
        self.softbodies = softbodies
        self.polygons = polygons
        self.speed = speed
        self.mousePower = 1000
    
    def run(self):
        running = True
        clock = pygame.time.Clock()
        lockedPoint = None
        mousePushing = False

        font = pygame.font.SysFont('Monocraft Medium', 30)

        while running:
            dt = clock.tick(60) / 1000.0 * self.speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # If left mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if lockedPoint is None:
                        pos = np.array(pygame.mouse.get_pos(), dtype=float)
                        closestPoint = None
                        closestDistance = float('inf')

                        # Find the closest point
                        for softbody in self.softbodies:
                            for point in softbody.points:
                                distance = np.linalg.norm(point.position - pos)
                                if distance < closestDistance:
                                    closestPoint = point
                                    closestDistance = distance

                        # If the closest point is close enough
                        if closestPoint:
                            lockedPoint = closestPoint
                            lockedPoint.color = pygame.Color("orange")
                elif event.type == pygame.MOUSEBUTTONUP:
                    if lockedPoint:
                        lockedPoint.color = pygame.Color("red")
                    lockedPoint = None

                # If right mouse button is pressed
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    # Push all points away from the mouse
                    # p α 1/d²
                    pos = np.array(pygame.mouse.get_pos(), dtype=float)
                    for softbody in self.softbodies:
                        for point in softbody.points:
                            distance = np.linalg.norm(point.position - pos)
                            if distance < 1000:
                                point.add_force((point.position - pos) * self.mousePower / distance ** 2)

                    mousePushing = True
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    mousePushing = False

            window_surface.blit(background, (0, 0))
            
            if mousePushing:
                # Draw 8 force arrows from mouse pos
                for i in range(8):
                    angle = i * np.pi / 4
                    pos = np.array(pygame.mouse.get_pos(), dtype=float)
                    pygame.draw.line(window_surface, pygame.Color("blue"), pos.astype(int), (pos + np.array([np.cos(angle), np.sin(angle)]) * 100).astype(int), 1)

            # Update softbodies
            for softbody in self.softbodies:
                softbody.update(dt, self.polygons)

            if lockedPoint:
                lockedPoint.velocity = np.array([0, 0], dtype=float)
                lockedPoint.position = np.array(pygame.mouse.get_pos(), dtype=float)

            # Draw polygons
            for polygon in self.polygons:
                polygon.draw(window_surface)
            
            # Draw softbodies
            for softbody in self.softbodies:
                softbody.draw(window_surface)
            
            # Draw speed
            speed_text = font.render(f"{self.speed}x speed    {'Pushing' if mousePushing else ''}", True, pygame.Color("white"))
            window_surface.blit(speed_text, (10, 10))

            pygame.display.update()
# ========================== SIMULATION ========================== #