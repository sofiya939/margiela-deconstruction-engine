import pygame
import numpy as np

class MargielaDeconstructor:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.wax_viscosity = 0.4  
    def apply_wax_melt(self, surface: pygame.Surface) -> pygame.Surface:  
        pixels = pygame.surfarray.array3d(surface)
        brightness = (0.299 * pixels[:,:,0] + 0.587 * pixels[:,:,1] + 0.114 * pixels[:,:,2])
        melt_mask = (brightness / 255.0) * self.wax_viscosity
        for x in range(self.width):
            shift = int(np.sin(x * 0.05) * 5 + np.random.uniform(0, 3))
            if shift > 0:
                pixels[x] = np.roll(pixels[x], shift, axis=0)
                pixels[x, :shift] = [225, 200, 160] 
        return pygame.surfarray.make_surface(pixels)

    def apply_text_glitch(self, text_surface: pygame.Surface) -> pygame.Surface:
        pixels = pygame.surfarray.array3d(text_surface)
        for y in range(0, self.height, 4):
            if np.random.rand() < 0.15: 
                shift = np.random.randint(-15, 15)
                pixels[:, y] = np.roll(pixels[:, y], shift, axis=0)
                
        return pygame.surfarray.make_surface(pixels)
