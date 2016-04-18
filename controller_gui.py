import tkinter as tk
from tkinter import *
import random
import math
import time

#Modules
from tiles import Grid, Tile


class GUI_Controller():
    def __init__(self, root):
    ##TK Params
        self.root=root
        self.entry = tk.Entry(root)
        root.wm_title("Probability Finder v1.0")

        self.xWidth = 1000
        self.yWidth = 1000

    ##Frames
        self.mainFrame = Frame(self.root, relief='flat', borderwidth=4)
        self.mainFrame.grid(row=0,column=0, sticky="n")
        
        self.canvas=tk.Canvas(root, width=self.xWidth, height=self.yWidth, background='white')
        self.canvas.grid(row=0,column=1)

    ##Grid Params
        self.tileNum = 45
        self.grid= Grid((self.tileNum, self.tileNum))
        self.offset = 1000/self.tileNum

        self.maxRange = 50

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

    ##Draw calls
        self.draw()

    def button1Clicked(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile(None))
        self.draw()

    def button3Clicked(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        if self.grid.getTile((x_coor, y_coor)).getID() != "item":
            self.grid.setTile((x_coor, y_coor), Tile("item"))
        self.draw()
    
    def button1Pressed(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile('item'))
        self.drawTileColor((x_coor, y_coor), 'red')

    def button3Pressed(self, event=None):
        x_coor = int((float(event.x)/float(self.xWidth))*float(self.tileNum))
        y_coor = int((float(event.y)/float(self.yWidth))*float(self.tileNum))
        self.grid.setTile((x_coor, y_coor), Tile(None))
        self.resetTile((x_coor, y_coor))

    def button1Released(self, event=None):
        self.drawProbs()

    def button3Released(self, event=None):
        self.drawProbs()

    def drawTileColor(self, coord, color):
        i = coord[0]
        j = coord[1]
        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=color, width = 1)

    def resetTile(self, coord):
        i = coord[0]
        j = coord[1]
        self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill='blue', width = 1)

    def draw(self):
        for j in range(0, self.tileNum):
            for i in range(0,self.tileNum):
                if self.grid.getTile((i,j)).getID() != 'item':
                    val = self.grid.getClosestID((i,j), 'item')
                    ratio = (1.0-(float(val)/float(self.maxRange)))**2
                    index = int(float(ratio)*len(self.grayScale))
                    self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.grayScale[index], width = 1)
                else:
                    self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.IDValues[self.grid.getTile((i,j)).getID()], width = 1)

    def drawProbs(self):
        for j in range(0, self.tileNum):
            for i in range(0,self.tileNum):
                if self.grid.getTile((i,j)).getID() != 'item':
                    val = self.grid.getClosestID((i,j), 'item')
                    ratio = (1.0-(float(val)/float(self.maxRange)))**2
                    index = int(float(ratio)*len(self.grayScale))
                    self.canvas.create_rectangle(i*self.offset, j*self.offset, i*self.offset+self.offset, j*self.offset+self.offset,fill=self.grayScale[index], width = 1)

if __name__== '__main__':
    root=tk.Tk()
    gui=GUI_Controller(root)
    root.mainloop()
