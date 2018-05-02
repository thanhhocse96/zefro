from level import callLevel
from utils import bloxorzPrintMap
from bloxors import State, Direction, BlzBlock, getStateStart, move

level = 1
blzMap = callLevel(level)

bloxorzPrintMap(blzMap)

block = getStateStart(blzMap)

print(block.blzBlockIdx)

bloxorzPrintMap(blzMap)

newBlock = move(block, blzMap, Direction.RIGHT)

print(newBlock.blzBlockIdx)

bloxorzPrintMap(blzMap)

newBlock = move(newBlock, blzMap, Direction.DOWN)

print(newBlock.blzBlockIdx)

bloxorzPrintMap(blzMap)

newBlock = move(newBlock, blzMap, Direction.UP)

print(newBlock.blzBlockIdx)

bloxorzPrintMap(blzMap)

newBlock = move(newBlock, blzMap, Direction.LEFT)

print(newBlock.blzBlockIdx)

bloxorzPrintMap(blzMap)