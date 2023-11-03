import random
def GenerateLevel(level=0, exp=0, expthresh=0):
  level = 1
  exp = 0
  expthresh = 20
  return level, exp, expthresh
def GenerateStats(health=0, strength=0, intelligence=0, constitution=0, agility=0):
  health = random.randint(10,20) #Unsure if this should be fixed or random or if it should be in this function at all.
  strength = random.randint(1,10)
  intelligence = random.randint(1,10)
  constitution = random.randint(1,10)
  agility = random.randint(1,10)
  return health, strength, intelligence, constitution, agility
def GeneratePlayer():
    stats = GenerateStats()
    level = GenerateLevel()
    player = {
    "health": stats[0], 
    "strength": stats[1], 
    "intelligence": stats[2], 
    "constitution": stats[3], 
    "agility": stats[4],
    "level": level[0],
    "exp": level[1],
    "expthresh": level[2]}
    return player
Player = GeneratePlayer()
print(Player)
def CharSheet():
    print(f"health: {Player['level']}")
#To be continued
