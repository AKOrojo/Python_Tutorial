import converters
from converters import kg_to_lbs
import ecommerce.shipping

ecommerce.shipping.calc_shipping()
from ecommerce import shipping

import random

for i in range(3):
    print(random.random())
    print(random.randint(10, 20))


memebers = ['john', 'mary', 'bob']

leader = random.choice(memebers)

print(leader)
shipping.calc_shipping()

kg_to_lbs(100)
numbers = [1, 2, 3]
print(converters.find_max(numbers))
print(converters.kg_to_lbs(70))

