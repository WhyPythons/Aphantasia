from dataclasses import dataclass
from common import read_files
from pathlib import Path

@dataclass
class World:
    level: int
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

        storage, files = read_files("jdata/world")

        return storage["buildings"]

    
