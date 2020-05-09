"""
Replace the contents of this module docstring with your own details
Name:Aaishwinder Kaur
Date started: 22-4-2020
GitHub URL:https://github.com/jc725951/assignment_1.git
"""


def displaying_menu_choices():
    """" This function asks user to choose from menu choices that are L - to list all songs from csv file, A - Add new
     song into csv file, C - to complete a song and Q-  to quit """
    print("Menu:")
    print("L - List songs \nA - Add new song \nC - Complete a song \nQ- Quit")
    choices_in_menu = ["L", "A", "C", "Q"]
    user_choice = input(">>> ").upper()
    while user_choice not in choices_in_menu:
        print("Invalid Menu Choice")
        print("Please choose again from menu")
        user_choice = input(">>> ").upper()
    return user_choice
