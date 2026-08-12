#functions of random
import random

print(random.random())

print(random.randint(1, 10))  # Example: 7

items = ["apple", "banana", "cherry"]
print(random.choice(items))  # Example: "banana"

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)  # Example: [3, 5, 1, 4, 2]


