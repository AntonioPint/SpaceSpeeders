import math
from enum import Enum
from turtle import Vec2D
import pygame
from OptionsReader import OptionsReader


class GameObject(object):
    def __init__(
        self,
        width,
        height,
        position,
        acceleration=1,
        image=pygame.image.load("assets/test.png")
    ):
        self.width = width
        self.height = height
        self.position = position
        self.acceleration = acceleration
        self.image = image
        self.center = image.get_rect(center=position)
        self.movement = pygame.Vector2(0, 0)

        # Additional image properties TODO:
        # self.additional_image = None
        # self.additional_image_corner = "top-left" 


    def isOutOfBounds(self):
        isOutOfBoundsX = self.position.x < 0 or (
            self.position + pygame.Vector2(self.width, 0)).x > int(OptionsReader().getValue("WindowWidth"))
        isOutOfBoundsY = self.position.y < 0 or (self.position + pygame.Vector2(
            0, self.height)).y > int(OptionsReader().getValue("WindowHeight"))

        return isOutOfBoundsX or isOutOfBoundsY

    def isOffScreen(self):
        isOutScreenX = (self.position + pygame.Vector2(self.width, 0)
                        ).x < 0 or self.position.x > int(OptionsReader().getValue("WindowWidth"))
        isOutScreenY = (self.position + pygame.Vector2(0, self.height)
                        ).y < 0 or self.position.y > int(OptionsReader().getValue("WindowHeight"))
        return isOutScreenX or isOutScreenY

    def move(self):
        if self.movement == pygame.Vector2(0, 0):
            return
        self.position += self.movement.normalize() * self.acceleration

    def getCenter(self):
        return self.position + pygame.Vector2(self.width/2, self.height / 2)

    def getPosition(self):
        return self.position

    def getHitBox(self):
        return self.getImage().get_rect(x=self.position[0], y=self.position[1])

    def isCollidingPoint(self, pos):
        return self.getHitBox().collidepoint(pos)

    def isCollidingObject(self, object):
        return self.getHitBox().colliderect(object.getHitBox())

    def getImage(self):
        return pygame.transform.scale(
            self.image, (self.width, self.height))
    
    def setImage(self, image: pygame.Surface):
        self.image = image

    def getObjectPointingToPosition(self, targetPosition):
        (x, y) = self.getCenter()
        (targetX, targetY) = targetPosition

        angle = -math.atan2(targetY-y, targetX-x)*180/math.pi
        result = pygame.transform.rotate(self.getImage(), angle)
        self.center = result.get_rect(center=(x, y))

        return result
    
    # TODO:    
    # def addAdditionalImage(self, image: pygame.Surface, position="top-left"):

    #     self.additional_image = image
    #     self.additional_image_position = position
    # TODO:
    # def getCombinedImage(self):
        combined_image = self.getImage().copy()

        if self.additional_image:
            if self.additional_image_position == "top-left":
                x = 0
                y = 0
            elif self.additional_image_position == "top-right":
                x = self.width - self.additional_image.get_width()
                y = 0
            elif self.additional_image_position == "bottom-left":
                x = 0
                y = self.height - self.additional_image.get_height()
            elif self.additional_image_position == "bottom-right":
                x = self.width - self.additional_image.get_width()
                y = self.height - self.additional_image.get_height()
            elif self.additional_image_position == "top-center":
                x = (self.width - self.additional_image.get_width()) // 2
                y = 0
            elif self.additional_image_position == "left-center":
                x = 0
                y = (self.height - self.additional_image.get_height()) // 2
            elif self.additional_image_position == "right-center":
                x = self.width - self.additional_image.get_width()
                y = (self.height - self.additional_image.get_height()) // 2
            elif self.additional_image_position == "bottom-center":
                x = (self.width - self.additional_image.get_width()) // 2
                y = self.height - self.additional_image.get_height()
            elif self.additional_image_position == "center":
                x = (self.width - self.additional_image.get_width()) // 2
                y = (self.height - self.additional_image.get_height()) // 2

            print(self.additional_image)
            combined_image.blit(self.additional_image(), (x, y))

        return combined_image