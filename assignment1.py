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


def adding_new_song_to_list():
    """ This function will ask user to give inputs for title, artist and year of song and then add it to the csv file
    as unlearned song"""
    title = input("Please enter the title of song : ").capitalize()        # take input for title
    while not title.isalpha():                                          # checks error
        print("Invalid Input. Please enter valid value.")
        title = input("Please enter the title of song :").capitalize()     # take input again after checking error
    artist = input("Please enter the artist of song :").capitalize()        # take input for artist
    while not artist.isalpha():                                                # checks error
        print("Invalid Input.  Please enter valid value.")
        artist = input("Please enter the artist of song :").capitalize()   # take input again after checking error
    year = input("Please enter the year of song :").capitalize()            # take input for year
    while not year.isdigit() or int(year) <= 0:                               # checks error
        print("Invalid Input.  Please enter valid value.")
        year = input("Please enter the year for song :").capitalize()         # take input again after checking error
    print("{} by {} ({}) added to song list".format(title, artist, year))
    file1 = open("songs.csv", "a")                                               # append song
    file1.writelines("{},{},{},u\n".format(title, artist, year))
    file1.close()


def mark_unlearn_to_learn():
    """ Marking unlearned song to learned"""
    x = 0
    count = 0
    import csv
    songs = list(csv.reader(open("songs.csv")))
    for i in songs:
        if songs[x][3] == "u":
            count = count+1
        x = x+1
    if count == 0:
        print("No more songs to learn!")
    else:
        song = input("Enter the number of song to mark as learned :")
        song_number = int(song)
        if song_number+1 > len(songs) or song_number < 0:
            print("Invalid Sequence Selection Try Again")
        else:
            if songs[song_number][3] == "l":
                print("Your selected song is already Learned")
            else:
                songs[song_number][3] = "l"
                import csv
                with open("songs.csv", "w", newline='') as fp:
                    a = csv.writer(fp, delimiter=',')
                    a.writerows(songs)
                print("Your selected Song is marked as Learned")


def main():
    """ Main function will take user input and then according to the input take action like L - to list all songs from
     csv file, A - Add new song into csv file, C - to complete a song and Q-  to quit"""
    print("Songs to learn 1.0 - by Aaishwinder Kaur")
    learned_songs = calculating_learned_songs()                # give all learned songs
    unlearned_songs = calculating_unlearned_songs()              # give all unlearned songs
    total_songs = learned_songs + unlearned_songs              # calculate total number of songs
    print("{} songs loaded". format(total_songs))             # prints total songs
    choice = displaying_menu_choices()                           # display menu
    while choice != "Q":
        if choice == "L":                                   # display list of songs
            get_formatted_list(loading_csv_file())
            print("{} songs learned, {} songs still to learn".format(learned_songs, unlearned_songs))
            choice = displaying_menu_choices()                  # display menu
        elif choice == "A":
            adding_new_song_to_list()                            # display function to add new song
            choice = displaying_menu_choices()                   # display menu
        elif choice == "C":
            mark_unlearn_to_learn()
            choice = displaying_menu_choices()                  # display menu
    print("{} songs saved to songs.csv".format(total_songs))
    print("Have a nice day :")           # end message on giving input q


main()
