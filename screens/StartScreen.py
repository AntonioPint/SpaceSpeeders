from OptionsReader import OptionsReader
from Screens.Screen import Screen
import Screens.ScreenManager
import pygame


class StartScreen(Screen):
    display = None
    backgrounfGif = []
    activeBackgroundIndex = 0
    frame = 0
    targetFrame = 0
    
    def __init__(self, display):
        super().__init__(display)

        self.logo = pygame.image.load("assets/logo.png")
        self.startInstructions = pygame.image.load("assets/start.png")
        self.targetFrame = int(OptionsReader().getValue("TargetFPS"))
        for i in range(0, 6):
            self.backgrounfGif.append(
                pygame.image.load(f"assets/intro/{i}.png"))

    def execute(self, input):
        self.definePressedActions()
        self.executeInputs(input)

        # Draw GIF
        self.display.blit(pygame.transform.scale(
            self.backgrounfGif[self.activeBackgroundIndex], self.WindowDimensions), (0, 0))

        if self.frame >= self.targetFrame/6:
            self.frame = 0
            self.activeBackgroundIndex += 1
            if self.activeBackgroundIndex >= 6:
                self.activeBackgroundIndex = 0
        else:
            self.frame += 1

        # Draw Application Logo
        self.display.blit(pygame.transform.scale(
            self.logo, (self.WindowDimensions[0]*2/3, self.WindowDimensions[0]*0.07)), ((self.WindowDimensions[0] - self.WindowDimensions[0]*2/3)/2, self.WindowDimensions[1]*0.15))

        # Draw Start Instructions
        self.display.blit(pygame.transform.scale(
            self.startInstructions, (self.WindowDimensions[0]*2/3, self.WindowDimensions[1]*0.06)), ((self.WindowDimensions[0] - self.WindowDimensions[0]*2/3)/2, self.WindowDimensions[1]*0.77))

    def startGame(self):
        return Screens.ScreenManager.ScreenManager().changeToGameScreen()

    pressedActions = {}

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_SPACE: (self.startGame, [], {}),
        }
