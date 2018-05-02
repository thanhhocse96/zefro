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
