"""
Replace the contents of this module docstring with your own details
Name:Aaishwinder Kaur
Date started: 22-4-2020
GitHub URL:https://github.com/jc725951/assignment_1.git
"""


from operator import itemgetter


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


def sorting_songs(songs):
    """"This function will sort the list of songs"""
    songs.sort(key=itemgetter(1, 0))            # sort songs according to index 1 and 0
    return songs


def formatting_list_of_songs(songs):
    """ This function will print the formatted list of songs"""
    for i in range(len(songs)):
        if 'u' in songs[i]:
            print("{}.{:>3s} \t {} \t - {} \t({})".format(i, "*", songs[i][0], songs[i][1], songs[i][2],  songs[i][3]))
        else:
            print("{}.{:>3s} \t {} \t - {} \t({})".format(i, " ", songs[i][0], songs[i][1], songs[i][2],  songs[i][3]))


def get_formatted_list(loading_csv_file):
    """" This function will pass the csv file through other functions to give a complete songs list"""
    sorted_list_of_songs = sorting_songs(loading_csv_file)
    songs_list = formatting_list_of_songs(sorted_list_of_songs)
    return songs_list


def calculating_learned_songs():
    """ calculating_learned_songs function will calculate the all learned songs in csv file"""
    import csv
    list_of_songs = list(csv.reader(open("songs.csv")))
    song = 0
    for i in list_of_songs:
        if i[3] == "l":
            song += 1
    return song


def calculating_unlearned_songs():
    """ calculating_unlearned_songs function will calculate the all unlearned songs in csv file"""
    import csv
    list_of_songs = list(csv.reader(open("songs.csv")))
    song = 0
    for i in list_of_songs:
        if i[3] == "u":
            song += 1
    return song



def main():
    """ Main function will take user input and then according to the input take action like L - to list all songs from
     csv file, A - Add new song into csv file, C - to complete a song and Q-  to quit"""
    print("Songs to learn 1.0 - by Aaishwinder Kaur")
    learned_songs = calculating_learned_songs()  # give all learned songs
    unlearned_songs = calculating_unlearned_songs()  # give all unlearned songs
    total_songs = learned_songs + unlearned_songs  # calculate total number of songs
    print("{} songs loaded".format(total_songs))  # prints total songs
    choice = displaying_menu_choices()  # display menu
    while choice != "Q":
        if choice == "L":  # display list of songs
            get_formatted_list(loading_csv_file())
            print("{} songs learned, {} songs still to learn".format(learned_songs, unlearned_songs))
            choice = displaying_menu_choices()  # display menu
        elif choice == "A":
            choice = displaying_menu_choices()  # display menu
        elif choice == "C":
            choice = displaying_menu_choices()  # display menu
    print("{} songs saved to songs.csv".format(total_songs))
    print("Have a nice day :")  # end message on giving input q


main()
