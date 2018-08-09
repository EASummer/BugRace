from enum import Enum


class Square(Enum):
    Empty = 0
    Wall = 1
    Bug = 2
    setTrap = 3
    usedTrap = 4
    bugInTrap = 5
    Speed = 6
    Jump = 7


class Square:
    def __init__(self,setType):
        self.type = setType

    def get_type(self):
        return self.type

    def get_type_enum(self):
        return self.type.name

    def change_type(self, setType):
        self.type = setType