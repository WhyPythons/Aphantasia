import random
#To do:
#Making output clearer is in my top 10 things to do, and making it cleaner looking.
#Scale enemy health and stats to player level, make resource gathering funner by adding flavor text, and make code nicer looking? doubt.
Debug_Mode = False
Quest_Taken = False
Have_Item_equip = False
Have_Tool_equip = False
Have_Armor_equip = False
Npc = False
Class_loop = True 
Equipped = False
WShop = False
level_up = False
Fighting = False
Shop = False
Village = False
Guild = False
Blacksmith = True
item = {}
tools = {}
Utility = {}
Armor = {}
wood = 0 
iron = 0
Gold = 0
Level = 1
Exp = 0
Wood_Chopping_skill = 0 
Mining_Skill = 0 
Skill_Exp_Wood = 0
Skill_Exp_Iron = 0
Tool_bonus = 0
Armor_bonus = 0
Health = 0
Karma = 0
Alignment = 'Neutral'
Skill_Skill_Exp = 0
enemies_health = 0
Strength_EN = 0
Intelligence_EN = 0
Agility_EN = 0
Constitution_EN = 0
Defence_En = 0 
strength = 0
intelligence = 0
agility = 0
constitution = 0 
defence = 0
Needed_for_Quest_Iron = 10
Needed_for_Quest_Wood = 10
Likeability_Wandering_Merchant = 0
Likeability_Village_Merchant = 0
stats = strength, intelligence, agility
enemy_stats = Strength_EN, Intelligence_EN, Agility_EN  
Craft_List = {'WoodenSword': 1, 'IronSword': 1}#Think what im going to do with this is do, woodensword: 10, woodenblade: 20, etc etc for wood and iron
Craft_List_Tools = {'WoodenAxe': 1, 'Ironaxe': 1}
Craft_List_Armor = {'WoodenHelmet': 1}
enemy_types = ['Demon', 'Bandit', 'Opponent', 'Wolf', 'Bear'] #Planning for this to actually matter, after combat is finished, or atleast semi completed
Choice_type = random.choice(enemy_types)
Utility_items = {'Health Potion': 10} #Unsure but this is gonna be a drop item, unsure if i should make a drop item list/dict or just use this for shit like that or make both.
Item_Rarity_list = ['Common',  'Uncommon', 'Rare', 'Epic'] 
Area = ['Forest', 'Rocky hills', 'Grassland', 'Mountains', 'Mine', 'Lumberyard'] #2 more, one for wood, one for iron
Equipped_Items = {}
in_Area = random.choice(Area) 
Quests = {"Defeat Enemy": 5}
Random_Quest = random.choice(list(Quests.items()))
Enter_Shop = ''
Shop_loop = ''
Crafting_input = ''
Equip_Item = ''
Rarity = ''
Unequip_What = ''
Job = input('Pick a class, Warrior, Mage, Rouge:')
Player_class = Job  

while Class_loop:
    if Job == 'Warrior':
        print("Plot: You are a old warrior, and you have decided to leave your village and go adventuring!, You decided you won't go back until your level 5")
        print('You are now a warrior')
        main_stat = strength = 10
        secondary_stat = agility = 6
        third_stat = intelligence = 2
        fourth_stat = constitution = 4
        defence = constitution // 2
        stats = strength, intelligence, agility, constitution
        Health = 40
        Karma += 5
        Skill_ = Warrior_Skill = 0 
        print(f'You are in a {in_Area}')
        Class_loop = False
    elif Job == 'Mage':
        print('Plot: You are a young wizard that has just been sent out to your first journey, they tell you to come back once you have become a level 5 mage.')
        print('You are now a Mage')
        main_stat = intelligence = 10 
        secondary_stat = agility = 6 
        third_stat = strength = 4 
        fourth_stat = constitution = 2
        defence = constitution // 2
        stats = strength, intelligence, agility, constitution
        Health = 20
        Karma = 0
        Skill_ = Mage_Skill = 0
        print(f'You are in a {in_Area}')
        Class_loop = False
    elif Job == 'Rouge':
        print('Plot: You are a rouge, you have been caught stealing and have been kicked out of the village!, they tell you they will accept you back if you become level 5.')
        print('You are now a Rouge')
        main_stat = agility = 10
        secondary_stat = strength = 6
        third_stat = intelligence = 4
        fourth_stat = constitution = 2
        defence = constitution // 2
        stats = strength, intelligence, agility, constitution
        Health = 30
        Karma -= -5
        Skill_ = Rouge_Skill = 0 
        print(f'You are in a {in_Area}')
        Class_loop = False
    else:
        print('That is not a valid class, pick again')
        Job = input('Pick a class, Warrior, Mage, Rouge:')
        Player_class = Job 
        
    

#Main game loop
while True:
    #Temp Fix
    if wood < 0:
        wood = 0
    elif iron < 0:
        iron = 0
    elif Health < 0:
        Health = 0
    #End Temp Fix 
    
    
    if Karma == 0:
        Alignment = 'Neutral'
    elif Karma <= -10:
        Alignment = 'Neutral Evil'
    elif Karma <= -30:
        Alignment = 'Lawful Evil'
    elif Karma <= -50:
        Alignment = 'Evil'
    elif Karma >= 10:
        Alignment = 'Neutral Good' 
    elif Karma >= 30:
        Alignment = 'Lawful Good'
    elif Karma >= 50:
        Alignment = 'Good'
    
    #would be nice if i could make this need less code, so i can actually make the enemy scale
    if Level == 1:
        Strength_EN =  random.randint(6, 9)
        Intelligence_EN = random.randint(2, 5)
        Agility_EN = random.randint(3, 7)
        Constitution_EN = random.randint(1, 3)
        Defence_En = Constitution_EN // 2
        enemy_stats = Strength_EN, Intelligence_EN, Agility_EN, Constitution_EN
        Level_Health_Enemy = random.randint(5, 20)
        enemies_health = Level_Health_Enemy
        Tool_Bonusl = random.randint(1, 4)
        
    
    if Level == 2:
        Crafting_input = random.randint(3, 7)

    
    if Level == 5:
        Strength_EN =  random.randint(8, 12)
        Intelligence_EN = random.randint(4, 8)
        Agility_EN = random.randint(6, 9)
        enemy_stats = Strength_EN, Intelligence_EN, Agility_EN
        enemies_health = random.randint(10, 12)

    if Exp >= 100:
        Level += 1
        level_up = True
        Exp = 0    

    if level_up == True:
        print('You have leveled up, Main stat +4 all others +2')
        main_stat += 4
        secondary_stat += 2
        third_stat += 2
        level_up = False
    
    if Skill_Exp_Wood == 100:
        Wood_Chopping_skill += 1
        Skill_Exp_Wood = 0
    elif Skill_Exp_Iron == 100:
        Mining_Skill += 1
        Skill_Exp_Iron = 0
    elif Skill_Skill_Exp == 100:
        Skill_ += 1
    
    if wood == Needed_for_Quest_Wood:
        infin_Quest_gold = random.randint(5, 20)
        print("Infinite Quest wood completed. Check /infin quests to see current progress")
        print(f"You have gotten {infin_Quest_gold}")
        Gold += infin_Quest_gold
        Needed_for_Quest_Wood += random.randint(10, 20)
    elif iron == Needed_for_Quest_Iron:
        infin_Quest_gold_iron = random.randint(5, 20)
        print("Infinite Quest iron completed. Check /infin quests to see current progress")
        print(f"You have gotten {infin_Quest_gold_iron}")
        Gold += infin_Quest_gold_iron
        Needed_for_Quest_Iron += random.randint(10, 20)
        
    #Main Command prompt
    Command = input('Command?')
    #End Main Command
    if Command == '/Debug':
        Debug_Password = input('Password:')
        if Debug_Password == 'DevRandoDebug123':
            Debug_Mode = True
            print('Debug activated!')

    if Command == 'Give gold' and Debug_Mode == True:
        Gold_Cmd = int(input('Give gold:'))
        Gold += Gold_Cmd
    elif Command == 'Set level' and Debug_Mode == True:
        Level_Cmd = int(input('Set Level:'))
        Level = Level_Cmd
    elif Command == 'Set Exp' and Debug_Mode == True:
        Exp_Cmd = int(input('Set Exp:'))
        Exp = Exp_Cmd
    elif Command == 'Set Wood' and Debug_Mode == True:
        Wood_Cmd = int(input('Set Wood:'))
        Wood = Wood_Cmd
    elif Command == 'Set Iron' and Debug_Mode == True:
        Iron_Cmd = int(input('Set Iron:'))
        Iron = Iron_Cmd
    elif Command == 'Set Area' and Debug_Mode == True:
        Area_Cmd = input('Area')
        if Area_Cmd in Area:
            in_Area = Area_Cmd
        else:
            print('Invalid Area')
    elif Command == 'stats' and Debug_Mode == True:
        Stats_Cmd = input('Set which stat(strength, agility, intelligence, constitution):')
        Stats_Set_Cmd = int(input('Set to what'))
        if Stats_Cmd == "strength":
            strength = Stats_Set_Cmd
        elif Stats_Cmd == "agility":
            agility = Stats_Set_Cmd
        elif Stats_Cmd == "intelligence":
            intelligence = Stats_Set_Cmd
        elif Stats_Cmd == "constitution":
            constitution = Stats_Set_Cmd
        else:
            print('Invalid Stat')
    elif Command == 'Set Karma' and Debug_Mode == True:
        Karma_Cmd = int(input('Set Karma:'))
        Karma = Karma_Cmd
    elif Command == 'Set skill exp' and Debug_Mode == True:
        Skill_Cmd = input('Which skill:')
        Skill_Cmd_Set = int(input('Set:'))
        if Skill_Cmd == 'WoodChopping':
            Wood_Chopping_skill = Skill_Cmd_Set
        elif Skill_Cmd == 'Mining':
            Mining_Skill = Skill_Cmd_Set
        elif Skill_Cmd == 'Skill':
            Skill_ = Skill_Cmd_Set
        else:
            print('Invalid Skill')
    #giving yourself items/tools/armor are next on the list

    if Command == '/Look':
        print(f'You are in a {in_Area} ')
    
    if Command == '/Infin Quests':
        print(f"Collect Wood Quest, Needed: {Needed_for_Quest_Wood - wood}")
        print(f"Collect Iron Quest, Needed: {Needed_for_Quest_Iron - iron}")
    
    #Resource gathering stuff starts here
    if Command == '/Chop wood':
        if in_Area == 'Forest' or in_Area == 'Grassland' or in_Area == 'Lumberyard':
            if 'Axe' in Equip_Item and Have_Tool_equip == True:
                wood += Tool_bonus // 2
            elif 'Axe' != Equip_Item and Have_Tool_equip:
                print(f'You cannot chop wood with {Equip_Item}, No bonus added.')
                pass
            wood += 1
            wood += Wood_Chopping_skill // 2
            Exp += 5
            Skill_Exp_Wood += 10
            print(f'You have chopped a tree: {1+Wood_Chopping_skill+Tool_bonus}+ wood')#This is wrong
            print('You have earned 5 Exp')
            print('You have earned 10 Skill Exp')
        else:
            print(f'You cannot chop wood in a {in_Area} biome')
            print('Do /Look to see current biome')
    
    if Command == '/Mine iron':
        if in_Area == 'Rocky hills' or in_Area == 'Mountains' or in_Area == 'Mine':
            if 'Pick' in Equip_Item and Have_Tool_equip == True:
                iron += Tool_bonus // 2
            elif 'Pick' != Equip_Item and Have_Tool_equip == True:
                print(f'You cannot mine iron with {Equip_Item}, No bonus added.')
            iron += 1 
            iron += Mining_Skill // 2
            Exp += 5
            Skill_Exp_Iron += 10
            print(f'You have mined iron {Tool_bonus // 2 + Mining_Skill // 2 + 1}+ iron')
            print('You have earned 5 Exp')
            print('You have earned 10 Skill Exp')
        else:
            print(f'You cannot mine iron in a {in_Area} biome')
            print('Do /Look to see current biome')
    #Resource gathering ends here
    

    def inventory(wood, iron, item, tools, Utility):
        Inventory = [f"Wood: {wood} Iron: {iron} items: {item}, Tools: {tools} Utility: {Utility}"]
        print("/".join([str(element) for element in Inventory]))
        print(f"Equipped items: {Equipped_Items}")
        
    if Command == ('/inventory'):
        inventory(wood, iron, item, tools, Utility)
        
    if Command == ('/Player'):
        print(f"Level: {Level}")
        print(f'Exp: {Exp}/100')
        print(f"Gold: {Gold}")
        print(f"Health: {Health}")
        print(f"Defence: {defence}")
        print(f'You are a {Player_class}')
        print(f'Alignment: {Alignment}')
        if Job == 'Mage':
            print(f"Strength: {third_stat} Constitution: {fourth_stat} Intelligence: {main_stat} Agility: {secondary_stat}")
        elif Job == 'Warrior':
            print(f"Strength: {main_stat} Constitution: {fourth_stat} Intelligence: {third_stat} Agility: {secondary_stat}")
        elif Job == 'Rouge':
            print(f"Strength: {secondary_stat} Constitution: {fourth_stat} Intelligence: {third_stat} Agility: {main_stat}")
        #Gonna format the above better later, i have an idea since i already did all this.
        #Strength: Main_Stat etc
    
    def Commands():
        print('----------')
        print('/Chop tree:', 'Get wood')
        print('/Mine iron:', 'Get iron')
        print('/Look:', 'See current area')
        print('/Inventory:', 'See inventory')
        print('/Commands:', 'See all commands')
        print('/Craft:', 'Craft items using wood and iron')
        print('/Player:', 'See current class and stats')
        print('/Recipes:', 'See current recipes unlocked')
        print('/Travel:', 'Travel around and maybe find some loot')
        print('/Skills:', 'See current skill exp and levels')
        print('/Infin Quests:', 'See infinite quest progress ')
        print('----------')
        #more commands needed here probably
    
    if Command == '/Commands' or Command == 'help' or Command == '/help':
        Commands()
    
    if Command == '/Skills':
        print('-------------------------------------------------------------------------------')
        print(f'Wood_Chopping: Exp: {Skill_Exp_Wood}/100 Level: {Wood_Chopping_skill} (Get +Skill / 2 iron)')
        print(f"Mining: Exp: {Skill_Exp_Iron}/100 Level: {Mining_Skill} (Get + Skill / 2 iron)")
        print(f'Fighting skill: Exp: {Skill_Skill_Exp}/100 Level: {Skill_} (Boosts damage by 1 every level)')
        print('-------------------------------------------------------------------------------')
    
    #Gotta make this better, specifically output.
    if Command == ('/Recipes') or Command == '/recipes':
        print(f"{Craft_List}-Cost")
        print(f'{Craft_List_Tools}-Cost')
   
    if Command == '/Travel' or Command == '/travel':
        Encounter_Chance = random.randint(1, 12)
        if Encounter_Chance == 4:
            print('You have encountered a enemy')
            Fighting = True
        elif Encounter_Chance == 5:
            print('You have gotten +5 Gold!')
            Gold += 5
            in_Area = random.choice(Area)
            print(f'You have traveled to a {in_Area}')
        elif Encounter_Chance == 6:
            print('You have found a wandering merchant!')
            WShop = True
        elif Encounter_Chance == 2:
            Someone_InDanger = input('You have found someone in danger! Save them!')
            if Someone_InDanger == 'y':
                print('You have saved them, they reward you with gold')
                print('Gold +6')
                Gold += 6
            if Someone_InDanger == 'n':
                print('You ignore the cries for help and get nothing')
                print('Perhaps another time')
                in_Area = random.choice(Area)
                print(f'You have traveled to a {in_Area}')
        else:  
            print('You traveled for a bit and found nothing') 
            in_Area = random.choice(Area)
            print(f'You have traveled to a {in_Area}')

    #Start of wandering Shop shit
    if WShop == True or Command == '/Shop' or Command == '/shop':
        Enter_Shop = input('Enter shop?')

        if Enter_Shop == 'yes':
            Shop_loop = True
            print('Hello! i am the wandering merchant, please do come browse my wares.')   
        elif Enter_Shop == 'no':
            Shop_loop = False
            WShop = False
    
    while Shop_loop:
        Shopping = input('/Sell, /Leave, /Buy /Talk') #Do want to add a random factor to the shop, like it picks a few from the utility dict everytime you come in
            
        if Shopping == '/Leave' or Shopping == '/leave':
            print('Goodbye then!')
            Shop_loop = False
            Wshop = False
            break
        
        if Shopping == '/Talk' or Shopping == '/talk':
            print('---------------------------')
            print("Wandering Merchant")
            print(f'Likeability: {Likeability_Wandering_Merchant}')
            print('---------------------------')
            Talk_W_Merchant_prompt = input('Speak to the wandering merchant?')
            if Talk_W_Merchant_prompt == 'yes' or Talk_W_Merchant_prompt == 'y':
                Talk_W_Merchant = input('Dialogue options: Say hello, Locked, Locked, Locked')
                if Talk_W_Merchant == 'Say hello':
                    W_Merchant_Like = random.randint(1,5)
                    print('You said hello to the wandering merchant')
                    print('He says hello back then goes back to what he was doing')
                    Likeability_Wandering_Merchant += W_Merchant_Like
                    print(f'Wandering merchant likeability increased by {W_Merchant_Like}')
                    if Likeability_Wandering_Merchant == 50:
                        W_Merchant_Like = random.randint(1,8)
                        print('You said hello to the wandering merchant')
                        print('He greets you with a smile then gets back to work')
                        Likeability_Wandering_Merchant += W_Merchant_Like
                        print(f'Wandering merchant likeability increased by {W_Merchant_Like}')

        if Shopping == '/Sell':
            print('Do /sell(wood/iron/item) to sell something.')
        
        if Shopping == '/Buy':
            print(f'{Utility_items}-Cost')
            Buying = input('Buy what:')
            if Buying in Utility_items and Gold >= Utility_items[Buying]:
                Utility[Buying] = Utility_items[Buying] + random.randint(1, 5)
                Gold -= Utility_items[Buying]
                print(f'You have bought {Buying}')
            elif Buying not in Utility_items:
                print("The is no such item in this shop")
            else:
                print("You do not have enough gold to buy this item.")

            
        
        if Shopping == '/Sellwood':
            HowMuchWood = int(input('Sell how much?'))
            wood -= HowMuchWood
            Gold += HowMuchWood
            print(f"+{HowMuchWood} Gold")
            print('Thank you for your business!')
        elif Shopping == '/Selliron':
            HowMuchIron = int(input('Sell how much?'))
            iron -= HowMuchIron
            Gold += HowMuchIron
            print(f'+{HowMuchIron} Gold')
            print('Thank you for your business!')
        elif Shopping == '/SellItem':
            Item_Sell = input('Sell what item:')
            if Item_Sell in item:
                Increase_Sell_Item = random.randint(1, 8)
                print(f'You have gotten {item[Item_Sell] + Increase_Sell_Item} Gold')
                Gold += item[Item_Sell] + Increase_Sell_Item
                del item[Item_Sell]
                print(f'+{item[Item_Sell] + Increase_Sell_Item} Gold')
                print('Thank you for your business!')
        #End of wandering Shop shit
    if Command == '/Quests':
        print(f'Current Quests: {Random_Quest}')

    if Level >= 5 and Command == '/Village':
        Village_Enter = input('Enter village?')
        if Village_Enter == 'yes':
            Village = True
        elif Village_Enter == 'no':
            print('Okay')
    
    while Village:
        Village_Command = input('/Shop /Blacksmith /Guild /Leave:')

        if Village_Command == '/Leave':
            print('Goodbye')
            Village = False
            break
            
        if Village_Command == '/Shop':
            print('------------------------')
            print('Entering village shop')
            Shop = True
            print('------------------------')
        
        if Village_Command == '/Guild':
            print('-------------')
            print('Entering Guild')
            print('-------------')
            Guild = True
        #Quests need to be rehualed.
        while Guild:
            Guild_Input = input('/Quest, /Talk, /Leave')
            if Guild_Input == "/Quest":
                Random_Quest = random.choice(list(Quests.items()))
                print(Random_Quest)
                Quest_Taken = True
                print('Do /Quests to see current quests')
            if Quest_Taken == True and Guild_Input == '/Quests' or Command == '/Quests':
                print(f'Current quest: {Random_Quest}-Reward')
                Quest = input('You already have a quest, Abandon quest?')
                if Quest == 'y':
                    print('Okay! -5 Gold')
                    Gold -= 5
                    Quest_Taken == False
                elif Quest == 'n':
                    print('Okay!')
            if Random_Quest == 'Defeat Enemy':
                if enemies_health <= 0:
                    print('Quest completed!')
                    Gold += Quests[Random_Quest]
                    print(f"Gold +{Quests[Random_Quest]}")
            if Guild_Input == '/Leave':
                print('Good luck!')
                Guild = False
                break

        #Village shop
        while Shop:
            Shopping = input('/Sell, /Leave, /Buy /Talk:') #Do want to add a random factor to the shop, like it picks a few from the utility dict everytime you come in
            
            if Shopping == '/Leave':
                print('Goodbye then!')
                Shop = False
                break
        
            if Shopping == '/Talk':
                print('---------------------------')
                print("Merchant")
                print(f'Likeability: {Likeability_Village_Merchant}')#Likeablity for merchant
                print('---------------------------')
                Talk_V_Merchant = input('Speak to merchant?')
            #Work in progress


            if Shopping == '/Sell':
                print('Do /sell(wood/iron/item) to sell something.')
        
            if Shopping == '/Buy':
                print(f'{Utility_items}-Cost')
                Buying = input('Buy what:')
                if Buying in Utility_items and Gold >= Utility_items[Buying]:
                    Utility[Buying] = Utility_items[Buying] + random.randint(1, 5)
                    Gold -= Utility_items[Buying]
                    print(f'You have bought {Buying}')
                elif Buying not in Utility_items:
                    print("The is no such item in this shop")
                elif Gold < Buying:
                    print("You do not have enough gold to buy this item.")

            
        
            if Shopping == '/Sellwood':
                HowMuchWood = int(input('Sell how much?'))
                wood -= HowMuchWood
                Gold += HowMuchWood
                print(f"+{HowMuchWood} Gold")
                print('Thank you for your business!')
            elif Shopping == '/Selliron':
                HowMuchIron = int(input('Sell how much?'))
                iron -= HowMuchIron
                Gold += HowMuchIron
                print(f'+{HowMuchIron} Gold')
                print('Thank you for your business!')
            elif Shopping == '/SellItem':
                Item_Sell = input('Sell what item:')
                if Item_Sell in item:
                    Increase_Sell_Item = random.randint(1, 8)
                    print(f'You have gotten {item[Item_Sell] + Increase_Sell_Item} Gold')
                    Gold += item[Item_Sell] + Increase_Sell_Item
                    del item[Item_Sell]
                    print(f'+{item[Item_Sell] + Increase_Sell_Item} Gold')
                    print('Thank you for your business!')
            #Village shop end

        if Village_Command == '/Blacksmith':
            print('----------------------')
            print('Entering Blacksmith')
            print('----------------------')
            Blacksmith = True
        
        while Blacksmith:
            Blacksmith_price_up = random.randint(5, 20)
            print('Blacksmith gives higher rarity chance')
            Blacksmith_Input = input('Welcome! /buy /talk /Leave')
            if Blacksmith_Input == '/Leave':
                Blacksmith = False
                break
            if Blacksmith_Input == '/Buy':
                Crafting = True
                print('What would you like to buy??')
                print(f"Current items: {Craft_List}")
                Crafting_input = input('What would you like to buy?')
    
            if Crafting_input in Craft_List and Crafting and Blacksmith:
                if wood >= Craft_List[Crafting_input] or iron >= Craft_List[Crafting_input] and Gold >= Craft_List[Crafting_input] + Blacksmith_price_up and Crafting:
                    if 'Wooden' in Crafting_input:   
                        Rarity = random.choices(Item_Rarity_list, weights=(31, 70, 35, 7), k=1)
                        if Rarity == ['Common']:
                            Crafting_Damage = random.randint(2, 6)   
                        elif Rarity == ['Uncommon']:
                            Crafting_Damage = random.randint(6, 12)  
                        elif Rarity == ['Rare']:
                            Crafting_Damage = random.randint(12, 24)   
                        elif Rarity == ['Epic']:
                            Crafting_Damage = random.randint(24, 38)
                        item[Crafting_input] = Crafting_Damage + Craft_List[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        wood -= Craft_List[Crafting_input] 
                        Gold -= Craft_List[Crafting_input] + Blacksmith_price_up
                        print(Crafting_Damage)
                        Crafting = False
                    elif 'Iron' in Crafting_input:
                        Rarity = random.choices(Item_Rarity_list, weights=(20, 85, 50, 10), k=1)
                        if Rarity == ['Common']:
                            Crafting_Damage = random.randint(3, 7)   
                        elif Rarity == ['Uncommon']:
                            Crafting_Damage = random.randint(8, 16)  
                        elif Rarity == ['Rare']:
                            Crafting_Damage = random.randint(16, 32)   
                        elif Rarity == ['Epic']:
                            Crafting_Damage = random.randint(32, 48)
                        item[Crafting_input] = Crafting_Damage + Craft_List[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        iron -= Craft_List[Crafting_input] 
                        Gold -= Craft_List[Crafting_input] + Blacksmith_price_up
                        print(Crafting_Damage)
                        Crafting = False
                else:
                    print('You do not have enough for this item')
                    Crafting = False
        
            if Crafting_input in Craft_List_Tools and Crafting and Blacksmith:
                if wood >= Craft_List_Tools[Crafting_input] or iron >= Craft_List_Tools[Crafting_input] and Gold >= Craft_List_Tools[Crafting_input] + Blacksmith_price_up and Crafting:
                    if 'Wood' in Crafting_input:
                        Rarity = random.choices(Item_Rarity_list, weights=(31, 70, 35, 7), k=1)
                        if Rarity == ['Common']:
                            Tool_bonus = random.randint(2, 6)   
                        elif Rarity == ['Uncommon']:
                            Tool_bonus = random.randint(6, 12)  
                        elif Rarity == ['Rare']:
                            Tool_bonus = random.randint(12, 24)   
                        elif Rarity == ['Epic']:
                            Tool_bonus = random.randint(24, 32) 
                        tools[Crafting_input] = Tool_bonus + Craft_List_Tools[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        wood -= Craft_List_Tools[Crafting_input]
                        print(Tool_bonus)
                        Crafting = False
                    elif 'Iron' in Crafting_input:
                        Rarity = random.choices(Item_Rarity_list, weights=(20, 85, 50, 10), k=1)
                        if Rarity == ['Common']:
                            Tool_bonus = random.randint(2, 6)   
                        elif Rarity == ['Uncommon']:
                            Tool_bonus = random.randint(6, 12)  
                        elif Rarity == ['Rare']:
                            Tool_bonus = random.randint(12, 24)   
                        elif Rarity == ['Epic']:
                            Tool_bonus = random.randint(24, 32) 
                        tools[Crafting_input] = Tool_bonus + Craft_List_Tools[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        iron -= Craft_List_Tools[Crafting_input]
                        print(Tool_bonus)
                        Crafting = False
                else:
                    print('You do not have enough for this item')
                    Crafting = False
            
            if Crafting_input in Craft_List_Armor and Crafting and Blacksmith:
                if wood >= Craft_List_Armor[Crafting_input] or iron >= Craft_List_Armor[Crafting_input] and Gold >= Craft_List_Armor[Crafting_input] and Crafting:
                    if 'Wood' in Crafting_input:
                        Rarity = random.choices(Item_Rarity_list, weights=(31, 70, 35, 7), k=1)
                        if Rarity == ['Common']:
                            Armor_bonus = random.randint(2, 6)   
                        elif Rarity == ['Uncommon']:
                            Armor_bonus = random.randint(6, 10)  
                        elif Rarity == ['Rare']:
                            Armor_bonus = random.randint(12, 18)   
                        elif Rarity == ['Epic']:
                            Armor_bonus = random.randint(20, 28) 
                        Armor[Crafting_input] = Armor_bonus + Craft_List_Armor[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        wood -= Craft_List_Armor[Crafting_input]
                        print(Armor_bonus)
                        Crafting = False
                    elif 'Iron' in Crafting_input:
                        Rarity = random.choices(Item_Rarity_list, weights=(20, 85, 50, 10), k=1)
                        if Rarity == ['Common']:
                            Armor_bonus = random.randint(2, 7)   
                        elif Rarity == ['Uncommon']:
                            Armor_bonus = random.randint(6, 11)  
                        elif Rarity == ['Rare']:
                            Armor_bonus = random.randint(12, 20)  
                        elif Rarity == ['Epic']:
                            Armor_bonus = random.randint(22, 30)
                        Armor[Crafting_input] = Armor_bonus + Craft_List_Armor[Crafting_input] // 3
                        print(f'Blacksmith has crafted a {Crafting_input} it is {Rarity}')
                        iron -= Craft_List_Armor[Crafting_input]
                        print(Armor_bonus)
                        Crafting = False
                else:
                    print('You do not have enough for this item')
                    Crafting = False
                #Got to put the rest of the stuff in here, tools and armor, then i can get started on other things

        #Village end
        

    #Start of fighting shit
    if Command == ('/fight') and Health <= 0:
        print(f'You cannot fight, Current health: {Health}')    
    elif Command == '/fight' and Health >= 0:
        print(f'You have encountered a {Choice_type}')
        Fighting = True
        #Making the output clearer is something i want to do.
        #Flavor text maybe? I have some idea's like a list for each job with different lines, and it will print them, yeah that should work
    while Fighting:
        Fight_Command = input('Fight?')   
        if Fight_Command == ('yes'):
                print(f"enemy health: {enemies_health}")
                if Debug_Mode == True:
                    Attack_Dev = input('Physical or Magical or instant kill:')
                else:
                    Attack = input('Physical or Magical:')
                if Attack == 'Magical' or Attack_Dev == 'Magical':
                    if agility > Agility_EN: 
                        print('Player initiative!')
                        Dealt_DamageP = random.randrange(secondary_stat, main_stat) + Skill_ - Defence_En
                        print(f'You have dealt {Dealt_DamageP} damage')
                        enemies_health -= Dealt_DamageP
                        Dealt_DamageE = random.randrange(Intelligence_EN, Strength_EN)
                        print(f'Ememy has dealt {Dealt_DamageE} damage')
                        Health -= Dealt_DamageE
                        print(f'Your health: {Health}')
                        print(f"Enemy health: {enemies_health}")
                    elif Agility_EN > agility:
                        print('Enemy initiative!')
                        Dealt_DamageE = random.randrange(Intelligence_EN, Strength_EN)
                        print(f'Ememy has dealt {Dealt_DamageE} damage')
                        Health -= Dealt_DamageE
                        Dealt_DamageP = random.randrange(secondary_stat, main_stat) + Skill_ - Defence_En // 2
                        print(f'You have dealt {Dealt_DamageP} damage')
                        enemies_health -= Dealt_DamageP
                        print(f'Your health: {Health}')
                        print(f"Enemy health: {enemies_health}")
                    if enemies_health <= 0:
                        print('You have won!')
                        print('You have gained 60 Exp and 10 skill exp')
                        print("You have gained 10 Gold")
                        Exp += 60
                        Gold += 10
                        Skill_Skill_Exp += 10
                        enemies_health = Level_Health_Enemy
                        Fighting = False
                    elif Health <= 0:
                        print('You lose')
                        print('You have lost 15 gold')
                        Gold -= 15
                        enemies_health = Level_Health_Enemy
                        Fighting = False      
                elif Attack == 'Physical':
                    if agility > Agility_EN:
                        Dealt_DamageP = random.randrange(secondary_stat, main_stat) + Skill_ - defence // 2
                        print(f'You have dealt {Dealt_DamageP} damage')
                        enemies_health -= Dealt_DamageP
                        Dealt_DamageE = random.randrange(Intelligence_EN, Strength_EN) - defence // 2
                        print(f'Enemy has dealt {Dealt_DamageE} damage')
                        Health -= Dealt_DamageE
                    elif Agility_EN > agility:
                        Dealt_DamageE = random.randrange(Intelligence_EN, Strength_EN) - defence // 2
                        print(f'Enemy has dealt {Dealt_DamageE} damage')
                        Health -= Dealt_DamageE
                        Dealt_DamageP = random.randrange(secondary_stat, main_stat) + Skill_ - defence // 2
                        print(f'You have dealt {Dealt_DamageP} damage')
                        enemies_health -= Dealt_DamageP
                        print(f'Your health: {Health}')
                        print(f'Enemy health {enemies_health}')
                elif Attack == 'Kill':
                    enemies_health = 0
                    if enemies_health <= 0:
                        print('You have won!')
                        print('You have gained 60 Exp and 10 skill exp')
                        print('You have gained 10 gold')
                        Exp += 60
                        Gold += 10
                        Skill_Skill_Exp += 10
                        enemies_health = Level_Health_Enemy
                        Fighting = False         
                    elif Health <= 0:
                        print('You lose')
                        print('You have lost 15 gold')
                        Gold -= 15
                        enemies_health = Level_Health_Enemy
                        Fighting = False 
            #Fighting ends here
    
    #found bug, fix later, new item replace old item, they don't add they replace.
    #Crafting shit
    if Command == ('/Craft'):
        Crafting = True
        print('What would you like to craft?')
        print("if you don't know check /Recipes")
        Crafting_input = input('What would you like to craft?')
    
    if Crafting_input in Craft_List and Crafting:
        if wood >= Craft_List[Crafting_input] or iron >= Craft_List[Crafting_input] and Crafting:
            if 'Wooden' in Crafting_input:   
                Rarity = random.choices(Item_Rarity_list, weights=(80, 45, 30, 5), k=1)
                if Rarity == ['Common']:
                    Crafting_Damage = random.randint(2, 6)   
                elif Rarity == ['Uncommon']:
                    Crafting_Damage = random.randint(6, 12)  
                elif Rarity == ['Rare']:
                    Crafting_Damage = random.randint(12, 24)   
                elif Rarity == ['Epic']:
                    Crafting_Damage = random.randint(24, 38)
                item[Crafting_input] = Crafting_Damage + Craft_List[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                wood -= Craft_List[Crafting_input]
                print(Crafting_Damage)
                Crafting = False
            elif 'Iron' in Crafting_input:
                Rarity = random.choices(Item_Rarity_list, weights=(45, 80, 30, 8), k=1)
                if Rarity == ['Common']:
                    Crafting_Damage = random.randint(3, 7)   
                elif Rarity == ['Uncommon']:
                    Crafting_Damage = random.randint(8, 16)  
                elif Rarity == ['Rare']:
                    Crafting_Damage = random.randint(16, 32)   
                elif Rarity == ['Epic']:
                    Crafting_Damage = random.randint(32, 48)
                item[Crafting_input] = Crafting_Damage + Craft_List[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                iron -= Craft_List[Crafting_input]
                print(Crafting_Damage)
                Crafting = False
        else:
            print('You cannot craft this item')
            Crafting = False


    if Crafting_input in Craft_List_Tools and Crafting:
        if wood >= Craft_List_Tools[Crafting_input] or iron >= Craft_List_Tools[Crafting_input] and Crafting:
            if 'Wood' in Crafting_input:
                Rarity = random.choices(Item_Rarity_list, weights=(80, 45, 30, 5), k=1)
                if Rarity == ['Common']:
                    Tool_bonus = random.randint(2, 6)   
                elif Rarity == ['Uncommon']:
                    Tool_bonus = random.randint(6, 12)  
                elif Rarity == ['Rare']:
                    Tool_bonus = random.randint(12, 24)   
                elif Rarity == ['Epic']:
                    Tool_bonus = random.randint(24, 32) 
                tools[Crafting_input] = Tool_bonus + Craft_List_Tools[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                wood -= Craft_List_Tools[Crafting_input]
                print(Tool_bonus)
                Crafting = False
            elif 'Iron' in Crafting_input:
                Rarity = random.choices(Item_Rarity_list, weights=(45, 80, 30, 8), k=1)
                if Rarity == ['Common']:
                    Tool_bonus = random.randint(2, 6)   
                elif Rarity == ['Uncommon']:
                    Tool_bonus = random.randint(6, 12)  
                elif Rarity == ['Rare']:
                    Tool_bonus = random.randint(12, 24)   
                elif Rarity == ['Epic']:
                    Tool_bonus = random.randint(24, 32) 
                tools[Crafting_input] = Tool_bonus + Craft_List_Tools[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                iron -= Craft_List_Tools[Crafting_input]
                print(Tool_bonus)
                Crafting = False
        else:
            print('You cannot craft this tool')
            Crafting = False

    if Crafting_input in Craft_List_Armor and Crafting:
        if wood >= Craft_List_Armor[Crafting_input] or iron >= Craft_List_Armor[Crafting_input] and Crafting:
            if 'Wood' in Crafting_input:
                Rarity = random.choices(Item_Rarity_list, weights=(80, 45, 30, 5), k=1)
                if Rarity == ['Common']:
                    Armor_bonus = random.randint(2, 6)   
                elif Rarity == ['Uncommon']:
                    Armor_bonus = random.randint(6, 10)  
                elif Rarity == ['Rare']:
                    Armor_bonus = random.randint(12, 18)   
                elif Rarity == ['Epic']:
                    Armor_bonus = random.randint(20, 28) 
                Armor[Crafting_input] = Armor_bonus + Craft_List_Armor[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                wood -= Craft_List_Armor[Crafting_input]
                print(Armor_bonus)
                Crafting = False
            elif 'Iron' in Crafting_input:
                Rarity = random.choices(Item_Rarity_list, weights=(45, 80, 30, 8), k=1)
                if Rarity == ['Common']:
                    Armor_bonus = random.randint(2, 7)   
                elif Rarity == ['Uncommon']:
                    Armor_bonus = random.randint(6, 11)  
                elif Rarity == ['Rare']:
                    Armor_bonus = random.randint(12, 20)  
                elif Rarity == ['Epic']:
                    Armor_bonus = random.randint(22, 30)
                Armor[Crafting_input] = Armor_bonus + Craft_List_Armor[Crafting_input] // 3
                print(f'You have crafted a {Crafting_input} it is {Rarity}')
                iron -= Craft_List_Armor[Crafting_input]
                print(Armor_bonus)
                Crafting = False
        else:
            print('You cannot craft this tool')
            Crafting = False

    if Command == '/equip':
            Equip_Item = input('Equip what:')
            Equip = True 

        
    if Equip_Item in item and Equip:
        Equipped_Items[Equip_Item] = item[Equip_Item]
        del item[Equip_Item]
        print('You have equipped', Equip_Item)
        main_stat += Equipped_Items[Equip_Item]
        print(f'Your main stat had been boosted by {Equipped_Items[Equip_Item]}')
        print(Equipped_Items)
        Have_Item_equip = True
        Equip = False
    elif Equip_Item in tools and Equip:
            Equipped_Items[Equip_Item] = tools[Equip_Item]
            del tools[Equip_Item]
            Tool_bonus = Equipped_Items[Equip_Item]
            print(f'You have equipped {Equip_Item}')
            Have_Tool_equip = True 
            Equip = False
    elif Equip_Item in Armor and Equip:
        Equipped_Items[Equip_Item] = Armor[Equip_Item]
        del Armor[Equip_Item]
        Armor_bonus += Armor[Equip_Item]
        defence += Armor_bonus
        print(f'You have equipped {Equip_Item}')
        Have_Armor_equip = True
        Equip = False
  
    if Command == '/Unequip':
        Unequip_What = input('Unequip what:')
    #Alright, so equipping another item, gets rid of it. already have a solution i think, just gotta do it, all i gotta do is, make the item being replaced be put back in to the dict they are in and boom ez
    if Unequip_What == Equip_Item and Have_Item_equip:
        item[Equip_Item] = Equipped_Items[Equip_Item]
        del Equipped_Items[Equip_Item]
        main_stat -= item[Equip_Item]
        Have_Item_equip = False 
        print(f"You have have unequipped your {Equip_Item}")
    elif Unequip_What == Equip_Item and Have_Tool_equip:
        tools[Equip_Item] = Equipped_Items[Equip_Item]
        del Equipped_Items[Equip_Item]
        print(f'You have unequiped your {Equip_Item}')
        Tool_bonus -= tools[Equip_Item]
        Have_Tool_equip = False
    elif Unequip_What == Equip_Item and Have_Armor_equip:
        Armor[Equip_Item] = Equipped_Items[Equip_Item]
        del Equipped_Items[Equip_Item]
        print(f'You have unequiped your {Equip_Item}')
        Armor_bonus -= Armor[Equip_Item]
        defence -= Armor[Equip_Item]
        Have_Armor_equip = False

    
    if Command == '/exit':
        break
        
        #If i use .lower for my input statements that should make them case insensitive. 
        #Should really add this sometime soon, preferably when i have fighting working, or when crafting and items are finished.
        #So much for that i guess, for sure when i'm done with whatever it is im doing.
        #Lol i finished whatever it was i was doing and i still haven't done it, maybe when i finish with debugs, and combat is polished and checked and npcs are finished.
        #Basically it will happen maybe, when the game is almost finished
        #Ha a week+ later and still haven't got to it. Honestly i could, but im lazy
        #Months later, added to git and still haven't gotten to it. poor game.
    continue
