from bloxors import State, Direction, BlzBlock, getStateStart, move, checkBlockInList


def DFS(blzMap, blzStartBlock):
  blzStack = [blzStartBlock]
  
  blzTrace = []

  while (len(blzStack) != 0): 
    curBlock = blzStack.pop()
    curBlock.checkMovable(blzMap)

    # Debug
    print ("Cur block: ", curBlock.blzBlockIdx)
    if (not(checkBlockInList(curBlock, blzTrace))):
      blzTrace.append(curBlock)

      lenCur = len(curBlock.blzMovable)
      print (lenCur)
      for i in range(lenCur):
        if (curBlock.blzMovable[i] == True):
          print("next",Direction(i), curBlock.blzMovable[i])
          nextBlock = move(curBlock, blzMap, Direction(i))
          nextBlock.checkMovable(blzMap)
          blzStack.append(nextBlock)
           # Debug
          print ("Next block: ", nextBlock.blzBlockIdx)
        else: 
          continue
    else:
      continue
    if (curBlock.checkFinish(blzMap)):
      break
  return blzTrace

def BFS():
  pass    