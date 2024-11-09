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


def ai_move():
  for i, row in enumerate(board):
    for j, cell in enumerate(row):
      if cell == None:
        return j, i


while victory() != True:
    printboard()
    move = input('Enter the coordinates for your move in the format x,x: ')
    coord1 = int(move[0]) -1
    coord2 = int(move[2]) -1
    board[coord2][coord1] = 'x'
    coord1, coord2 = ai_move()
    board[coord2][coord1] = 'o'

printboard()
print('Victory is mine!!')