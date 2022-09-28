from Singleton import SingletonMeta

class OptionsReader(metaclass=SingletonMeta):
    dictionary = {}

    def __init__(self):
        with open("options.txt") as file:
            for line in file:
                (key,value) = line.split("=")
                self.dictionary[key] = value

    def getValue(self, value):
        return self.dictionary[value]