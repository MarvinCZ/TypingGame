from datetime import datetime, timedelta


class Enemy:
    def __init__(self, max_health=5000, experience_drop=5000, name='Ghost', damage=10, damage_time=10000):
        self.max_health = max_health
        self.health = self.max_health
        self.experience_drop = experience_drop
        self.name = name
        self.damage = damage
        self.damage_time = damage_time  # ms
        self.channeling_start = datetime.now()

    def delay_channeling(self, player):
        self.channeling_start += timedelta(milliseconds=player.recovery_time)
        if self.channeling_start > datetime.now():
            self.channeling_start = datetime.now()

    def process_channeling(self, player):
        if self.channeling_start <= datetime.now() - timedelta(milliseconds=self.damage_time):
            player.hit(self.damage)
            self.channeling_start = datetime.now()

    def timer(self):
        return (self.channeling_start - (datetime.now() - timedelta(milliseconds=self.damage_time))).total_seconds()

    def hit(self, amount, player):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        self.delay_channeling(player)

