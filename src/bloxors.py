"""Bloxorz state:
Stand: | cost 1 element in space
Ground: _ cost 2 element in space

Move(Direction)
Direction: [up, down, left, right]
"""
from enum import Enum, IntEnum

class State(Enum):
  DONTKNOW = 0
  STAND = 1
  GROUND_HOZ = 2 # Horizontal
  GROUND_VEC = 3 # Vectical

# Direction on Bloxorz map
class Direction(IntEnum):
  UP = 0
  DOWN = 1
  LEFT = 2
  RIGHT = 3

class BlzElement:
  def __init__(self):
    self.blzState = State.DONTKNOW 
    # Index of Bloxorz Element [[row1, col1],[row2, col2]]
    # If state: STAND => row2 = col2 = -1
    self.BlzElementIdx = [[-1, -1], [-1, -1]]
    # Direction where Block can move to
    # Index: UP, DOWN, LEFT, RIGHT
    self.blzMovable = [True, True, True, True]
  
  """Check if Block can be movable"""
  def checkMovable(self, blzMap):
    # Use to check the condition block canmove
    numrows = len(blzMap)
    numcols = len(blzMap[0])

    # Switch between state
    if (self.blzState == State.STAND):
      # Move Right
      colR1 = self.BlzElementIdx[0][1] + 1
      colR2 = self.BlzElementIdx[0][1] + 2
      self.blzMovable[int(Direction.RIGHT)] = False if (colR1 >= numcols or colR2 >= numcols) else True
      # Move Left
      colL1 = self.BlzElementIdx[0][1] - 2
      colL2 = self.BlzElementIdx[0][1] - 1
      self.blzMovable[int(Direction.LEFT)] = False if (colL1 < 0 or colL2 < 0) else True
      # Move Up
      rowU1 = self.BlzElementIdx[0][0] - 2
      rowU2 = self.BlzElementIdx[0][0] - 1
      self.blzMovable[int(Direction.UP)] = False if (rowU1 < 0 or rowU2 < 0) else True
      # Move Down
      rowD1 = self.BlzElementIdx[0][0] + 1
      rowD2 = self.BlzElementIdx[0][0] + 2
      self.blzMovable[int(Direction.DOWN)] = False if (rowD1 >= numrows or rowD2 >= numrows) else True

    elif (self.blzState == State.GROUND_HOZ):
      # Move Right
      colR = self.BlzElementIdx[1][1] + 1
      self.blzMovable[int(Direction.RIGHT)] = False if (colR >= numcols) else True
      # Move Left
      colL = self.BlzElementIdx[0][1] - 1
      self.blzMovable[int(Direction.LEFT)] = False if (colL < 0) else True
      # Move Up
      rowU = self.BlzElementIdx[0][0] - 1
      self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
      # Move Down
      rowD = self.BlzElementIdx[0][0] + 1
      self.blzMovable[int(Direction.DOWN)] = False if (rowD < 0) else True

    elif (self.blzState == State.GROUND_VEC):
      # Move Right
      colR = self.BlzElementIdx[0][1] + 1
      self.blzMovable[int(Direction.RIGHT)] = False if (colR >= numcols) else True
      # Move Left
      colL = self.BlzElementIdx[0][1] - 1
      self.blzMovable[int(Direction.LEFT)] = False if (colL < 0) else True
      # Move Up
      rowU = self.BlzElementIdx[0][0] - 1
      self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
      # Move Down
      rowD = self.BlzElementIdx[1][0] + 1
      self.blzMovable[int(Direction.DOWN)] = False if (rowD < 0) else True
    else: pass

  """Check the Block in the Finish position
  Return: True - Block in Finish postion
          False - Unless
  """
  def checkFinish(self, blzMap):
    row = self.BlzElementIdx[0][0]
    col = self.BlzElementIdx[0][1]
    state = self.blzState
    if(state == State.STAND and blzMap[row][col] == 'G'):
      return True
    else:
      return False

  """Move Right
  Return: 
  + True - the block move Right
  + False - the block can't move"""
  def moveRight(self, blzMap):
    self.checkMovable(blzMap)

    newBlz = BlzElement()
    if (self.blzMovable[int(Direction.RIGHT)]):
      # STAND
      if (self.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0]
        col1 = self.BlzElementIdx[0][1] + 1
        col2 = self.BlzElementIdx[0][1] + 2
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'
      
      # GROUND HORIZONTAL
      elif (self.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0]
        col = self.BlzElementIdx[1][1] + 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'
      
      # GROUND VECTICAL
      elif (self.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row1 = self.BlzElementIdx[0][0] + 1
        row2 = self.BlzElementIdx[1][0] + 1
        col = self.BlzElementIdx[0][1]
        # Update Location of Block
        newBlz.BlzElementIdx = [[row1, col], [row2, col]]
        # Update Map
        blzMap[row1][col] = blzMap[row2][col] = 'B'
      else: pass
        
      return newBlz
    else :
      pass

  """Move Left
  Return: 
  + True - the block move Left
  + False - the block can't move"""
  def moveLeft(self, blzMap):
    self.checkMovable(blzMap)
    newBlz = BlzElement()

    if (self.blzMovable[int(Direction.LEFT)]):
      # STAND
      if (self.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0]
        col1 = self.BlzElementIdx[0][1] - 2
        col2 = self.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'
      
      # GROUND HORIZONTAL
      elif (self.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0]
        col = self.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'
      
      # GROUND VECTICAL
      elif (self.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row1 = self.BlzElementIdx[0][0] 
        row2 = self.BlzElementIdx[1][0] 
        col = self.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row1, col], [row2, col]]
        # Update Map
        blzMap[row1][col] = blzMap[row2][col] = 'B'
      else: pass
        
      return newBlz
    else :
      pass

  """Move Up
    Return: 
    + newBlz - the block move Up
    + pass - the block can't move"""
  def moveUp(self, blzMap):
    self.checkMovable(blzMap)
    newBlz = BlzElement()

    if (self.blzMovable[int(Direction.UP)]):
      # STAND
      if (self.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        # Update
        row1 = self.BlzElementIdx[0][0] - 2
        row2 = self.BlzElementIdx[0][0] - 1
        col = self.BlzElementIdx[0][1]
        # Update Location of Block
        newBlz.BlzElementIdx = [[row1, col], [row2, col]]
        # Update Map
        blzMap[row1][col] = blzMap[row2][col] = 'B'
      
      # GROUND HORIZONTAL
      elif (self.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0] - 1
        col1 = self.BlzElementIdx[0][1]
        col2 = self.BlzElementIdx[1][1]  
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'
      
      # GROUND VECTICAL
      elif (self.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0] - 1
        col = self.BlzElementIdx[0][1]
        
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'
      else: pass
        
      return newBlz
    else :
      pass


  """Move Down
    Return: 
    + True - the block move Down
    + False - the block can't move"""
  def moveDown(self, blzMap):
    self.checkMovable(blzMap)
    newBlz = BlzElement()

    if (self.blzMovable[int(Direction.DOWN)]):
      # STAND
      if (self.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        # Update
        row1 = self.BlzElementIdx[0][0] + 1
        row2 = self.BlzElementIdx[0][0] + 2
        col = self.BlzElementIdx[0][1]
        # Update Location of Block
        newBlz.BlzElementIdx = [[row1, col], [row2, col]]
        # Update Map
        blzMap[row1][col] = blzMap[row2][col] = 'B'
      
      # GROUND HORIZONTAL
      elif (self.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[0][0] + 1
        col1 = self.BlzElementIdx[0][1]
        col2 = self.BlzElementIdx[1][1]  
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'
      
      # GROUND VECTICAL
      elif (self.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[self.BlzElementIdx[0][0]][self.BlzElementIdx[0][1]] = '+'
        blzMap[self.BlzElementIdx[1][0]][self.BlzElementIdx[1][1]] = '+'
        # Update
        row = self.BlzElementIdx[1][0] + 1
        col = self.BlzElementIdx[0][1]
        
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'
      else: pass
        
      return newBlz
    else :
      pass


"""Goal: Get State, Index of Blozorx block
Update state of Bloxorz Map
"""
def getStateStart(blzMap):
  blzStart = BlzElement()
  numrows = len(blzMap)
  numcols = len(blzMap[0])
  for row in range(numrows):
    for col in range(numcols):
      if blzMap[row][col] == 'S':
        blzStart.blzState = State.STAND
        blzStart.BlzElementIdx[0][0] = row
        blzStart.BlzElementIdx[0][1] = col
        blzStart.checkMovable(blzMap)

        # BLOXORZ: B => block stand here
        blzMap[row][col] = 'B'
        return blzStart

"""Return the new BlzElement Object"""
def move(blzBlock, blzMap, direction):
  if (blzBlock.blzMovable[int(direction)]):
    if(direction == Direction.UP):
      return blzBlock.moveUp(blzMap)
    elif (direction == Direction.DOWN):
      return blzBlock.moveDown(blzMap)
    elif (direction == Direction.RIGHT):
      return blzBlock.moveRight(blzMap)
    else:
      return blzBlock.moveLeft(blzMap)
  else: pass