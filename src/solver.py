from bloxors import State, Direction, BlzElement, move
from collections import deque

def DFS(blzMap, blzStartElement):
  # blzStack: Depth-first search stack
  blzStack = []
  blzStack.append(blzStartElement)
  # blzStack: Tracing List for Drawing every state 
  blzTrace = []

  print(Direction(1))

  # DFS iterative way
  while (len(blzStack)):
    vertex = blzStack.pop()
    if (blzTrace.count(vertex) == 0):
      blzTrace.append(vertex)
      for i in range(len(vertex.BlzElementIdx)):
        if(vertex.blzMovable[i]):
          newVex = move(vertex, blzMap, Direction(i))
          blzStack.append(newVex)
        else:
          continue 

  return blzTrace


