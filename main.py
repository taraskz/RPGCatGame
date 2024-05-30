##############################################################################
# Title: RPG_Cat_Game
# Class: CS 30
# Date: May 30, 2024
# Coders: Taras K and Trey Z
# Version: 001
##############################################################################
'''This program is a text based game where the player gets to explore and 
fight enemies using cats, the goal is to save the catverse by defeating the 
main villian
'''
##############################################################################
#---imports and global variables----------------------------------------------
from game_map import export_map, read_map


rooms = {
    "Outscirts of Catville": "You are in the starting area of the game, \
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


#---functions-----------------------------------------------------------------
def menu():
    '''This function acts as the main menu where the player gets to choose 
    what action to do whenever they want to
    '''


#---main----------------------------------------------------------------------
export_map()
#read_map()