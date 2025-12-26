from enum import Enum
import random, json

#Numbers act as weights
class Rarity(Enum):
    NULL = ("null", 0)
    COMMON = ("common", 55)
    UNCOMMON = ("uncommon", 25)
    RARE = ("race", 10)
    EPIC = ("epic", 5)
    LEGENDARY = ("legendary", 4)
    MYTHIC = ("mythic", 1)
    
    def __init__(self, name_str, number):
        self.name_str = name_str
        self.number = number

class ItemType(Enum):
    WEAPON = "weapon"
    SHIELD = "shield"
    ARMOR = "armor"
    RESOURCE = "resource"

class Item:
    def __init__(self, name: str, description: str, rarity: Rarity, itemtype: ItemType, properties: dict):
        self.name = name
        self.description = description
        self.rarity = rarity
        self.itemtype = itemtype
        self.properties = properties
    
    #Not quite sure how to go about this. This is just temporary.
    def create_item():

        with open("jdata/weapons.json", "r") as f:
            data = json.load(f)
        
        return data



