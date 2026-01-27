print("Välkomen till konsol 3 i rad!")
turn = True
player_1 = []
player_2 = []

board = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
board_Hidden = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def Board_State():
    for rad in range(len(board)):
        for kolumn in board[rad]:
            print(f"[{kolumn}]", end="")
        print()

def Board_State_Hidden():
    for rad in range(len(board_Hidden)):
        for kolumn in board_Hidden[rad]:
            print(f"[{kolumn}]", end="")
        print()

def Update_Board():
    global turn
    if turn == True:
        where = int(input("Vart vill du placera ditt X? "))
        
        if where in range(7, 10):
            if where == 7:
                board_Hidden[0][0] = 10
                board[0][0] = "X"
            elif where == 8:
                board_Hidden[0][1] = 10
                board[0][1] = "X"
            else:
                board_Hidden[0][2] = 10
                board[0][2] = "X"
            Board_State()

        elif where in range(4, 7):
            if where == 4:
                board_Hidden[1][0] = 10
                board[1][0] = "X"
            elif where == 5:
                board_Hidden[1][1] = 10
                board[1][1] = "X"
            else:
                board_Hidden[1][2] = 10
                board[1][2] = "X"
            Board_State()

        elif where in range(1, 4):
            if where == 1:
                board_Hidden[2][0] = 10
                board[2][0] = "X"
            elif where == 2:
                board_Hidden[2][1] = 10
                board[2][1] = "X"
            else:
                board_Hidden[2][2] = 10
                board[2][2] = "X"
            Board_State()

        else:
            Update_Board()
        turn = False
    elif turn == False:
        where = int(input("Vart vill du placera ditt O? "))
        if where in range(7, 10):
            if where == 7:
                board_Hidden[0][0] = 3
                board[0][0] = "O"
            elif where == 8:
                board_Hidden[0][1] = 3
                board[0][1] = "O"
            else:
                board_Hidden[0][2] = 3
                board[0][2] = "O"
            Board_State()

        elif where in range(4, 7):
            if where == 4:
                board_Hidden[1][0] = 3
                board[1][0] = "O"
            elif where == 5:
                board_Hidden[1][1] = 3
                board[1][1] = "O"
            else:
                board_Hidden[1][2] = 3
                board[1][2] = "O"
            Board_State()

        elif where in range(1, 4):
            if where == 1:
                board_Hidden[2][0] = 3
                board[2][0] = "O"
            elif where == 2:
                board_Hidden[2][1] = 3
                board[2][1] = "O"
            else:
                board_Hidden[2][2] = 3
                board[2][2] = "O"
            Board_State()

        else:
            Update_Board()
        turn = True


Board_State()
Update_Board()
print()
Board_State_Hidden()

Update_Board()
print()
Board_State_Hidden()