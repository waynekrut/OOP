import time
class Dog:
    SPECIES = "Camis familaris"
    def __init__(self, name, age, kind, colour, trained):
        self.name = name
        self.age = age
        self.kind = kind
        self.colour = colour
        self.trained = trained

        self.age_in_human_years = age * 7
    def bark(self):
        if self.trained:
            print(f'{self.name} says: Гав-гав!')
        else:
            print(f'{self.name} says: Не знаю команды')
    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Breed: {self.kind}')
        print(f'Colour: {self.colour}')
        if self.trained:
            print('Знает команды')
        else:
            print("Не знает команды")
        print(f'Human years: {self.age_in_human_years}')
my_dog = Dog('Бобик', 3, 'british', 'white', True)
your_dog = Dog('Шарик', 5, 'german', 'brown', False)
print(my_dog.name)
my_dog.bark()
your_dog.bark()
my_dog.info()

class GameCharacter:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed

    def move_left(self):
        self.x -= self.speed
        print("Персонаж двигается влево."
              f'Новая позиция: x={self.x}')
    def move_right(self):
        self.x += self.speed
        print("Персонаж двигается вправо."
              f'Новая позиция: x={self.x}')

player = GameCharacter(400, 500, 10)
player.move_right()
for i in range(5):
    player.move_left()
    time.sleep(0.1)