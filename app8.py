# Comments

# Classes

numbers = [1, 2, 3]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point1 = Point(10, 20)
point1.x = 10
point1.y = 20

point2 = Point(1, 2)
point2.x = 1

point1.draw()


class Mammal:
    def walk(self):
        print('walk')


class Person(Mammal):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi i am {self.name}')


class Cat(Mammal):
    pass




