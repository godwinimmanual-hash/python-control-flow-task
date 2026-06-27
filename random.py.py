# random_demo.py

import random

numbers = [10, 20, 30, 40, 50]

print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(numbers))

random.shuffle(numbers)

print("Shuffled List:", numbers)