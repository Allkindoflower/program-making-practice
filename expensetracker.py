
expenses = {
    'Food': 0,
    'Transportation': 0,
    'Bills': 0,
    'Entertainment': 0,
    'Emergency': 0
}

def expenseAddLogic():
    print('Please enter the category of your expense.')
    chosen_category = input('> ').strip().capitalize()
    if chosen_category not in expenses:
        print('That category is invalid, please try again.')
    print('Please choose an expense value.')
    try:
        expense_value = int(input('> '))
    except ValueError:
        print('Please enter a valid positive number.')
        return
    if chosen_category in expenses:
        expenses[chosen_category] += expense_value
        print('Expense successfully added!')
    
def viewExpenses():
    print('\n ----- Expense Overview -----')
    for category, amount in expenses.items():
        print(f'{category:<15}: {amount:>5}')
    print('\n ----------------------------')


def printHelp():
    print('''
help - for a list of commands
add - to add an expense
view - to view all expenses
quit - to quit program

all categories:
food
transportation
bills
entertainment
emergency
''')

print('"help" for a list of commands.')

while True:
    user_command = input('> ')
    if user_command == 'add':
        expenseAddLogic()
    elif user_command == 'help':
        printHelp()   
    elif user_command == 'view':
        viewExpenses()
    elif user_command == 'quit':
        quit()
    else:
        print('Sorry, I do not understand that.')
    













