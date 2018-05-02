from bloxors import State, Direction, BlzBlock, getStateStart, move

def DFS(blzMap, blzBlock):
  # Stack used for DFS
  blzStack = []
  blzStack.append(blzBlock)

  # Trace List use for reCreat the moving of DFS
  blzTrace = []

  while (len(blzStack) != 0):
    block = blzStack.pop()
    block.checkMovable()
    if()
