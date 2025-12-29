import items, units, world, render


def game():
    day = 0
    gameloop = True

    wrld = world.World(0, 1000, [], {})

    wrld.buildings.update(world.Building.load_buildings())
    render.main_menu()

    while gameloop:

        for i in wrld.units:
            for place in wrld.buildings:
                if i.meta.assigned_building == place:
                    wrld.buildings[place]["occupants"] += 1

        print("-----------------------")
        print(f"WORLD LEVEL: {wrld.level}")
        print(f"COINS: {wrld.coins}")

        print("BUILDINGS:")

        for b in wrld.buildings:
            print(wrld.buildings[b]["name"], f"{wrld.buildings[b]["occupants"]}/{wrld.buildings[b]["maxoccupants"]}")
            print(wrld.buildings[b]["description"])
        
        print("-----------------------")

        usr = input(">")
        print("\033[F\033[K", end="") 

        if usr == "summon":
            summon = units.Unit.summon_unit(0)
            for place in wrld.buildings:
                if place == "building_plaza":
                    summon.meta.assigned_building = place
                    wrld.buildings[place]["occupants"] = 0
            print(f"You have summoned {summon.identity.backstory["name"]} {summon.identity.name}, a tier {summon.meta.tier} unit!")
            wrld.units.append(summon)

        if usr == "units":
            if not wrld.units:
                print("You have no units!")
            else:
                print(f"Unit List:")
                for unit in wrld.units:
                    print(f"(Tier {unit.meta.tier}) {unit.identity.backstory["name"]} {unit.identity.name}")
                unit_input = input("Would you like to view a specific unit in detail? (Type unit name or q to quit) ")
                if unit_input == "q":
                    pass
                else:
                    for u in wrld.units:
                        if unit_input == u.identity.name:
                            print(u.display_unit_info())

        if usr == "q":
            break