from OptionsReader import OptionsReader
import pygame
import screens.ScreenManager
from screens.Screen import Screen

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
        screens.ScreenManager.ScreenManager().changeToGameScreen()

    def checkMouseClick(self):
        if(self.resumeButton.isCollidingPoint(self.mousePosition)):
            screens.ScreenManager.ScreenManager().exitApp()

    pressedActions = {}

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE : (self.backToGame,[],{}),
            pygame.MOUSEBUTTONDOWN : (self.checkMouseClick,[],{})
        }
