from Singleton import SingletonMeta

class OptionsReader(metaclass=SingletonMeta):
    options = {}
    def __init__(self):
        with open("options.txt") as file:
            for line in file:
                (key,value) = line.split("=")
                self.options[key] = value

    def getValue(self, value):
        return self.options[value]