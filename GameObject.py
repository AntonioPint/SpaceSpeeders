from pygame import Vector2
from OptionsReader import OptionsReader

class GameObject(object):

    def __init__(self,width,height,position):
        self.position = position
        self.height = height
        self.width = width

    def isOutOfBounds(self):
        isOutOfBoundsX = (self.position - Vector2(self.width/2, 0)).x < 0  or (self.position + Vector2(self.width/2,0)).x > int(OptionsReader().getValue("WindowWidth"))
        isOutOfBoundsY = (self.position - Vector2(0, self.height/2)).y < 0  or (self.position + Vector2(0, self.height/2)).y > int(OptionsReader().getValue("WindowHeight"))
        return isOutOfBoundsX or isOutOfBoundsY

    def move(self,func):
        previousPosition = self.position
        func()
        if(self.isOutOfBounds()):
            self.position = previousPosition

    def getCharacterPos(self):
        return self.position - Vector2(self.width/2,self.height/2)

    def colisions(self, gameObjectToVeryfy):
        pass
        #return [gameObjectToVeryfy]
