from OptionsReader import OptionsReader
from screens.Screen import Screen
import screens.ScreenManager
import pygame

class StartScreen(Screen):
    display = None
    backgrounfGif = []
    activeBackgroundIndex=0
    frame = 0

    def __init__(self, display):
        super().__init__(display)

        self.logo = pygame.image.load("assets/logo.png")
        self.startInstructions = pygame.image.load("assets/start.png")

        for i in range(0,6):
            self.backgrounfGif.append(pygame.image.load(f"assets/intro/{i}.png"))


    def execute(self, input):
        
        self.executeInputs(input)

        # Draw GIF
        self.display.blit(pygame.transform.scale(self.backgrounfGif[self.activeBackgroundIndex],self.WindowDimensions),(0,0))

        if self.frame >= int(OptionsReader().getValue("TargetFPS"))/6:
            self.frame = 0
            self.activeBackgroundIndex += 1
            if self.activeBackgroundIndex >= 6:
                self.activeBackgroundIndex = 0
        else:
            self.frame += 1

        # Draw Application Logo
        self.display.blit(pygame.transform.scale(self.logo, (720,70)), (180, 100))

        # Draw Start Instructions
        self.display.blit(pygame.transform.scale(self.startInstructions,(720,40)), (180,550))

    def startGame():
        return screens.ScreenManager.ScreenManager().changeToGameScreen()

    myPressedActions = {
        pygame.K_SPACE : startGame,
    }