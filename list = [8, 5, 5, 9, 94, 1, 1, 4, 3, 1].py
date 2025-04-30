list = [8, 5, 5, 9, 94, 1, 1, 4, 3, 1]

def removeDuplicates(list):
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
    print(new_list)

removeDuplicates(list)
