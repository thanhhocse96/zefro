from level import *
from utils import *
from bloxors import *

map = callLevel(1)

bloxorzPrintMap(map)

blzBlock = blzElement()

blzBlock.getStateStart(map)

print(blzBlock.blzState, '; \n', blzBlock.blzElementIdx, '\n', blzBlock.blzMovable)

blzBlock.checkMovable(map)

print(blzBlock.blzMovable)

bloxorzPrintMap(map)
print('right')
blzBlock.moveRight(map)
bloxorzPrintMap(map)
print('left')
blzBlock.moveLeft(map)
bloxorzPrintMap(map)
print('down')
blzBlock.moveDown(map)

bloxorzPrintMap(map)
print('up')
blzBlock.moveUp(map)

bloxorzPrintMap(map)
print('down')
blzBlock.moveDown(map)

bloxorzPrintMap(map)
print('left')
blzBlock.moveLeft(map)
bloxorzPrintMap(map)
print('down')
blzBlock.moveDown(map)

bloxorzPrintMap(map)
print('up')
blzBlock.moveUp(map)

bloxorzPrintMap(map)

blzBlock.checkMovable(map)

print(blzBlock.blzElementIdx)
blzBlock.checkMovable(map)



print(blzBlock.blzMovable)