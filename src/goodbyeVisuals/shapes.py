from abc import ABC, abstractmethod
import pygame
import math
from typing import Tuple, List

class Shape(ABC):
    def __init__(self, x: float, y: float, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.color = color
        
    @abstractmethod
    def update(self) -> None:
        """Update the shape's state."""
        pass
        
    @abstractmethod
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the shape on the given surface."""
        pass
    
class Circle(Shape):
    def __init__(
        self,
        x: float,
        y: float,
        radius: float,
        color: Tuple[int, int, int],
        pulse_speed: float = 1.0,
        pulse_range: float = 10.0
    ):
        super().__init__(x, y, color)
        self.base_radius = radius
        self.radius = radius
        self.pulse_speed = pulse_speed
        self.pulse_range = pulse_range
        self.time = 0
        
    def update(self) -> None:
        """Update the circle's pulse animation."""
        self.time += 0.02 * self.pulse_speed
        self.radius = self.base_radius + math.sin(self.time) * self.pulse_range
        
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the circle on the given surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.radius), 2)

class Polygon(Shape):
    def __init__(
        self, 
        x: float, 
        y: float, 
        radius: float, 
        sides: int, 
        color: Tuple[int, int, int],
        rotation_speed: float = 1.0
    ):
        super().__init__(x, y, color)
        self.radius = radius
        self.sides = sides
        self.rotation = 0
        self.rotation_speed = rotation_speed
        
    def update(self) -> None:
        """Update the polygon's rotation."""
        self.rotation += self.rotation_speed * 0.02
        
    def draw(self, surface: pygame.Surface) -> None:
        """Draw the polygon on the given surface."""
        points = []
        for i in range(self.sides):
            angle = self.rotation + (2 * math.pi * i / self.sides)
            point_x = self.x + self.radius * math.cos(angle)
            point_y = self.y + self.radius * math.sin(angle)
            points.append((point_x, point_y))
        pygame.draw.polygon(surface, self.color, points, 2)