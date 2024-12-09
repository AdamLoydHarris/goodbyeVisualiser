import pygame
import numpy as np
from typing import Tuple

def gaussian_blur(surface: pygame.Surface, radius: int = 5) -> pygame.Surface:
    """Apply gaussian blur to a surface"""
    size = surface.get_size()
    scaled_size = (size[0] // radius, size[1] // radius)
    
    # Scale down
    scaled = pygame.transform.smoothscale(surface, scaled_size)
    # Scale back up
    blurred = pygame.transform.smoothscale(scaled, size)
    
    return blurred