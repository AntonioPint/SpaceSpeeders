import pygame
from GameObject.Enemy.Enemy import Enemy
from GameObject.PercentageBar import PercentageBar

class EnemyBiggerAsteroid(Enemy):
    
    Health = 15
    Height = 200
    Width = 200
    AccelerationIncrement = .0005
    EXTRA_POINTS = 2000
    
    def __init__(self, position, acceleration=0.5):
        super().__init__(
            position,
            acceleration
        )

    def whenHit(self):
        super().whenHit()

        # self.setImage(pygame.image.load("assets/logo.png"))
        # self.addAdditionalImage(PercentageBar.render)
        # self.setImage(self.getCombinedImage())
    
        