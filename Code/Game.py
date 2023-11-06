import random, ruamel.yaml, sys
from Colors import color


def CharacterCreation(race='', name=''):
    print("Welcome to [TEMP NAME]")
    print("Character Creation start!")
    while True:
        name = input('Enter a name:')
        sure = input('Are you sure? (y/n) ')
        if sure == 'y':
            break
    while race != 'Human' or race != 'Orc' or race != 'Elf':
        #Set up colors for each race name.
        print('Human:')
        print('Balanced stats.')
        print('Orc:')
        print('Higher physical stats, lower mental stats.')
        print('Elf:')
        print('Higher mental stats, lower physical stats.')
        race = input('Choose:').lower()
        if race == 'human' or race == 'orc' or race == 'elf':
            return name, race
        else:
            print()
            print('Invalid choice, please try again.')
            print()

def GenerateCharAttributes(race='', name='', level=0, exp=0, expthresh=0, health=0, maxhealth=0, mana=0, maxmana=0, gold=0, strength=0, intelligence=0, wisdom=0, constitution=0, dexterity=0):
    name, race = CharacterCreation()
    level = 1
    expthresh = 20  # Temporary expthreshold, Well yes because it will go up every level up, but i mean temp in the other way.
    if race == "human":
        strength = random.randint(3,10)
        intelligence = random.randint(3,10)
        wisdom = random.randint(3,10)
        constitution = random.randint(3,10)
        dexterity = random.randint(3,10)
        health = int(constitution * 1.5 + 10)
        maxhealth = health
        mana = int(wisdom * 1.5 + 5)
        maxmana = mana
    elif race == "orc":
        strength = random.randint(5,12)
        intelligence = random.randint(2,8)
        wisdom = random.randint(2,8)
        constitution = random.randint(5,12)
        dexterity = random.randint(5,12)
        health = int(constitution * 1.8 + 15)
        maxhealth = health
        mana = int(wisdom * 1.2 + 3)
        maxmana = mana
    elif race == "elf":
        strength = random.randint(2,8)
        intelligence = random.randint(5,12)
        wisdom = random.randint(5,12)
        constitution = random.randint(2,8)
        dexterity = random.randint(2,8)
        health = int(constitution * 1.2 + 6)
        maxhealth = health
        mana = int(wisdom * 1.8 + 10)
        maxmana = mana
    return name, race, level, exp, expthresh, health, maxhealth, mana, maxmana, gold, strength, intelligence, wisdom, constitution, dexterity

def GenerateCharacter():
    charattr = GenerateCharAttributes()
    character = {
    "name": charattr[0],
    "race": charattr[1],
    "level": charattr[2],
    "exp": charattr[3] ,
    "expthresh": charattr[4],
    "health": charattr[5],
    "maxhealth": charattr[6],
    "mana": charattr[7],
    "maxmana": charattr[8],
    "gold": charattr[9],
    "strength": charattr[10],
    "intelligence": charattr[11],
    "wisdom": charattr[12],
    "constitution": charattr[13],
    "dexterity": charattr[14]}
    return character

Character = GenerateCharacter()

#Set up different colors for each stat, red for strength light blue for intel, orange for const, purple for wisdom and green for agil
#The above is not set in stone, just ideas.

def Equipment():
    #All of them are just 1 for each
    equipment = {
    "Armor": {"Head": {}, "Torso": {}, "Arms": {}, "Legs": {}, "Feet": {}},
    "Weapons": {"MainHand": {}, "OffHand": {}},
    "Accessories":{"Neck": {}, "Hands": {}}
    }
    yaml = ruamel.yaml.YAML()
    formatted = yaml.dump(equipment, sys.stdout)
    return formatted

def Inventory():
    return 0

def Skills():
    return 0

def CharSheet():
    print(color.BLUE, "[CHARACTER SHEET]", color.END, sep='')
    print(f"Name: {Character['name']}")
    print(f"Race: {Character['race']}")
    print(f"Level: {Character['level']}")
    print(f"Exp: {Character['exp']}/{Character['expthresh']}")
    print(f"Health: {Character['health']}/{Character['maxhealth']}")
    print(f"Mana: {Character['mana']}/{Character['maxmana']}")
    print(f"Gold: {Character['gold']}")
    print("Stats:")
    print(f"Strength: {Character['strength']}")
    print(f"Intelligence: {Character['intelligence']}")
    print(f"Wisdom: {Character['wisdom']}")
    print(f"Constitution: {Character['constitution']}")
    print(f"Dexterity: {Character['dexterity']}")

def Menu():
    while True:
        options = input("Stats, Equipment, Inventory, Skills:").lower()
        if options == "stats" or options == 'st':
            CharSheet()
        elif options == "equipment" or options == 'eq':
            Equipment()
        elif options == 'skills' or options == 'sk':
            Skills()
        elif options == 'inventory' or options == 'in':
            Inventory()
        elif options == 'exit' or options == 'leave':
            print('Exiting menu')
            break
Menu()


#Next up is description of the character in the sheet, and whatever else that needs to be fleshed out more.

#Stat explantion:
#Assume all of these will have "narrative" consequences(By that i mean things like quest reqs or whatever)
#Strength-Physical attack damage
#Intelligence-Magical attack damage
#Wisdom-Calculates your total mana and your mana regen
#Constituiton-Calculates your total health and your health regen
#Agility-Not yet decided but, probably priority in fights or dodge chance, or maybe both.
#The below is for when equipping is a thing.
"""for outer, inner in armor.items():
        x = len(inner)
        if x > 1:
            print("no!")"""
