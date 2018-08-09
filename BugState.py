class BugState():

    def __init__(self,setType):
        self.Act = 0
        self.Dir = 0
        self.checked = 0
        self.X = 0
        self.Y = 0
        self.BugName =""
        self.surroundings = []

    def bugact(self):
        if self.checked == 1:
            Act = 1
