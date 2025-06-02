user_weight = int(input('What is your weight? '))
type = input('In pounds(lb) or kilos(kg)? ').lower()


if type == 'lb':
    user_weight = user_weight * 0.453
    print(f'Your weight in kilograms is {user_weight}.')
elif type == 'kg':
    user_weight = user_weight * 2.205
    print(f'Your weight in pounds is {user_weight}.')
else:
    print('Please enter a valid weight type(kg or lb).')


