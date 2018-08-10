from Bug import Bug
import random

class BasicBitchBug(Bug):
    pass

    def __init__(self):
        self.Act = 0
        self.Dir = 0

    def get_action(self):
        keep_try = 1
        while(keep_try):
            tempDir = random.randint(0, 3)
            if self.surroundings[tempDir] == 0:
                self.Dir = tempDir
                keep_try = 0