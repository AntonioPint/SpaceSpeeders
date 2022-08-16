from pygame import Vector2
from OptionsReader import OptionsReader

class GameObject(object):

    def __init__(self,width,height,position):
        self.width = width
        self.height = height
        self.position = position

    def isOutOfBounds(self):
        isOutOfBoundsX = (self.position - Vector2(self.width/2, 0)).x < 0  or (self.position + Vector2(self.width/2,0)).x > int(OptionsReader().getValue("WindowWidth"))
        isOutOfBoundsY = (self.position - Vector2(0, self.height/2)).y < 0  or (self.position + Vector2(0, self.height/2)).y > int(OptionsReader().getValue("WindowHeight"))
        return isOutOfBoundsX or isOutOfBoundsY

    def isOffScreen(self):
        isOutScreenX = (self.position + Vector2(self.width, 0)).x < 0  or self.position.x > int(OptionsReader().getValue("WindowWidth"))
        isOutScreenY = (self.position + Vector2(0, self.height)).y < 0  or self.position.y > int(OptionsReader().getValue("WindowHeight"))
        if isOutScreenX : print("x",self.position)
        if isOutScreenY : print("y",self.position)
        return isOutScreenX or isOutScreenY

    def move(self,func):
        previousPosition = self.position
        func()
        if(self.isOffScreen()):
            print("OUT!!")
            self.position = previousPosition

    def getCenterPosition(self):
        return self.position - Vector2(self.width/2,self.height/2)

    def getPosition(self):
            return self.position

    def isColiding(self, gameObjectToVeryfy):
        pass
        #return [gameObjectToVeryfy]
