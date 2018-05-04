from level import callLevel
from utils import bloxorzPrintMap
from bloxors import State, Direction, BlzBlock, getStateStart, move
from solver import DFS

level = 1
blzMap = callLevel(level)

bloxorzPrintMap(blzMap)

block = getStateStart(blzMap)

print(block.blzBlockIdx)

bloxorzPrintMap(blzMap)

# newBlock = move(block, blzMap, Direction(1))

# newBlock2 = move(newBlock, blzMap, Direction(0))

# print(newBlock2.blzBlockIdx)

# print (newBlock2 == block)

# print(newBlock.blzBlockIdx)

bloxorzPrintMap(blzMap)

blzSolver = DFS(blzMap, block)

lenSolver = len(blzSolver)

print(lenSolver)

print(blzSolver[lenSolver - 1].blzBlockIdx)