'''
Module tic_tac_toe contains the TicTacToe class, instances of which model Tic-Tac-Toe games.
'''


class TicTacToe:
  '''
  Tic-Tac-Toe. Player names are defaulted to 'X' and 'O', but can be reassigned.
  X has the first turn. The board is marked by calling the mark() method. 
  Row and column values are indexes 0–2.
  '''
  # 3x3 Tic-Tac-Toe Empty Board represented as a dictionary
  _board = {(0, 0): '_', (0, 1): '_', (0, 2): '_',
            (1, 0): '_', (1, 1): '_', (1, 2): '_',
            (2, 0): '_', (2, 1): '_', (2, 2): '_'}

  def __init__(self, x='X', o='O'):
    '''
    Initializes a Tic-Tac-Toe game with player names set to 'X' and 'O', unless reassigned.
    Player x goes first, then turns alternate until winner or stalemate.
    '''
    self._game = TicTacToe._board.copy()  # intialize game w empty board, note use copy() for dict
    self._player1, self._player2 = x, o  # store player name
    self._currentplayer = 'X'  # 'X' goes first
    self._turn = 1  # initialize turn count
    self._winner = None  # no winner at start of game

  def __bool__(self):
    '''Game is Boolean True if still in play (there is no winner and possible moves remain).'''
    # Check Horizontal Cases for Win
    if   (self._game[(0, 0)] == self._game[(0, 1)] == self._game[(0, 2)] != '_') \
      or (self._game[(1, 0)] == self._game[(1, 1)] == self._game[(1, 2)] != '_') \
      or (self._game[(2, 0)] == self._game[(2, 1)] == self._game[(2, 2)] != '_'):
      self._winner = self._currentplayer if self._currentplayer == 'X' else 'O'
      return False
    # Check Vertical Cases for Win
    elif (self._game[(0, 0)] == self._game[(1, 0)] == self._game[(2, 0)] != '_') \
      or (self._game[(0, 1)] == self._game[(1, 1)] == self._game[(2, 1)] != '_') \
      or (self._game[(0, 2)] == self._game[(1, 2)] == self._game[(2, 2)] != '_'):
      self._winner = self._currentplayer if self._currentplayer == 'X' else 'O'
      return False
    # Check Diagonal Cases for Win
    elif (self._game[(0, 0)] == self._game[(1, 1)] == self._game[(2, 2)] != '_') \
      or (self._game[(0, 2)] == self._game[(1, 1)] == self._game[(2, 0)] != '_'):
      self._winner = self._currentplayer if self._currentplayer == 'X' else 'O'
      return False
    # Check if No Win Cases after All Possible 9 Moves
    elif self._turn > 9:
      return False
    # Else Game is Still in Play
    else: 
      return True

  def __str__(self):
    '''
    Returns a string representation of the game board, formatted below:
    Where '_' is empty spot and 'X' or 'O' is marked.

    |_|_|_|
    |_|_|_|
    |_|_|_|
    '''
    return (f"|{self._game[(0, 0)]}|{self._game[(0, 1)]}|{self._game[(0, 2)]}|\n"
            f"|{self._game[(1, 0)]}|{self._game[(1, 1)]}|{self._game[(1, 2)]}|\n"
            f"|{self._game[(2, 0)]}|{self._game[(2, 1)]}|{self._game[(2, 2)]}|")

  def grid(self):
    '''
    Returns a tuple of the current board, consisting of 9 values that are 'X', 'O', or None.
    grid()[:3] is first row, grid()[3:6] is second, and grid()[6:] is third. See example:

    ('X', None, None, 'O', 'X', None, 'O', None, 'X') is the tuple representation of below

    |X|_|_|
    |O|X|_|
    |O|_|X|
    '''
    return tuple(val if val in {'X', 'O'} else None for val in self._game.values())

  def mark(self, row: int, col: int):
    '''
    Current player takes a turn by marking the given row and column (0–2). 
    Turn is valid and will end if spot is unmarked. If not raise ValueError if spot is marked,
    if not in grid, or if games has ended already. Turns alternate, with player x going first.
    '''
    # If Game is Still in Play ...
    if bool(self):
      # Check if row and col in range from 0-2
      if row in range(3) and col in range(3):
        # Check if spot is taken and if not then mark spot
        if self._game[(row, col)] == '_':
          self._currentplayer = 'O' if self._turn % 2 == 0 else 'X'
          self._game[(row, col)] = self._currentplayer
          self._turn += 1
        else:  # Raise error if selecting a spot that has 'X' or 'O' already
          raise ValueError('Spot is taken! Try again.')
      else:  # Raise error if row and col are out of range 0-2
        raise ValueError('Grid Position is Out of Range! Use (0-2, 0-2).')
    else:  # Raise error if trying to play a game that finished
      raise ValueError('Game Finished')

  def winner(self):
    '''Returns the winner or None if the game is still in play or has ended without a winner.'''
    # Check if Game Ended and There is a Winner (self._winner != None)
    if not bool(self) and self._winner:
      # Check if winner is 'X' and return player1, else return player2
      return self._player1 if self._winner == 'X' else self._player2
    # Else return None for No Winner
    else:
      return None


# Execute a Tic-Tac-Toe Game
if __name__ == '__main__':
  # Get player names and if empty default to player1 = 'X' and player2 = 'O'. 
  player_names = input('Input player names separated by whitespace with player1 going first:\n')
  # Start game with player names
  game = TicTacToe(*player_names.strip().split())

  # Exceute a turn if game is in play (Boolean True)
  while bool(game):
    # Check if input is valid character for int()
    try:
      if game._turn % 2 == 0:  # player2's turn
        player_input = input(f"Turn {game._turn} - {game._player2}'s move as row col: ")
      else:  # player1's turn
        player_input = input(f"Turn {game._turn} - {game._player1}'s move as row col: ")
      # Make sure input is separated by whitespace
      try:
        game.mark(*map(int, player_input.split()))
      except TypeError:
        print('Need row and col separated by whitespace!')
      # Print current game board 
      print(game)
    except ValueError as err:  # Catch if input is non-numeric
      print(err)

  # Print winner of game if not None
  if game.winner():
    print(f'Winner is {game.winner()}!')
  else:
    print('No winner, please play again.')
