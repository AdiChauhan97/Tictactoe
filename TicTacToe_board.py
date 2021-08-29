import random
player = 'X'
cpu = 'O'

def ttt_board(board):
    for j in range(0, 9, 3):
        row = board[j:j+3]
        row_str = [str(r) for r in row]
        print(' | '.join(row_str))

def check(user_pos, board):
    if board[user_pos] == ' ':
        return True
    else:
        return False

def humanplayer(board):
    while True:
        try:
            user_pos = int(input("Please enter a position (0-8): "))
        except ValueError :
            print("Please enter a valid integer (0-8).")
            continue
        if user_pos not in range(9):
            print("Please enter a valid integer (0-8).")
            continue

        valid_move = check(user_pos, board)
        if valid_move == True:  
            board[user_pos] = player
            break
        else:
            print(f"{user_pos} is an invalid move please enter a valid move.")
            continue

def computerplayer(board, diff):
    if diff == 'e':
        while True:
            comp_pos = random.randint(0, 8)
            valid_move = check(comp_pos, board)
            if valid_move == True:
                board[comp_pos] = cpu
                print(f"opponent move is: {comp_pos}")
                break
    elif diff == 'h':
        comp_pos = bestmove(board)
        board[comp_pos] = cpu


def winner(board):
    count_row = 0
    while count_row < len(board):
        row = board[count_row:count_row+3]
        first = row[0]
        if first != ' ':
            row_match = row.count(first) == len(row)
            if row_match == True:
                if first == cpu:
                    return 10
                elif first == player:
                    return -10
        count_row+=3

    count_col = 0
    while count_col < 3:
        col = board[count_col::3]
        first_col = col[0]
        if first_col != ' ':
            col_match = col.count(first_col) == len(col)
            if col_match == True:
                if first_col == cpu:
                    return 10
                elif first_col == player:
                    return -10
        count_col+=1

    if board[4] != ' ':
        if (board[0] == board[4] == board[8]):
            if board[0] == cpu:
                return 10
            elif board[0] == player:
                return -10
        elif (board[2] == board[4] == board[6]):
            if board[2] == cpu:
                return 10
            elif board[2] == player:
                return -10
    return 0

def is_tie(board):
    if ' ' not in board:
        return 0


def minimax(board, depth, ismax):
    score = winner(board)

    if score == 10:
        return score
    
    if score == -10:
        return score
    
    if is_tie(board) == 0:
        return 0
    
    if ismax:
        best = -1000
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = cpu
                best = max(best, minimax(board, depth+1, False))
                board[i] = ' '
        return best

    else:
        best = 1000
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = player
                best = min(best, minimax(board, depth+1, True))
                board[i] = ' '
        return best

def bestmove(board):
    bestval = -1000
    bestmove = -1

    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = cpu
            moveval = minimax(board, 0, False)
            board[i] = ' '
            if moveval > bestval:
                bestmove = i
                bestval = moveval
    print(f"Opponent move is: {bestmove}")
    return bestmove

def main():
    while True:
        diff = input("Would you like to play on easy or hard (e/h)? ")
        if diff == 'e' or diff == 'h':
            break
        print("Please enter e for easy or h for hard.")
        continue

    pos_board = [i for i in range(0, 9)]
    print("Positions of the board:")
    ttt_board(pos_board)

    board = [' ' for i in range(0, 9)]
    while True:
        humanplayer(board)
        ttt_board(board)
        if winner(board) == 10 or winner(board) == -10:
            print("Congratulations you have won.")
            break
        if is_tie(board) == 0:
            print("The game was a tie.")
            break
        computerplayer(board, diff)
        ttt_board(board)
        if winner(board) == 10 or winner(board) == -10:
            print("Your opponent won. Better luck next time.")
            break
        if is_tie(board) == 0:
            print("The game was a tie.")
            break
    while True:
        again = input("Would you like to play again (y/n)? ")
        if again == 'y' or again == 'n':
            break
        print("Please type y for yes and n for no.")
    if again == 'y':
        main()
main()

