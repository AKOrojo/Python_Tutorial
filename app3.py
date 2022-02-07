is_hot = True
is_cold = False

if is_hot:
    print('it is a hoot day')
elif is_cold:
    print('its is a cold day')
else: print('it is a lovely day')
print('Enjoy your day')

if is_hot and is_cold:
    print('Bi-Polar Weather')
if is_hot or is_cold:
    print('Bi-Polar Weather')
if is_hot and not is_cold:
    print('Bi-Polar Weather')

name = 'bani'

if len(name) < 3:
    print('greater than 3 char')

'Weigh Coverter'

weight = input('what is your weight ')
unit = input('is this (K)g or (l)BS')

if unit == 'l' or unit == 'L':
    convertion = int(weight) / 2
    print(str(convertion) + ' kg')
elif unit == 'K' or unit == 'k':
    convertion = int(weight) * 2
    print(str(convertion) + ' lbs')
