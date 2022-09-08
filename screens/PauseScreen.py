import sys

import pygame
from GameObject.Button import Button
from OptionsReader import OptionsReader

import screens.ScreenManager
from screens.GameScreen import GameScreen
from screens.Screen import Screen


class PauseScreen(Screen):
    display = None
    mousePosition = (0,0)

    def __init__(self, display):
        super().__init__(display)
        self.resumeButton = Button("EXIT", (self.WindowDimensions[0]/2,self.WindowDimensions[1]*2/3),30,"black","red", screens.ScreenManager.ScreenManager().exitApp)

    def execute(self, input):
        # Mouse Input
        self.mousePosition = input["mousePos"]

        self.definePressedActions()
        self.executeInputs(input)
        
        # Background      
        self.display.fill((0, 0, 0))
        
        self.display.blit(self.resumeButton.surface,(self.resumeButton.x, self.resumeButton.y))


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
