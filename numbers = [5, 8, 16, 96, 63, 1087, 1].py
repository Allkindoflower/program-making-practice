import random

numbers = [random.randint(0, 100) for _ in range(10)]

print(f'Random numbers generated: {numbers}')

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number
print(f'Largest number in the sequence is {largest_number}.')


