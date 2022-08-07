from screens.ScreensEnum import ScreensEnum
from Singleton import SingletonMeta 

class ScreenManager(metaclass=SingletonMeta):
    screen = ScreensEnum.GameScreen.value

    def changeToStartScreen(self):
        self.screen = ScreensEnum.StartScreen.value
        return self.screen

    def changeToGameScreen(self):
        self.screen = ScreensEnum.GameScreen.value
        return self.screen

    def changeToExitScreen(self):
        self.screen = ScreensEnum.ExitScreen.value
        return self.screen
