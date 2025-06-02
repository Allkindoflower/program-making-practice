def removeDuplicates(list):
    uniques = []
    for number in list:
        if number not in uniques:
            uniques.append(number)
    return uniques
    
print('Enter a series of numbers to remove the duplicates in the following fashion: (1, 2, 3, 4, 4)')
try:    
    usr_cmd = input('> ').strip('()')
    splitted = usr_cmd.split(', ')
    splitted = [int(char) for char in splitted]
    print('Removed duplicates succesfully!')
    print(removeDuplicates(splitted))
except ValueError:
    print('Please enter a valid set of numbers in the correct format.')






