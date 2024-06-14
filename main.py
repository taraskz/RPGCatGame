##############################################################################
# Title: RPG_Cat_Game
# Class: CS 30
# Date: May 30, 2024
# Coders: Taras K and Trey Z
# Version: 004
##############################################################################
'''This program is a text based game where the player gets to explore and 
fight enemies using cats, the goal is to save the catverse by defeating the 
main villian
'''
##############################################################################
#---imports and global variables----------------------------------------------
from cat import Cat
from enemies import Enemy
from game_map import export_map, read_map
from player import Player


player = Player(name = "Cat Master")


# starting cats
available_cats = {
    "Sphynx": Cat(name = "Sphynx", damage = 10),
    "Ragdoll": Cat(name = "Ragdoll", damage = 10),
    "B": Cat(name = "B", damage = 10000)
}


# cats in the shop
shop_cats = {
    "Persian": {"cat": Cat(name = "Persian", damage = 20), "\
cost": 40},
    "Bombay": {"cat": Cat(name = "Bombay", damage = 35), "\
cost": 80},
    "Siberian": {"cat": Cat(name = "Siberian", damage = 50), "\
cost": 110},
    "Munchkin": {"cat": Cat(name = "Munchkin", damage = 80), "\
cost": 170},
    "Siamese": {"cat": Cat(name = "Siamese", damage = 100), "\
cost": 330} 
}


# enemies and their stats
enemy_definitions = {
    "Stray Cat": Enemy("Stray Cat", 20, 5, 20), #Outskirts of Catville
    "Goon": Enemy("Goon", 20, 10, 20), #Mount Caterest
    "Wild Kitty": Enemy("Wild Kitty", 40, 15, 30), #Catlands
    "City Beast": Enemy("City Beast", 50, 15, 40), #Catville City
    "Desert Lynx": Enemy("Desert Lynx", 100, 30, 60), #Catpagne Beach
    "Lake Panther": Enemy("Lake Panther", 85, 25, 60), #Lake MacCatzie
    "Sir_Barksalot": Enemy("Sir Barksalot", 120, 35, 100), #Catana Desert
    "Clawmancer_Felisar": Enemy("Clawmancer Felisar", 200, 40, 250) #Cat Ruins
}


# cats
player_cats = []


# rooms/places of the game
rooms = {
    "Outskirts of Catville": {"description": "You are in the starting area \
of the game, here you can get your first cat companion if you manage to \
defeat an enemy", 
                              "enemy": "Stray Cat"},
    "Catlands": {"description": "You are in the lands of cats, here is \
where most non combat cats live in peace", 
                 "enemy": "Wild Kitty"},
    "Catville City": {"description": "You are in the central city, it's been \
taken over by Clawmancer Felisar's goons, be careful to not get spotted",
                     "enemy": "City Beast"},
    "Lake MacCatzie": {"description": "You are in front of a beautiful lake, \
there are catfish everywhere", 
                       "enemy": "Lake Panther"},
    "Mount Caterest": {"description": "In front of you is the biggest \
mountain in the catverse, no one has ever been able to climb it\
",
                       "enemy": "Goon"},
    "Catpagne Beach": {"description": "You are at a warm beach, no enemies \
managed to get here yet, you are safe for now...",
                       "enemy": "Desert Lynx"},
    "Catana Desert": {"description": "Now you are in a desert, its hot \
and humid in here staying for too long would be bad",
                      "enemy": "Sir_Barksalot"},
    "Cat-Street Mall": {"description": "You have made it to the shopping \
center, here you can buy anything your hearts desires",
                        "enemy": None},
    "Cat Ruins": {"description": "You have finally made to to the lair of \
Clawmancer Felisar hopefully you are strong enough to defeat him this time. \
GOOD LUCK!!!",
                  "enemy": "Clawmancer_Felisar"},
}

# coordinates of where the room/place is
room_location = {
    "Outskirts of Catville": (0,0), "Catlands": (1,0), "Lake \
MacCatzie": (2,0), "Mount Caterest": (0,-1), "Catville City": (1,-1),
    "Catpagne Beach": (2,-1), "Cat-Street Mall": (0,-2), "Catana Desert\
": (1,-2), "Cat Ruins": (2,-2)
}


directions = {
    "north": (0,1), # up
    "south": (0,-1), # down
    "west": (-1,0), # left
    "east": (1,0) # right
}


current_location = "Catana Desert" # starting location


defeated_enemies = set() # enemy that is defeated moves here


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
        check_for_enemies()
    else:
        print("\nUnfortunately you can't leave the land of cats try a \
different direction, unless you want to end the game :(")


def movement_menu():
    '''This function is a sub menu that handles the movement
    of the user based on their input
    '''
    while True:
        print("\nHere are your movement options or type 'back' \
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


def battle(enemy):
    '''This function activates when there are enemies in the area the user
    is in and they are forced to fight them, if they lose the game ends if
    they win they get a reward
    '''
    while player.is_alive() and enemy.is_alive():
        print(f"Enemy : {enemy.name} (Health: {enemy.health}, Damage: \
{enemy.damage})\n")
        action = input("What do you want to do? input 'attack' or 'run', \
: ").lower()
        if action == 'attack':
            if player_cats:
                print("Choose a cat to attack with:")
                # makes the user input numbers instead of printing cat name
                for i, cat in enumerate(player_cats):
                    print(f"{i + 1}. {cat.name} (Damage: {cat.damage})")
                try:
                    cat_choice = int(input("Choose: ")) - 1
                    if 0 <= cat_choice < len(player_cats):
                        chosen_cat = player_cats[cat_choice]
                        chosen_cat.attack(enemy)
                        print(f"\n{chosen_cat.name} attacked {enemy.name} \
for {chosen_cat.damage} damage!")
                    else:
                        print("Invalid choice, please try again!!!\n")
                        continue
                except:
                    print("Invalid choice\n")
                    continue
        elif action == 'run':
            print("You ran away, coward :(")
            return
        else:
            print("Invalid input please try again!!!\n")
            continue
        if enemy.is_alive():
            print(f"\n{enemy.name} attacks you for {enemy.damage} damage!")
            enemy.attack(player)
            print(f"Your Health: {player.health}")
        else:
            print(f"You beat {enemy.name}")
            player.coins += enemy.coins
            print(f"You gained {enemy.coins} coins.")
            player.health = 150 # resets player health
            #defeated_enemies.add(enemy.name)
            if enemy.name == "Clawmancer Felisar":
                print("\nCongratulations you have defeated Clawmancer \
Felisar and saved the land of cats from his evil gang of cats that \
terrorized the residents for years. The residents throw you a party \
as a thanks for everything you've done.")
                game_exit()
            else: 
                defeated_enemies.add(enemy.name)
            return
        if not player.is_alive():
            print("You have been defeated. Try again")
            game_exit()


def check_for_enemies():
    '''This function checks if there is enemies in the current location
    and intiates the battle function
    '''
    enemy_name = rooms[current_location]["enemy"]
    if enemy_name and enemy_name not in defeated_enemies:
        print("\nAn enemy is here! get ready to fight")
        battle(enemy_definitions[enemy_name])


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
            print("\n***Welcome player, to the lands of cats and prosperity\
***")
            print("Here is an explanation as to what is happening in the \
world and your mission.\n")
            print("***Long ago in the land of cats... Everyone lived \
peacefully amongst each other, enjoying nature and each others company. \
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
quest. Good Luck!!! <3\n")
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
        print("\nChoose your starting cat!!!")
        print("Options: ")
        for cat_name, cat in available_cats.items():
            print(f"- {cat_name}: {cat}")
        cat_choice = input("Choose: ").capitalize()
        if cat_choice in available_cats:
            chosen_cat = available_cats[cat_choice]
            player_cats.append(chosen_cat)
            print(f"\nYou chose {chosen_cat.name} as your first cat")
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
        print(f"\nYou are currently in {current_location}")
        print("Type 'options' to see your options")
        choice = input("Choose your action: ").lower()
        if choice == 'options':
            print("\nType 'quit' to quit the game")
            print("Type 'move' to move around the map")
            print("Type 'map' to view the map and description of your \
            current location")
            print("Type 'money' to see how much money you have")
            print("Type 'shop' to access the shop when you get to Cat-Street \
Mall\n")
        elif choice == 'quit':
            game_exit()
        elif choice == 'move':
            movement_menu()
        elif choice == 'map':
            print("Here you go <3\n")
            read_map()
            print(f"{rooms[current_location]['description']}\n")
        elif choice == 'money':
            print(f"You have: {player.coins} coins.")
        elif choice == 'shop':
            if current_location == "Cat-Street Mall":
                shop()
            else:
                print("You need to go to Cat-Street Mall!!!")
        else:
            print("Invalid input please type in your action properly!<3")


def shop():
    '''This function is a shop for the user to buy cats when they get to
    Cat-Street mall'''
    while True:
        print("\nWelcome to the Shop! Here you can buy cats to fight.\n")
        print(f"You have: {player.coins} coins.")
        for cat_name, cat_info in shop_cats.items():
            cat = cat_info["cat"]
            cost = cat_info["cost"]
            print(f"- {cat_name}: {cat} (Cost: {cost} coins.)")
        cat_choice = input("\nWhich cat would you like to buy? ***Type \
'back' to exit the shop***").capitalize()
        if cat_choice == 'Back':
            return
        elif cat_choice in shop_cats:
            chosen_cat_info = shop_cats[cat_choice]
            chosen_cat = chosen_cat_info["cat"]
            cost = chosen_cat_info["cost"]
            if any(cat.name == chosen_cat.name for cat in player_cats):
                print("\nYou already own this cat, can't buy it again.")
            elif player.coins >= cost:
                player.coins -= cost
                player_cats.append(chosen_cat)
                print(f"\nYou bought {chosen_cat.name} for {cost} coins.")
                print(f"Remaining coins: {player.coins}")
            else:
                print("Unfortunately you don't have enough coins to buy this \
cat")
        else:
            print("Invalid choice, please type the name of the cat correctly \
<3")


def game_exit():
    '''This function leaves the game for the user when they want to quit'''
    print("Thanks for playing, hope you had a great time <3")
    exit() # ends game


def game():
    '''This function calls other function and acts as a main game'''
    export_map() # creates the map
    intro() # runs intro
    menu() # runs menu


#---main----------------------------------------------------------------------
game() # runs game