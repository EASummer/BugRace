from BasicBitchBug import BasicBitchBug

def get_bugs() -> object:
    print("getting bugs")
    bug1 = BasicBitchBug()
    bug2 = BasicBitchBug()
    return [bug1,bug2]