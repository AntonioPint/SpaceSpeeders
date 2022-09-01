import sys
from Button import Button
from OptionsReader import OptionsReader
from screens.GameScreen import GameScreen
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class PauseScreen(Screen):
    display = None
    mousePosition = (0,0)

    def __init__(self, display):
        super().__init__(display)
        self.resumeButton = Button("EXIT", (self.WindowDimensions[0]/2,self.WindowDimensions[1]*2/3),30,"black","red", screens.ScreenManager.ScreenManager().exitApp)

    def execute(self, input):
        # Mouse Input
        self.mousePosition = input["mousePos"]

        self.executeInputs(self, input)

        # Background      
        self.display.fill((0, 0, 0))
        
        # Buttons
        pygame.mouse.set_visible(True)
        
        self.display.blit(self.resumeButton.surface,(self.resumeButton.x, self.resumeButton.y))
        return None


    def backToGame(self):
        screens.ScreenManager.ScreenManager().changeToGameScreen()

    def checkMouseClick(self):
        if(self.resumeButton.isColliding(self.mousePosition)):
            screens.ScreenManager.ScreenManager().exitApp()


    myPressedActions = {
        pygame.K_ESCAPE : backToGame,
        pygame.MOUSEBUTTONDOWN : checkMouseClick
    }