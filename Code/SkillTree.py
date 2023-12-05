class SkillTree():
    def __init__(self, mage_skill_tree, warrior_skill_tree, rouge_skill_tree):
        mage_skill_tree = {"Tier 1": 
        {"Fireball": 
         {"Type": "Active",
          "Damage": 4, 
          "Desc": "Hurl a ball of fire at your enemies!", 
          "Effect": "Has a minor chance to burn",
          "ManaCost": 5,
          "PointsNeeded": 2}}
        }
        warrior_skill_tree = {"Tier 1": 
        {"PowerStrike",
         {"Type": "Active",
          "Damage": 6, 
          "Desc": "Use your mana to increase the damage of your strike!", 
          "Effect": None,
          "ManaCost": 4,
          "PointsNeeded": 3}}}
        rouge_skill_tree = {"Tier 1": 
        {"Backstab": 
         {"Type": "Active",
          "Damage": 3, 
          "Desc": "Backstab your opponent before they can see you coming!", 
          "Effect": "If your dexterity is higher than the enemies this attack does double damage",
          "ManaCost": 2,
          "PointsNeeded": 4}}}
        
#3 Skills for tier 1 2 active 1 passive
#4 Skills for tier 2 2 passive 2 active
#5 Skills for tier 3 2 active 3 passive
#Tier 3 is the final tier
#So in total for each class skill tree there are 12 skills
#so in true total 36 skills for every skill tree combined