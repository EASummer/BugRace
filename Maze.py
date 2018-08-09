import random

class Maze:
    #x length of maze
    xLen = 50
    #y length of maze
    yLen = 50
    grid=[]

    def __init__(self):
        print("initing maze")
        for i in range(self.xLen):
            self.grid.append([])
            for j in range(self.yLen):
                self.grid[i].append(1)
        #sets current coords to random location(FIX ERIC)
        currX = 0
        currY = 0
        self.fill_maze(currX,currY)


    def fill_maze(self,x,y):
        print("makin maze")
        #this is to see how many times it has iterated (check all sides)
        times = 0
        #choose random direction to go first
        direction = random.randint(1, 4)
        #while all sides havent been checked for a single square
        while times < 4:

            xdir = 0
            ydir = 0

            if direction == 0:
                xdir=-2
            if direction == 1:
                xdir=2
            if direction == 2:
                ydir=-2
            if direction == 3:
                ydir=2

            xdir=x+xdir;
            ydir=y+ydir;
            #if the point we are looking at is in bouds
            if 0 <= xdir < self.xLen and 0 <= ydir < self.yLen :
                print ("pointin bounds")
                #if the adjacent square we are looking at isn't filled in yet go there
                if self.grid[xdir][ydir] == 1 and times < 4:
                    print("changing points")
                    #fill in that adjacent square
                    self.grid[xdir][ydir] = 0
                    #break wall in between them
                    self.grid[xdir+(x - xdir) // 2][ydir+(y - ydir) // 2] = 0
                    #go go deeper
                    self.fill_maze(xdir, ydir)
            #increment times so you dont check more than 4 sides
            times += 1
            #move to the next direction
            direction += 1
            #if direction is greater than the options then start back at 0
            if direction > 3:
                direction = 0
        #let eric know mazing is done
        print("done mazing")