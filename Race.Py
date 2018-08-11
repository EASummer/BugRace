from Maze import Maze

class Race:

    def __init__(self):
        self.mazy = Maze()
        self.start = 0
        self.timer = 0
        # where bugs in race are stored
        self.bugList = []
        # bug locations in X Y
        self.bugLocs = []
        # status of bug (timeout penalty, death, etc.) 1 = normal
        self.bugStatus = []
        self.winnerList = []

    def add_bugs(self,bugs):
        for i in range(0,len(bugs)):
            self.bugList.append(bugs[i])
            self.bugStatus.append(1)
            self.bugLocs.append([0,0])

    #do actions for all bugs
    def bug_actions(self):
        if len(self.winnerList)<len(self.bugList):
            # go through all bugs in bug list ADD ROTATION!
            for i in range(0,len(self.bugList)):
                # if the action is 0 don't act
                if self.bugList[i].Act == 0:
                    self.bugList[i].checked = 1
                # if the action is 1 try to move
                elif self.bugList[i].Act == 1:
                    # get the real bug surroundings
                    if self.mazy.grid[self.bugLocs[i][0]][self.bugLocs[i][1]] != 3:
                        bugSurroundings = self.get_real_bug_surroundings(i)
                        # if the spot is a valid move
                        if bugSurroundings[self.bugList[i].Dir] != 1 or bugSurroundings[self.bugList[i].Dir]  != -1:
                            #if north add one to the Y loc
                            if self.bugList[i].Dir == 0:
                                self.bugLocs[i][1]+=1
                            # if south sub one to the Y loc
                            if self.bugList[i].Dir == 2:
                                self.bugLocs[i][1] -= 1
                            # if east add one to the Y loc
                            if self.bugList[i].Dir == 1:
                                self.bugLocs[i][0] += 1
                            # if south sub one to the Y loc
                            if self.bugList[i].Dir == 3:
                                self.bugLocs[i][0] -= 1
                            # let bug know valid move has been made
                            self.bugList[i].checked = 1
                    # if its an invalid move
                    else:
                        self.bugList[i].checked = 2
                # do these actions later
                elif self.bugList[i].Act == 2:
                    self.bugList[i].checked = 1
                # invalid bug request gets 2 back
                else:
                    self.bugList[i].checked = 2
                # update bugs surroundings
                if self.mazy.grid[self.bugLocs[i][0]][self.bugLocs[i][1]] != 3:
                    self.bugList[i].surroundings = self.get_bug_surroundings(i)
            # update all bug moves
            self.get_next_move()

    # gets bugs surroundings and returns them in a list
    def get_bug_surroundings(self,index):
        NESWDirs = []
        Xloc = self.bugLocs[index][0]
        Yloc = self.bugLocs[index][1]
        # if the y i on the north boarder return a wall (1)
        if Yloc > self.mazy.yLen:
            NESWDirs.append(1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc][Yloc + 1])
        # if the x i on the east boarder return a wall (1)
        if Xloc > self.mazy.xLen:
            NESWDirs.append(1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc + 1][Yloc])
        # if the y location is on the south boarder return 1 for south wall
        if 1 >= Yloc:
            NESWDirs.append(1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc][Yloc - 1])
        # if the y i on the south boarder return a wall (1)
        if 1 >= Xloc:
            NESWDirs.append(1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc - 1][Yloc])
        #return the array we made
        return NESWDirs

    # same as previous function but with -1 instead of 1 for edge walls
    def get_real_bug_surroundings(self,index):
        NESWDirs = []
        Xloc = self.bugLocs[index][0]
        Yloc = self.bugLocs[index][1]
        # if the y i on the north boarder return a wall (1)
        if Yloc > self.mazy.yLen:
            NESWDirs.append(-1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc][Yloc + 1])
        # if the x i on the east boarder return a wall (1)
        if Xloc > self.mazy.xLen:
            NESWDirs.append(-1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc + 1][Yloc])
        # if the y location is on the south boarder return 1 for south wall
        if 1 >= Yloc:
            NESWDirs.append(-1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc][Yloc - 1])
        # if the y i on the south boarder return a wall (1)
        if 1 >= Xloc:
            NESWDirs.append(-1)
        # otherwise just return what it actually is
        else:
            NESWDirs.append(self.mazy.grid[Xloc - 1][Yloc])
        # return the array we made
        return NESWDirs

    def get_next_move(self):
        # go through all bugs in bug list and call their get next action function
        for i in range(0, len(self.bugList)):
            self.bugList[i].get_action()

    def check_winners(self):
        for i in range(0, len(self.bugLocs())):
            if self.mazy.grid[self.bugLocs[i][0]][self.bugLocs[i][1]] == 3:
                if i not in self.winnerList:
                    self.winnerList.append(i)
