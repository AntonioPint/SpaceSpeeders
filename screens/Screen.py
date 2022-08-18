from OptionsReader import OptionsReader


class Screen(object):
    display = None
    
    WindowDimensions = (int(OptionsReader().getValue("WindowWidth")),
                           int(OptionsReader().getValue("WindowHeight")))

    def __init__(self, display):
        self.display = display

    def execute(self, input):
        return None

    def executeInputs(self, input):
        # Execute Keyboard Inputs
        for i in input["pressed"]:
            if self.myPressedActions.get(i) is not None:
                a = self.myPressedActions.get(i)()
                if a is not None:
                    return a

        for f in input["hold"]:
            if self.myHoldActions.get(f) is not None:
                a = self.myHoldActions.get(f)()
                if a is not None:
                    return a

        for g in input["released"]:
            if self.myReleasedActions.get(g) is not None:
                a = self.myReleasedActions.get(g)()
                if a is not None:
                    return a

    myHoldActions = {}
    myPressedActions = {}
    myReleasedActions = {}
