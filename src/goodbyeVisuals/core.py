import pygame
from typing import List
from .shapes import Shape
from .audio import AudioProcessor


class Visualizer:
    def __init__(self, width: int = 800, height: int = 600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = False
        self.shapes = []
        self.audio_processor = AudioProcessor()
        self.blur_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        
    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        
        try:
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                
                # Get audio intensity
                bass_intensity = self.audio_processor.get_bass_intensity()
                
                # Clear surfaces
                self.screen.fill((0, 0, 0))
                self.blur_surface.fill((0, 0, 0, 0))
                
                # Update and draw shapes with audio reactivity
                for shape in self.shapes:
                    if hasattr(shape, 'update_with_audio'):
                        shape.update_with_audio(bass_intensity)
                    shape.update()
                    shape.draw(self.blur_surface)
                
                # Apply blur
                blur_amount = int(1 + bass_intensity * 10)  # Blur increases with bass
                blurred = gaussian_blur(self.blur_surface, blur_amount)
                self.screen.blit(blurred, (0, 0))
                
                pygame.display.flip()
                clock.tick(60)
                
        finally:
            self.cleanup()
    
    def cleanup(self):
        self.audio_processor.cleanup()
        pygame.quit()
