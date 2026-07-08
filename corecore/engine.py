import pygame
import numpy as np
import sys

class MargielaEngine:
    def __init__(self, width: int, height: int):
        pygame.init()
        pygame.mixer.init()
        
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Maison Margiela 2026 // Deconstruction Engine")
        
        self.clock = pygame.time.Clock()
        self.is_running = True
        
        self.colors = {
            "raw_white": (245, 245, 240),
            "void_black": (10, 10, 12),
            "wax_yellow": (225, 200, 160),
            "industrial_grey": (60, 62, 65)
        }
        
        self.layers = []
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_running = False
                elif event.key == pygame.K_SPACE:
                    self.trigger_deconstruction()

    def trigger_deconstruction(self):
        print("[SYSTEM]: Deconstructing current look... Reassembling atoms.")

    def update(self):
        pass

    def render(self):
        self.screen.fill(self.colors["void_black"])
        pygame.draw.rect(self.screen, self.colors["raw_white"], (50, 50, self.width - 100, self.height - 100), 1)
        pygame.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
            
        pygame.quit()
        sys.exit()
