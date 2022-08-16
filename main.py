# imports
from queue import Empty
import sys
import pygame
from OptionsReader import OptionsReader
from screens.ScreenManager import ScreenManager


# ScreenVariables
_screenHeight = int(OptionsReader().getValue("WindowHeight"))
_screenWidth = int(OptionsReader().getValue("WindowWidth"))

# Allowed Game Input
KeyInputs = [
    pygame.K_UP, pygame.K_w,
    pygame.K_DOWN, pygame.K_s,
    pygame.K_LEFT, pygame.K_a,
    pygame.K_RIGHT, pygame.K_d,
    pygame.K_SPACE, pygame.K_ESCAPE,
    pygame.MOUSEBUTTONDOWN
]

def main():
    # PyGame
    pygame.init()
    clock = pygame.time.Clock()
    display = pygame.display.set_mode(
        [_screenWidth, _screenHeight])  # , pygame.NOFRAME
    screen = ScreenManager().getScreen()
    screenDisplayed = screen(display)
    pygame.display.set_caption('SpaceSpeeders')

    while True:
        inputs = {"hold": [], "pressed": [],
                    "released": [], "mousePos": ()}

        hold = pygame.key.get_pressed()
        pressed = pygame.event.get()

        # Gets Pressed inputs
        for event in pressed:
            inputs["mousePos"] = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #print("Pressed ", pygame.key.name(event.key))
                inputs["pressed"].append(event.key)
            elif event.type == pygame.KEYUP:
                #print("Released ", pygame.key.name(event.key))
                inputs["released"].append(event.key)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #print("🖱️ at " , pygame.mouse.get_pos())
                inputs["pressed"].append(pygame.MOUSEBUTTONDOWN)

        # Gets Holded inputs
        for key in KeyInputs:
            if hold[key]:
                if(not inputs["pressed"].__contains__(key) and not inputs["released"].__contains__(key)):
                    #print("Holded ", pygame.key.name(key))
                    inputs["hold"].append(key)


        if ScreenManager().getScreen() != screen:
            screen = ScreenManager().getScreen()
            screenDisplayed = screen(display)

        screenDisplayed.execute(inputs)

        pygame.display.update()
        #pygame.display.flip()
        
        clock.tick(int(OptionsReader().getValue("TargetFPS")))

        print(f"FPS:", int(clock.get_fps()), end="\r") if int(
            OptionsReader().getValue("ShowFPS")) else None

if __name__ == '__main__':
    main()