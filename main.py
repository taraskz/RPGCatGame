##############################################################################
# Title: RPG_Cat_Game
# Class: CS 30
# Date: May 30, 2024
# Coders: Taras K and Trey Z
# Version: 003
##############################################################################
'''This program is a text based game where the player gets to explore and 
fight enemies using cats, the goal is to save the catverse by defeating the 
main villian
'''
##############################################################################
#---imports and global variables----------------------------------------------
from game_map import export_map, read_map
from player import Player
from inventory import Inventory
from cat import Cat


player = Player(name = "Cat Master")
inventory = Inventory()


available_cats = {
    "Sphynx": Cat(name = "Sphynx", damage = 10, health = 50),
    "Ragdoll": Cat(name = "Ragdoll", damage = 15, health = 40)
    
}


player_cats = []


rooms = {
    "Outskirts of Catville": "You are in the starting area of the game, \
here you can get your first cat companion if you manage to defeat an enemy",
    "Catlands": "You are in the lands of cats, here is where most non \
combat cats live in peace",
    "Catville City": "You are in the central city, it's been taken over \
by Clawmancer Felisar's goons, be careful to not get spotted",
    "Lake MacCatzie": "You are in front of a beatiful lake, there are \
catfish everywhere",
    "Mount Caterest": "In front of you is the biggest mountain in the \
catverse, no one has every been able to climb it",
    "Catpagne Beach": "You are at a warm beach, no enemies managed to \
get here yet, you are safe for now",
    "Catana Desert": "Now you are in a desert, its hot and humid in here \
staying for too long would be bad",
    "Cat-Street Mall": "You have made it to the shopping center, here \
you can buy anything your hearts desires",
    "Cat Ruins": "You have finally made to to the lair of Clawmancer Felisar \
hopefully you are strong enough to defeat him this time. GOOD LUCK!!!"
}


room_location = {
    "Outskirts of Catville": (0,0), "Catlands": (1,0), "Lake \
MacCatzie": (2,0), "Mount Caterest": (0,-1), "Catville City": (1,-1),
    "Catpagne Beach": (2,-1), "Cat-Street Mall": (0,-2), "Catana Desert\
": (1,-2), "Cat Ruins": (2,-2)
}


directions = {
    "north": (0,1),
    "south": (0,-1),
    "west": (-1,0),
    "east": (1,0)
}


current_location = "Outskirts of Catville"

#---functions-----------------------------------------------------------------
def movement(direction):
    '''This function handles the movement input of the user in the menu'''
    global current_location
    new_x = room_location[current_location][0] + directions[direction][0]
    new_y = room_location[current_location][1] + directions[direction][1]
    new_location = (new_x, new_y)
    # conditional branching for user input
    if new_location in room_location.values():
        current_location = next(room for room, index in room_location.items()
                               if index == new_location)
    else:
        print("Unfortunately you can't leave the land of cats try a different \
direction, unless you want to end the game :(")


def movement_menu():
    '''This function is a sub menu that handles the movement
    of the user based on their input
    '''
    while True:
        print("Here are your movement options or type 'back' \
if you want to go back to the menu.")
        for direction in directions:
            print(f"- {direction}")
        direction = input("Choose: ")
        if direction in directions:
            movement(direction)
            return
        elif direction == 'back':
            return
        else: 
            print("Invalid direction please type it in properly!<3")


def introduction():
    '''This function prints out the introduction of the game so the user
    understands how to play. They can skip it if they want to in the menu 
    funtion
    '''
    print("You can quit by typing 'quit'!!!")
    print("Welcome human do you want to hear the introduction? 'yes' or 'no'")
    while True:
        int_choice = input("Choose: ")
        if int_choice == 'yes':
            print("***Welcome player, to the lands of cats and prosperity\
***")
            print("Here is an explanation as to what is happening in the \
world and your mission is to save the world.\n")
            print("***Long ago in the land of cats... Everyone lived \
peacefully amongst each other, enjoying nature and each others company.\
Both humans and cats found a way to coexist.\n")
            print("However an evil person by the name of Clawmancer Felisar \
came from the forgotten place called the cat ruins. Him and his gang of evil \
cats and humans are trying to take over the land of cats in order to control \
everyone.")
            print("No one really knows why he's doing this but many \
speculate it's because of his childhood. But thats besides the point.\n")
            print("***We have summoned you here from another world in hopes \
that you can defeat his army and save the lands of cats.")
            print("Go ahead and explore the many places in this wonderful \
land while trying to find good cat companions that will help you in your \
quest. Good Luck!!! <3")
            return
        elif int_choice == 'no':
            return
        elif int_choice == 'quit':
            game_exit()
        else:
            print("Please type the right input, thanks. <3")


def intro():
    '''This function is the intro to the game to get the user started'''
    introduction()
    while True:
        print("Choose your starting cat!!!")
        print("Options: ")
        for cat_name, cat in available_cats.items():
            print(f"- {cat_name}: {cat}")
        cat_choice = input("Choose: ").capitalize()
        if cat_choice in available_cats:
            chosen_cat = available_cats[cat_choice]
            player_cats.append(chosen_cat)
            print(f"You chose {chosen_cat.name} as your first cat")
            return
        elif cat_choice == 'quit':
            game_exit()
        else:
            print("Invalid choice, please choose a valid cat name! <3")


def menu():
    '''This function acts as the main menu where the player gets to choose 
    what action to do whenever they want to
    '''
    while True:
        print(f"You are currently in {current_location}")
        choice = input("Choose your action: ").lower()
        if choice == 'options':
            print("Type 'quit' to quit the game")
            print("Type 'move' to move around the map")
            print("Type 'map' to view the map")
        elif choice == 'quit':
            game_exit()
        elif choice == 'move':
            movement_menu()
        elif choice == 'map':
            print("Here you go <3")
            read_map()
        elif choice == 'inventory':
            inventory.view_inventory()
        else:
            print("Invalid input please type in your action properly!<3")


def game_exit():
    '''This function leaves the game for the user when they want to quit'''
    print("Thanks for player, hope you had a great time <3")
    exit()

kitties = {"Maine":20}

def store():
    os.system('clear')
    print("Welcome to the shop!")
    print("\n What would you like to buy?\n")
    print("1. Maine")
    print(" ")
    option = raw_input(' ')

    if option in kitties:
        if 

def game():
    '''This function calls other function and acts as a main game'''
    export_map()
    intro()
    menu()


#---main----------------------------------------------------------------------
game()
#read_map()