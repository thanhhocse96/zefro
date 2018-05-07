import tkinter as tk
import time 

from utils import checkLevelInput, bloxorzPrintMap, bloxorzPrintMapWithBlk
from level import callLevel
from bloxors import getStateStart
from solver import DFS

MAX_LEVEL = 5
level = 0
blzMap = []
class Bloxorz(tk.Frame):
    def __init__(self, master):
      tk.Frame.__init__(self, master)
     

      # create a prompt, an input box, an output label,
      # and a button to do the computation
      self.prompt = tk.Label(self, text="Xin mời bạn chọn Level:", anchor="w")
      self.entry = tk.Entry(self)
      self.submit = tk.Button(self, text="Mở map", command = self.loadMap, anchor='s')
      self.DFSsolve = tk.Button(self, text="DFS Solving", command = self.DFSSolver, anchor='s')
      self.BFSsolve = tk.Button(self, text="BFS Solving", anchor='s')
      self.next = tk.Button(self, text="Bước sau")
      self.prev = tk.Button(self, text="Bước trước")
      self.output = tk.Label(self, text="")
      self.winfo_toplevel().title("BLOXORZ")

      # Use for solving
      blzMap = []
      self.level = 0
      self.step = []
      self.timeSolve = 0
      self.stepMoving = -1
      # lay the widgets out on the screen. 
      self.prompt.pack(side="top", fill="x")
      self.entry.pack(side="top", fill="x", padx=30)
      self.output.pack(side="top", fill="x", expand=True)
      self.submit.pack(side="left")
      
      

    def loadMap(self):
      # get the value from the input widget, convert
      # it to an int, and do a calculation
      try:
          i = int(self.entry.get())
          if (checkLevelInput(i)):
            result = bloxorzPrintMap(callLevel(i))
            self.level = i
            result += " \n \n LEVEL: " + str(i)
            blzMap = callLevel(self.level)
            self.startBlk = getStateStart(blzMap)
            note = "\n \n CHÚ THÍCH: \n[+] : Các ô trống có thể di chuyển \n[_] : Các ô không thể di chuyển \n[S] : Ô bắt đầu của trò chơi\n[G]: Ô kết thúc của trò chơi\n[B]: Các ô mà Block hiện diện "
            result += note
            self.BFSsolve.pack(side = "right")
            self.DFSsolve.pack(side = "right", padx = (20,1))
          else:
            result = "Vui lòng chọn level từ 1-" + str(MAX_LEVEL)
      except ValueError:
          result = "Vui lòng chọn level từ 1-" + str(MAX_LEVEL)

      # set the output widget to have our result
      self.output.configure(text=result)

    def DFSSolver(self):
      self.prev.pack(side="left", anchor='n')
      self.next.pack(side="left", anchor='n')
      solveBlzMap = blzMap
      startBlk = getStateStart(blzMap)

      start = time.time()
      self.step = DFS(solveBlzMap, startBlk)
      end = time.time()
      self.timeSolve = end - start

      self.stepMoving = 0
      result = bloxorzPrintMapWithBlk(solveBlzMap, self.startBlk)
      self.output.configure(text=result)

    def nextStep(self):
      if (self.stepMoving < 0 or self.stepMoving > len(self.step)):
        result = "\n KHÔNG DI CHUYỂN ĐƯỢC"
        self.output.configure(text=result)
      




# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

if __name__ == "__main__":
    root = tk.Tk()
    Bloxorz(root).pack(fill="both", expand=True)
    root.mainloop()