import pygame
import random

class MargielaGenerator:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        
    def generate_procedural_look(self) -> list:
        layers = []
        num_elements = random.randint(3, 7)
        
        for _ in range(num_elements):
            w = random.randint(100, 500)
            h = random.randint(150, 600)
            x = (self.width - w) // 2 + random.randint(-50, 50)
            y = (self.height - h) // 2 + random.randint(-50, 50)
            
            color_chance = random.random()
            if color_chance < 0.4:
                color = (245, 245, 240)
            elif color_chance < 0.8:
                color = (225, 200, 160)
            else:
                color = (60, 62, 65)
                
            layers.append({"rect": (x, y, w, h), "color": color, "width": random.choice([0, 2, 5])})
            
        return layers
