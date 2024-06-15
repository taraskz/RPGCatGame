# class for cats
class Cat:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage
        self.abilities = []
        self.skill_points = 0

    def attack(self, target):
        target.health -= self.damage
    
    def __str__(self):
        return f"{self.name} (Damage: {self.damage})"