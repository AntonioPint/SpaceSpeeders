# imports
import pygame
from Character import Character
from Singleton import SingletonMeta
 # Necessary to not have circular imports

class Game(metaclass=SingletonMeta):
    #ScreenVariables
    _screenHeight = 720
    _screenWidth = 1080
    _backgroundColor = (255,255,255)

    #GlobalVariables
    myCharacter = Character(_screenWidth/2,_screenHeight/2)
    myCharacterActions = {
        pygame.K_UP : myCharacter.moveUp,
        pygame.K_DOWN : myCharacter.moveDown,
        pygame.K_LEFT : myCharacter.moveLeft,
        pygame.K_RIGHT : myCharacter.moveRight      
    }

    #PyGame
    pygame.init()
    pygame.key.set_repeat() #Be able to see hold down keys
    clock = pygame.time.Clock()
    display = pygame.display.set_mode([_screenWidth, _screenHeight])

    def __init__(self):
        pass

    def start(self):
        pygame.display.set_caption('SpaceSpeeders')
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pressed = pygame.key.get_pressed()

            for func in (self.myCharacterActions[key] for key in self.myCharacterActions if pressed[key]):
                func()
                
            self.display.fill(self._backgroundColor)
            # Draw a solid blue circle in the center
            pygame.draw.circle(self.display, (255,140,0), (250, 250), 75)
            pygame.draw.circle(self.display, (255,255,0), (250, 250), 65)
            self.display.blit(self.myCharacter.getCharacterImage(),self.myCharacter.getCharacterPos())
            
            pygame.display.flip()
            # self.clock.tick(30)

Game().start()