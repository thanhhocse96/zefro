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
    GROUND_HOZ = 2  # Horizontal
    GROUND_VEC = 3  # Vectical

# Direction on Bloxorz map


class Direction(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# -----------Begin class BlzBlock
class BlzBlock:
    def __init__(self):
        self.blzState = State.DONTKNOW
        # Index of Bloxorz Element [[row1, col1],[row2, col2]]
        # If state: STAND => row2 = col2 = -1
        self.blzBlockIdx = [[-1, -1], [-1, -1]]
        # Direction where Block can move to
        # Index: UP, DOWN, LEFT, RIGHT
        self.blzMovable = [True, True, True, True]

    """Check if Block can be movable
    Update blzMovable"""
    def checkMovable(self, blzMap):
        # Use to check the condition block can move
        numrows = len(blzMap)
        numcols = len(blzMap[0])

        # Switch between state
        if (self.blzState == State.STAND):
            # Move Right
            colR1 = self.blzBlockIdx[0][1] + 1
            colR2 = self.blzBlockIdx[0][1] + 2
            rowR = self.blzBlockIdx[0][0]
            self.blzMovable[int(Direction.RIGHT)] = False if (colR1 >= numcols or colR2 >= numcols) else True
            self.blzMovable[int(Direction.RIGHT)] = False if (blzMap[rowR][colR1] == '.' or blzMap[rowR][colR2] == '.') else True

            # Move Left
            colL1 = self.blzBlockIdx[0][1] - 2
            colL2 = self.blzBlockIdx[0][1] - 1
            rowL = self.blzBlockIdx[0][0]
            self.blzMovable[int(Direction.LEFT)] = False if (colL1 < 0 or colL2 < 0) else True
            self.blzMovable[int(Direction.LEFT)] = False if (blzMap[rowL][colL1] == '.' or blzMap[rowL][colL2] == '.') else True

            # Move Up
            rowU1 = self.blzBlockIdx[0][0] - 2
            rowU2 = self.blzBlockIdx[0][0] - 1
            colU = self.blzBlockIdx[0][1]
            self.blzMovable[int(Direction.UP)] = False if (rowU1 < 0 or rowU2 < 0) else True
            self.blzMovable[int(Direction.UP)] = False if (blzMap[rowU1][colU] == '.' or blzMap[rowU2][colU] == '.') else True

            # Move Down
            rowD1 = self.blzBlockIdx[0][0] + 1
            rowD2 = self.blzBlockIdx[0][0] + 2
            colD = self.blzBlockIdx[0][1]
            self.blzMovable[int(Direction.DOWN)] = False if (rowD1 >= numrows or rowD2 >= numrows) else True
            self.blzMovable[int(Direction.UP)] = False if (blzMap[rowU1][colD] == '.' or blzMap[rowU2][colD] == '.') else True

        elif (self.blzState == State.GROUND_HOZ):
            # Move Right
            colR = self.blzBlockIdx[1][1] + 1
            rowR = self.blzBlockIdx[0][0]
            self.blzMovable[int(Direction.RIGHT)] = False if (colR >= numcols) else True
            self.blzMovable[int(Direction.RIGHT)] = False if (blzMap[rowR][colR] == '.') else True

            # Move Left
            colL = self.blzBlockIdx[0][1] - 1
            self.blzMovable[int(Direction.LEFT)] = False if (
                colL < 0) else True
            # Move Up
            rowU = self.blzBlockIdx[0][0] - 1
            self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
            # Move Down
            rowD = self.blzBlockIdx[0][0] + 1
            self.blzMovable[int(Direction.DOWN)] = False if (rowD >= numrows) else True

        elif (self.blzState == State.GROUND_VEC):
            # Move Right
            colR = self.blzBlockIdx[0][1] + 1
            self.blzMovable[int(Direction.RIGHT)] = False if (
                colR >= numcols) else True
            # Move Left
            colL = self.blzBlockIdx[0][1] - 1
            self.blzMovable[int(Direction.LEFT)] = False if (
                colL < 0) else True
            # Move Up
            rowU = self.blzBlockIdx[0][0] - 1
            self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
            # Move Down
            rowD = self.blzBlockIdx[1][0] + 1
            self.blzMovable[int(Direction.DOWN)] = False if (rowD >= numrows) else True
        else:
            pass

    """Check the Block in the Finish position
    Return: True - Block in Finish postion
            False - Unless
    """
    def checkFinish(self, blzMap):
      row = self.blzBlockIdx[0][0]
      col = self.blzBlockIdx[0][1]
      state = self.blzState
      if(state == State.STAND and blzMap[row][col] == 'G'):
        return True
      else:
        return False

# -----------End class BlzBlock


"""Goal: Get State, Index of Blozorx block
Update state of Bloxorz Map
Return: blockStart (State, Index, Movable list)
"""


def getStateStart(blzMap):
    blockStart = BlzBlock()

    numrows = len(blzMap)
    numcols = len(blzMap[0])
    for row in range(numrows):
        for col in range(numcols):
            if blzMap[row][col] == 'S':
                blockStart.blzState = State.STAND
                blockStart.blzBlockIdx[0][0] = row
                blockStart.blzBlockIdx[0][1] = col

                # BLOXORZ: B => block stand here
                blzMap[row][col] = 'B'
                return blockStart

    return blockStart

"""Return the new BlzBlock Object
Simplyfied approach"""
def move(blzBlock, blzMap, direction):
  if (blzBlock.blzMovable[int(direction)]):
    if(direction == Direction.UP):
      return moveUp(blzBlock, blzMap)
    elif (direction == Direction.DOWN):
      return moveDown(blzBlock, blzMap)
    elif (direction == Direction.RIGHT):
      return moveRight(blzBlock, blzMap)
    else:
      return moveLeft(blzBlock, blzMap)
  else: 
    return None

"""Return True: Have blzBlock in blzList"""
def checkBlockInList(blzBlock, blzList):
  for i in range(len(blzList)):
    if (blzList[i].blzBlockIdx == blzBlock.blzBlockIdx):
      return True
  return False

# -----------Begin move function
"""Move Right
Return:
+ new Block - the block move Right
+ None - the block can't move"""

def moveRight(block, blzMap):
    block.checkMovable(blzMap)
    newBlz = BlzBlock()

    if (block.blzMovable[int(Direction.RIGHT)]):
            # STAND
        if (block.blzState == State.STAND):
                # Update next state
            newBlz.blzState = State.GROUND_HOZ

            # Remove current position
            blzMap[block.blzBlockIdx[0][0]
                   ][block.blzBlockIdx[0][1]] = '+'
            # Update
            row = block.blzBlockIdx[0][0]
            col1 = block.blzBlockIdx[0][1] + 1
            col2 = block.blzBlockIdx[0][1] + 2
            # Update Location of Block
            newBlz.blzBlockIdx = [[row, col1], [row, col2]]
            # Update Map
            blzMap[row][col1] = blzMap[row][col2] = 'B'

        # GROUND HORIZONTAL
        elif (block.blzState == State.GROUND_HOZ):
            # Update next state
            newBlz.blzState = State.STAND

            # Remove current position
            blzMap[block.blzBlockIdx[0][0]
                   ][block.blzBlockIdx[0][1]] = '+'
            blzMap[block.blzBlockIdx[1][0]
                   ][block.blzBlockIdx[1][1]] = '+'
            # Update
            row = block.blzBlockIdx[0][0]
            col = block.blzBlockIdx[1][1] + 1
            # Update Location of Block
            newBlz.blzBlockIdx = [[row, col], [-1, -1]]
            # Update Map
            blzMap[row][col] = 'B'

        # GROUND VECTICAL
        elif (block.blzState == State.GROUND_VEC):
            # Update next state
            newBlz.blzState = State.GROUND_VEC

            # Remove current position
            blzMap[block.blzBlockIdx[0][0]
                   ][block.blzBlockIdx[0][1]] = '+'
            blzMap[block.blzBlockIdx[1][0]
                   ][block.blzBlockIdx[1][1]] = '+'
            # Update
            row1 = block.blzBlockIdx[0][0] + 1
            row2 = block.blzBlockIdx[1][0] + 1
            col = block.blzBlockIdx[0][1]
            # Update Location of Block
            newBlz.blzBlockIdx = [[row1, col], [row2, col]]
            # Update Map
            blzMap[row1][col] = blzMap[row2][col] = 'B'
        else:
            pass

        return newBlz
    else:
        return None


"""Move Left
  Return:
  + new Block - the block move Left
  + None - the block can't move"""

def moveLeft(block, blzMap):
  block.checkMovable(blzMap)
  newBlz = BlzBlock()

  if (block.blzMovable[int(Direction.LEFT)]):
    # STAND
    if (block.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[block.blzBlockIdx[0][0]
                ][block.blzBlockIdx[0][1]] = '+'
        # Update
        row = block.blzBlockIdx[0][0]
        col1 = block.blzBlockIdx[0][1] - 2
        col2 = block.blzBlockIdx[0][1] - 1
        # Update Location of Block
        newBlz.blzBlockIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'

    # GROUND HORIZONTAL
    elif (block.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[block.blzBlockIdx[0][0]
                ][block.blzBlockIdx[0][1]] = '+'
        blzMap[block.blzBlockIdx[1][0]
                ][block.blzBlockIdx[1][1]] = '+'
        # Update
        row = block.blzBlockIdx[0][0]
        col = block.blzBlockIdx[0][1] - 1
        # Update Location of Block
        newBlz.blzBlockIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'

    # GROUND VECTICAL
    elif (block.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[block.blzBlockIdx[0][0]
                ][block.blzBlockIdx[0][1]] = '+'
        blzMap[block.blzBlockIdx[1][0]
                ][block.blzBlockIdx[1][1]] = '+'
        # Update
        row1 = block.blzBlockIdx[0][0]
        row2 = block.blzBlockIdx[1][0]
        col = block.blzBlockIdx[0][1] - 1
        # Update Location of Block
        newBlz.blzBlockIdx = [[row1, col], [row2, col]]
        # Update Map
        blzMap[row1][col] = blzMap[row2][col] = 'B'
    else:
        pass

    return newBlz
  else:
    return None

"""Move Up
Return: 
+ new Block - the block move Up
+ None - the block can't move"""
def moveUp(block, blzMap):
  block.checkMovable(blzMap)
  newBlz = BlzBlock()

  if (block.blzMovable[int(Direction.UP)]):
      # STAND
      if (block.blzState == State.STAND):
          # Update next state
          newBlz.blzState = State.GROUND_VEC

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          # Update
          row1 = block.blzBlockIdx[0][0] - 2
          row2 = block.blzBlockIdx[0][0] - 1
          col = block.blzBlockIdx[0][1]
          # Update Location of Block
          newBlz.blzBlockIdx = [[row1, col], [row2, col]]
          # Update Map
          blzMap[row1][col] = blzMap[row2][col] = 'B'

      # GROUND HORIZONTAL
      elif (block.blzState == State.GROUND_HOZ):
          # Update next state
          newBlz.blzState = State.GROUND_HOZ

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          blzMap[block.blzBlockIdx[1][0]
                  ][block.blzBlockIdx[1][1]] = '+'
          # Update
          row = block.blzBlockIdx[0][0] - 1
          col1 = block.blzBlockIdx[0][1]
          col2 = block.blzBlockIdx[1][1]
          # Update Location of Block
          newBlz.blzBlockIdx = [[row, col1], [row, col2]]
          # Update Map
          blzMap[row][col1] = blzMap[row][col2] = 'B'

      # GROUND VECTICAL
      elif (block.blzState == State.GROUND_VEC):
          # Update next state
          newBlz.blzState = State.STAND

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          blzMap[block.blzBlockIdx[1][0]
                  ][block.blzBlockIdx[1][1]] = '+'
          # Update
          row = block.blzBlockIdx[0][0] - 1
          col = block.blzBlockIdx[0][1]

          # Update Location of Block
          newBlz.blzBlockIdx = [[row, col], [-1, -1]]
          # Update Map
          blzMap[row][col] = 'B'
      else:
          pass

      return newBlz
  else:
      return None

"""Move Down
Return: 
+ True - the block move Down
+ False - the block can't move"""
def moveDown(block, blzMap):
  block.checkMovable(blzMap)
  newBlz = BlzBlock()
  if (block.blzMovable[int(Direction.DOWN)]):
      # STAND
      if (block.blzState == State.STAND):
          # Update next state
          newBlz.blzState = State.GROUND_VEC

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          # Update
          row1 = block.blzBlockIdx[0][0] + 1
          row2 = block.blzBlockIdx[0][0] + 2
          col = block.blzBlockIdx[0][1]
          # Update Location of Block
          newBlz.blzBlockIdx = [[row1, col], [row2, col]]
          # Update Map
          blzMap[row1][col] = blzMap[row2][col] = 'B'

      # GROUND HORIZONTAL
      elif (block.blzState == State.GROUND_HOZ):
          # Update next state
          newBlz.blzState = State.GROUND_HOZ

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          blzMap[block.blzBlockIdx[1][0]
                  ][block.blzBlockIdx[1][1]] = '+'
          # Update
          row = block.blzBlockIdx[0][0] + 1
          col1 = block.blzBlockIdx[0][1]
          col2 = block.blzBlockIdx[1][1]
          # Update Location of Block
          newBlz.blzBlockIdx = [[row, col1], [row, col2]]
          # Update Map
          blzMap[row][col1] = blzMap[row][col2] = 'B'

      # GROUND VECTICAL
      elif (block.blzState == State.GROUND_VEC):
          # Update next state
          newBlz.blzState = State.STAND

          # Remove current position
          blzMap[block.blzBlockIdx[0][0]
                  ][block.blzBlockIdx[0][1]] = '+'
          blzMap[block.blzBlockIdx[1][0]
                  ][block.blzBlockIdx[1][1]] = '+'
          # Update
          row = block.blzBlockIdx[1][0] + 1
          col = block.blzBlockIdx[0][1]

          # Update Location of Block
          newBlz.blzBlockIdx = [[row, col], [-1, -1]]
          # Update Map
          blzMap[row][col] = 'B'
      else:
          pass

      return newBlz
  else:
      return None

# -----------End move function
