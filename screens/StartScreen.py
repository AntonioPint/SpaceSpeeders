from screens.Screen import Screen

class StartScreen(Screen):
    display = None

    def __init__(self, display):
        super().__init__(display)

    def execute(self, input):
        self.display.fill((255,255,1))