numbers = (1, 2, 3)
x, y, z = numbers

customer = {
    'name': 'John Smith',
    'age': 30,
    'is_verified': True
}

print(customer['name'])

numbers = input('Phone: ')


customer = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three'
}

for ch in numbers:
    game = customer.get(ch, '!')
print(game)


def emoji_converter(message1):
    words = message1.split(' ')
    emojis = {
        ':)': "😊",
        ':(': '😟'
    }

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '


message = input('>')
print(emoji_converter(message))


def greet_user(name):
    print(f'Hi There! {name}')
    print('Welcome aboard')


print('Start')
greet_user('John')
print('Finish')


def square(number):
    return number * number


print(square(3))

try:
    age = int(input('age: '))
    print(age)
except ValueError:
    print('Invalid Value') 


