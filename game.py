from tkinter import *
from random import *
class Player:
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__frames_r = []
        self.__frames_l = []
        self.__speed = 10
        self.__vx = self.__speed
        self.__size = 100
        self.__current_frame = 0
        self.__sprite_id = None
        self.__direction = 'right'

        self._lives = 3
    def load_frames(self):
        self.__frames_r = [PhotoImage(file=f'textures/man{i}.png') for i in range(1, 8)]
        self.__frames_l = [PhotoImage(file=f'textures/man{i}.png') for i in range(1, 8)]
    def create(self):
        if self.__frames_r:
            self.__sprite_id = self.__canvas.create_image(self.__x, self.__y, image=self.__frames_r[0], anchor=NW)

    def move_right(self):
        self.__direction = 'right'
        self.__vx = self.__speed

    def move_left(self):
        self.__direction = 'left'
        self.__vx = -self.__speed

    def update_position(self):
        self.__x += self.__vx
        if self.__x < 0:
            self.__x = 0
            self.move_right()
        if self.__x > 800 - self.__size:
            self.__x = 800 - self.__size
            self.move_left()
        if self.__sprite_id:
            self.__canvas.coords(self.__sprite_id, self.__x, self.__y)


    def animate(self):
        self.__current_frame = (self.__current_frame + 1) % 7
        if self.__direction == 'right':
            frame = self.__frames_r[self.__current_frame]
        else:
            frame = self.__frames_l[self.__current_frame]

        if self.__sprite_id:
            self.__canvas.itemconfig(self.__sprite_id, image=frame)

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def get_direction(self):
        return self.__direction
    def get_speed(self):
        return self.__speed
    def get_lives(self):
        return self._lives

    # def set_speed(self, speed):
    #     if 5 <= speed <= 30:
    #         self.__speed = speed
    #         if self.__vx > 0
    #             self.__vx = speed


    def lose_life(self):
        if self._lives > 0:
            self._lives -= 1
            print(f"Потеряна жизнь. Осталось жизней: {self._lives}")
            if self._lives == 0:
                print("ИГРА ОКОНЧЕНА!")
            return True
        return False

class Fallingitems:
    def __init__(self, canvas, x, y, item_type):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.type = item_type

        self.vy = 10
        self.size = 50
        self.image = None
        self.sprite_id = None
        self.is_active = True

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
            self.sprite_id = self.canvas.create_image(self.x, self.y, image=self.image, anchor = NW)

    def fall(self):
        if self.is_active:
            self.y += self.vy
            if self.sprite_id:
                self.canvas.coords(self.sprite_id, self.x, self.y)

    def is_off_screen(self):
        return self.y > 600

    def check_collision(self, player_x, player_y, player_size):
        if not self.is_active:
             return False
        if (self.x < player.__x + player_size and
                 self.x + self.size > player_x and
                 self.y < player_y + player_size and
                 self.y + self.size > player_y):
            self.is_active = False
            if self.sprite_id:
                self.canvas.delete(self.sprite_id)
            return True
        return False


def animate():
    global apple
    player.update_position()
    player.animate()

    apple.fall()

    if apple.check_collision(player.__x, player.__y, player.__size):
        print("Поймал предмет")
        new_x = randint(0, 800 - apple.size)
        apple = Fallingitems(canvas, new_x, 0, 'fruit')
        apple.load_items()
        apple.create()
    elif apple.is_off_screen():
        print("Предмет упал")
        canvas.delete(apple.sprite_id)
        new_x = randint(0, 800 - apple.size)
        apple = Fallingitems(canvas, new_x, 0, 'fruit')
        apple.load_items()
        apple.create()
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