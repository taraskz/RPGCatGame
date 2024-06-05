from tabulate import tabulate


# name of each of the locations on the map converted into a tile
tile = ["Outskirts of Catville", "Catville City", "Catlands",
    "Mount Caterest", "Lake MacCatzie", "Catanna Desert",
    "Catpagne Beach", "Cat-Street Mall", "Cat Ruins"
       ]


# location of the tiles on the map
tiles = [
    [tile[0],tile[2],tile[4]],
    [tile[3], tile[1], tile[6]],
    [tile[7], tile[5], tile[8]]
    ]


# external map file name
mapfile = 'map.txt'


def export_map():
    '''This function creates the map for our game with the tabulate module'''
    try:
        with open(mapfile, 'w') as file:
            file.write(tabulate(tiles, tablefmt = 'heavy_grid'))
    except:
        print("Something went wrong")


def read_map():
    '''This function prints the map when called'''
    try:
        with open(mapfile, 'r') as file:
            print(file.read())
    except:
        print("Something went wrong")
