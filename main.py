import random

move_count = 0

board = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]


def get_cell_value(v):
    if v is None:
        return ' '
    else:
        return v


def printboard():
    for i, row in enumerate(board):
        print(get_cell_value(row[0]) + '|' + get_cell_value(row[1]) + '|' + get_cell_value(row[2]))
        if i < 2:
            print('-----')


def get_player_move():
    while True:
        move = input("Enter the coordinates for your move in the format x,x (1-3 for both): ")

        # Check if the input matches the expected format
        if len(move) != 3 or move[1] != ',' or not move[0].isdigit() or not move[2].isdigit():
            print("Invalid format! Please enter in 'x,y' format where x and y are between 1 and 3.")
            continue

        # Convert input to board coordinates
        coord1, coord2 = int(move[0]) - 1, int(move[2]) - 1

        # Check if the coordinates are within bounds
        if not (0 <= coord1 <= 2 and 0 <= coord2 <= 2):
            print("Coordinates out of bounds! Please enter values between 1 and 3.")
            continue

        # Check if the cell is empty
        if board[coord2][coord1] is not None:
            print("Cell is already occupied! Choose an empty cell.")
            continue

        # If all checks pass, return the validated coordinates
        return coord1, coord2


def ai_move():
    # Create a list of all available cells
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] is None]

    # Check if there are any moves left (the game might end on a full board)
    if available_moves:
        # Select a random cell from the available moves
        a, b = random.choice(available_moves)
        board[a][b] = 'o'  # Place the AI's move


def victory():
    if 'x' == board[0][0] and 'x' == board[0][1] and 'x' == board[0][2]:
        return True
    if 'x' == board[1][0] and 'x' == board[1][1] and 'x' == board[1][2]:
        return True
    if 'x' == board[2][0] and 'x' == board[2][1] and 'x' == board[2][2]:
        return True
    if 'x' == board[0][0] and 'x' == board[1][0] and 'x' == board[2][0]:
        return True
    if 'x' == board[0][1] and 'x' == board[1][1] and 'x' == board[2][1]:
        return True
    if 'x' == board[0][2] and 'x' == board[1][2] and 'x' == board[2][2]:
        return True
    if 'x' == board[0][2] and 'x' == board[1][1] and 'x' == board[2][0]:
        return True
    if 'x' == board[0][0] and 'x' == board[1][1] and 'x' == board[2][2]:
        return True

    if 'o' == board[0][0] and 'o' == board[0][1] and 'o' == board[0][2]:
        return True
    if 'o' == board[1][0] and 'o' == board[1][1] and 'o' == board[1][2]:
        return True
    if 'o' == board[2][0] and 'o' == board[2][1] and 'o' == board[2][2]:
        return True
    if 'o' == board[0][0] and 'o' == board[1][0] and 'o' == board[2][0]:
        return True
    if 'o' == board[0][1] and 'o' == board[1][1] and 'o' == board[2][1]:
        return True
    if 'o' == board[0][2] and 'o' == board[1][2] and 'o' == board[2][2]:
        return True
    if 'o' == board[0][2] and 'o' == board[1][1] and 'o' == board[2][0]:
        return True
    if 'o' == board[0][0] and 'o' == board[1][1] and 'o' == board[2][2]:
        return True
    return False


while not victory():
    printboard()
    coord1, coord2 = get_player_move()
    board[coord2][coord1] = 'x'  # Place player's move
    move_count += 1  # Increment move count

    # Check if the board is full after player's move
    if move_count == 9:
        print("Game ends with a stalemate!")
        break

    ai_move()  # AI makes its move
    move_count += 1  # Increment move count again

    # Check if the board is full after AI's move
    if move_count == 9:
        print("Game ends with a stalemate!")
        break
    if victory():
        print("Victory is mine!!")

printboard()
