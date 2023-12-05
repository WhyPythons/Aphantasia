import random, ruamel.yaml, sys, threading, time
from Colors import color

def SlowText(text='', speed=0.06):
    ls = []
    for char in text:
        ls.append(char)
        print(char, end='')
        time.sleep(speed)
        if len(ls) == len(text):
            print()
def CharacterCreation(race='', name=''):
    print("Welcome to [Aphantasia]")
    skipintro = input('Skip intro? (y/n):')
    if skipintro == 'y':
        SlowText("Character-Creator is online", 0.05)
    else:
        SlowText(f"Now i'm sure your wondering why {color.BOLD}you{color.END} are here! or maybe you've already been here before?")
        SlowText("Anyways thats besides the point, lets get to the good stuff!")
        SlowText(f"You! Yes, {color.BOLD}you{color.END}! have been chosen to be the hero of this world")
        SlowText('Now you may be wondering why me? now of course i could lie to you and say you are a wonderful person and deserve to be a hero')
        SlowText('or maybe i could just send you off with zero explanation, allowing you to experience a sense of mystery as you set out to find about me')
        SlowText('But that would be way less fun! so the truth is this a low level world, extremely low level. one so low it was barely on our radar until')
        SlowText("we discovered that there is a demon lord! now that may not mean much to you but demon lords are universal threats and to find one so early in development is even rarer")
        SlowText("So now you may be thinking, 'why don't you just go down there yourself and kill it or something', well i say to that, i'd rather not die.")
        SlowText("Aw well enough with the info dump, i'm sure you'll figure the rest out yourself! have fun!")
        SlowText("*distant* oh! and by the way there's gonna be this character creator for ya, its the least we can do!")
        SlowText('.........................................')
        SlowText("Character-Creator is online", 0.06)
    while True:
        name = input('Please enter a name:')
        sure = input('Are you sure? (y/n) ')
        if sure == 'y' or sure == 'yes':
            print()
            break
    print('Please choose a race:')
    while race != 'Human' or race != 'Orc' or race != 'Elf':
        #Set up colors for each race name.
        print('Human:')
        print('Balanced base stats.')
        print('Orc:')
        print('Higher base physical stats, lower base mental stats.')
        print('Elf:')
        print('Higher base mental stats, lower base physical stats.')
        race = input('Choose:').lower()
        if race == 'human' or race == 'orc' or race == 'elf':
            return name, race
        else:
            print()
            print('Invalid choice, please try again.')
            print()

def GenerateCharAttributes(race='', name='', job=None, level=0, exp=0, expthresh=0, health=0, maxhealth=0, mana=0, maxmana=0, gold=0, strength=0, intelligence=0, wisdom=0, constitution=0, dexterity=0, skills={}, skillpoints=0, inventory={}, quests={}):
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
        skills = {"Passive:": {},
                  "Active:": {}}
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
        skills = {"Passive:": {},
                  "Active:": {}}
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
        skills = {"Passive:": {},
                  "Active:": {}}
    return name, race, job, level, exp, expthresh, health, maxhealth, mana, maxmana, gold, strength, intelligence, wisdom, constitution, dexterity, skills, skillpoints, inventory, quests
    
def GenerateCharacter():
    charattr = GenerateCharAttributes()
    character = {
    "name": charattr[0],
    "race": charattr[1],
    "job": charattr[2],
    "level": charattr[3],
    "exp": charattr[4] ,
    "expthresh": charattr[5],
    "health": charattr[6],
    "maxhealth": charattr[7],
    "mana": charattr[8],
    "maxmana": charattr[9],
    "gold": charattr[10],
    "strength": charattr[11],
    "intelligence": charattr[12],
    "wisdom": charattr[13],
    "constitution": charattr[14],
    "dexterity": charattr[15],
    "skills": charattr[16],
    "skillpoints": charattr[17],
    "inventory": charattr[18],
    "quests": charattr[19]}
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
    print(Character['inventory'])

def Skills():
    print(Character["skills"])

def CharSheet():
    print(color.BLUE, "[CHARACTER SHEET]", color.END, sep='')
    print(f"Name: {Character['name']}")
    print(f"Race: {Character['race']}")
    print(f"Job: {Character['job']}")
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

def RegenMana():
    #When combat is created this should be changed to stop when in a fight so turn based mana regen can come into play.
    manaless = False
    while not manaless:
        if Character['mana'] == Character['maxmana']:
            manaless = False
        else:
            manaless = True
        while manaless:
            time.sleep(200 - Character['wisdom'])
            Character['mana'] += 1
            if Character['mana'] == Character['maxmana']:
                manaless = False
            
def RegenHealth():
    #The idea here is to encourage using things like health potions or paying for healing and discourage waiting for health to regen unlike mana which i allow more leniency for lore reasons.
    healthless = False
    while not healthless:
        if Character['health'] == Character['maxhealth']:
            healthless = False
        else:
            healthless = True
        while healthless:
            time.sleep(400 - Character['constitution'])
            Character['health'] += 1
            if Character['health'] == Character['maxhealth']:
                healthless = False

RegenManaThread = threading.Thread(target=RegenMana)
RegenManaThread.start()
RegenHealthThread = threading.Thread(target=RegenHealth)
RegenHealthThread.start()

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
#"""for outer, inner in armor.items():
#       x = len(inner)
#       if x > 1:
#          print("no!")"""
