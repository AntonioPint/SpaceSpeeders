import math
from random import randrange

import pygame
from GameObject.Character import Character
from GameObject.CrossHair import CrossHair
from GameObject.Enemy.Enemy import Enemy
from GameObject.Enemy.EnemyBiggerAsteroid import EnemyBiggerAsteroid
from GameObject.Enemy.EnemyHealth import EnemyHealth
from GameObject.Enemy.EnemyMachineGun import EnemyMachineGun
from GameObject.PowerUp import PowerUp, PowerUpEnum

import screens.ScreenManager
from screens.Screen import Screen


class GameScreen(Screen):
    # Wallpaper
    WallpaperImage = pygame.image.load("assets/wallpaper.png")

    # Points
    Points = 0

    # Heart
    Heart = pygame.transform.scale(
        pygame.image.load("assets/heart.png"), (50, 50))

    # Crosshair
    CrossHair = CrossHair()

    LastMousePosition = (0, 0)
    Enemies = []

    def __init__(self, display):
        super().__init__(display)

        self.Wallpaper = pygame.transform.scale(
            self.WallpaperImage, self.WindowDimensions)

        self.Character = Character(
            tuple(ti/2 for ti in super().WindowDimensions)
        )

        # CrossHair
        pygame.mouse.set_visible(False)

    def execute(self, input):
        # Mouse Input
        mousePosition = super().getMousePosition()

        self.executeInputs(input)

        # Walpaper
        self.display.blit(self.Wallpaper, (0, 0))

        if mousePosition != () and mousePosition != self.LastMousePosition:
            self.defineHoldActions()
            self.definePressedActions()
            self.defineReleasedActions()

            self.LastMousePosition = mousePosition

        # Draw Shots
        nextShots = []
        for shot in self.Character.Shots:
            shot.move()
            if(not shot.isOffScreen()):
                nextShots.append(shot)
                self.display.blit(shot.getImage(), shot.getPosition())

        # Draw character
        if self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU) != None:
            self.activateMachineGun()

        self.Character.move()  # First move character

        self.display.blit(
            self.Character.getObjectPointingToPosition(
                self.LastMousePosition),
            self.Character.center
        )

        # Draw Enemies
        nextEnemies = []
        if self.Enemies.__len__() < self.getAmountOfEnemies():
            r = randrange(0, 100)
            NewEnemie: Enemy = Enemy(self.generateCornerPosition(
                Enemy.EnemyWidth, Enemy.EnemyHeight), 2)
            if range(0, 5).__contains__(r):
                if self.Character.getHealth() < 10:
                    NewEnemie = EnemyHealth(self.generateCornerPosition(
                        Enemy.EnemyWidth, Enemy.EnemyHeight))
                    NewEnemie.setCallback(self.Character.incrementHealth)
            if range(5, 8).__contains__(r):
                # Eliminate the possibility of spawning more machinegun asteroids whit activated power
                if self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU) == None:
                    NewEnemie = EnemyMachineGun(self.generateCornerPosition(
                        Enemy.EnemyWidth, Enemy.EnemyHeight))
                    NewEnemie.setCallback(self.activateMachineGun)
            if range(8, 10).__contains__(r):
                NewEnemie = EnemyBiggerAsteroid((self.generateCornerPosition(
                        EnemyBiggerAsteroid.EnemyWidth, EnemyBiggerAsteroid.EnemyHeight)))    
                #NewEnemie.setCallback()

            self.Enemies.append(NewEnemie)

        for enemy in self.Enemies:
            enemy.move()

            if enemy.isOffScreen():
                return

            self.display.blit(enemy.getImage(), enemy.getPosition())

            # Verify Collisions
            # Verify Asteroids -> Character
            if enemy.isCollidingObject(self.Character):
                self.Character.takeDamage()
                if self.Character.getHealth() <= 0:
                    self.gameOver()

                #print(f'Systems Critical! ({self.Character.getHealth()}/5)')
                continue

            # Verify Shots -> Asteroids
            for shot in nextShots:
                if shot.isCollidingObject(enemy):
                    
                    # print("HIT!")
                    nextShots.remove(shot)
                    enemy.whenHit()
                    if enemy.getHealth() > 0:
                        nextEnemies.append(enemy)
                    else:
                        if self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU) == None:
                            self.Points += 100
                    break
            else:
                nextEnemies.append(enemy)

        self.Character.Shots = nextShots
        self.Enemies = nextEnemies

        # Draw Character Heart
        for i in range(self.Character.getHealth()):
            self.display.blit(self.Heart, (i * 50, 0))

        # Draw Points
        font = pygame.font.SysFont(None, 50)
        img = font.render(f'Points: {self.Points}', True, (255, 255, 255))
        self.display.blit(img, (0, 50))

        # Draw Cursor
        self.CrossHair.moveChrossHair(self.LastMousePosition)
        self.display.blit(
            self.CrossHair.getImage(), self.CrossHair.getPosition())

    def crossHairPositionOffset(self, pos):
        return (pos[0]-self.crosshairSize[0]/2, pos[1]-self.crosshairSize[1]/2)

    def generateCornerPosition(self, width, height):
        # corner top=0,left=1,right=2,bottom=3
        x = 0
        y = 0

        match randrange(0, 4):
            case 0:
                x = randrange(0, self.WindowDimensions[0]-width)
                y = 0
            case 1:
                x = 0
                y = randrange(0, self.WindowDimensions[1]-height)
            case 2:
                x = self.WindowDimensions[0]-width
                y = randrange(0, self.WindowDimensions[1]-height)
            case 3:
                x = randrange(0, self.WindowDimensions[0]-width)
                y = self.WindowDimensions[1]-height

        return (x, y)

    def getLevel(self):
        return int(self.Points/1000) or 1

    def getAmountOfEnemies(self):
        return int(5.4*math.log(self.getLevel()+1, 10))

    def activateMachineGun(self):
        if not self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU) != None:
            self.Character.addPowerUp(
                PowerUp(PowerUpEnum.MACHINEGUN_PWU, 5 + self.InternalSeconds))

        if self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU).time <= self.InternalSeconds:
            self.deactivateMachineGun()

        self.holdActions[pygame.K_SPACE] = (
            self.fire, [self.LastMousePosition], {})
        self.holdActions[pygame.MOUSEBUTTONDOWN] = (
            self.fire, [self.LastMousePosition], {})

    def deactivateMachineGun(self):
        machineGunPowerUp = self.Character.getPowerUp(
            PowerUpEnum.MACHINEGUN_PWU)
        if machineGunPowerUp != None:
            self.Character.removePowerUp(machineGunPowerUp)

    def getMousePosition(self):
        return self.LastMousePosition

    def exitGame(self):
        pygame.mouse.set_visible(True)
        return screens.ScreenManager.ScreenManager().changeToPauseScreen()

    def gameOver(self):
        pygame.mouse.set_visible(True)
        return screens.ScreenManager.ScreenManager().changeToGameOverScreen()

    def fire(self, mousePos):
        # TODO: se character tem powerup então não perde pontos
        if self.Character.getPowerUp(PowerUpEnum.MACHINEGUN_PWU) == None and self.Points > 0:
            self.Points -= 10
        self.Character.fire(mousePos)

    holdActions = {}
    pressedActions = {}
    releasedActions = {}

    def defineHoldActions(self):
        self.holdActions = {
            pygame.K_UP: (self.Character.moveUp, [], {}), pygame.K_w: (self.Character.moveUp, [], {}),
            pygame.K_DOWN: (self.Character.moveDown, [], {}), pygame.K_s: (self.Character.moveDown, [], {}),
            pygame.K_LEFT: (self.Character.moveLeft, [], {}), pygame.K_a: (self.Character.moveLeft, [], {}),
            pygame.K_RIGHT: (self.Character.moveRight, [], {}), pygame.K_d: (self.Character.moveRight, [], {}),
            pygame.K_SPACE: (lambda: None, [], {}),
            pygame.MOUSEBUTTONDOWN: (lambda: None, [], {}),
        }

    def definePressedActions(self):
        self.pressedActions = {
            pygame.K_ESCAPE: (self.exitGame, [], {}),
            pygame.K_SPACE: (self.fire, [self.getMousePosition()], {}),
            pygame.MOUSEBUTTONDOWN: (self.fire, [self.getMousePosition()], {})
        }

    def defineReleasedActions(self):
        self.releasedActions = {}
