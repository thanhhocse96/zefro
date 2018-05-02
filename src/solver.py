from bloxors import State, Direction, BlzBlock, getStateStart, move

def DFS(blzMap, blzBlock):
  # Stack used for DFS
  blzStack = []
  blzStack.append(blzBlock)

  # Trace List use for reCreat the moving of DFS
  blzTrace = []

  while (len(blzStack) != 0):
    block = blzStack.pop()
    block.checkMovable(blzMap)

    blzTrace.append(block)
    if(block.):
      for dicr in range(len(block.blzMovable)):
        direction = Direction(dicr)
        if(block.blzMovable[dicr]):
          newBlock = move(block, blzMap, direction)
          newBlock.checkMovable(blzMap)
          blzStack.append(newBlock)

          blzTrace.append(newBlock)
        else: 
          continue 
    
    
  return blzTrace
