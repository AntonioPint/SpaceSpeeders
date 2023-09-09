from random import random

import pygame

from GameObject.GameObject import GameObject


class Enemy(GameObject):
    Width = 75
    Height = 75
    Angle = 0
    Health = 1
    AccelerationIncrement = 0.01
    Image = pygame.image.load("assets/asteroid.png")

    def __init__(self, position, acceleration=1):
        super().__init__(
            self.Width,
            self.Height,
            position,
            acceleration,
            self.Image
        )
        self.setCallback()

    def move(self):
        # Add movement random in the beginning and then every
        # time it collides with wall it changes movement

        # If is not moving
        if self.movement == pygame.Vector2(0, 0):
            self.movement = pygame.Vector2(random(
            )*self.acceleration - self.acceleration/2, random()*self.acceleration - self.acceleration/2)

        self.Angle += 10

        if self.Angle == 360:
            self.Angle = 0

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

        self.acceleration += self.AccelerationIncrement

    def passCallback():
        pass

    def setCallback(self, func=passCallback):
        self.Callback = func

    def getHealth(self):
        return self.Health

    def whenHit(self):
        self.Health -= 1 

        if self.Health == 0:
            if self.Callback == None:
                pass  
            self.Callback()

