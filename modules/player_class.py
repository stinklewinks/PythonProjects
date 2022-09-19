import sys
sys.path.insert(1, './player_creation')
from skills import magic_skills

class Player:
    def __init__(self):
        self.name = ""
        self.damage = 25
        self.level = 0
        self.hp = 100
        self.mp = 100
        self.defense = 50
        self.race = ""
        self.skills = []
        

    location = 'Level One: The Southlands'

    # TODO: Check to see if there can be logic added to the class
    def attack(self):
        return "You attack for {} damage".format(self.damage)

    def block(self):
        return "You block with {} defense".format(self.defense)

    def evade(self):
        return "You evade from the conflict"

    def heal_self(self):
        return f"You heal. You now have {self.hp} health."
