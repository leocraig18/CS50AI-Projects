"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    # Returns player who has the next turn on a board.
    """
    count_X, count_O = 0, 0
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == X:
                count_X += 1
            elif board[row][col] == O:
                count_O += 1
    if count_X > count_O:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_moves = set()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possible_moves.add((row, col))
    return possible_moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("This move is not valid.")
    row, col = action
    copy_board = copy.deepcopy(board)
    copy_board[row][col] = player(board)
    return copy_board


# Extra Functions
def check_rows(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False


def check_cols(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False


def check_diagonals(board, player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if check_rows(board, X) or check_cols(board, X) or check_diagonals(board, X):
        return X
    if check_rows(board, O) or check_cols(board, O) or check_diagonals(board, O):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def maxvalue(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, minvalue(result(board, action)))
    return v


def minvalue(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, maxvalue(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    # Max Player
    elif player(board) == X:
        moves = []
        # Loop through possible moves
        for action in actions(board):
            moves.append([minvalue(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0], reverse=True)[0][1]
    # Min Player
    elif player(board) == O:
        moves = []
        # Loop through possible moves
        for action in actions(board):
            moves.append([maxvalue(result(board, action)), action])
        return sorted(moves, key=lambda x: x[0])[0][1]


