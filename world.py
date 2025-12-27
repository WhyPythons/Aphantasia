from dataclasses import dataclass
from pathlib import Path
from enum import Enum
import json, random

class WorldLevel(Enum):
    DESOLATE = "desolate"
    OPTIMISTIC = "optimistic"
    PROSPEROUS = "prosperous"
    THRIVING = "thriving"
    Utopia = "utopia"

@dataclass
class World:
    level: WorldLevel
    coins: int
    units: list
    buildings: dict

@dataclass
class Building:
    level: int 
    name: str
    description: str
    occupants: dict
    maxoccupants: int

    def load_buildings():
        folder = Path("jdata/world")
        files = {f.stem: str(f) for f in folder.rglob("*") if f.is_file()}

        storage = {}
        for key, path in files.items():
            with open(path, "r") as f:
                content = f.read()
                print(content)
                if not content:
                    print(f"Empty Json: {key}. [Ignoring]")
                    continue
                storage[key] = json.loads(content)

        return storage["buildings"]

    
