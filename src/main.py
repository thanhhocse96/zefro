import random
import os
import time

from level import callLevel
from utils import bloxorzPrintMap, checkLevelInput, bloxorzPrintMapWithBlk
from bloxors import State, Direction, BlzBlock, getStateStart, move
from solver import DFS

# Clear Screen
def clearScr():
    os.system('cls' if os.name=='nt' else 'clear')


MAX_LEVEL = 5

# Opening game 
level = random.randint(1,MAX_LEVEL)

print("Generate Level - Sinh ngẫu nhiên Level: ", level)

blzMap = callLevel(level)

initMap = bloxorzPrintMap(blzMap)

print("Initial Map - Trò chơi ban đầu: \n")
print(initMap)

# Chose the Algorithm
solvingInput = -1

while(solvingInput == -1):
  inputA = input("Bạn muốn dùng thuật toán nào?\n1: D.F.S\n2: B.F.S\n")
  if(int(inputA) == 1 or int(inputA) == 2):
    solvingInput = int(inputA)
  else:
    solvingInput = -1

block = getStateStart(blzMap)
tempMap = initMap

start = time.time()
# Solving
if (solvingInput == 1):
  blkList = DFS(blzMap, block)
else:
  pass
end = time.time()

# Measure the time Solving
timeSolve = (end - start)

if(solvingInput == 1):
  result = "Thuật toán DFS\n"
  result += "Thời gian thực thi: " + str(timeSolve) + '\n'
elif(solvingInput == 2):
  result = "Thuật toán BFS - chưa có lời giải\n"

print(result)