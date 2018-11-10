class Player:
    def __init__(self):
        self.experience = 0
        self.max_health = 100
        self.health = 1000
        self.base_damage = 10000
        self.recovery_time = 1000  # ms

    def hit(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
