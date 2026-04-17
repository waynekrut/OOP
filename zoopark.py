class Object:
    def __init__(self, name, age):
        self.name = name
    def introduce(self):
        print("1")
class Animal(Object):
    def __init__(self, name, age, species):
        super().__init__(name,age)
        self.species = species
    def make_sound(self):
        print(f'Животное {self.name} издает звуки')
class Human(Object):
    def __init__(self, name, age, status):
        super().__init__(name, age)
        self.status = status

class WildAnimal(Animal):
    def __init__(self, name, age, species, is_dangerous):
        super().__init__(name, age, species)
        self.is_dangerous = is_dangerous
    def make_sound(self):
        print(f'Дикое животное {self.name} издает звук', end=': ')

class DomesticAnimal(Animal):
    def __init__(self, name, age, species, owner):
        super().__init__(name,age,species)
        self.owner = owner
        def make_sound(self):
            print(f'Домашнее животное {self.name} издает звуки')
        def pet(self):
            print(f'{self.name} мычит от удовольствия')

class Staff(Human):
    def __init__(self, name, age, status, salary):
        super().__init__(name, age, status)
        self.salary = salary
    def work(self):
        print(f'Сотрудник {self.name} работает')
class Visitor(Human):
    def __init__(self, name, age, status, has_ticket):
        super().__init__(name, age, status)
        self.has_ticket = has_ticket
    def look_at_animals(self):
        print(f'Посетитель {self.name} смотрит на животных')

class Wolf(WildAnimal):
    def __init__(self, name, age):
        super().__init__(name, age, "Млекопитающее", True)
    def make_sound(self):
        super().make_sound()
        print("Аууууу")

class Cow(DomesticAnimal):
    def __init__(self, name, age, owner):
        super().__init__(name, age, "Млекопитающее", owner)
    def make_sound(self):
        super().make_sound()
        print("Мууу")
    def pet(self):

class Director(Staff):
    def __init__(self, name, age, salary):
        super().__init__(name, age, "директор", salary)
    def work(self):
        super().work()
        print("управляет зоопарком")

class Child(Visitor):
    def __init__(self, name, age, has_ticket):
        super().__init__(name, age, "ребенок", has_ticket)
    def fun(self):
        super().look_at_animals()
        print(f"Ребенок {self.name} радуется и хлопает в ладоши")



wolf = Wolf("Серый", 5)
cow = Cow("Буренка", 4, "Зоопарк")
director = Director("Иван Петрович", 45, 150000)
child = Child("Маша", 8, True)

wolf.introduce()
wolf.make_sound()

cow.introduce()
cow.make_sound()
cow.pet()

child.introduce()
child.fun()
#дз создать другие классы(лев, кошка кощел, взрослый, ветеринар, слон, лев