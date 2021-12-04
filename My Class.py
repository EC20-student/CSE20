"""
Ethan Cadaoas
Your Own Class
In this assignment, you will implement your own class based on a real-world object.
You will write a class to meet certain requirements and write a short demo program in 
the main function that highlights all your class variables and methods. Along with this code, 
you will also create a short README file (this can be a .txt, .md, or .pdf) that describes your class, 
each of the variables and methods within, and describes the demo program and how to use it."""

class Pokemon_Creator:
    def __init__(self, name, type, hp, attack, defense, special, speed):
        self.name = name
        #takes in 7 arguments
        if type != "Fire" and type != "Water" and type != "Grass":
            print("Invalid Type: Choose Fire, Water, or Grass")
        else:
            self.type = type
        #limits 'type' to Fire, Water, and Grass
        if hp > 100 or hp < 1:
            print("Invalid Input: Stat Values range from 1 to 100")
        else:
            self.hp = hp
        if attack > 100 or attack < 1:
            print("Invalid Input: Stat Values range from 1 to 100")
        else:
            self.attack = attack
        if defense > 100 or defense < 1:
            print("Invalid Input: Stat Values range from 1 to 100")
        else:
            self.defense = defense
        if special > 100 or special < 1:
            print("Invalid Input: Stat Values range from 1 to 100")
        else:
            self.special = special
        if speed > 100 or speed < 1:
            print("Invalid Input: Stat Values range from 1 to 100")
        else:
            self.speed = speed
        #sets range for stat values from 1 to 100
    def get_hp(self):
        return (f'Pokemon Name: {self.name}\n HP Stat: {self.hp}')
        #function returns hp stat
    def get_attack(self):
        return (f'Pokemon Name: {self.name}\n Attack Stat: {self.attack}')
        #function returns attack stat
    def get_defense(self):
        return (f'Pokemon Name: {self.name}\n Defense Stat: {self.defense}')
        #fuction returns defense stat
    def get_special(self):
        return (f'Pokemon Name: {self.name}\n Special Stat: {self.special}')
        #function returns special stat
    def get_speed(self):
        return (f'Pokemon Name: {self.name}\n Speed Stat: {self.speed}')
        #fucntion returns speed stat
    def __str__(self):
        return (f"Pokemon Name: {self.name}\n Type: {self.type}\n HP: {self.hp}\n Attack: {self.attack}\n Defense: {self.defense}\n Special: {self.special}\n Speed: {self.speed}")
        #returns string of the Pokemon's Name, Type, and Stat Values

class change_hp(Pokemon_Creator):
        def __init__(self, name, type, hp, attack, defense, special, speed, new_hp="hp"):
            super().__init__(name=name, type=type, hp=hp, attack=attack, defense=defense, special=special, speed=speed)
            #inhereting from Pokemon Creator
            self.new_hp = new_hp
        def hp_change(self,change):
            self.new_hp = change
            #new input for new hp
        def __str__(self):
            return (f"Pokemon Name: {self.name}\n Type: {self.type}\n Old HP: {self.hp}\n New HP: {self.new_hp}\n Attack: {self.attack}\n Defense: {self.defense}\n Special: {self.special}\n Speed: {self.speed}")
            #returns string with new stats

class change_attack(Pokemon_Creator):
        def __init__(self, name, type, hp, attack, defense, special, speed, new_attack="attack"):
            super().__init__(name=name, type=type, hp=hp, attack=attack, defense=defense, special=special, speed=speed)
            #inhereting from Pokemon Creator
            self.new_attack = new_attack
        def attack_change(self,change):
            self.new_attack = change
            #new input for new attack
        def __str__(self):
            return (f"Pokemon Name: {self.name}\n Type: {self.type}\n HP: {self.hp}\n Old Attack: {self.attack}\n New Attack: {self.new_attack}\n Defense: {self.defense}\n Special: {self.special}\n Speed: {self.speed}")
            #returns string with new stats

class change_defense(Pokemon_Creator):
        def __init__(self, name, type, hp, attack, defense, special, speed, new_defense="defense"):
            super().__init__(name=name, type=type, hp=hp, attack=attack, defense=defense, special=special, speed=speed)
            #inhereting from Pokemon Creator
            self.new_defense = new_defense
        def defense_change(self,change):
            self.new_defense = change
            #new input for new defense
        def __str__(self):
            return (f"Pokemon Name: {self.name}\n Type: {self.type}\n HP: {self.hp}\n Attack: {self.attack}\n Old Defense: {self.defense}\n New Defense: {self.new_defense}\n Special: {self.special}\n Speed: {self.speed}")
            #returns string with new stats

class change_special(Pokemon_Creator):
        def __init__(self, name, type, hp, attack, defense, special, speed, new_special="special"):
            super().__init__(name=name, type=type, hp=hp, attack=attack, defense=defense, special=special, speed=speed)
            #inhereting from Pokemon Creator
            self.new_special = new_special
        def special_change(self,change):
            self.new_special = change
            #new input for new special stat
        def __str__(self):
            return (f"Pokemon Name: {self.name}\n Type: {self.type}\n HP: {self.hp}\n Attack: {self.attack}\n Defense: {self.defense}\n Old Special: {self.special}\n New Special: {self.new_special}\n Speed: {self.speed}")
            #returns string with new stats

class change_speed(Pokemon_Creator):
        def __init__(self, name, type, hp, attack, defense, special, speed, new_speed="speed"):
            super().__init__(name=name, type=type, hp=hp, attack=attack, defense=defense, special=special, speed=speed)
            #inhereting from Pokemon Creator
            self.new_speed = new_speed
        def speed_change(self,change):
            self.new_speed = change
            #new input for new speed
        def __str__(self):
            return (f"Pokemon Name: {self.name}\n Type: {self.type}\n HP: {self.new_hp}\n Attack: {self.attack}\n Defense: {self.defense}\n Special: {self.special}\n Old Speed: {self.speed}\n New Speed: {self.new_speed}")
            #returns string with new stats

def main():
    mon = Pokemon_Creator('Flameboy', 'Fire', 75, 45, 67, 87, 73)
    #created pokemon with name, type, and stats
    mon2 = change_hp('Plantboy', 'Grass', 93, 54, 32, 44, 94, 81)
    mon3 = change_attack('Waterboy', 'Water', 64, 96, 88, 70, 65, 47)
    mon4 = change_defense('Charmander', 'Fire', 39, 52, 100, 55, 65, 43)
    mon5 = change_special('Oshawott', 'Water', 55, 55, 45, 10, 45, 54)
    mon6 = change_speed('Rowlet', 'Grass', 68, 55, 55, 50, 83, 42)
    #pokemon with changed stats
    print(str(mon))
    #displaying string of created pokemon
    print(mon.get_hp())
    print(mon.get_attack())
    print(mon.get_defense())
    print(mon.get_special())
    print(mon.get_speed())
    #displaying specific stat of created pokemon
    print(str(mon2))
    print(str(mon3))
    print(str(mon4))
    print(str(mon5))
    print(str(mon6))
    #displaying new stat of pokemon
    

if __name__ == "__main__":
    main()
