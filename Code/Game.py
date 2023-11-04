import random
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
        print('Balanced stats. Basic skill tree unlocked')
        print('Orc:')
        print('Higher physical stats, lower mental stats. Special skill tree unlocked')
        print('Elf:')
        print('Higher mental stats, lower physical stats. Special skill tree unlocked')
        race = input('Choose:').lower()
        if race == 'human' or race == 'orc' or race == 'elf':
            return name, race
        else:
            print()
            print('Invalid choice, please try again.')
            print()

def GenerateCharAttributes(race='', name='', level=0, exp=0, expthresh=0, health=0, mana=0, strength=0, intelligence=0, wisdom=0, constitution=0, agility=0):
    name, race = CharacterCreation()
    if race == "human":
        level = 1
        expthresh = 20 #Temporary expthreshold
        strength = random.randint(3,10)
        intelligence = random.randint(3,10)
        wisdom = random.randint(3,10)
        constitution = random.randint(3,10)
        agility = random.randint(3,10)
        health = int(constitution * 1.5 + 10)
        mana = int(wisdom * 1.5 + 5)
    elif race == "orc":
        strength = random.randint(5,12)
        intelligence = random.randint(2,8)
        wisdom = random.randint(2,8)
        constitution = random.randint(5,12)
        agility = random.randint(5,12)
        health = int(constitution * 1.8 + 15)
        mana = int(wisdom * 1.2 + 3)
    elif race == "elf":
        strength = random.randint(2,8)
        intelligence = random.randint(5,12)
        wisdom = random.randint(5,12)
        constitution = random.randint(2,8)
        agility = random.randint(2,8)
        health = int(constitution * 1.2 + 6)
        mana = int(wisdom * 1.8 + 10)
    return name, race, level, exp, expthresh, health, mana, strength, intelligence, wisdom, constitution, agility

def GenerateCharacter():
    charattr = GenerateCharAttributes()
    character = {
    "name": charattr[0],
    "race": charattr[1],
    "level": charattr[2],
    "exp": charattr[3] ,
    "expthresh": charattr[4],
    "health": charattr[5],
    "mana": charattr[6],
    "strength": charattr[7],
    "intelligence": charattr[8],
    "wisdom": charattr[9],
    "constitution": charattr[10],
    "agility": charattr[11]}
    return character

#Change these names to char/character
Player = GenerateCharacter()

#Set up different colors for each stat, red for strength light blue for intel, orange for const, purple for wisdom and green for agil
#The above is not set in stone, just ideas.
def CharSheet():
    print(color.BLUE, "[CHARACTER SHEET]", color.END, sep='')
    print(f"Name: {Player['name']}")
    print(f"Race: {Player['race']}")
    print(f"Level: {Player['level']}")
    print(f"Exp: {Player['exp']}/{Player['expthresh']}")
    print(f"Health: {Player['health']}")
    print(f"Mana: {Player['mana']}")
    print("Stats:")
    print(f"Strength: {Player['strength']}")
    print(f"Intelligence: {Player['intelligence']}")
    print(f"Wisdom: {Player['wisdom']}")
    print(f"Constitution: {Player['constitution']}")
    print(f"Agility: {Player['agility']}")
#Next up is description of the character in the sheet, and whatever else that needs to be fleshed out more.
    
#Stat explantion:
#Assume all of these will have "narrative" consequences(By that i mean things like quest reqs or whatever)
#Strength-Physical attack damage
#Intelligence-Magical attack damage
#Wisdom-Calculates your total mana and your mana regen
#Constituiton-Calculates your total health and your health regen
#Agility-Not yet decided but, probably priority in fights or dodge chance, or maybe both.
