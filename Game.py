import random
def GenerateLevel(level, exp, expthresh):
  level = 1
  exp = 0
  expthresh = 20
  return level, exp, expthresh
def GenerateStats(health, strength, intelligence, constitution, agility):
  health = random.randint(10,20) #Unsure if this should be fixed or random.
  strength = random.randint(1,10)
  intelligence = random.randint(1,10)
  constitution = random.randint(1,10)
  agility = random.randint(1,10)
  return health, strength, intelligence, constitution, agility
def GeneratePlayer():
    stats = GenerateStats(0,0,0,0,0)
    level = GenerateLevel(0,0,0)
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
