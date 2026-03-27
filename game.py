from tkinter import *
class Player:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.frames_r = []
        self.frames_l = []
        self.speed = 10
        self.vx = self.speed
        self.size = 100
        self.current_frame = 0
        self.sprite_id = None
        self.direction = 'right'
    def load_frames(self):
        self.frames_r = [PhotoImage(file=f'textures/man{i}.png') for i in range(1,8)]
        self.frames_l = [PhotoImage(file=f'textures/man{i}.png') for i in range(1,8)]
    def create(self):
        if self.frames_r:
            self.sprite_id = self.canvas.create_image(self.x, self.y, image=self.frames_r[0], anchor=NW)

    def move_right(self):
        self.direction = 'right'
        self.vx = self.speed

    def move_left(self):
        self.direction = 'left'
        self.vx = -self.speed

    def update_position(self):
        print("пошел")
        self.x += self.vx
        if self.x < 0:
            self.x = 0
            self.move_right()
        if self.x > 800 - self.size:
            self.x = 800-self.size
            self.move_left()
        if self.sprite_id:
            self.canvas.coords(self.sprite_id, self.x, self.y)


    def animate(self):
        self.current_frame = (self.current_frame + 1) % 7
        if self.direction == 'right':
            frame = self.frames_r[self.current_frame]
        else:
            frame = self.frames_l[self.current_frame]

        if self.sprite_id:
            self.canvas.itemconfig(self.sprite_id, image=frame)

class Fallingitems:
    def __init__(self, canvas, x, y, item_type):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.type = item_type
        self.image = None

    def load_items(self):
        if self.type == 'apple':
            self.image = PhotoImage(file='textures/apple.png')
        elif self.type == 'banana':
            self.image = PhotoImage(file='textures/banana.png')
        if self.type == 'sberry':
            self.image = PhotoImage(file='textures/sberry.png')
        if self.type == 'watermelon':
            self.image = PhotoImage(file='textures/watermelon.png')
        if self.type == 'axe':
            self.image = PhotoImage(file='textures/axe.png')

    def create(self):
        if self.image:
            self.sprite_id = self.canvas.create_image(self.x, self.y, image=self.image,anchor = NW)


def animate():
    player.update_position()
    player.animate()
    window.after(50,animate)
def on_key_press(event):
    if event.keysym == 'Left':
        player.move_left()
    elif event.keysym == 'Right':
        player.move_right()
window = Tk()
window.title("Съедобное - несъедобное 2")
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='skyblue')
canvas.pack()

player = Player(canvas,400,500)
player.load_frames()
player.create()

banana = Fallingitems(canvas, 150, 0, 'banana')
banana.load_items()
banana.create()

sberry = Fallingitems(canvas, 250, 0, 'sberry')
sberry.load_items()
sberry.create()

watermelon = Fallingitems(canvas, 350, 48, 'watermelon')
watermelon.load_items()
watermelon.create()

axe = Fallingitems(canvas, 450, 0, 'axe')
axe.load_items()
axe.create()

apple = Fallingitems(canvas, 550, 0, 'apple')
apple.load_items()
apple.create()

window.bind('<KeyPress>', on_key_press)

animate()

window.mainloop()