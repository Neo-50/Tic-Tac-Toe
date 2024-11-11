from random import randint

board = [
  [None, None, None],
  [None, None, None],
  [None, None, None]
]

def get_cell_value(v):
  if v == None:
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
    while True:
        a, b = randint(0, 2), randint(0, 2)
        if board[a][b] is None:  # Check if the cell is empty
            board[a][b] = 'o'  # Place 'o' for the AI move
            break  # Exit loop once a valid move is made


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
    ai_move()  # AI makes its move

printboard()
print("Victory is mine!!")
