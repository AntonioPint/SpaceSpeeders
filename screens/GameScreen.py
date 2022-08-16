from OptionsReader import OptionsReader
from Character import Character
from screens.Screen import Screen
import screens.ScreenManager
import pygame


class GameScreen(Screen):
    # lastMousePosition = (int(OptionsReader().getValue("CrossHairSize")), int(
    #     OptionsReader().getValue("CrossHairSize")))
    lastMousePosition = (0, 0)
    WallpaperDimensions = (int(OptionsReader().getValue("WindowWidth")),
                           int(OptionsReader().getValue("WindowHeight")))

    myCharacter = Character(
        (int(OptionsReader().getValue("WindowWidth"))/2,
         int(OptionsReader().getValue("WindowHeight"))/2)
    )

    ChrossHair = pygame.transform.scale(
        pygame.image.load("assets/crosshair.png"),
        (int(OptionsReader().getValue("CrossHairSize")), int(OptionsReader().getValue("CrossHairSize"))))

    def __init__(self, display):
        super().__init__(display)

    def execute(self, input):
        # Mouse Input
        mousePosition = input["mousePos"]

        # Execute Keyboard Inputs
        for i in input["pressed"]:
            if self.myPressedActions.get(i) is not None:
                a = self.myPressedActions.get(i)(i)
                if a is not None:
                    return a

        for f in input["hold"]:
            if self.myHoldActions.get(f) is not None:
                a = self.myHoldActions.get(f)(f)
                if a is not None:
                    return a

        for g in input["released"]:
            if self.myReleasedActions.get(g) is not None:
                a = self.myReleasedActions.get(g)(g)
                if a is not None:
                    return a

        # Walpaper
        Wallpaper = pygame.transform.scale(pygame.image.load(
            "assets/wallpaper1.png"), self.WallpaperDimensions)
        self.display.blit(Wallpaper, (0, 0))

        # CrossHair
        pygame.mouse.set_visible(False)

        if mousePosition != ():
            self.lastMousePosition = self.crossHairPositionOffset(
                mousePosition)

        # Point Character to cursor
        # self.myCharacter.pointToPosition(self.lastMousePosition)

        # Draw character
        print(self.myCharacter.getCenterPosition())
        self.display.blit(self.myCharacter.getCharacterPointingToPosition(self.lastMousePosition),
                          self.myCharacter.center
                          )

        # Draw Cursor
        self.display.blit(self.ChrossHair, self.lastMousePosition)

    def crossHairPositionOffset(self, pos):
        return (pos[0]-int(OptionsReader().getValue("CrossHairSize"))/2, pos[1]-int(OptionsReader().getValue("CrossHairSize"))/2)

    def exitGame(args):
        return screens.ScreenManager.ScreenManager().changeToExitScreen()

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
        pygame.K_LEFT: myCharacter.reset, pygame.K_RIGHT: myCharacter.reset,
        pygame.K_a: myCharacter.reset, pygame.K_d: myCharacter.reset
    }
