turn = True
turn_counter = 0
player_1 = []
player_2 = []

board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]

def Board_State():
    for rad in range(len(board)):
        for kolumn in board[rad]:
            print(f"[{kolumn}]", end="")
        print()

def Update_Board():
    global turn, turn_counter
    if turn == True:
        where = int(input("Spelare 1, vart vill du placera ditt X? "))
        for rad in range(len(board)):
            for kolumn in range(len(board[rad])):
                if (board[rad][kolumn] != "X") or (board[rad][kolumn] != "O"):
                    if where == 1:
                        board[2][0] = "X"
                        break
                    elif where == 2:
                        board[2][1] = "X"
                    elif where == 3:
                        board[2][2] = "X"
                    elif where == 4:
                        board[1][0] = "X"
                    elif where == 5:
                        board[1][1] = "X"
                    elif where == 6:
                        board[1][2] = "X"
                    elif where == 7:
                        board[0][0] = "X"
                    elif where == 8:
                        board[0][1] = "X"
                    elif where == 9:
                        board[0][2] = "X"
                    else:
                        Update_Board()
                else:
                    print("Välj en ruta med nummer och inte X eller O!")
                    Update_Board()
            break
        turn = False
        turn_counter += 1
        Board_State()
    elif turn == False:
        where = int(input("Spelare 2, vart vill du placera ditt O? "))
        for rad in range(len(board)):
            for kolumn in range(len(board[rad])):
                if (board[rad][kolumn] != "X") or (board[rad][kolumn] != "O"):
                    if where == 1:
                        board[2][0] = "O"
                        break
                    elif where == 2:
                        board[2][1] = "O"
                    elif where == 3:
                        board[2][2] = "O"
                    elif where == 4:
                        board[1][0] = "O"
                    elif where == 5:
                        board[1][1] = "O"
                    elif where == 6:
                        board[1][2] = "O"
                    elif where == 7:
                        board[0][0] = "O"
                    elif where == 8:
                        board[0][1] = "O"
                    elif where == 9:
                        board[0][2] = "O"
                    else:
                        Update_Board()
                else:
                    print("Välj en ruta med nummer och inte X eller O!")
                    Update_Board()
            break
        turn = True
        turn_counter += 1
        Board_State()

def Cheack_Win():
    win_player_1 = "XXX"
    win_player_2 = "OOO"
    if ((f"{board[0][0]}{board[0][1]}{board[0][2]}") == win_player_1 or
        (f"{board[1][0]}{board[1][1]}{board[1][2]}") == win_player_1 or
        (f"{board[2][0]}{board[2][1]}{board[2][2]}") == win_player_1 or
        (f"{board[0][0]}{board[1][0]}{board[2][0]}") == win_player_1 or
        (f"{board[0][1]}{board[1][1]}{board[2][1]}") == win_player_1 or
        (f"{board[0][2]}{board[1][2]}{board[2][2]}") == win_player_1 or
        (f"{board[0][0]}{board[1][1]}{board[2][2]}") == win_player_1 or
        (f"{board[2][0]}{board[1][1]}{board[0][2]}") == win_player_1):
        print("Spelare 1 Vann!")
        return True

    elif ((f"{board[0][0]}{board[0][1]}{board[0][2]}") == win_player_2 or
        (f"{board[1][0]}{board[1][1]}{board[1][2]}") == win_player_2 or
        (f"{board[2][0]}{board[2][1]}{board[2][2]}") == win_player_2 or
        (f"{board[0][0]}{board[1][0]}{board[2][0]}") == win_player_2 or
        (f"{board[0][1]}{board[1][1]}{board[2][1]}") == win_player_2 or
        (f"{board[0][2]}{board[1][2]}{board[2][2]}") == win_player_2 or
        (f"{board[0][0]}{board[1][1]}{board[2][2]}") == win_player_2 or
        (f"{board[2][0]}{board[1][1]}{board[0][2]}") == win_player_2):
        print("Spelare 2 Vann")
        return True
    
    if turn_counter == 9:
        print("Ingen vann, too bad")
        return True
    
    return False


print("Välkomen till konsol 3 i rad!")
Board_State()
while True:
    Update_Board()
    if Cheack_Win() == True:
        break