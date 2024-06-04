class Player:
    def __init__(self, name, health = 100):
        '''This function has player name and health'''
        self.name = name
        self.health = health

    def take_damage(self, damage):
        '''Allows player to take damage'''
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def player_is_alive(self):
        '''Checks if player is alive'''
        return self.health > 0