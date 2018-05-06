from bloxors import State, Direction, BlzBlock, getStateStart, move, checkBlockInList
from utils import returnGoalOfMap

"""Return trace list
DFS search"""
def DFS(blzMap, blzStartBlock):
  blzStack = [blzStartBlock]
  
  blzTrace = []
  # Check the goal of Map
  goal = returnGoalOfMap(blzMap)

  while (len(blzStack) != 0): 
    curBlock = blzStack.pop()
    curBlock.checkMovable(blzMap)
   
    print ("Cur block: ", curBlock.blzBlockIdx, curBlock.blzState)
    
    # Match to Goal -> Break the Loop
    if(curBlock.blzBlockIdx == goal and curBlock.blzState == State.STAND):
      blzTrace.append(curBlock)
      break
        
    if (checkBlockInList(curBlock, blzTrace) == False):
      blzTrace.append(curBlock)

      lenCur = len(curBlock.blzMovable)
      for i in range(lenCur):
        if (curBlock.blzMovable[i] == True):
          
          nextBlock = move(curBlock, blzMap, Direction(i))
          nextBlock.checkMovable(blzMap)
          blzStack.append(nextBlock)
          
        else: 
          continue
    else:
      continue
    
  return blzTrace

"""BFS search"""
def BFS():
  pass    