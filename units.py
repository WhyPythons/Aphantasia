from dataclasses import dataclass
from items import Rarity
from enum import Enum
from pathlib import Path
import json, random

#Traits?

class Sex(Enum):
    MALE = "male"
    FEMALE = "female"

class Age(Enum):
    TEENAGER = "teenager"
    YOUNGADULT = "young-adult"
    ADULT = "adult"
    ELDER = "elder"

@dataclass 
class Stats:
    strength: int
    toughness: int
    agility: int
    intelligence: int

@dataclass
class Skill:
    name: str
    rarity: Rarity
    level: int
    description: str

@dataclass
class Race:
    name: str 
    rarity: Rarity
    description: str
    racial_stat_ranges: dict #strength: (0, 10), agility: (0, 100), etc
    racial_skills: list[Skill]

@dataclass
class Personality:
    name: str
    rarity: Rarity
    description: str
    personality_stat_modifiers: dict
    personality_skill: Skill

@dataclass
class Backstory:
    name: str
    rarity: Rarity
    description: str
    affiliation: str
    backstory_skills: list[Skill]
    backstory_stat_modifiers: dict 
    possible_personalities: list[Personality] # Two rarity intended personalites, and one rare one that's better than the other two

@dataclass
class Identity:
    name: str
    age: Age
    race: Race 
    sex: Sex
    backstory: Backstory
    personality: Personality

@dataclass
class Appearance:
    skincolor: str
    eyecolor: str
    haircolor: str
    hairstyle: str
    height: str
    weight: str
    muscle: str
    ears: str

@dataclass
class Meta:
    tier: int
    level: int
    exp: int
    stats: Stats
    skills: dict[str, Skill]
    inventory: dict

@dataclass
class Unit:
    identity: Identity
    appearance: Appearance
    meta: Meta

    def choose_sex():
        final_sex = random.choices(list(Sex), weights=[60, 40], k=1)

        return final_sex[0]
    
    def choose_age():
        return random.choice(list(Age))
    
    def choose_name(storage, sex):
        if sex == Sex.MALE:
            pool = storage["names"]["male_names"]
        else:
            pool = random.choice([storage["names"]["female_names"], storage["names"]["neutral_names"]])

        return random.choice(pool)
    
    def choose_by_rarity(storage: dict, files: dict, file_type: str):
        list = []
        weights = []

        for key in files.keys():
            if file_type in key:
                try:
                    for i in storage[key]:
                        list.append(storage[key][i])
                        weights.append(Rarity[storage[key][i]["rarity"]].number)
                except KeyError:
                    print("Error with assigning rarity (Lowercase 'common' or empty json) [Ignoring]")
                except TypeError:
                    print("Something has gone horribly wrong here.")

        final_race = random.choices(list, weights=weights, k=1)

        return list[0]
    
    def compute_identity(storage, files):
        age = Unit.choose_age()
        sex = Unit.choose_sex()
        name = Unit.choose_name(storage, sex)
        race = Unit.choose_by_rarity(storage, files, "races")
        backstory = Unit.choose_by_rarity(storage, files, "backstories")
        personality = Unit.choose_by_rarity(storage, files, "personality")

        return Identity(name, age, race, sex, backstory, personality)

    #Improve this later
    def compute_appearance(storage): 

        final_appearance = Appearance(random.choice(storage["skincolors"]),
        random.choice(storage["eyecolors"]),
        random.choice(storage["haircolors"]),
        random.choice(storage["hairstyles"]),
        random.choice(storage["heights"]),
        random.choice(storage["weights"]),
        random.choice(storage["muscle"]),
        random.choice(storage["ears"]))

        return final_appearance
    
    def compute_meta(race: dict, backstory, personality):
        final_stat_total = []

        race_stats: dict = race["racial_stat_ranges"]
        backstory_stats: dict = backstory["backstory_stat_modifiers"]
        personality_stats: dict = personality["personality_stat_modifiers"]

        for rstat in race_stats.values():
            final_stat_total.append(random.randint(rstat[0], rstat[1]))
        
        for i, k in enumerate(backstory_stats.keys()):
            final_stat_total[i] += backstory_stats[k]

        for e, d in enumerate(personality_stats.keys()):
            final_stat_total[e] += personality_stats[d]

        return Meta(0, 1, 0, Stats(*final_stat_total), {}, {})
    
    @staticmethod
    def summon_unit():
        folder = Path("jdata/units")
        files = {f.stem: str(f) for f in folder.rglob("*") if f.is_file()}

        storage = {}
        for key, path in files.items():
            with open(path, "r") as f:
                content = f.read()
                if not content:
                    print(f"Empty Json: {key}. [Ignoring]")
                    continue
                storage[key] = json.loads(content)

        identity = Unit.compute_identity(storage, files)
        appearance = Unit.compute_appearance(storage)
        meta = Unit.compute_meta(identity.race, identity.backstory, identity.personality)

        return Unit(identity, appearance, meta)

    def display_unit_info(self):
        print("[Character Sheet]")
        print(f"Level: {self.meta.level}")
        print(f"EXP: {self.meta.exp}")
        print("SUMMARY:")
        print(f"{self.identity.name} is a {self.identity.age.value} {self.identity.sex.value} {self.identity.race["name"]}, previously a {self.identity.backstory["name"]}.")
        print(
            f"They have {self.appearance.skincolor} skin, {self.appearance.eyecolor} eyes, "
            f"and {self.appearance.haircolor} hair worn in a {self.appearance.hairstyle} fashion. "
            f"{self.identity.name} stands {self.appearance.height} with a {self.appearance.weight} build, "
            f"marked by {self.appearance.muscle} musculature and {self.appearance.ears}"
        )  