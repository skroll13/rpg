from email.base64mime import header_length
import random


class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        if enemy.characterName != "zombie":
            enemy.health-=self.power
        elif (self.characterName == "hero"):
            print(f"You do {self.power} points of damage to {enemy.characterName}.")
        elif (self.characterName == "goblin" or self.characterName == "zombie"):
            print(F"The {self.characterName} does {self.power} damage to you.")
    def print_status(self):
        if self.characterName == "hero":
         print(f"You have {self.health} health and {self.power} power.")
        elif self.characterName == "goblin" or self.characterName == "zombie" or self.characterName == "shadow" or self.characterName == "gnome":
            print(f"The {self.characterName} has {self.health} health and {self.power} power.")
    def alive(self):
        if self.health > 0:
            return True
        else: #####This isn't working
            print(f'{self.characterName} has perished.') #this isn't pulling in correctly
            hero.coins = ()
            if self.characterName == 'goblin':
                hero.coins + 6
                print(hero.coins())
            elif self.characterName == 'shadow':
                hero.coins + 8
                print(hero.coins())
            elif self.characterName == 'gnome':
                hero.coins + 9
                print(hero.coins())
            elif self.characterName == 'drow':
                hero.coins + 1
                print(hero.coins()) 
            return False        
    
class Hero(Character):
    def __init__(self, health, power):
        self.characterName = "hero"
        super(Hero, self).__init__(health, power)
    def doublePointsAttack(self,enemy): #### This isn't working
        power_int = random.randint(1, 5)
        if power_int() == 5:
            enemy.health -= self.power * 2
            print("\nDouble damage points!")
        else:
            enemy.health -= self.power
            print(f"{enemy.characterName} receives {self.power} damage points from {self.characterName} .")
            if enemy.health <= 0:
                print(f"The {enemy.characterName} is dead.")
    
class Goblin(Character):
    def __init__(self, health, power):
        self.characterName = "goblin"
        super(Goblin, self).__init__(health, power)
        
class Zombie(Character):
    def __init__(self, health, power):
        self.characterName = "zombie"
        super(Zombie, self).__init__(health, power)
        
class Medic(Character):
    def __init__(self, health, power):
        self.characterName = "medic"
        super(Medic, self).__init__(health, power)
    def doubleHealthPoints(self):
        power_int = random.randint(1, 5)
        if power_int == 5:
            self.medic += self.health * 2
            print("\nHealed by 2 Health Points")
            
class Shadow(Character):
    def __init__(self, health, power):
        self.characterName = "shadow"
        super(Shadow, self).__init__(health, power)
    def minimalDamage(self): ##### this isn't working
        power_int = random.randint(1, 10)
        if power_int == 10:
            self.health - 1
            print("\nMinimal Damage Points!")
        else:
            self.health = 50
            print(f"{self.characterName} receives {self.power} damage points from {self.characterName} .")
            if self.health <= 0:
                print(f"The {self.characterName} is dead.")
                
class Gnome(Character):
    def __init__(self, health, power):
        self.characterName = 'gnome'
        super(Gnome, self).__init__(health, power)
    def stabbingAttack(self): ####This isn't working 
        power_int = random.randint(1,2)
        if power_int == 2:
            self.power + 5
            print("Power Stabbing Attack")
            print(f"{self.characterName} yells 'You can't tell me what to do!'")
        
class Drow(Character):
    def __init__(self, health, power):
        self.characterName = 'drow'
        super(Drow, self).__init__(health, power)

class HelpfulItems():
    def __init__(self, health, worth):
        self.health = health 
        self.worth = worth
            
class SuperTonic(HelpfulItems):
    def __init__(self, health, worth):
        self.itemName = 'superTonic'
        super(SuperTonic, self).__init__(health, worth)
    #this will restore 10 health points back to the hero
        
class Armor(HelpfulItems):
    def __init__(self, health, worth):
        self.itemName = 'armor'
        super(Armor, self).__init__(health, worth)
    #this will add 2 armor points to the hero, adding a new attribute.
    #each time the hero is attacked, the hit points received will be reduced by the armor attribute.
    
class Evade(HelpfulItems):
    def __init__(self, health, worth):
        self.itemName = 'evade'
        super(Evade, self).__init__(health, worth)
    #this will add 2 evade points to the hero - adding another attribute
    #the more evade owned, the more likely that the hero will avoid the attack.
    #100% avoidance is not possible
    #for example: 2 evade points: 10% probably of avoiding attack, 
    # 4 evade points: 15% probability of avoiding attack.              

class Magic(HelpfulItems):
    def __init__(self, health, worth):
        self.itemName = 'magic'
        super(Magic, self).__init__(health, worth)
    #this allows the hero to cast healing on themselves returning them to full health

class Fly(HelpfulItems):
    def __init__(self, health, worth):
        self.itemName = 'fly'
        super(Fly, self).__init__(health, worth)
    #this allows the Hero to unfurl wings and fly a few feet away, avoiding any damage
           
            
hero = Hero(10,5)
goblin = Goblin(6, 2)
zombie = Zombie(10,1)
shadow = Shadow(50,10)
gnome = Gnome(7,3)
    
def fight(enemy):

    while enemy.alive() > 0 and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print(f"1. fight {enemy.characterName}")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            hero.attack(enemy)
            enemy.attack(hero)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye! Better adventuring next time.")
            break
        else:
            print("Invalid input {}. Please choose again.".format(raw_input))
            return
fight(gnome)

def store():
    while #not sure what goes here but it needs to stay open for shopping
    print(hero.coins)
    print()
        print("Hello! What would you like to buy?")
        print(f"1. buy {SuperTonic}")
        print(f"2. buy {Armor}")
        print(f"3. buy {Evade}")
        print(f"4. buy {Magic}")
        print(f"5. buy {Fly}")
        print("6. just look around")
        print("7. leave the shop")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":#1-5
            #buy things
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Shopkeep says 'Thanks for stopping by!' as {hero.characterName} leaves the shop.")
            break
        else:
            print("Invalid input {}. Please choose again.".format(raw_input))
            return
        #how do I return the user to the fight?
