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

# -----------Begin class BlzElement


class BlzElement:
    def __init__(self):
        self.blzState = State.DONTKNOW
        # Index of Bloxorz Element [[row1, col1],[row2, col2]]
        # If state: STAND => row2 = col2 = -1
        self.BlzElementIdx = [[-1, -1], [-1, -1]]
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
            colR1 = self.BlzElementIdx[0][1] + 1
            colR2 = self.BlzElementIdx[0][1] + 2
            self.blzMovable[int(Direction.RIGHT)] = False if (
                colR1 >= numcols or colR2 >= numcols) else True
            # Move Left
            colL1 = self.BlzElementIdx[0][1] - 2
            colL2 = self.BlzElementIdx[0][1] - 1
            self.blzMovable[int(Direction.LEFT)] = False if (
                colL1 < 0 or colL2 < 0) else True
            # Move Up
            rowU1 = self.BlzElementIdx[0][0] - 2
            rowU2 = self.BlzElementIdx[0][0] - 1
            self.blzMovable[int(Direction.UP)] = False if (
                rowU1 < 0 or rowU2 < 0) else True
            # Move Down
            rowD1 = self.BlzElementIdx[0][0] + 1
            rowD2 = self.BlzElementIdx[0][0] + 2
            self.blzMovable[int(Direction.DOWN)] = False if (
                rowD1 >= numrows or rowD2 >= numrows) else True

        elif (self.blzState == State.GROUND_HOZ):
            # Move Right
            colR = self.BlzElementIdx[1][1] + 1
            self.blzMovable[int(Direction.RIGHT)] = False if (
                colR >= numcols) else True
            # Move Left
            colL = self.BlzElementIdx[0][1] - 1
            self.blzMovable[int(Direction.LEFT)] = False if (
                colL < 0) else True
            # Move Up
            rowU = self.BlzElementIdx[0][0] - 1
            self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
            # Move Down
            rowD = self.BlzElementIdx[0][0] + 1
            self.blzMovable[int(Direction.DOWN)] = False if (
                rowD < 0) else True

        elif (self.blzState == State.GROUND_VEC):
            # Move Right
            colR = self.BlzElementIdx[0][1] + 1
            self.blzMovable[int(Direction.RIGHT)] = False if (
                colR >= numcols) else True
            # Move Left
            colL = self.BlzElementIdx[0][1] - 1
            self.blzMovable[int(Direction.LEFT)] = False if (
                colL < 0) else True
            # Move Up
            rowU = self.BlzElementIdx[0][0] - 1
            self.blzMovable[int(Direction.UP)] = False if (rowU < 0) else True
            # Move Down
            rowD = self.BlzElementIdx[1][0] + 1
            self.blzMovable[int(Direction.DOWN)] = False if (
                rowD < 0) else True
        else:
            pass

# -----------End class BlzElement


"""Goal: Get State, Index of Blozorx block
Update state of Bloxorz Map
Return: blockStart (State, Index, Movable list)
"""


def getStateStart(blzMap):
    blockStart = BlzElement()

    numrows = len(blzMap)
    numcols = len(blzMap[0])
    for row in range(numrows):
        for col in range(numcols):
            if blzMap[row][col] == 'S':
                blockStart.blzState = State.STAND
                blockStart.BlzElementIdx[0][0] = row
                blockStart.BlzElementIdx[0][1] = col

                # BLOXORZ: B => block stand here
                blzMap[row][col] = 'B'
                return blockStart

    return blockStart


"""Move Right
Return:
+ new Block - the block move Right
+ None - the block can't move"""


def moveRight(block, blzMap):
    block.checkMovable(blzMap)
    newBlz = BlzElement()

    if (block.blzMovable[int(Direction.RIGHT)]):
            # STAND
        if (block.blzState == State.STAND):
                # Update next state
            newBlz.blzState = State.GROUND_HOZ

            # Remove current position
            blzMap[block.BlzElementIdx[0][0]
                   ][block.BlzElementIdx[0][1]] = '+'
            # Update
            row = block.BlzElementIdx[0][0]
            col1 = block.BlzElementIdx[0][1] + 1
            col2 = block.BlzElementIdx[0][1] + 2
            # Update Location of Block
            newBlz.BlzElementIdx = [[row, col1], [row, col2]]
            # Update Map
            blzMap[row][col1] = blzMap[row][col2] = 'B'

        # GROUND HORIZONTAL
        elif (block.blzState == State.GROUND_HOZ):
            # Update next state
            newBlz.blzState = State.STAND

            # Remove current position
            blzMap[block.BlzElementIdx[0][0]
                   ][block.BlzElementIdx[0][1]] = '+'
            blzMap[block.BlzElementIdx[1][0]
                   ][block.BlzElementIdx[1][1]] = '+'
            # Update
            row = block.BlzElementIdx[0][0]
            col = block.BlzElementIdx[1][1] + 1
            # Update Location of Block
            newBlz.BlzElementIdx = [[row, col], [-1, -1]]
            # Update Map
            blzMap[row][col] = 'B'

        # GROUND VECTICAL
        elif (block.blzState == State.GROUND_VEC):
            # Update next state
            newBlz.blzState = State.GROUND_VEC

            # Remove current position
            blzMap[block.BlzElementIdx[0][0]
                   ][block.BlzElementIdx[0][1]] = '+'
            blzMap[block.BlzElementIdx[1][0]
                   ][block.BlzElementIdx[1][1]] = '+'
            # Update
            row1 = block.BlzElementIdx[0][0] + 1
            row2 = block.BlzElementIdx[1][0] + 1
            col = block.BlzElementIdx[0][1]
            # Update Location of Block
            newBlz.BlzElementIdx = [[row1, col], [row2, col]]
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
  newBlz = BlzElement()

  if (block.blzMovable[int(Direction.LEFT)]):
    # STAND
    if (block.blzState == State.STAND):
        # Update next state
        newBlz.blzState = State.GROUND_HOZ

        # Remove current position
        blzMap[block.BlzElementIdx[0][0]
                ][block.BlzElementIdx[0][1]] = '+'
        # Update
        row = block.BlzElementIdx[0][0]
        col1 = block.BlzElementIdx[0][1] - 2
        col2 = block.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col1], [row, col2]]
        # Update Map
        blzMap[row][col1] = blzMap[row][col2] = 'B'

    # GROUND HORIZONTAL
    elif (block.blzState == State.GROUND_HOZ):
        # Update next state
        newBlz.blzState = State.STAND

        # Remove current position
        blzMap[block.BlzElementIdx[0][0]
                ][block.BlzElementIdx[0][1]] = '+'
        blzMap[block.BlzElementIdx[1][0]
                ][block.BlzElementIdx[1][1]] = '+'
        # Update
        row = block.BlzElementIdx[0][0]
        col = block.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row, col], [-1, -1]]
        # Update Map
        blzMap[row][col] = 'B'

    # GROUND VECTICAL
    elif (block.blzState == State.GROUND_VEC):
        # Update next state
        newBlz.blzState = State.GROUND_VEC

        # Remove current position
        blzMap[block.BlzElementIdx[0][0]
                ][block.BlzElementIdx[0][1]] = '+'
        blzMap[block.BlzElementIdx[1][0]
                ][block.BlzElementIdx[1][1]] = '+'
        # Update
        row1 = block.BlzElementIdx[0][0]
        row2 = block.BlzElementIdx[1][0]
        col = block.BlzElementIdx[0][1] - 1
        # Update Location of Block
        newBlz.BlzElementIdx = [[row1, col], [row2, col]]
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
  newBlz = BlzElement()

  if (block.blzMovable[int(Direction.UP)]):
      # STAND
      if (block.blzState == State.STAND):
          # Update next state
          newBlz.blzState = State.GROUND_VEC

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          # Update
          row1 = block.BlzElementIdx[0][0] - 2
          row2 = block.BlzElementIdx[0][0] - 1
          col = block.BlzElementIdx[0][1]
          # Update Location of Block
          newBlz.BlzElementIdx = [[row1, col], [row2, col]]
          # Update Map
          blzMap[row1][col] = blzMap[row2][col] = 'B'

      # GROUND HORIZONTAL
      elif (block.blzState == State.GROUND_HOZ):
          # Update next state
          newBlz.blzState = State.GROUND_HOZ

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          blzMap[block.BlzElementIdx[1][0]
                  ][block.BlzElementIdx[1][1]] = '+'
          # Update
          row = block.BlzElementIdx[0][0] - 1
          col1 = block.BlzElementIdx[0][1]
          col2 = block.BlzElementIdx[1][1]
          # Update Location of Block
          newBlz.BlzElementIdx = [[row, col1], [row, col2]]
          # Update Map
          blzMap[row][col1] = blzMap[row][col2] = 'B'

      # GROUND VECTICAL
      elif (block.blzState == State.GROUND_VEC):
          # Update next state
          newBlz.blzState = State.STAND

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          blzMap[block.BlzElementIdx[1][0]
                  ][block.BlzElementIdx[1][1]] = '+'
          # Update
          row = block.BlzElementIdx[0][0] - 1
          col = block.BlzElementIdx[0][1]

          # Update Location of Block
          newBlz.BlzElementIdx = [[row, col], [-1, -1]]
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
  newBlz = BlzElement()
  if (block.blzMovable[int(Direction.DOWN)]):
      # STAND
      if (block.blzState == State.STAND):
          # Update next state
          newBlz.blzState = State.GROUND_VEC

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          # Update
          row1 = block.BlzElementIdx[0][0] + 1
          row2 = block.BlzElementIdx[0][0] + 2
          col = block.BlzElementIdx[0][1]
          # Update Location of Block
          newBlz.BlzElementIdx = [[row1, col], [row2, col]]
          # Update Map
          blzMap[row1][col] = blzMap[row2][col] = 'B'

      # GROUND HORIZONTAL
      elif (block.blzState == State.GROUND_HOZ):
          # Update next state
          newBlz.blzState = State.GROUND_HOZ

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          blzMap[block.BlzElementIdx[1][0]
                  ][block.BlzElementIdx[1][1]] = '+'
          # Update
          row = block.BlzElementIdx[0][0] + 1
          col1 = block.BlzElementIdx[0][1]
          col2 = block.BlzElementIdx[1][1]
          # Update Location of Block
          newBlz.BlzElementIdx = [[row, col1], [row, col2]]
          # Update Map
          blzMap[row][col1] = blzMap[row][col2] = 'B'

      # GROUND VECTICAL
      elif (block.blzState == State.GROUND_VEC):
          # Update next state
          newBlz.blzState = State.STAND

          # Remove current position
          blzMap[block.BlzElementIdx[0][0]
                  ][block.BlzElementIdx[0][1]] = '+'
          blzMap[block.BlzElementIdx[1][0]
                  ][block.BlzElementIdx[1][1]] = '+'
          # Update
          row = block.BlzElementIdx[1][0] + 1
          col = block.BlzElementIdx[0][1]

          # Update Location of Block
          newBlz.BlzElementIdx = [[row, col], [-1, -1]]
          # Update Map
          blzMap[row][col] = 'B'
      else:
          pass

      return newBlz
  else:
      return None
