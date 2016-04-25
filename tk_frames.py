import tkinter as tk
from tkinter.ttk import *

class playerFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        ##Objects
        self.child = tk.Frame(self.parent, height=2, bd=1, relief='groove', borderwidth=4)
        self.nextGenButton = tk.Button(self.child, text = ">")
        self.prevGenButton = tk.Button(self.child, text = "<")

        self.gameFrame = tk.Frame(self.parent)

        gameOps = ["Game Of Life", "Battleship", "Tetris"]

        self.comboBox = Combobox(self.child, values = gameOps)
        
        ##Packing
        self.child.pack(side='right')
        self.nextGenButton.pack(side='right', padx=5)
        self.prevGenButton.pack(side='right', padx=5)
        self.comboBox.pack(side='right', padx=5)
        self.gameFrame.pack(side='right', padx=5)

        self.comboBox.bind('<<ComboboxSelected>>', self.handler)
        

    def handler(self, event=None):
        try:
            self.gameFrame.child.pack_forget()
        except:
            None
        current = self.comboBox.current()
        if current != -1:
            if current == 0:
                self.gameFrame = LifePanel(self.gameFrame)
                self.gameFrame.pack(side='right', padx=5)
            elif current == 1:
                self.gameFrame = BattleshipPanel(self.gameFrame)
                self.gameFrame.pack(side='right', padx=5)
            else:
                self.gameFrame = TetrisPanel(self.gameFrame)
                self.gameFrame.pack(side='right', padx=5)

class LifePanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.child = tk.Frame(self.parent, height=2, bd=1, relief='groove', borderwidth=4)
        
        self.frameLife = tk.Frame(self.child)
        self.liveCondLabel = tk.Label(self.frameLife, text = "Reproduction Condition")
        self.liveEntry = tk.Entry(self.frameLife)

        self.frameDeath = tk.Frame(self.child)
        self.deathCondLabel = tk.Label(self.frameDeath, text = "Death Condition")
        self.deathEntry = tk.Entry(self.frameDeath)

        self.child.pack()
        self.liveCondLabel.pack(side='top', pady=5)
        self.liveEntry.pack(side="top")
        self.deathCondLabel.pack(side='top', pady=5)
        self.deathEntry.pack(side="top")
        self.frameLife.pack(side="right")
        self.frameDeath.pack(side="right")
        

class BattleshipPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.child = tk.Frame(self.parent, height=2, bd=1, relief='groove', borderwidth=4)
        self.nextGenButton = tk.Button(self.child, text = "Battleship")

        self.child.pack(side='right')
        self.nextGenButton.pack(side='right', padx=5)

class TetrisPanel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.child = tk.Frame(self.parent, height=2, bd=1, relief='groove', borderwidth=4)
        self.nextGenButton = tk.Button(self.child, text = "Tetris")

        self.child.pack(side='right')
        self.nextGenButton.pack(side='right', padx=5)
        

class DensityFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.bool = False

        self.child = tk.Frame(self.parent, height=2, bd=1, relief='groove', borderwidth=4)
        self.enableDensity = tk.Checkbutton(self.child, text="Density", variable=self.bool)
        self.subChild = tk.Frame(self.child)

        maxLabel=Label(self.subChild, text="Maximum Distance")
        self.maxScale = tk.Scale(self.subChild, from_=0, to=142, orient=tk.HORIZONTAL)
        maxLabel.pack(side = tk.BOTTOM)
        self.maxScale.pack(side = tk.BOTTOM)

        self.child.pack()
        self.enableDensity.pack()
        #self.subChild.pack()

        self.enableDensity.bind("<Button-1>", self.checkToggled)

    def checkToggled(self, event=None):
        if self.bool is False:
            self.subChild.pack()
        else:
            self.subChild.pack_forget()
        self.bool = not self.bool

if __name__=="__main__":
    root=tk.Tk()
    player = DensityFrame(root)
    root.mainloop()
