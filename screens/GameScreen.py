from functools import partial
from GameObject.CrossHair import CrossHair
from GameObject.Enemy import Enemy
from OptionsReader import OptionsReader
from GameObject.Character import Character
from screens.Screen import Screen
from GameObject.Shot import Shot
import screens.ScreenManager
import pygame


class GameScreen(Screen):
    # Wallpaper
    WallpaperImage = pygame.image.load("assets/wallpaper.png")    

    Character = Character(
        (int(OptionsReader().getValue("WindowWidth"))/2,
         int(OptionsReader().getValue("WindowHeight"))/2)
    )

    # Crosshair
    CrossHair = CrossHair()

    LastMousePosition = (0, 0)
    Enemies = [Enemy(pygame.Vector2(100,300))]

    def __init__(self, display):
        super().__init__(display)
        
        self.Wallpaper = pygame.transform.scale(
            self.WallpaperImage, self.WindowDimensions)

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
        self.display.blit(self.Wallpaper, (0, 0))

        if mousePosition != ():
            self.LastMousePosition = mousePosition

        # Draw Shots
        nextShots = []
        for shot in self.Character.Shots:
            shot.move()
            self.display.blit(shot.getImage(), shot.getPosition())
            if(not shot.isOffScreen()):
                nextShots.append(shot)

        self.Character.Shots = nextShots

        # Draw character
        self.Character.move()  # First move character

        self.display.blit(
            self.Character.getObjectPointingToPosition(
                self.LastMousePosition),
            self.Character.center
        )

        # Draw Enemies
        nextEnemies = []

        for enemy in self.Enemies:
            enemy.move()

            if enemy.isOffScreen(): 
                return

            self.display.blit(enemy.getImage(), enemy.getPosition())

            # Verify Collisions
            # Verify Asteroids -> Character
            if enemy.isCollidingObject(self.Character):
                self.Character.takeDamage()
                print(f'Systems Critical! ({self.Character.getHealth()}/3)')
                break
            # Verify Shots -> Asteroids
            for shot in self.Character.Shots:
                if shot.isCollidingObject(enemy):
                    print("HIT!")
                    break
                
            else:
                nextEnemies.append(enemy) 

        self.Enemies = nextEnemies

        # Draw Cursor
        self.CrossHair.moveChrossHair(self.LastMousePosition)
        self.display.blit(
            self.CrossHair.getImage(), self.CrossHair.getPosition())

    def crossHairPositionOffset(self, pos):
        return (pos[0]-self.crosshairSize[0]/2, pos[1]-self.crosshairSize[1]/2)

    def exitGame(self):
        return screens.ScreenManager.ScreenManager().changeToPauseScreen()

    holdActions = {}
    pressedActions = {}
    releasedActions = {}

    def defineHoldActions(self):
        self.holdActions = {
            pygame.K_UP: (self.Character.moveUp, [], {}), pygame.K_w: (self.Character.moveUp, [], {}),
            pygame.K_DOWN: (self.Character.moveDown, [], {}), pygame.K_s: (self.Character.moveDown, [], {}),
            pygame.K_LEFT: (self.Character.moveLeft, [], {}), pygame.K_a: (self.Character.moveLeft, [], {}),
            pygame.K_RIGHT: (self.Character.moveRight, [], {}), pygame.K_d: (self.Character.moveRight, [], {}),
        }

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE: (self.exitGame, [], {}),
            pygame.K_SPACE: (self.Character.fire, [self.LastMousePosition], {}),
            pygame.MOUSEBUTTONDOWN: (self.Character.fire, [self.LastMousePosition], {}),
        }

    def defineReleasedActions(self):
        self.releasedActions = {}
