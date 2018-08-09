from Race import Race
from tkinter import Tk, Canvas, PhotoImage, mainloop

def print_state(race):
    mazy = race.mazy
    for i in range (0,mazy.xLen):
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j]== 1:
                img.put("#000000", (i+3, j+3))
            if mazy.grid[i][j]== 0:
                img.put("#ffffff", (i+3, j+3))

def text_print(race):
    mazy = race.mazy
    for i in range(0,mazy.xLen):
        print("\n")
        for j in range(0,mazy.yLen):
            if mazy.grid[i][j] == 1:
                print('x' , end='')
            if mazy.grid[i][j] == 0:
                print(' ', end='')

race = Race()

width = race.mazy.xLen
height = race.mazy.yLen

window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
canvas.pack()
img = PhotoImage(width=width, height=height)


canvas.create_image((width // 2, height // 2), image=img, state="normal")
print_state(race)


mainloop()