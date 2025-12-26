import items, units, world, render

                                                                                                                                                                                    
def main():
    wrld = world.World(world.WorldLevel.DESOLATE, 1000, {}, {}, {})
    wrld.units["testing"] = units.Unit.summon_unit()
    render.main_menu()
    print(wrld.units["testing"].display_unit_info())


main()