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
    #def pet(self):
    #    print(f"Корова {self.name} мычит от удовольтсвия")

class Director(Staff):
    def __init__(self, name, age, status, salary):
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

class Lion(WildAnimal):
    def __init__(self, name, age, species, is_dangerous):
        super().__init__(name, age, species, is_dangerous)
    def make_sound(self):
        print(f"Лев {self.name} рычит")

class Cat(DomesticAnimal):
    def __init__(self, name, age, species, owner):
        super().__init__(name, age, species, owner)
    def make_sound(self):
        print(f"Кошка {self.name} мякает")
    #def pet(self):
    #    print(f"Кошка {self.name} мурлычет от удовольствия")
class Goat(DomesticAnimal):
    def __init__(self, name, age, species, owner):
        super().__init__(name,age,species, owner)
    def make_sound(self):
        print(f'Козел {self.name} блеет')

class Elephant(WildAnimal):
    def __init__(self, name, age, species, is_dangerous):
        super().__init__(name, age, species, is_dangerous)
    def make_sound(self):
        print(f"Слон {self.name} трубит")

class Veterinary(Staff):
    def __init__(self, name, age, status, salary):
        super().__init__(name,age,"Ветеринар", salary)
    def work(self):
        print(f"Ветеринар {self.name}  лечит людей")
wolf = Wolf("Серый", 5)
cow = Cow("Буренка", 4, "Зоопарк")
director = Director("Иван Петрович", 45, "директор", 150000)
child = Child("Маша", 8, True)
lion = Lion('Лео', 5, "Млекопитающее", True)
cat = Cat("Мурка", 2, "Млекопитающее", "Зоопарк")
goat = Goat("Дымок", 4, "млекопитающее", False)
elephant = Elephant("Тини", 6, "млекопитающее", False)
veterinary = Veterinary("Анна", 27, "Ветеринар", 70000)

wolf.introduce()
wolf.make_sound()

cow.introduce()
cow.make_sound()
cow.pet()

child.introduce()
child.fun()

director.introduce()
director.work()

lion.introduce()
lion.make_sound()

elephant.introduce()
elephant.make_sound()

veterinary.introduce()
veterinary.work()

goat.introduce()
goat.make_sound()

cat.introduce()
cat.make_sound()
cat.pet()

#дз создать другие классы(лев, кошка козел, взрослый, ветеринар, слон, лев