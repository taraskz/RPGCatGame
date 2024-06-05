class Cat:
    def __init__(self, name, damage, health):
        self.name = name
        self.damage = damage
        self.health = health

    def attack(self, target):
        target.health -= self.damage

    def __str__(self):
        return f"{self.name} (Damage: {self.damage}, Health: {self.health})"