from Race import Race
from tkinter import Tk, Canvas, PhotoImage, mainloop
from BasicBitchBug import BasicBitchBug

def print_bugs(race):
    for i in range (0,len(race.bugLocs)):
        if i == 0:
            img.put("#00FF00", (race.bugLocs[i][0],race.bugLocs[i][1]))
        elif i == 1:
            img.put("#FF0000", (race.bugLocs[i][0], race.bugLocs[i][1]))
        elif i == 2:
            img.put("#0000FF", (race.bugLocs[i][0], race.bugLocs[i][1]))
        elif i == 3:
            img.put("#8000FF", (race.bugLocs[i][0], race.bugLocs[i][1]))

def print_state(race):
    mazy = race.mazy
    for i in range (0,mazy.xLen):
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j]== 1:
                img.put("#000000", (i+2, j+2))
            if mazy.grid[i][j]== 0:
                img.put("#ffffff", (i+2, j+2))

def text_print(race):
    mazy = race.mazy
    for i in range(0,mazy.xLen):
        print("\n")
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j] == 1:
                print('x' , end='')
            if mazy.grid[i][j] == 0:
                print(' ', end='')

def bug_clock(race):
    print("bug clockin'")
    race.bug_actions()
    print_state(race)
    print_bugs(race)
    window.after(1000, bug_clock(race))
    #increment race timer
    race.timer+=1

#create race
race = Race()
#
bbbug = BasicBitchBug()
race.add_bug(bbbug)
#set width and height of picture to make. add a row for black on each side
width = race.mazy.xLen+2
height = race.mazy.yLen+2
#create new TK window
window = Tk()
#set canvas size
canvas = Canvas(window, width=width, height=height, bg="#000000")
#create photo image at width and height
img = PhotoImage(width=width, height=height)
#print out the state of the race on it
print_state(race)
#put image on canvas
canvas.create_image((width // 2, height // 2), image=img, state="normal")

#make image larger
zoomAmount= 10
canvas = Canvas(window, width=width*zoomAmount, height=height*zoomAmount, bg="#000000")
canvas.pack()
img = img.zoom(10,10)
canvas.create_image((width*zoomAmount // 2, height*zoomAmount // 2), image=img, state="normal")
bug_clock(race)
window.mainloop()
