numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    0: 'Zero'
}

user_input = int(input('Phone: '))

user_input = str(user_input)

for char in user_input:
    print(numbers[int(char)])




