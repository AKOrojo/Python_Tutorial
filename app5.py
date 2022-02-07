for item in 'Python':
    print(item)

for item in ['Python', 'john', 'banny']:
    print(item)

for item in range(5, 10, 2):
    print(item)

price = [10, 20, 30]
total = 0
for item in price:
    total += item
print(total)


'Program 2'
for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

'Program 3'
numbers = [5, 2, 5, 2, 2]
for items in numbers:
    print('x' * items)
