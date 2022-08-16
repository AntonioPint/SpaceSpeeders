from Button import Button
from screens.GameScreen import GameScreen
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class ExitScreen(Screen):
    display = None

    def __init__(self, display):
        super().__init__(display)
        

    def execute(self, input):
        # Mouse Input
        mousePosition = input["mousePos"]

        # Execute Keyboard Inputs
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
        # Background      
        self.display.fill((0, 0, 0))
        
        # Buttons
        pygame.mouse.set_visible(True)
        resumeButton = Button("RESUME", (250,250),30,"white",screens.ScreenManager.ScreenManager().exitApp)
        self.display.blit(resumeButton.surface,(resumeButton.x, resumeButton.y))
        return None

    def backToGame():
        screens.ScreenManager.ScreenManager().changeToGameScreen()
        return screens.ScreenManager.ScreenManager().getScreen()

    myHoldActions = {
    }    

    myPressedActions = {
        pygame.K_ESCAPE : backToGame
    }