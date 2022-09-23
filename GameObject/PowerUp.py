from enum import Enum

class PowerUpEnum(Enum):
    MACHINEGUN_PWU = 1
    INVENCIBLE_PWU = 2

class PowerUp(object):
    name: PowerUpEnum = None
    time: int = 0

    def __init__(self, powerUpName, time) -> None:
        self.name = powerUpName
        self.time = time
        
    def __eq__(self, __o: object) -> bool:
        if type(__o) != PowerUpEnum:
            return False

        return self.name == __o.name
