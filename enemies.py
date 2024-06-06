class Enemy():
  def __init__(self, name, health, skills, attack, loot, text):
      self.name = name
      self.health = health
      self.skills = skills
      self.attack = attack
      self.loot = loot
      self.text = text

  def take_damage(self, damage):
      self.health -= damage
      if self.health < 0:
          self.health = 0

  def is_alive(self):
      return self.health > 0

Clawmancer_Felisar = Enemy("Clawmancer Felisar", 200, "Spawn in goons",
                            "Scratch", "Catnip",
                           "It's the dreaded Clawmancer Felisar, \
watch out!")

Goon = Enemy("Goon", 20, "None", "Hiss", "Nothing", "Just some easy goons to \
kill.")

Sir_Barksalot = Enemy("Sir Barksalot", 120, "Drool", "Barks and Bite", 
                      "Bone key", "Uh is this a dog?")