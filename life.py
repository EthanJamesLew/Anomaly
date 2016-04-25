from tiles import *

class Life:
    def __init__(self, grid):
        super(self.__class__,self).__init__()
        self.grid = grid
        self.liveCond = [2,3]
        self.reproduceCond = [3]
        self.prevStates = []
        self.lifeType = "item"

    def step(self, tile):
        self.prevStates.append(self.grid)
        temp = Grid((self.grid.getWidth(), self.grid.getHeight()))
        for i in range(0, temp.getWidth()):
            for j in range (0, temp.getHeight()):
                subGrid =self.grid.getGridNeighbors((i,j))
                try:
                    if len(subGrid.types[self.lifeType]) in self.liveCond and (self.grid.getTile((i,j)).getID() == Tile(self.lifeType).getID()):
                        temp.setTile((i,j), Tile(self.lifeType))
        
                    if len(subGrid.types[self.lifeType]) in self.reproduceCond:
                        temp.setTile((i,j), Tile(self.lifeType))
                except:
                    None
        self.grid = temp
        return temp

    def setPrev(self):
        print(self.prevStates)
        temp = self.prevStates[-1]
        self.prevStates= self.prevStates[:-1]
        self.grid = temp
        return temp

    def setLiveCond(self, die):
        self.liveCond = die

    def setReproduceCond(self, repro):
        self.reproduceCond = repro

    def getLiveCond(self, die):
        return self.liveCond

    def getReproduceCond(self, repro):
        return self.reproduceCond
    def updateGrid(self,grid):
        self.grid=grid

        
    
