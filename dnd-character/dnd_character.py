from math import floor
NUMBER_OF_DICE = 4
import random 


class Character:
    def __init__(self):
       self.strength = dice_throw()
       self.dexterity = dice_throw()
       self.constitution = dice_throw()
       self.intelligence = dice_throw()
       self.wisdom = dice_throw()
       self.charisma = dice_throw()
       self.hitpoints = modifier(self.constitution) + 10 
       self.attributes = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma, self.hitpoints]

    def ability(self):
        return random.sample(self.attributes, 1)[0]


def modifier(number):
    return floor((number - 10) /2)


def dice_throw():
    dices = sorted([random.randint(1,6) for i in range(NUMBER_OF_DICE)])[1:]
    return sum(dices)

