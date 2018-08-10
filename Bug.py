class Bug():

    def __init__(self):
        #1 = move 2 = use
        self.Act = 0
        #0 = up 1 = right 2 = down 3 = left
        self.Dir = 0
        #if 0 action hasn't been executed if 1 action has been executed if 2 action could not be executed
        self.checked = 0
        #variable to show if bug has item
        self.hasItem = 0
        #name of the bug
        self.BugName =""
        #returned list of the bugs surroundings
        self.surroundings = []
        #movement stat for bug
        self.numMoves = 0
        #misc stat for bug
        self.numUses = 0


    def get_action(self):
        if self.checked == 1:
            Act = 0
