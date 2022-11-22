import sys

import pygame
from GameObject.Button import Button
from OptionsReader import OptionsReader

import Screens.ScreenManager
from Screens.GameScreen import GameScreen
from Screens.Screen import Screen


class PauseScreen(Screen):
    display = None
    mousePosition = (0,0)

    def __init__(self, display):
        super().__init__(display)
        self.resumeButton = Button("EXIT", (self.WindowDimensions[0]/2,self.WindowDimensions[1]*2/3),30,"black","red", Screens.ScreenManager.ScreenManager().exitApp)

    def execute(self, input):
        # Mouse Input
        self.mousePosition = input["mousePos"]

        self.definePressedActions()
        self.executeInputs(input)
        
        # Background      
        self.display.fill((0, 0, 0))
        
        self.display.blit(self.resumeButton.surface,(self.resumeButton.x, self.resumeButton.y))


    def backToGame(self):
        Screens.ScreenManager.ScreenManager().changeToGameScreen()

    def checkMouseClick(self):
        if(self.resumeButton.isCollidingPoint(self.mousePosition)):
            Screens.ScreenManager.ScreenManager().exitApp()

    pressedActions = {}

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE : (self.backToGame,[],{}),
            pygame.MOUSEBUTTONDOWN : (self.checkMouseClick,[],{})
        }
