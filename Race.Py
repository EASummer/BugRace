from Maze import Maze

class Race:
    def __init__(self):
        self.mazy = Maze()
        self.start = 0
        self.timer = 0
        bugList = []

    def AddBugState(self,BugState):
        self.bugList.Append(BugState)
