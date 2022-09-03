from functools import partial
from GameObject import GameObject
from OptionsReader import OptionsReader
from Character import Character
from screens.Screen import Screen
import Shot
import screens.ScreenManager
import pygame


class GameScreen(Screen):

    WallpaperImage = pygame.image.load("assets/wallpaper.png")
    ChrossHairImage = pygame.image.load("assets/crosshair.png")

    Character = Character(
        (int(OptionsReader().getValue("WindowWidth"))/2,
         int(OptionsReader().getValue("WindowHeight"))/2)
    )

    ChrossHairSize = (50, 50)

    ChrossHair = pygame.transform.scale(
        pygame.image.load("assets/crosshair.png"), ChrossHairSize)

    LastMousePosition = (0, 0)

    def __init__(self, display):
        super().__init__(display)
        # CrossHair
        pygame.mouse.set_visible(False)

    def execute(self, input):
        # Mouse Input
        mousePosition = input["mousePos"]
        
        self.defineHoldActions()
        self.definePressedActions()
        self.defineReleasedActions()
        self.executeInputs(input)

        # Walpaper
        Wallpaper = pygame.transform.scale(
            self.WallpaperImage, self.WindowDimensions)
        self.display.blit(Wallpaper, (0, 0))

        if mousePosition != ():
            self.LastMousePosition = mousePosition

        # Draw character
        self.Character.move()  # First move character

        self.display.blit(
            self.Character.getObjectPointingToPosition(
                self.LastMousePosition),
            self.Character.center
        )

        # Draw Cursor
        self.display.blit(
            self.ChrossHair, self.crossHairPositionOffset(self.LastMousePosition))

        # Draw Shots
        nextShots = []
        for shot in self.Character.Shots:
            shot.move()
            self.display.blit(shot.getImage(), shot.getPosition())
            if(not shot.isOffScreen()):
                nextShots.append(shot)

        self.Character.Shots = nextShots

    def crossHairPositionOffset(self, pos):
        return (pos[0]-self.ChrossHairSize[0]/2, pos[1]-self.ChrossHairSize[1]/2)

    def exitGame(self):
        return screens.ScreenManager.ScreenManager().changeToPauseScreen()

    def getLastMousePosition(self):
        return self.LastMousePosition

    holdActions = {}
    pressedActions = {}
    releasedActions = {}

    def defineHoldActions(self):
        self.holdActions = {
            pygame.K_UP: (self.Character.moveUp, [], {}), pygame.K_w: (self.Character.moveUp, [], {}),
            pygame.K_DOWN: (self.Character.moveDown, [], {}), pygame.K_s: (self.Character.moveDown, [], {}),
            pygame.K_LEFT: (self.Character.moveLeft, [], {}), pygame.K_a: (self.Character.moveLeft, [], {}),
            pygame.K_RIGHT: (self.Character.moveRight, [], {}), pygame.K_d: (self.Character.moveRight, [], {}),
            pygame.K_SPACE: (self.Character.fire, [self.LastMousePosition], {}),
            pygame.MOUSEBUTTONDOWN: (self.Character.fire, [self.LastMousePosition], {}),
        }

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE: (self.exitGame, [], {}),
            # pygame.K_SPACE: (self.Character.fire, [self.LastMousePosition], {}),
            # pygame.MOUSEBUTTONDOWN: (self.Character.fire, [self.LastMousePosition], {}),
        }

    def defineReleasedActions(self):
        self.releasedActions = {}
