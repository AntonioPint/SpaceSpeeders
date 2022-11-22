from GameObject.Enemy.Enemy import Enemy

class EnemyBiggerAsteroid(Enemy):
    
    Health = 15
    EnemyHeight = 200
    EnemyWidth = 200
    AccelerationIncrement = .0005
    
    def __init__(self, position, acceleration=0.5):
        super().__init__(
            position,
            acceleration
        )

    
        