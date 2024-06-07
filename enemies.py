class Enemy():
    def __init__(self, name, health, damage, coins):
        self.name = name
        self.health = health
        self.damage = damage
        self.coins = coins

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0 

    def attack(self, target):
        target.health -= self.damage

Sir_Barksalot = Enemy("Sir Barksalot", 120, 30, 250)