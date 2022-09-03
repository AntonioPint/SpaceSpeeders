from OptionsReader import OptionsReader
from functools import partial


class Screen(object):
    display = None

    WindowDimensions = (int(OptionsReader().getValue("WindowWidth")),
                        int(OptionsReader().getValue("WindowHeight")))

    holdActions = {}
    pressedActions = {}
    releasedActions = {}

    def __init__(self, display):
        self.display = display

    def execute(self, input):
        return None

    def executeInputs(self, input):
        # Execute Keyboard Inputs
        for i in input["pressed"]:
            if self.pressedActions.get(i) is not None:
                self.executeInputsAux(self.pressedActions.get(
                    i)[0], self.pressedActions.get(i)[1])

        for f in input["hold"]:
            if self.holdActions.get(f) is not None:
                self.executeInputsAux(self.holdActions.get(
                    f)[0], self.holdActions.get(f)[1])

        for g in input["released"]:
            if self.releasedActions.get(g) is not None:
                self.executeInputsAux(self.releasedActions.get(
                    g)[0], self.releasedActions.get(g)[1])

    def executeInputsAux(self,function, args):
        funcResult = function(*args)
        return funcResult if funcResult is not None else None
       
