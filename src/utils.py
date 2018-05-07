from bloxors import State

# Print Bloxorz Puzzle
def bloxorzPrintMap(blzMap):
    numrows = len(blzMap)
    numcols = len(blzMap[0])
    tableString = ""
    for row in range(numrows):
        for col in range(numcols):
            if(blzMap[row][col] == '.'):
              char = '_'
            else:
              char = blzMap[row][col]
            tableString += char + " "
        tableString += "\n"
    return tableString

# Print Bloxorz Puzzle with Block
def bloxorzPrintMapWithBlk(blzMap, blockBlz):
    numrows = len(blzMap)
    numcols = len(blzMap[0])

    block = blockBlz.blzBlockIdx
    tempBlzMap = blzMap
  
    tableString = ""
    for row in range(numrows):
      for col in range(numcols):
        if(tempBlzMap[row][col] == '.'):
          char = '_'
        else:
          if((row == block[0][0] and col == block[0][1]) or (row == block[1][0] and col == block[1][1])):
            char = 'B'
          else: 
            char = '+'
        tableString += char + " "
      tableString += "\n"
    return tableString

# Get Goal Position
def returnGoalOfMap(blzMap):
    numrows = len(blzMap)
    numcols = len(blzMap[0])

    a = b = -1

    for row in range(numrows):
        for col in range(numcols):
            if(blzMap[row][col] == 'G'):
                a = row
                b = col

    return [[a, b], [-1, -1]]

# Check if level match with the condition of Level


def checkLevelInput(levelInput):
    if(type(levelInput) is int and 0 < levelInput <= 5):
        return True
    else:
        return False
