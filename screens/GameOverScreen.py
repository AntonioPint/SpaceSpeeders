from OptionsReader import OptionsReader
import pygame
import Screens.ScreenManager
from Screens.Screen import Screen

class GameOverScreen(Screen):
    display = None
    mousePosition = (0,0)

    def __init__(self, display):
        super().__init__(display)
        

    def execute(self, input):
        # Mouse Input
        self.mousePosition = input["mousePos"]

        self.definePressedActions()
        self.executeInputs(input)
        
        # Background      
        self.display.fill((0, 0, 0))
        
        return None

    def backToGame(self):
        Screens.ScreenManager.ScreenManager().changeToGameScreen()

    def checkMouseClick(self):
        # if(self.resumeButton.isCollidingPoint(self.mousePosition)):
        #     Screens.ScreenManager.ScreenManager().exitApp()
        pass

    pressedActions = {}

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE : (self.backToGame,[],{}),
            pygame.MOUSEBUTTONDOWN : (self.checkMouseClick,[],{})
        }
