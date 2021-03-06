from tkinter import *
import tkinter as tk
import random
import math
import time
import life


from tk_frames import *

#Modules
from tiles import Grid, Tile

class GUI_Controller():
    def __init__(self, root):
    ##TK Params
        self.root=root
        self.entry = tk.Entry(root)
        root.wm_title("Anomaly v1.0")

        self.xWidth = 800
        self.yWidth = 800

    ##Frames
        self.mainFrame = tk.Frame(self.root, relief='flat', borderwidth=4)
        self.mainFrame.grid(row=0,column=0, sticky="n")

        self.bottomFrame = tk.Frame(self.root, relief='flat', borderwidth=4)
        self.bottomFrame.grid(row=1,column=1, sticky="n")

        self.playerFrame = playerFrame(self.bottomFrame)
        
        self.canvas=tk.Canvas(root, width=self.xWidth, height=self.yWidth, background='white')
        self.canvas.grid(row=0,column=1)

        self.frame1 = tk.Frame(self.mainFrame, relief='flat', borderwidth=4)
        self.frame1.grid(row=1,column=0, sticky="n")
        outlineLabel=tk.Label(self.frame1, text="Outline")
        self.outlineScale = tk.Scale(self.frame1, from_=0, to=10, orient=HORIZONTAL)
        outlineLabel.pack(side = BOTTOM)
        self.outlineScale.pack(side = BOTTOM)

        self.frame2 = tk.Frame(self.mainFrame, relief='flat', borderwidth=4)
        self.frame2.grid(row=0,column=0, sticky="n")


        self.frame3 = tk.Frame(self.mainFrame, relief='flat', borderwidth=4)
        self.frame3.grid(row=3,column=0, sticky="n")
        distLabel=Label(self.frame2, text="Current Distance:")
        self.distText = Label(self.frame2, text="", width=20)
        distLabel.pack(side = BOTTOM)
        self.distText.pack(side = BOTTOM)


        self.frame3 = tk.Frame(self.mainFrame, relief='flat', borderwidth=4)
        self.frame3.grid(row=4,column=0, sticky="n")
        tileNumLabel=tk.Label(self.frame3, text="Tiles")
        self.tileNumScale = tk.Scale(self.frame3, from_=5, to=100, orient=HORIZONTAL)
        tileNumLabel.pack(side = BOTTOM)
        self.tileNumScale.pack(side = BOTTOM)

        self.densityFrame = DensityFrame(self.frame2)

        self.xPrime = 0
        self.yPrime = 0
        

    ##Grid Params
        self.tileNum = 15
        self.grid= Grid((self.tileNum, self.tileNum))
        self.offset = self.xWidth/self.tileNum

        self.maxRange = int(math.sqrt(2*(self.tileNum**2)))

        self.grid.setTile((2,3), Tile('item'))


    ##Color Params
        self.grayRange = range(256)
        self.grayScale = tuple(map(lambda v: "#%02x%02x%02x" % (v, v, v), self.grayRange))

        self.IDValues = {None:'gray', 'item': 'red'}


    ##Mouse Bindings
        self.canvas.bind("<Button-1>", self.button1Clicked)
        self.canvas.bind("<B1-Motion>", self.button1Pressed)
        self.canvas.bind("<ButtonRelease-1>", self.button1Released)

        self.canvas.bind("<Button-3>", self.button3Clicked)
        self.canvas.bind("<B3-Motion>", self.button3Pressed)
        self.canvas.bind("<ButtonRelease-3>", self.button3Released)

        self.outlineScale.bind("<ButtonRelease-1>", self.outlineClicked)
        self.densityFrame.maxScale.bind("<ButtonRelease-1>", self.maxDistClicked)

        self.tileNumScale.bind("<ButtonRelease-1>", self.tileNumClicked)
        

        self.canvas.bind("<Motion>", self.enteredCanvas)
        self.canvas.bind("<Leave>", self.leftCanvas)

        self.playerFrame.nextGenButton.bind("<Button-1>", self.nextGen)
        self.playerFrame.prevGenButton.bind("<Button-1>", self.prevGen)

    ##Draw calls
        self.draw()
        
        self.life = life.Life(self.grid)
        
        self.maxRange = int(math.sqrt(2*(self.tileNum**2)))
        self.densityFrame.maxScale.set(self.maxRange)

    def nextGen(self, event = None):
        self.grid = self.life.step(Tile("item"))
        self.draw()

    def prevGen(self, event=None):
        self.grid = self.life.setPrev()
        self.draw()
        

    def enteredCanvas(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        i = x_coor
        j = y_coor
        dist = self.grid.getClosestID((x_coor, y_coor),'item')
        self.distText.configure(text=str(round(dist,2))+" units")

    def leftCanvas(self, event=None):
        self.distText.configure(text="0.00")

    def tileNumClicked(self, event=None):
        self.grid = Grid((self.tileNumScale.get(),self.tileNumScale.get()))
        self.tileNum = self.tileNumScale.get()
        self.offset = self.xWidth/self.tileNum
        self.maxRange = int(math.sqrt(2*(self.tileNum**2)))
        self.densityFrame.maxScale.set(self.maxRange)
        self.grid.setTile((2,3), Tile('item'))
        self.draw()
        self.life.updateGrid(self.grid)
        
    def button1Clicked(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile("item"))
        self.drawTileColor((x_coor, y_coor), 'red')

    def button1Pressed(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile('item'))
        self.drawTileColor((x_coor, y_coor), 'red')

    def button1Released(self, event=None):
        self.drawProbs()

    def button3Clicked(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile(None))
        #self.draw()

    def button3Pressed(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile(None))
        self.resetTile((x_coor, y_coor))

    def button3Released(self, event=None):
        self.drawProbs()

    def outlineClicked(self, event=None):
        self.draw()

    def maxDistClicked(self, event=None):
        self.maxRange = self.densityFrame.maxScale.get()
        self.draw()

    def drawTileColor(self, coord, color):
        i = coord[0]
        j = coord[1]
        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=color, width = self.outlineScale.get())

    def resetTile(self, coord):
        i = coord[0]
        j = coord[1]
        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill='blue', width = self.outlineScale.get())

    def draw(self):
        self.canvas.delete("all")
        for j in range(0, self.tileNum):
            for i in range(0,self.tileNum):
                if self.grid.getTile((i,j)).getID() != 'item':
                    if self.densityFrame.bool is True:
                        val = self.grid.getClosestID((i,j), 'item')
                        ratio = (1.0-(float(val)/float(self.maxRange)))**2
                        index = int(float(ratio)*len(self.grayScale))
                        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.grayScale[index], width = self.outlineScale.get())
                    else:
                        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill="white", width = self.outlineScale.get())
                else:
                    self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.IDValues[self.grid.getTile((i,j)).getID()], width = self.outlineScale.get())

    def drawProbs(self):
        for j in range(0, self.tileNum):
            for i in range(0,self.tileNum):
                if self.grid.getTile((i,j)).getID() != 'item':
                    if self.densityFrame.bool is True:
                        val = self.grid.getClosestID((i,j), 'item')
                        ratio = (1.0-(float(val)/float(self.maxRange)))**2
                        index = int(float(ratio)*len(self.grayScale))
                        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.grayScale[index], width = self.outlineScale.get())
                    else:
                        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill="white", width = self.outlineScale.get())

if __name__== '__main__':
    root=tk.Tk()
    gui=GUI_Controller(root)
    root.mainloop()
