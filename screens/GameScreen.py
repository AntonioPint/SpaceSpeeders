from OptionsReader import OptionsReader
from Character import Character
from screens.Screen import Screen
import screens.ScreenManager
import pygame


class GameScreen(Screen):

    WallpaperImage = pygame.image.load("assets/wallpaper.png")
    ChrossHairImage = pygame.image.load("assets/crosshair.png")

    myCharacter = Character(
        (int(OptionsReader().getValue("WindowWidth"))/2,
         int(OptionsReader().getValue("WindowHeight"))/2)
    )
    
    ChrossHair = pygame.transform.scale(
        pygame.image.load("assets/crosshair.png"),
        (int(OptionsReader().getValue("CrossHairSize")), int(OptionsReader().getValue("CrossHairSize"))))

    lastMousePosition = (0,0)

    def __init__(self, display):
        super().__init__(display)

        # CrossHair
        pygame.mouse.set_visible(False)

    def execute(self, input):
        # Mouse Input
        mousePosition = input["mousePos"]

        self.executeInputs(input)

        # Walpaper
        Wallpaper = pygame.transform.scale(self.WallpaperImage, self.WindowDimensions)
        self.display.blit(Wallpaper, (0, 0))

        if mousePosition != ():
            self.lastMousePosition = mousePosition

        # Draw character
        self.myCharacter.move() # First move character
        
        self.display.blit(
            self.myCharacter.getObjectPointingToPosition(self.lastMousePosition),
            self.myCharacter.center
        ) 

        # Draw Cursor
        self.display.blit(self.ChrossHair, self.crossHairPositionOffset(self.lastMousePosition))


    def crossHairPositionOffset(self, pos):
        return (pos[0]-int(OptionsReader().getValue("CrossHairSize"))/2, pos[1]-int(OptionsReader().getValue("CrossHairSize"))/2)

    def exitGame():
        return screens.ScreenManager.ScreenManager().changeToPauseScreen()

    myHoldActions = {
        pygame.K_UP: myCharacter.moveUp, pygame.K_w: myCharacter.moveUp,
        pygame.K_DOWN: myCharacter.moveDown, pygame.K_s: myCharacter.moveDown,
        pygame.K_LEFT: myCharacter.moveLeft, pygame.K_a: myCharacter.moveLeft,
        pygame.K_RIGHT: myCharacter.moveRight, pygame.K_d: myCharacter.moveRight,
    }

    myPressedActions = {
        pygame.K_ESCAPE: exitGame,
        pygame.K_SPACE: myCharacter.fire, pygame.MOUSEBUTTONDOWN: myCharacter.fire,
    }

    myReleasedActions = {

    }
