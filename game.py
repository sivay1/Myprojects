def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i][0], "|", board[i][1], "|", board[i][2], "|")
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player) or \
           (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player) or \
       (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False

def get_move(player):
    print("Player", player, "turn:")
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))
    return row, col

def play_game():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    print_board(board)
    player = 'X'
    while True:
        row, col = get_move(player)
        if board[row][col] != ' ':
            print("Invalid move, try again!")
            continue
        board[row][col] = player
        print_board(board)
        if check_win(board, player):
            print("Player", player, "wins!")
            break
        if all([board[i][j] != ' ' for i in range(3) for j in range(3)]):
            print("Tie!")
            break
        player = 'O' if player == 'X' else 'X'

play_game()
