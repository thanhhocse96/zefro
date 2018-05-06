# Print Bloxorz Puzzle
def bloxorzPrintMap(blzMap):
  numrows = len(blzMap)
  numcols = len(blzMap[0])
  tableString = ""
  for row in range(numrows):
      for col in range(numcols):
          tableString += blzMap[row][col] + " "
      tableString += "\n"
  print(tableString)

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
      