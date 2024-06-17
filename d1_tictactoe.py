# Set up for the game

from random import randrange


# Function that starts the game!
# Here I wanted to add a function that lets the player choose which mark s/he uses and how big the board should be. But to be honest: I had troubles with other parts of the code and this was just a nice to have, so I decided to skip it!

# Function that evaluates the current state of the game
def evaluate(board):
  if "xxx" in board:
    print("Player (x) has won! Congrats!")
    return ("x", True)
  elif "ooo" in board:
    print("PC (o) has won! Try again next time!")
    return ("o", True)
  elif "-" not in board:
    print("Draw - nobody won!")
    return ("!", True)
  else:
    print("The game is not over yet - keep playing to see who wins!")
    return ("-", False)

# Function that returns the game board with the mark in the given position.
def move(board, mark, position):
    return board[:position] + mark + board[position+1:]

# Function that lets the player choose where to put the mark and returns the game board with the mark in the given position.
def player_move(board, player_mark):
   # It just now occurs to me, that it would have made sense to use the move function in this function, which I did not. But I want to move on to my own projects, so I am not changing this part anymore. Maybe I will come back to it. 
  try:
    player_position= int(input(" At which position to you want to set your mark? "))
    if player_position < 0:
      print ("Please enter a positive number between 0 and 19!")
      return player_move(board, player_mark)

    elif player_position > 19:
      print ("Please enter a positive number between 0 and 19!")
      return player_move(board, player_mark)

    elif board[player_position] == "x":
      print ("Position already taken by x, please choose another position.")
      return player_move(board, player_mark)

    elif board[player_position] == "o":
      print ("Position already taken by o, please choose another position.")
      return player_move(board, player_mark)

    else:
      board = board[:player_position] + player_mark + board[player_position+1:]
      print("After this move, board is ", board)
      return board

  except ValueError:
        print("Please enter a valid integer between 0 and 19.")
        return player_move(board, player_mark)


# Function that puts the pc mark at a random position on the board.
def pc_move(board, pc_mark):
  pc_position = randrange(0,19)
  if board[pc_position] == "x":
      print("Already taken by x, please pick another postition!")
      return pc_position(board, pc_mark)
  elif board[pc_position] == "o":
      print("Already taken by o, please pick another position.")
      return pc_position(board, pc_mark)
  else:
      board = board[:pc_position] + pc_mark + board[pc_position+1:]
      print("After this move, board is ", board)
      return board

# Steps of the game - let the players play until either player or pc wins or there is a draw.
def d1_tictactoe():
  board = "-"*20
  player_mark = "x"
  pc_mark = "o"
  print ("Starting board is ", board, ". Player mark is", player_mark, ". PC mark is", pc_mark,"!")
    # Main game loop
  while True:
  # Player move
    board = player_move(board, player_mark)
    if evaluate(board)[1]:
      break
    # PC move
    board = pc_move(board, pc_mark)
    if evaluate(board)[1]:
        break

if __name__ == "__main__":
    d1_tictd1_tictactoe()

# I could have written a function that evaluates the current state of the board and then lets the pc chose where to put its mark next (e.g. an if function, if an x is already at a position try to use the one left or right of it next). This would have been a playing strategy for pc, which would have made the game harder for the human player