from screens.ScreensEnum import ScreensEnum
from Singleton import SingletonMeta 
import pygame 

class ScreenManager(metaclass=SingletonMeta):
    #Inicial Screen
    screen = ScreensEnum.StartScreen.value

    def getScreen(self): 
        return self.screen
    
    def changeToStartScreen(self):
        self.screen = ScreensEnum.StartScreen.value
        return self.getScreen()

    def changeToGameScreen(self):
        self.screen = ScreensEnum.GameScreen.value
        return self.getScreen()

    def changeToPauseScreen(self):
        self.screen = ScreensEnum.PauseScreen.value
        return self.getScreen()

    def exitApp(self):
        print("Exiting...")
        pygame.quit()