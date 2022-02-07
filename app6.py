matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix [0] [1])

for row in matrix:
    for item in row:
        print(item)

numbers = [5,2, 1, 7, 4]

numbers.append(20)
numbers.insert(0, 10)
numbers.remove(5)
numbers.clear()

numbers.pop()
numbers.index(5)
numbers.index(50)
print(50 in numbers)
numbers.count(5)
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()

for item in numbers:
    if item not in numbers2:
        numbers2.append(item)




print(numbers)
