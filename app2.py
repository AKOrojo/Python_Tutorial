import math

first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)
msg = f'{first} [{last}] is a coder'
print(msg)

'String Method'
course = ' python for beginners'
print(len(course))

print(course.upper())
print(course.lower())

course.find('P')
course.find('for')
course.replace('for','of')

print('for' in course)

'Arithemtic Operator'
print(10 + 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

x = 10
x = x + 3
x +=3
print(x)

x = 2.9
print(abs(-2.9))
print(round(2.9))
print(math.ceil(2.9))
print(math.floor(2.9))

