from Race import Race
from tkinter import Tk, Canvas, PhotoImage, mainloop
import tkinter as tk
from BugList import get_bugs



class BugApp(tk.Frame):
    def __init__(self, master=None):
        # create race
        self.race = Race()
        #gets all bugs in buglist document and adds to list
        self.race.add_bugs(get_bugs())
        tk.Frame.__init__(self, master)
        self.pack()
        self.addWidgets()
        self.zoomAmount = 4


    def addWidgets(self):
        # create and zoom to map image
        self.create_img()
        self.zoom_image()
        # set up canvas size
        self.canvas = Canvas(self, width=self.img.width(), height=self.img.height(), bg="#000000")
        # set up location of img on canvas
        self.canvas.create_image((self.img.width() // 2, self.img.height() // 2), image=self.img, state="normal")
        # pack canvas into window
        self.canvas.pack()
        # initial time display
        self.bug_clock()

    def print_bugs(self):
        for i in range(0, len(self.race.bugLocs)):
            if i == 0:
                self.img.put("#00FF00", (self.race.bugLocs[i][0] + 2, self.race.bugLocs[i][1] + 2))
            elif i == 1:
                self.img.put("#FF0000", (self.race.bugLocs[i][0] + 2, self.race.bugLocs[i][1] + 2))
            elif i == 2:
                self.img.put("#0000FF", (self.race.bugLocs[i][0] + 2, self.race.bugLocs[i][1] + 2))
            elif i == 3:
                self.img.put("#8000FF", (self.race.bugLocs[i][0] + 2, self.race.bugLocs[i][1] + 2))

    def print_state(self):
        for i in range(0, self.race.mazy.xLen):
            for j in range(0, self.race.mazy.yLen):
                if self.race.mazy.grid[i][j] == 1:
                    self.img.put("#000000", (i + 2, j + 2))
                if self.race.mazy.grid[i][j] == 0:
                    self.img.put("#ffffff", (i + 2, j + 2))


    def bug_clock(self):
        print("bug clockin' time = ",self.race.timer)
        self.race.bug_actions()
        self.create_img()
        self.zoom_image()
        self.canvas.create_image((self.img.width() // 2, self.img.height() // 2), image=self.img, state="normal")
        # increment race timer
        self.race.timer += 1
        self.after(1000, self.bug_clock)

    def create_img(self):
        # set width and height of picture to make. add a row for black on each side
        width = self.race.mazy.xLen + 2
        height = self.race.mazy.yLen + 2
        # create photo image at width and height
        self.img = PhotoImage(width=width, height=height)
        self.print_state()
        self.print_bugs()

    def zoom_image(self):
        self.img = self.img.zoom(4,4)#self.zoomAmount, self.zoomAmount)

def main():
    # create root app
    root = tk.Tk()
    # create instance of bugapp
    bugapp = BugApp(master=root)
    # launch app
    root.mainloop()


if __name__ == "__main__":
    main()