class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издает звуки...")

    def move(self):
        print(f'{self.name} двигается...')

animal = Animal("Зверь")
animal.speak()
animal.move()

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f'{self.name} говорит: Гав-гав.')

    def wag_tail(self):
        print(f'{self.name} виляет хвостом...')

dog = Dog("Бобик", "Такса")
dog.move()
dog.speak()
dog.wag_tail()

class Cat(Animal):
    def speak(self):
        print(f'{self.name} говорит Мяу.')

cat = Cat("Мурка")
cat.speak()
cat.move()

class ToyDog(Dog):
    def __init__(self, name, breed, material):
        super().__init__(name, breed)
        self.material = material
    def speak(self):
        if self.material == "металл":
            print(f'{self.name} говорит: Я - робот!')
        else:
            print(f'{self.name} говорит: Я - мягкая игрушка!')
toydog1 = ToyDog('Шарик', 'Такса', "металл")
toydog1.speak()