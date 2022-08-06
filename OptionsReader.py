class OptionsReader(object):
    dictionary = {}

    def __init__(self):
        with open("options.txt") as file:
            for line in file:
                (key,value) = line.split("=")
                # print(key + "-> " + value, end="")
                self.dictionary[key] = value

    def getValue(self, value):
        return self.dictionary[value]