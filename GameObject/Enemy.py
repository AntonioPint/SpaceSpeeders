from random import random

import pygame

from GameObject.GameObject import GameObject

class Enemy(GameObject):
    EnemyWidth = 75
    EnemyHeight = 75

    def __init__(self, position, acceleration=10):
        super().__init__(
            self.EnemyWidth,
            self.EnemyHeight,
            position,
            acceleration,
            pygame.image.load("assets/asteroid.png")
        )

    def move(self):
        # Add movement random in the beginning and then every
        # time it collides with wall it changes movement

        # If is not moving
        if self.movement == pygame.Vector2(0, 0):
            self.movement = pygame.Vector2(random()*self.acceleration -self.acceleration/2,random()*self.acceleration -self.acceleration/2)
            #self.movement = pygame.Vector2(-10, -10)
        
        VectorMovement = self.movement.normalize() * self.acceleration

        VectorMovementX = (VectorMovement[0], 0)
        VectorMovementY = (0, VectorMovement[1])

        self.position += pygame.Vector2(VectorMovementX)
        if self.isOutOfBounds():
            self.position -= pygame.Vector2(VectorMovementX)
            self.movement = pygame.Vector2(-self.movement.x, self.movement.y)

        self.position += pygame.Vector2(VectorMovementY)
        if self.isOutOfBounds():
            self.position -= pygame.Vector2(VectorMovementY)
            self.movement = pygame.Vector2(self.movement.x, -self.movement.y)

        #self.position += self.movement.normalize() * self.acceleration


        