from screens.GameScreen import GameScreen
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class ExitScreen(Screen):
    display = None

    def __init__(self, display):
        super().__init__(display)

    def execute(self, input):
        for i in input["hold"]:
            if self.myHoldActions.get(i) is not None:
                a = self.myHoldActions[i]()
                if a is not None:
                    return a

        for i in input["pressed"]:
            if self.myPressedActions.get(i) is not None:
                a = self.myPressedActions[i]()
                if a is not None:
                    return a   

        self.display.fill((1,1,1))
        return None

    def backToGame():
        screens.ScreenManager.ScreenManager().changeToGameScreen()
        return screens.ScreenManager.ScreenManager().screen

    myHoldActions = {
    }    

    myPressedActions = {
        pygame.K_ESCAPE : backToGame
    }