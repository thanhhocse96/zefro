from level import callLevel
from utils import bloxorzPrintMap
from bloxors import State, Direction, BlzElement, getStateStart, moveRight

level = 1
blzMap = callLevel(level)

bloxorzPrintMap(blzMap)

block = getStateStart(blzMap)

print(block.BlzElementIdx)

bloxorzPrintMap(blzMap)

newBlock = moveRight(block, blzMap)

print(newBlock.BlzElementIdx)

bloxorzPrintMap(blzMap)