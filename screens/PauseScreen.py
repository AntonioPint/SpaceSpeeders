import sys
from Button import Button
from OptionsReader import OptionsReader
from screens.GameScreen import GameScreen
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class PauseScreen(Screen):
    display = None

    def __init__(self, display):
        super().__init__(display)
        self.resumeButton = Button("RESUME", (self.WindowDimensions[0]/2,self.WindowDimensions[1]*2/3),30,"black","red", screens.ScreenManager.ScreenManager().exitApp)
        self.buttons = [self.resumeButton]

    def execute(self, input):
        # Mouse Input
        mousePosition = input["mousePos"]

        self.executeInputs(input)

        # Background      
        self.display.fill((0, 0, 0))
        
        # Buttons
        pygame.mouse.set_visible(True)
        
        self.display.blit(self.resumeButton.surface,(self.resumeButton.x, self.resumeButton.y))
        return None


    def backToGame():
        return screens.ScreenManager.ScreenManager().changeToGameScreen()

    def checkButtonClicked(self):
        print("I clicked")

        pass

    myPressedActions = {
        pygame.K_ESCAPE : backToGame,
        pygame.MOUSEBUTTONDOWN : checkButtonClicked
    }