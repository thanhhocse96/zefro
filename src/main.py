from level import callLevel
from utils import bloxorzPrintMap
from bloxors import State, Direction, BlzElement, getStateStart
from solver import DFS

level = 1
blzMap = callLevel(level)
blzStart = getStateStart(blzMap)

bloxorzPrintMap(blzMap)

A = DFS(blzMap,blzStart)

lenA = len(A)

print (lenA)
print(A[lenA - 1].BlzElementIdx)