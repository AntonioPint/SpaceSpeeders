# imports
from queue import Empty
import pygame
from OptionsReader import OptionsReader
from screens.ScreenManager import ScreenManager

class Game():
    #ScreenVariables
    _screenHeight = int(OptionsReader().getValue("WindowHeight"))
    _screenWidth = int(OptionsReader().getValue("WindowWidth"))
    _backgroundColor = (255,255,255)

    #GlobalVariables
    KeyHoldInputs=[
        pygame.K_UP, pygame.K_w,
        pygame.K_DOWN, pygame.K_s,
        pygame.K_LEFT, pygame.K_a,
        pygame.K_RIGHT, pygame.K_d,
        pygame.K_SPACE, pygame.K_ESCAPE
    ]

    KeyPressedInputs=[
        pygame.K_ESCAPE
    ]

    #PyGame
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode([_screenWidth, _screenHeight]) #, pygame.NOFRAME
    screen = ScreenManager.screen(display)

    def __init__(self):
        pass

    def start(self):
        pygame.display.set_caption('SpaceSpeeders')
        
        while True:
            keys = {"hold": [], "pressed": []}
            hold = pygame.key.get_pressed()
            pressed = pygame.event.get()

            #Gets Pressed Keys
            for event in pressed:
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    #print("Pressed " + pygame.key.name(event.key))
                    keys["pressed"].append(event.key)

            #Gets Holded Keys
            for key in self.KeyHoldInputs:
                if hold[key]:
                    #print("Holded " + pygame.key.name(key))
                    keys["hold"].append(key)

            # Remove duplicates
            for key in keys["hold"]:
                if key in keys["pressed"]: keys["pressed"].remove(key)
            
            # if there is next Screen
            nextScreen = self.screen.execute(keys)
            if(nextScreen is not None):
                self.screen = nextScreen(self.display)
 
            pygame.display.flip()
            self.clock.tick(int(OptionsReader().getValue("TargetFPS")))
            
            print(f"FPS:", int(self.clock.get_fps()),end="\r") if int(OptionsReader().getValue("ShowFPS")) else None

    def ChangeScreen():
        pass

Game().start()