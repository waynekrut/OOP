from tkinter import *
from random import *

class Player:
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__speed = 10
        self.__vx = self.__speed
        self.__size = 100
        self.__frames_r = []
        self.__frames_l = []
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

    def get_size(self):
        return self.__size
    def get_lives(self):
        return self._lives
    def get_direction(self):
        return self.__direction

    def set_position(self, x):
        if 0 <= x <= 800 -self.__size:
            self.__x = x
        else:
            print(f'Ошибка х={x} выходит за границы экрана!')

        if self.__sprite_id:
            self.__canvas.coords(self.__sprite_id, self.__x, self.__y)

    def set_speed(self, speed):
        if 5 <= speed <= 30:
            self.__speed = speed
            if self.__vx > 0:
                self.__vx = speed
            else:
                self.__vx = -speed
            print(f"скорость изменена на {speed}")
        else:
            print("Неверное число.")

    def lose_life(self):
        if self._lives > 0:
            self._lives -= 1
            print(f"Потеряна жизнь. Осталось жизней: {self._lives}")
            if self._lives == 0:
                print("ИГРА ОКОНЧЕНА!")
            return True
        return False


class Fallingitems:
    def __init__(self, canvas, x, y):
        self.__canvas = canvas
        self.__x = x
        self.__y = y
        self.__vy = 10
        self.__size = 50
        self.__image = None
        self.__sprite_id = None
        self.__is_active = True
        self.__rotation = 0
        self.__rotation_speed = 0

        # self.__points = {'fruit':1,
        #                'vegetable':3}.get(item_type, 0)

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    #def get_position(self):
    #    return self.__x, self.__y

    def get_type(self):
        return self.__type

    def get_points(self):
        return self.__points

    def is_active(self):
        return self.__is_active

    def get_size(self):
        return self.__size

    def get_sprite_id(self):
        return self.__sprite_id

    def set_speed(self, vy):
        if 0 <= vy <= 20:
            self.__vy = vy
        else:
            print(f'Ошибка: скорость {vy} слишком большая.')

    def set_rotation(self, speed):
        self.__rotation = speed

    def load_items(self, image_path):
        try:
            self.__image = PhotoImage(file=image_path)
        except:
            print(f'Ошибка загрузки: {image_path}')

    def create(self):
        if self.__image:
            self.__sprite_id = self.__canvas.create_image(self.__x, self.__y, image=self.__image, anchor=NW)

    def fall(self):
        if self.__is_active:
            self.__y += self.__vy
            if self.__sprite_id:
                self.__canvas.coords(self.__sprite_id, self.__x, self.__y)

    def is_off_screen(self):
        return self.__y > 600

    def check_collision(self, player_x, player_y, player_size):
        if not self.__is_active:
            return False
        if (self.__x < player_x + player_size and
            self.__x + self.__size > player_x and
            self.__y < player_y + player_size and
            self.__y + self.__size > player_y):
            self.__is_active = False
            if self.__sprite_id:
                self.__canvas.delete(self.__sprite_id)
            return True
        return False

    def on_collision(self):
        pass

    def destroy(self):
        if self.__sprite_id:
            self.__canvas.delete(self.__sprite_id)
        self.__is_active = False


def animate():
    global game_manager
    result = game_manager.update()
    if result != 'game_over':
        window.after(50,animate)


def on_key_press(event):
    if event.keysym == 'Left':
        player.move_left()
    elif event.keysym == 'Right':
        player.move_right()
    elif event.keysym == 'Up':
        player.set_speed(15)
    elif event.keysym == 'Down':
        player.set_speed(5)

class Fruit(Fallingitems):
    def __init__(self, canvas, x, y, fruit_type='apple'):
        super().__init__(canvas,x,y)
        self.fruit_type = fruit_type
        self.points = 1

        if fruit_type == 'apple':
            self.set_speed(10)
            self.load_items('textures/apple.png')
        if fruit_type == 'banana':
            self.set_speed(12)
            self.load_items('textures/banana.png')

    def get_points(self):
        return self.points
    def on_collision(self):
        print(f'Съеден {self.fruit_type}! +{self.points} очков')
        #здесь будет увеличение счета

class Vegetable(Fallingitems):
    def __init__(self, canvas, x, y, vegetable_type='apple'):
        super().__init__(canvas,x,y)
        self.fruit_type = vegetable_type
        self.points = 1

        if vegetable_type == 'watermelon':
            self.set_speed(15)
            self.load_items('textures/watermelon.png')
        if vegetable_type == 'sberry':
            self.set_speed(8)
            self.load_items('textures/sberry.png')

    def get_points(self):
        return self.points

    def on_collision(self):
        print(f'Съеден {self.fruit_type}! +{self.points} очков')
        # здесь будет увеличение счета

class Axe(Fallingitems):
    def __init__(self, canvas, x, y):
        super().__init__(canvas, x, y)

        # set.points = -1
        self.set_speed(15)
        self.load_items('textures/axe1.png')

        self.frames = []
        self.current_frame = 0
        self.load_frames()

    def load_frames(self):
        try:
            self.frames = [PhotoImage(file=f'textures/axe{i}.png') for i in range(1,5)]
        except:
            print("Не удалось загрузить анимацию топора.")

    def on_collision(self):
        print("Попал в топор! Игра окончена.")
        return('game_over')

    def get_points(self):
        return self.get_points()

class GameManager:
    def __init__(self, canvas, player):
        self.canvas = canvas
        self.player = player
        self.items = []
        self.score = 0
        self.game_over = False

        self.score_text = canvas.create_text(
            50, 30, text = "Счет: 0",
            font = ('Arial', 20), fill = 'white')

        self.lives_text = canvas.create_text(
            150, 30, text = "Жизни: 1",
            font = ('Arial', 20), fill = 'white')
    def spawn_items(self):
        x = randint(0,750)
        item_type = choice(['apple', 'banana', 'sberry', 'watermelon', 'axe'])
        if item_type == 'apple':
            item = Fruit(self.canvas, x, 0, 'apple')
        elif item_type == 'banana':
            item = Fruit(self.canvas, x, 0, 'banana')
        elif item_type == 'sberry':
            item = Vegetable(self.canvas, x, 0, 'sberry')
        elif item_type == 'watermelon':
            item = Vegetable(self.canvas, x, 0, 'watermelon')
        else:
            item = Axe(self.canvas, x, 0)
        item.create()
    def update(self):
        if self.game_over:
            return "game_over"
        self.player.update_position()
        self.player.animate()

        for item in self.items[:]:
            item.fall()

            player_x = self.player.get_x()
            player_y = self.player.get_y()
            player_size = self.player.get_size()

            if item.check_collision(player_x, player_y, player_size):
                self.score += item.get_points()
                self.canvas.itemconfig(self.score_text, text=f'Счет: {self.score}')

                if isinstance(item, Axe):
                    self.game_over = True
                    self.show_game_over()
                    return 'game_over'
                self.items.remove(item)
            elif item.is_of_screen():
                self.items.remove(item)
        self.canvas.itemconfig(self.lives_text,
                               text = f'Жизни: {self.player.get_lives()}')
        if len(self.items) < 7:
            if randint(1, 10) > 7:
                self.spawn_items()
        return "playing"
    def show_game_over(self):
        self.canvas.create_text(
            400, 300,
            text = f'ИГРА ОКОНЧЕНА!\nСчет: {self.score}',
            font = ('Arial', 30, 'bold'), fill = 'red')
window = Tk()
window.title("Съедобное - несъедобное 2")
window.geometry('800x600')

canvas = Canvas(window, width=800, height=600, bg='skyblue')
canvas.pack()

player = Player(canvas, 400, 500)
player.load_frames()
player.create()




game_manager = GameManager(canvas, player)



window.bind('<KeyPress>', on_key_press)

animate()

window.mainloop()