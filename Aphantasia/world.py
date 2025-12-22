from dataclasses import dataclass
from enum import Enum

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
    inventory: dict
    buildings: list

@dataclass
class Building:
    level: int 
    name: str
    description: str
    occupants: int
    maxoccupants: int
    
