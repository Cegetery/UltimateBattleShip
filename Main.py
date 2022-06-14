
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


# elem expected to be a single list element of a primitive type.
def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


# n expected to be str or int.
def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")
        # There is a \n because we want the board to start printing on the next line.


def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")


# ship expected to be str.
def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")


# ship expected to be str.
def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")


# n expected to be str or int.
def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")


# n expected to be str or int.
def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")


# n expected to be str or int.
def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")


# my_list expected to be a 3-dimensional list, formed from two 2-dimensional lists containing the boards of each player.
def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind+1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print("There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print("First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print("Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print("Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True  # You can change this to True to also output to a file so that you can check your outputs with diff.

print_rules()

# Remember to use list comprehensions at all possible times.
# If we see you populate a list that could be done with list comprehensions using for loops, append/extend/insert etc. you will lose points.

# Make sure to put comments in your code explaining your approach and the execution.

# We defined all the functions above for your use so that you can focus only on your code and not the formatting.
# You need to call them in your code to use them of course.

# If you have questions related to this homework, direct them to utku.bozdogan@boun.edu.tr please.

# Do not wait until the last day or two to start doing this homework, it requires serious effort.

try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.
    # DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
    player_boards = {}
    for player in range(2):
        #creating list of ships
        list_ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
        #creating the board
        board = [[['-' for i in range(board_size)] for j in range(board_size)],[['-' for i in range(board_size)] for j in range(board_size)]]
        list_ships_trash = []
        while len(list_ships) > 0:#limiting the loop by reducing the number of ships that are in the list
            len_ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
            print_3d_list(board)
            print_ships_to_be_placed()
            for i in list_ships:
                print_single_element(i)
            print_empty_line()
            print_player_turn_to_place(player + 1)
            print_to_place_ships()
            chosen_ship1 = input()
            try:#eliminating bugs from the input
                chosen_ship1_name = chosen_ship1.split()[0].title()
                chosen_ship1_x = int(chosen_ship1.split()[1])
                chosen_ship1_y = int(chosen_ship1.split()[2])
                chosen_ship1_rotation = chosen_ship1.split()[3].lower()
                if not chosen_ship1.split()[1].isdecimal() or not chosen_ship1.split()[2].isdecimal():
                    print_incorrect_input_format()
                    continue
            except:
                print_incorrect_input_format()
                continue
            if not 0 < chosen_ship1_x < 11 or not 0 < chosen_ship1_y < 11:
                print_incorrect_coordinates()
                continue
            if chosen_ship1_name not in list_ships and chosen_ship1_name not in list_ships_trash:
                print_incorrect_ship_name()
                continue
            if chosen_ship1_rotation != "h" and chosen_ship1_rotation != "v":
                print_incorrect_orientation()
                continue
            try:#changing the characters of board according to the input
                if chosen_ship1_name not in list_ships_trash:
                    if chosen_ship1_x + len_ships[chosen_ship1_name] - 1 <= 10 and chosen_ship1_rotation == "h":
                        ship_true_false = 1
                        for i in range(len_ships[chosen_ship1_name]):
                            if board[player][chosen_ship1_y - 1][chosen_ship1_x - 1 + i] == '#':
                                print_ship_cannot_be_placed_occupied(chosen_ship1_name)
                                ship_true_false = 0
                                break
                        if ship_true_false == 1:
                            for i in range(len_ships[chosen_ship1_name]):
                                board[player][chosen_ship1_y - 1][chosen_ship1_x - 1 + i] = '#'
                            list_ships.remove(chosen_ship1_name)
                            list_ships_trash.append(chosen_ship1_name)
                    elif chosen_ship1_y + len_ships[chosen_ship1_name] - 1 <= 10 and chosen_ship1_rotation == "v":
                        ship_true_false = 1
                        for i in range(len_ships[chosen_ship1_name]):
                            if board[player][chosen_ship1_y - 1 + i][chosen_ship1_x - 1] == '#':
                                print_ship_cannot_be_placed_occupied(chosen_ship1_name)
                                ship_true_false = 0
                                break
                        if ship_true_false == 1:
                            for i in range(len_ships[chosen_ship1_name]):
                                board[player][chosen_ship1_y - 1 + i][chosen_ship1_x - 1] = '#'
                            list_ships.remove(chosen_ship1_name)
                            list_ships_trash.append(chosen_ship1_name)
                    else:
                        print_ship_cannot_be_placed_outside(chosen_ship1_name)
                        continue
                else:
                    print_ship_is_already_placed(chosen_ship1_name)
            except:
                print_incorrect_input_format()
            if len(list_ships) == 0:#transition to the y/n part of the game
                print_3d_list(board)
                confirmation_counter = True#assigning a boolean to reask to the user if user says "n"
                while confirmation_counter:
                    print_confirm_placement()
                    confirmation = input()
                    if confirmation.lower() == "n":
                        list_ships = ['Carrier', 'Battleship', 'Cruiser', 'Submarine', 'Destroyer']
                        board = [[['-' for i in range(board_size)] for j in range(board_size)],[['-' for i in range(board_size)] for j in range(board_size)]]
                        list_ships_trash.clear()
                        confirmation_counter = False
                    elif confirmation.lower() == "y":
                        player_boards[player] = board.copy()#copying the board for the new player
                        confirmation_counter = False
    turn = 0
    hit_board_player1 = [[['-' for i in range(board_size)] for j in range(board_size)]]#creating a new board to show the players changes in the boards without showing the ships' places
    hit_board_player2 = [[['-' for i in range(board_size)] for j in range(board_size)]]#creating a new board to show the players changes in the boards without showing the ships' places
    counter1 = 17#counter of the number of the ships' tiles
    counter2 = 17#counter of the number of the ships' tiles
    print_3d_list(player_boards[turn])
    while counter1 > 0 and counter2 > 0:
        print_player_turn_to_strike(turn + 1)
        print_choose_target_coordinates()
        chosen_coordinates = input()
        try:#eliminating bugs from the input
            chosen_coordinates_x = int(chosen_coordinates.split()[0])
            chosen_coordinates_y = int(chosen_coordinates.split()[1])
            if not chosen_coordinates.split()[0].isdecimal() or not chosen_coordinates.split()[1].isdecimal():
                print_incorrect_input_format()
                if turn == 0:
                    the_board_for_player1_to_hit = [player_boards[0][0], hit_board_player2[0]]
                if turn == 1:
                    the_board_for_player1_to_hit = [hit_board_player1[0], player_boards[1][1]]
                print_3d_list(the_board_for_player1_to_hit)
                continue
        except:
            print_incorrect_input_format()
            if turn == 0:
                the_board_for_player1_to_hit = [player_boards[0][0], hit_board_player2[0]]
            if turn == 1:
                the_board_for_player1_to_hit = [hit_board_player1[0], player_boards[1][1]]
            print_3d_list(the_board_for_player1_to_hit)
            continue
        if not 0 < chosen_coordinates_x < 11 or not 0 < chosen_coordinates_y < 11:
            print_incorrect_coordinates()
            if turn == 0:
                the_board_for_player1_to_hit = [player_boards[0][0], hit_board_player2[0]]
            if turn == 1:
                the_board_for_player1_to_hit = [hit_board_player1[0], player_boards[1][1]]
            print_3d_list(the_board_for_player1_to_hit)
            continue
        if turn == 0:#changing the characters of board according to input
            if player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "!" or player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "O":
                print_tile_already_struck()
                the_board_for_player1_to_hit = [player_boards[turn][0], hit_board_player2[0]]
                print_3d_list(the_board_for_player1_to_hit)
                continue
            elif player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "-":
                player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "O"
                hit_board_player2[0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "O"
                the_board_for_player1_to_hit = [hit_board_player1[0], player_boards[turn + 1][1]]
                print_miss()
                type_done_true_false = 0
                while type_done_true_false == 0:
                    print_type_done_to_yield(turn + 2)
                    type_done = input()
                    if type_done.lower() == "done":
                        turn += 1#passing to the other player
                        type_done_true_false = 1
                    else:
                        type_done_true_false = 0#keeping the loop to reask
                print_3d_list(the_board_for_player1_to_hit)
                continue
            elif player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "#":
                player_boards[turn + 1][1][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "!"
                hit_board_player2[0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "!"
                the_board_for_player1_to_hit = [player_boards[turn][0], hit_board_player2[0]]
                print_hit()
                counter1 -= 1
                print_3d_list(the_board_for_player1_to_hit)
        if turn == 1:
            if player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "!" or player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "O":
                print_tile_already_struck()
                the_board_for_player2_to_hit = [hit_board_player1[0], player_boards[turn][1]]
                print_3d_list(the_board_for_player2_to_hit)
                continue
            elif player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "-":
                player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "O"
                hit_board_player1[0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "O"
                the_board_for_player2_to_hit = [player_boards[turn - 1][0], hit_board_player2[0]]
                print_miss()
                type_done_true_false = 0
                while type_done_true_false == 0:
                    print_type_done_to_yield(turn)
                    type_done = input()
                    if type_done.lower() == "done":
                        turn -= 1#passing to the other player
                        type_done_true_false = 1
                    else:
                        type_done_true_false = 0#keeping the loop to reask
                print_3d_list(the_board_for_player2_to_hit)
                continue
            elif player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] == "#":
                player_boards[turn - 1][0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "!"
                hit_board_player1[0][chosen_coordinates_y - 1][chosen_coordinates_x - 1] = "!"
                the_board_for_player2_to_hit = [hit_board_player1[0], player_boards[turn][1]]
                print_hit()
                counter2 -= 1
                print_3d_list(the_board_for_player2_to_hit)
    #finishing the game
    if counter1 == 0:
        print_player_won(1)
    elif counter2 == 0:
        print_player_won(2)
    print_thanks_for_playing()

    # DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE
except:
    f.close()

