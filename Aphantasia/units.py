from dataclasses import dataclass
from items import Rarity

@dataclass
class Identity:
    name: str
    age: str
    race: str
    sex: str
    backstory: str

@dataclass
class Appearance:
    skincolor: str
    eyecolor: str
    hairstyle: str
    haircolor: str 

@dataclass
class Skill:
    level: int
    name: str
    description: str

@dataclass
class Meta:
    rarity: Rarity
    inventory: dict
    equippeditems: dict

@dataclass
class Unit:
    identity: Identity
    appearance: Appearance
    skills: dict[str, Skill]
    meta = Meta

def summon_unit():
    print('todo')

def display_unit_info():
    print("todo")

