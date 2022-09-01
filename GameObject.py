import math
from enum import Enum
from pygame import Vector2, transform
from OptionsReader import OptionsReader

class GameObject(object):
    ACEL = 1
    objectType = None
    movement = Vector2(0,0)

    def __init__(self,width,height,position):
        self.width = width
        self.height = height
        self.position = position

    def isOutOfBounds(self):
        isOutOfBoundsX = (self.position - Vector2(self.width/2, 0)).x < 0  or (self.position + Vector2(self.width/2,0)).x > int(OptionsReader().getValue("WindowWidth"))
        isOutOfBoundsY = (self.position - Vector2(0, self.height/2)).y < 0  or (self.position + Vector2(0, self.height/2)).y > int(OptionsReader().getValue("WindowHeight"))
        return isOutOfBoundsX or isOutOfBoundsY

    def isOffScreen(self):
        isOutScreenX = (self.position + Vector2(self.width/2, 0)).x < 0  or (self.position - Vector2(self.width/2,0)).x > int(OptionsReader().getValue("WindowWidth"))
        isOutScreenY = (self.position + Vector2(0, self.height/2)).y < 0  or (self.position - Vector2(0, self.height/2)).y > int(OptionsReader().getValue("WindowHeight"))
        return isOutScreenX or isOutScreenY

    def move(self):
        if self.movement == Vector2(0,0) : return

        self.position += self.movement.normalize() * self.ACEL

        match self.objectType:
            case GameObjectTypes.CHARACTER:
                if(self.isOutOfBounds()):
                    self.position -= self.movement.normalize() * self.ACEL
                self.movement = Vector2(0,0)   
            case _:
                pass
        

    def getPosition(self):
        return self.position

    def areColliding(self, object1, object2):
        return False

    def collidingObjects(self, gameObjectToVerify):
        pass

    def getImage(self):
        pass

    def getObjectPointingToPosition(self, targetPosition):
        (x, y) = self.getPosition()
        (targetX, targetY) = targetPosition

        angle = -math.atan2(targetY-y,targetX-x)*180/math.pi 
        result = transform.rotate(self.getImage(), angle)
        self.center = result.get_rect(center=self.getPosition())

        return result   

class GameObjectTypes(Enum):
    CHARACTER="CHARACTER"
    ENEMY="ENEMY"
    SHOT="SHOT"