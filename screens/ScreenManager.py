import sys
# from screens.ScreensEnum import ScreensEnum
from Singleton import SingletonMeta 
from screens.StartScreen import StartScreen
from screens.GameScreen import GameScreen
from screens.PauseScreen import PauseScreen
from screens.GameOverScreen import GameOverScreen

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