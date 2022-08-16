from screens.ScreensEnum import ScreensEnum
from Singleton import SingletonMeta 
import pygame 

class ScreenManager(metaclass=SingletonMeta):
    #Inicial Screen
    screen = ScreensEnum.GameScreen.value

    
    def getScreen(self): 
        return self.screen
    
    def changeToStartScreen(self):
        self.screen = ScreensEnum.StartScreen.value

    def changeToGameScreen(self):
        self.screen = ScreensEnum.GameScreen.value

    def changeToExitScreen(self):
        self.screen = ScreensEnum.ExitScreen.value

    def exitApp(self):
        print("Exiting...")
        pygame.quit()