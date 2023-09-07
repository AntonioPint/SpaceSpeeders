import sys
# from Screens.ScreensEnum import ScreensEnum
from Utils.Singleton import SingletonMeta 
from Screens.StartScreen import StartScreen
from Screens.GameScreen import GameScreen
from Screens.PauseScreen import PauseScreen
from Screens.GameOverScreen import GameOverScreen

class ScreenManager(metaclass=SingletonMeta):
    #Inicial Screen
    screen = StartScreen

    def getScreen(self): 
        return self.screen
    
    def changeToStartScreen(self):
        self.screen = StartScreen
        return self.getScreen()

    def changeToGameScreen(self):
        self.screen = GameScreen
        return self.getScreen()

    def changeToPauseScreen(self):
        self.screen = PauseScreen
        return self.getScreen()
        
    def changeToGameOverScreen(self):
        self.screen = GameOverScreen
        return self.getScreen()

    def exitApp(self):
        print("Exiting...")
        sys.exit()
        #pygame.quit()