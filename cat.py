# class for cats
class Cat:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"