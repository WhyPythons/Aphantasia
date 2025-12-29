from dataclasses import dataclass
from common import Rarity
from enum import Enum
import json

class ItemType(Enum):
    WEAPON = "weapon"
    SHIELD = "shield"
    ARMOR = "armor"
    RESOURCE = "resource"

@dataclass
class Item:
    name: str
    description: str
    quality: Rarity
    itemtype: ItemType
    properties: dict
    
    #Temporary
    def create_item():

        with open("jdata/weapons.json", "r") as f:
            data = json.load(f)
        
        return data



