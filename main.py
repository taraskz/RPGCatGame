from game_map import export_map, read_map

export_map()
#read_map()

rooms = {
    "Outscirts of Catville": "You are in the starting area of the game, \
here you can get your first cat companion",
}

def menu():
    '''This function acts as the main menu where the player gets to choose 
    what action to do whenever they want to
    '''
    