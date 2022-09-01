from OptionsReader import OptionsReader


class Screen(object):
    display = None
    
    WindowDimensions = (int(OptionsReader().getValue("WindowWidth")),
                           int(OptionsReader().getValue("WindowHeight")))

    def __init__(self, display):
        self.display = display

    def execute(self, input):
        return None

    def executeInputs(self, selfRef, input):
        # Execute Keyboard Inputs
        for i in input["pressed"]:
            self.executeInputsAux(self.myPressedActions.get(i), selfRef)

        for f in input["hold"]:
            self.executeInputsAux(self.myHoldActions.get(f), selfRef)

        for g in input["released"]:
            self.executeInputsAux(self.myReleasedActions.get(g), selfRef)

    def executeInputsAux(self, function, args):
        if function is not None:
            try:
                funcResult = function(args)
                return funcResult if funcResult is not None else None
            except:
                funcResult = function()
                return funcResult if funcResult is not None else None

    myHoldActions = {}
    myPressedActions = {}
    myReleasedActions = {}
