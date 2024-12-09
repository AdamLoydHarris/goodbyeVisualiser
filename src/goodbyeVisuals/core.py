import pygame
from typing import List
from .shapes import Shape
from .effects import gaussian_blur

class Visualizer:
    def __init__(self, width: int = 800, height: int = 600):
        """Initialize the visualizer with given dimensions."""
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = False
        self.shapes: List[Shape] = []
        
    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the visualization."""
        self.shapes.append(shape)
        
    def run(self) -> None:
        """Run the visualization loop."""
        self.running = True
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            # Clear screen
            self.screen.fill((0, 0, 0))
            
            # Update and draw shapes
            for shape in self.shapes:
                shape.update()
                shape.draw(self.screen)
                
            pygame.display.flip()
            clock.tick(60)
            
        pygame.quit()