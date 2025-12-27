import items, units, world, render
      
def main():
    day = 0
    gameloop = False   
    wrld = world.World(world.WorldLevel.DESOLATE, 1000, [], {})
    wrld.buildings.update(world.Building.load_buildings())

    gameloop = render.main_menu(gameloop)

    while gameloop:
        print("-----------------------")
        print("BUILDINGS:")

        for b in wrld.buildings:
            print(wrld.buildings[b]["name"], f"{wrld.buildings[b]["occupants"]}/{wrld.buildings[b]["maxoccupants"]}")
            print(wrld.buildings[b]["description"])

        usr = input()

        if usr == "summon":
            unit = units.Unit.summon_unit()
            wrld.buildings["building_plaza"]["occupants"] = unit
            wrld.units.append(unit.identity.name)
            print(f"SUMMONED {unit.identity.backstory["name"]} {unit.identity.name}, a {unit.meta.tier} star unit!")

        if usr == "q":
            break
    
        



main()