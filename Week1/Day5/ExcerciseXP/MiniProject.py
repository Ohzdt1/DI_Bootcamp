# board = [
#     [" ", " ", " "],
#     [" ", " ", " "],
#     [" ", " ", " "]
# ]

# board = [[''] * 3 for x in range(3)]

# print(board)

# def display_board():
#     for row in enumerate(board):
#         print('  | '.join(row))
#         if row < len(board) - 1:
#             print('--+---+--')

# display_board()

# players = []

# def player_input(player1, player2):
#     print(input('1st players trun: '))

# board = [' '] * 9

# display_board(board)

def display_board(board):
    print("\nTIC TAC TOE!!!")
    print("***************\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n***************\n")

def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) -1
            
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                return row, col
            else:
                print("That place is taken! Try again.")
        except ValueError:
            print("Invalid input! Enter numbers between 0 and 2.")

def check_win(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        display_board(board)
        player = players[turn % 2]
        row, col = player_input(board, player)
        board[row][col] = player

        if check_win(board, player):
            display_board(board)
            print(f"Congrats Player {player} wins!")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie!")
            break
        
        turn += 1

play()