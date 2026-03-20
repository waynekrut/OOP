from tkinter import *
class player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.frames_r = []
        self.frames_l = []

    def load_frames(self):
        pass

    def create(self):
        pass

class fallingitems:
    pass


window = Tk()
window.title("Съедобное - несъедобное 2")
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='skyblue')
canvas.pack()


window.mainloop()