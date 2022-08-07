from OptionsReader import OptionsReader
from Character import Character
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class GameScreen(Screen):
    display = None
    
    myCharacter = Character(
        int(OptionsReader().getValue("WindowHeight"))/2,
        int(OptionsReader().getValue("WindowWidth"))/2
        )

    def __init__(self, display):
        super().__init__(display)

    def execute(self, input):
        for i in input["hold"]:
            if self.myHoldActions.get(i) is not None:
                a = self.myHoldActions.get(i)()
                if a is not None:
                    return a

        for i in input["pressed"]:
            if self.myPressedActions.get(i) is not None:
                a = self.myPressedActions.get(i)()
                if a is not None:
                    return a   
        
        self.display.fill((255,255,255))
        # Draw a sun
        pygame.draw.circle(self.display, (255,140,0), (250, 250), 75)
        pygame.draw.circle(self.display, (255,255,0), (250, 250), 65)
        # Draw character
        self.display.blit(self.myCharacter.getCharacterImage(),self.myCharacter.getCharacterPos())
        return None

    def exitGame():
        screens.ScreenManager.ScreenManager().changeToExitScreen()
        return screens.ScreenManager.ScreenManager().screen

    myHoldActions = {
        pygame.K_UP : myCharacter.moveUp, pygame.K_w : myCharacter.moveUp,
        pygame.K_DOWN : myCharacter.moveDown, pygame.K_s : myCharacter.moveDown,
        pygame.K_LEFT : myCharacter.moveLeft, pygame.K_a : myCharacter.moveLeft,
        pygame.K_RIGHT : myCharacter.moveRight, pygame.K_d : myCharacter.moveRight,
        pygame.K_SPACE : myCharacter.fire, 
    }    

    myPressedActions = {
        pygame.K_ESCAPE : exitGame
    }