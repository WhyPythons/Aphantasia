from dataclasses import dataclass
from common import read_files
from units import Unit
from pathlib import Path

@dataclass
class World:
    level: int
    coins: int
    units: list[Unit]
    buildings: dict

@dataclass
class Building:
    level: int 
    name: str
    description: str
    occupants: int
    maxoccupants: int

    def load_buildings():
        
        storage, files = read_files("data/world")

        return storage["buildings"]

    
