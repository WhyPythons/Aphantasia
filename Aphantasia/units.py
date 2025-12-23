from dataclasses import dataclass
from items import Rarity
from enum import Enum

class Sex(Enum):
    MALE = "male"
    FEMALE = "female"

class Age(Enum):
    TEENAGER = "teenager"
    YOUNGADULT = "young-adult"
    ADULT = "adult"
    ELDER = "elder"

@dataclass
class Skill:
    name: str
    level: int
    description: str

@dataclass
class Backstory:
    name: str
    rarity: Rarity
    description = str
    affiliation = str
    starting_skills = list[Skill]

class Race:
    name: str 
    description: str
    racial_features: str #TODO Appearance extras/limit options
    racial_skills: list[Skill]

@dataclass
class Identity:
    name: str
    age: Age
    race: Race 
    sex: Sex
    backstory: Backstory

@dataclass
class Appearance: 
    skincolor: str
    eyecolor: str
    hairstyle: str
    haircolor: str 
    height: str
    weight: str
    muscle: str
    ears: str

@dataclass
class Unit:
    identity: Identity
    appearance: Appearance
    skills: dict[str, Skill]
    inventory: dict

    def summon_unit():
        print('todo')

    def display_unit_info():
        print("todo")

