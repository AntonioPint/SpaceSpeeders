import pygame


class PercentageBar:
    def __init__(self, max_value, value, width, height, color_fill, color_background):
        self.max_value = max_value
        self.value = value
        self.width = width
        self.height = height
        self.color_fill = color_fill
        self.color_background = color_background

    def render(self):
        percentage = min(1, max(0, self.value / self.max_value))  # Calculate percentage between 0 and 1
        fill_width = int(self.width * percentage)

        # Create a Pygame Surface for the bar
        bar_surface = pygame.Surface((self.width, self.height), pygame.SRCALPHA)  # Enable alpha blending (transparency)
        bar_surface.fill(self.color_background)
        fill_rect = pygame.Rect(0, 0, fill_width, self.height)
        pygame.draw.rect(bar_surface, self.color_fill, fill_rect)

        return bar_surface