from Race import Race
from tkinter import Tk, Canvas, PhotoImage, mainloop

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

race = Race()

width = race.mazy.xLen+2
height = race.mazy.yLen+2

window = Tk()
canvas = Canvas(window, width=width, height=height, bg="#000000")
img = PhotoImage(width=width, height=height)
print_state(race)


canvas.create_image((width // 2, height // 2), image=img, state="normal")

#make image larger
zoomAmount= 10
canvas = Canvas(window, width=width*zoomAmount, height=height*zoomAmount, bg="#000000")
canvas.pack()
img = img.zoom(10,10)
canvas.create_image((width*zoomAmount // 2, height*zoomAmount // 2), image=img, state="normal")

mainloop()