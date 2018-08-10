from Race import Race
from tkinter import Tk, Canvas, PhotoImage, mainloop
from BasicBitchBug import BasicBitchBug

def print_bugs(race,image):
    for i in range (0,len(race.bugLocs)):
        if i == 0:
            img1.put("#00FF00", (race.bugLocs[i][0],race.bugLocs[i][1]))
        elif i == 1:
            img1.put("#FF0000", (race.bugLocs[i][0], race.bugLocs[i][1]))
        elif i == 2:
            img1.put("#0000FF", (race.bugLocs[i][0], race.bugLocs[i][1]))
        elif i == 3:
            img1.put("#8000FF", (race.bugLocs[i][0], race.bugLocs[i][1]))

def print_state(race,image):
    mazy = race.mazy
    for i in range (0,mazy.xLen):
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j]== 1:
                img1.put("#000000", (i+2, j+2))
            if mazy.grid[i][j]== 0:
                img1.put("#ffffff", (i+2, j+2))

def text_print(race):
    mazy = race.mazy
    for i in range(0,mazy.xLen):
        print("\n")
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j] == 1:
                print('x' , end='')
            if mazy.grid[i][j] == 0:
                print(' ', end='')

def bug_clock(window,race):
    print("bug clockin'")
    race.bug_actions()
    print_state(race)
    print_bugs(race)
    #increment race timer
    race.timer+=1
    window.after(1000, bug_clock(race))

def main():
    # create race
    race = Race()
    #
    bbbug = BasicBitchBug()
    race.add_bug(bbbug)
    # set width and height of picture to make. add a row for black on each side
    width = race.mazy.xLen + 2
    height = race.mazy.yLen + 2
    # create new TK window
    window = Tk()
    # set canvas size
    canvas1 = Canvas(window, width=width, height=height, bg="#000000")
    # create photo image at width and height
    img1 = PhotoImage(width=width, height=height)
    # print out the state of the race on it
    print_state(race)
    # put image on canvas
    canvas1.create_image((width // 2, height // 2), image=img1, state="normal")

    # make image larger
    zoomAmount = 10
    canvas2 = Canvas(window, width=width * zoomAmount, height=height * zoomAmount, bg="#000000")
    canvas2.pack()
    img2 = img1.zoom(10, 10)
    canvas2.create_image((width * zoomAmount // 2, height * zoomAmount // 2), image=img2, state="normal")
    bug_clock(window,race)
    window.mainloop()

if __name__ == "__main__":
    main()

