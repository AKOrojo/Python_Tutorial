import random
from pathlib import Path

path = Path('ecommerce')
print(path.exists())
path = Path('emails')
print(path.mkdir())
print(path.rmdir())
path = Path()

for file in (path.glob('*.py')):
    print(file)


def roll():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x, y


class Dice:
    pass


dice = Dice
print(roll())


