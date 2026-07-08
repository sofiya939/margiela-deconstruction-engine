import pygame
import numpy as np
import sys
from core.deconstructor import MargielaDeconstructor

class MargielaEngine:
    def __init__(self, width: int, height: int):
        pygame.init()
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maison Margiela 2026 // Deconstruction Engine")
        
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.colors = {
            "raw_white": (245, 245, 240),
            "void_black": (10, 10, 12),
            "wax_yellow": (225, 200, 160)
        }
        
        self.deconstructor = MargielaDeconstructor(self.width, self.height)
        self.active_melt = False 
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                elif event.key == pygame.K_SPACE:
                    self.active_melt = not self.active_melt
                    print(f"[SYSTEM]: Melt effect state: {self.active_melt}")

    def update(self):
        if self.active_melt:
            self.screen = self.deconstructor.apply_wax_melt(self.screen)

    def render(self):
        if not self.active_melt:
            self.screen.fill(self.colors["void_black"])
            pygame.draw.rect(self.screen, self.colors["raw_white"], (312, 184, 400, 400))
            pygame.draw.rect(self.screen, self.colors["wax_yellow"], (400, 250, 224, 250), 5)
            
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()
