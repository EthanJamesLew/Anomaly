import math
import life

class Tile(object):
    '''
    Tile class creates an object with data to be arrayed in the Grid Class
    '''
    def __init__(self, ID):
        super(self.__class__,self).__init__()
        self.ID = ID

    def setID(self, ID):
        self.ID = ID

    def getID(self):
        return self.ID
    
    def __str__(self):
        print(self.ID)

class Grid(object):
    '''
    The grid class arrays Tile and provides methods to get meaningful data from their positions on a plane.
    '''
    def __init__(self, size, grid=None):
        super(self.__class__,self).__init__()
        self.selection = []
        self.types = {}

        if grid != None:
            self.grid = grid
            self.sizeX = len(self.grid[0])
            self.sizeY = len(self.grid[1])

        else:            
            self.grid = [[Tile(None)]*size[0]]*size[1]
            for i in range(0, len(self.grid)):
                self.grid[i] = self.grid[i][:]
            self.sizeX = size[0]
            self.sizeY = size[1]
        self.calcTypePos()

    def setTile(self, coord, tile):
        self.grid[coord[1]][coord[0]] = tile
        self.calcTypePos()

    def getTile(self, coord):
        return self.grid[coord[1]][coord[0]]

    #Returns a sub-grid of neighbors
    def getGridNeighbors(self, coord, dist=1):
        subGrid = [row[max(0, coord[0]-dist):coord[0]+dist+1] for row in self.grid[max(0, coord[1]-1):coord[1]+dist+1]]
        return Grid(None,subGrid)

    def getDistanceTiles(self, coords1, coords2):
        xSquare = (float(coords1[0])-float(coords2[0]))**2
        ySquare = (float(coords1[1])-float(coords2[1]))**2
        return math.sqrt(xSquare + ySquare)

    def getClosestSimilar(self, coords):
        return min(self.getDistanceID(coords, self.getTile(coords).getID())[0])

    def getClosestID(self, coords, ID):
        return min(self.getDistanceID(coords, ID)[0])

    #Returns distances from a coodinate to a set of IDs. Ignores its own coordinate if it is homogeneous.
    def getDistanceID(self, coords, ID):
        choices = self.types[ID]
        ans = []
        ans1 = []
        for i in choices:
            if i != coords:
                ans += [self.getDistanceTiles(coords, i),]
                ans1 += i
        return [ans, ans1]

    def getDistanceFrequencies(self, coords, ID, distance):
        choices = self.types[ID]
        a = 0
        for i in choices:
            if i != coords:
                if self.getDistanceTiles(coords, i) == 1.0:
                    a += 1
        return a

    def calcTypePos(self):
        self.types = {}
        x = 0
        y = 0
        for i in self.grid:
            for j in i:
                if j.getID() in self.types:
                     self.types[j.getID()] += [(x, y)]
                else:
                    self.types[j.getID()] = [(x, y),]
                x += 1
            y += 1
            x = 0

    def getTypes(self):
        return self.types

    def getWidth(self):
        return self.sizeX

    def getHeight(self):
        return self.sizeY
    
    def __str__(self):
        statement = ""
        for i in self.grid:
            statement += "\n \n"
            for j in i:
                statement += str(j.getID()) + " \t"
        return statement

if __name__ == "__main__":
    grid = Grid((10, 10))
    
