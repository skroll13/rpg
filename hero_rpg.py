from email.base64mime import header_length
import random


class Character():
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        if self.characterName == "gnome":
            power_int = random.randint(1,2)
            if power_int == 2:
                self.power += 2
                enemy.health -= self.power
                print("\nThe gnome executes a POWER STABBING ATTACK and yells 'AAAarrgggghh!'")
            else: 
                enemy.health -= self.power
                print(f"\nThe {self.characterName} does {self.power} damage to {enemy.characterName}.")
        elif self.characterName == "shadow":
            power_int = random.randint(1, 10)
            if power_int == 10:
                self.health -= 1
                print("\nThe shadow MINIMIZES Damage Points!")
            else:
                enemy.health -= self.power
                print(f"The {enemy.characterName} receives {self.power} damage points from {self.characterName}.")
        elif (self.characterName == "goblin"):
            print(f"The {self.characterName} does {self.power} damage to you.")
        elif enemy.characterName != "zombie":
            enemy.health-=self.power
    def print_status(self):
        if self.characterName == "hero":
         print(f"\nThe hero has {self.health} health and {self.power} power and {self.coins} coins.")
        elif self.characterName != "hero":
        # "goblin" or self.characterName == "zombie" or self.characterName == "shadow" or self.characterName == "gnome":
            print(f"The {self.characterName} has {self.health} health and {self.power} power.")
    def alive(self):
        if self.health > 0:
            return True
        else: 
            print(f'The {self.characterName} has perished.') 
            print(f"The hero now has {hero.coins} coins.")
            return False        
    
class Hero(Character):
    def __init__(self, health, power, coins):
        self.characterName = "hero"
        self.coins = coins
        super(Hero, self).__init__(health, power)
    def doublePointsAttack(self,enemy): 
        power_int = random.randint(1, 5)
        if power_int == 5:
            enemy.health -= self.power * 2
            print("\nHero delivers double damage points!")
        else:
            enemy.health -= self.power
            print(f"\nThe {enemy.characterName} receives {self.power} damage points from {self.characterName}.")
    def collectBounty(self, bountyAmount):
        self.coins += bountyAmount
    
class Goblin(Character):
    def __init__(self, health, power):
        self.characterName = "goblin"
        self.bounty = 5
        super(Goblin, self).__init__(health, power)
        
class Zombie(Character):
    def __init__(self, health, power):
        self.characterName = "zombie"
        self.bounty = 4
        super(Zombie, self).__init__(health, power)
        
class Medic(Character):
    def __init__(self, health, power):
        self.characterName = "medic"
        self.bounty = 2
        super(Medic, self).__init__(health, power)
    def doubleHealthPoints(self):
        power_int = random.randint(1, 5)
        if power_int == 5:
            self.medic += self.health * 2
            print("\nHealed by 2 Health Points")
            
class Shadow(Character):
    def __init__(self, health, power):
        self.characterName = "shadow"
        self.bounty = 7
        super(Shadow, self).__init__(health, power)
                
class Gnome(Character):
    def __init__(self, health, power):
        self.characterName = 'gnome'
        self.bounty = 15
        super(Gnome, self).__init__(health, power)
        
class Drow(Character):
    def __init__(self, health, power):
        self.characterName = 'drow'
        self.bounty = 1
        super(Drow, self).__init__(health, power)

##### Items:
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
           
            
hero = Hero(20,5,10)
goblin = Goblin(10, 2)
zombie = Zombie(10,1)
shadow = Shadow(10,10)
gnome = Gnome(10,3)
drow = Drow(10,5)
    
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
            hero.doublePointsAttack(enemy)
            enemy.attack(hero)
            if enemy.alive() <= 0 and hero.alive():
                # add bounty to hero
                hero.collectBounty(enemy.bounty)
        elif raw_input == "2":
            pass
        elif raw_input == "3":
            print("Goodbye! Better adventuring next time.")
            break
        else:
            print("Invalid input {}. Please choose again.".format(raw_input))
            return
fight(shadow)

# def store():
#     while #not sure what goes here but it needs to stay open for shopping
#     print(hero.coins)
#     print()
#         print("Hello! What would you like to buy?")
#         print(f"1. buy {SuperTonic}")
#         print(f"2. buy {Armor}")
#         print(f"3. buy {Evade}")
#         print(f"4. buy {Magic}")
#         print(f"5. buy {Fly}")
#         print("6. just look around")
#         print("7. leave the shop")
#         print("> ", end=' ')
#         raw_input = input()
#         if raw_input == "1":#1-5
#             #buy things
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Shopkeep says 'Thanks for stopping by!' as {hero.characterName} leaves the shop.")
#             break
#         else:
#             print("Invalid input {}. Please choose again.".format(raw_input))
#             return
        #how do I return the user to the fight?
