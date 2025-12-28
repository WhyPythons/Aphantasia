from pathlib import Path
from enum import Enum
import json

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

def read_files(path: str):
    folder = Path(path)
    files = {f.stem: str(f) for f in folder.rglob("*") if f.is_file()}

    storage = {}
    for key, path in files.items():
        with open(path, "r") as f:
            content = f.read()
            if not content:
                print(f"Empty Json: {key}. [Ignoring]")
                continue
            storage[key] = json.loads(content)

    return storage, files