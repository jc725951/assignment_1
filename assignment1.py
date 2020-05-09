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


def loading_csv_file():
    """ This function will load the csv file into program """
    open_file = open("songs.csv", "r")              # load csv file
    created_list = open_file.readlines()            # read all lines in the form of paragraph
    songs = []                                      # empty songs list
    for line in created_list:
        split_line = line.split(",")                # split paragraph from ','
        split_line[2] = int(split_line[2])          # change string of year into integer
        split_line[3] = split_line[3][0]            # remove n from 3rd index
        songs.append(split_line)                    # append all songs to the empty songs list
        open_file.close()                           # close the file
    return songs


def main():
    """ Main function will take user input and then according to the input take action like L - to list all songs from
     csv file, A - Add new song into csv file, C - to complete a song and Q-  to quit"""
    print("Songs to learn 1.0 - by Aaishwinder Kaur")
    choice = displaying_menu_choices()                           # display menu
    while choice != "Q":
        if choice == "L":                                   # display list of songs
            choice = displaying_menu_choices()                  # display menu
        elif choice == "A":
            choice = displaying_menu_choices()                   # display menu
        elif choice == "C":
            choice = displaying_menu_choices()                  # display menu
    print("Have a nice day :")           # end message on giving input q