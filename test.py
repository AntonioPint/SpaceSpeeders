from screens.ScreenManager import ScreenManager

a = ScreenManager()
b = ScreenManager()

a.screen = 2

a.changeToExitScreen()
print(b.screen)