from enum import Enum
import random, json

class Rarity(Enum):
    NULL = "null"
    COMMON = "common"
    UNCOMMON = "uncommon"
    RARE = "rare"
    EPIC = "epic"
    LEGENDARY = "legendary"
    MYTHIC = "mythic"
    #Change to star based rating?
    
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



