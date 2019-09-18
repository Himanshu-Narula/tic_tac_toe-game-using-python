board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

current_player = "X"
turner = True


def choose_turn():
    global current_player
    global turner
    current_player = input("Who wants to go first X or O : ")
    if current_player == "x" or current_player == "X" or current_player == "o" or current_player == "O":
        current_player = current_player.upper()
        turner = False

def show_board():
    print("\n")
    print(board[0] + "|" + board[1] + "|" + board[2] + "      1|2|3")
    print(board[3] + "|" + board[4] + "|" + board[5] + "      4|5|6")
    print(board[6] + "|" + board[7] + "|" + board[8] + "      7|8|9")
    print("\n")


def turn_manager():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

def choose_place():
    if current_player == "X":
        print("It's X's move now")
        place = input("Enter place you want to put X on : ")
        board_value = int(place) - 1
        if board[board_value] == "-":
            board[board_value] = "X"
        elif board[board_value] == "O" or board[board_value] == "X":
            print("It's already taken")
            place = input("Choose another place where you want to put X on : ")
            board_value = int(place) - 1
            if board[board_value] == "-":
                board[board_value] = "X"
    elif current_player == "O":
        print("It's O's move now")
        place = input("Enter place you want to put O on : ")
        board_value = int(place) - 1
        if board[board_value] == "-":
            board[board_value] = "O"
        elif board[board_value] == "O" or board[board_value] == "X":
            print("It's already taken")
            place = input("Choose another place where you want to put O on : ")
            board_value = int(place) - 1
            if board[board_value] == "-":
                board[board_value] = "O"
    show_board()
            

def check_game_over():
    global game
    if board[0] == board[1] == board[2] == "X" or board[3] == board[4] == board[5] == "X" or board[6] == board[7] == board[8] == "X" or board[0] == board[3] == board[6] == "X" or board[1] == board[4] == board[7] == "X" or board[8] == board[5] == board[2] == "X" or board[0] == board[4] == board[8] == "X" or board[6] == board[4] == board[2] == "X":
        print("X Won the game")
        game = True
    elif board[0] == board[1] == board[2] == "O" or board[3] == board[4] == board[5] == "O" or board[6] == board[7] == board[8] == "O" or board[0] == board[3] == board[6] == "O" or board[1] == board[4] == board[7] == "O" or board[8] == board[5] == board[2] == "O" or board[0] == board[4] == board[8] == "O" or board[6] == board[4] == board[2] == "O":
        print("O Won the game")
        game = True


def check_tie():
    global game
    if board[0] != "-" and board[1] != "-" and board[2] != "-" and board[3] != "-" and board[4] != "-" and board[5] != "-" and board[6] != "-" and board[7] != "-" and board[8] != "-":
         print("Game Tie")
         game = True


game = False
while not game:
    while turner:
        choose_turn()
    choose_place()
    turn_manager()
    check_game_over()
    check_tie()