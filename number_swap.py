import random

a, b, c = 1, 2, 3
num = [a, b, c]

random.shuffle(num)

a, b, c = num

print(num)