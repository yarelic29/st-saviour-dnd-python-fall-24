import random
from draw import draw_d20

class Tav:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role  
     
        self.level = 1
     
        self.strengh = 0
        self.wisdom = 0
        self.charisma = 0
        self.intelligence = 0
        self.constitution = 0
        self.dexterity = 0
     
    def print_character_sheet(self):
        print('Name: ' + self.name)
        print('Role: ' + self.role)
        print('Level: ' + str(self.level))

    def roll(self):
        r = random.randint(1,20)
        draw_d20(r)
        return r
    
   

