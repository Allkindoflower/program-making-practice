import os

def userClear(user_command):
    if user_command == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')



print('Your personal notepad, type "help" for a list of commands. Do not worry, there are no SECRETs here...')
user_command = ''


while user_command != 'exit':
    user_command = input('> ').lower().strip()
    if user_command == 'help':
        print('''exit - to quit program
note - add note
read - read all notes
delete - remove a selected note from your list
      
''')
    elif user_command == 'note':
        note = input('Please enter your note: ')
        if note == 'secret':
            print('Holy Moly, you went above and beyond for this one! Props!')
        sure = input('Are you sure you want to add this note? (Y/N)').upper()
        if sure == 'Y':
            try:
                with open('my_notes.txt', 'a') as file:
                    file.write(note + '\n')
                    print('Note added successfully!')
            except FileNotFoundError:
                print('No note file created yet.')
        elif sure == 'N':
            print('You cancelled your note addition...')
    elif user_command == 'read':
        print('Here are your notes so far:')
        with open('my_notes.txt', 'r') as file:
            my_notes = file.readlines()
            if not my_notes:
                print('You have no notes saved so far.')
            else:
                for i, note in enumerate(my_notes, start=1):
                    print(f'{i}. {note.strip()}')
    elif user_command == 'delete':
        try:
            with open('my_notes.txt', 'r') as file:
                my_notes = file.readlines()
            for i, note in enumerate(my_notes, start=1):
                print(f'{i}. {note.strip()}')
            delete_selection = int(input('Please type the number of note you want to delete: '))           
            if delete_selection >= 1 and delete_selection <= len(my_notes):
                print(f'Are you sure to delete selected note: {delete_selection}')
                user_command = input('> ').lower().strip()
                if user_command == 'y':
                    del my_notes[delete_selection - 1]
                    with open('my_notes.txt', 'w') as file:
                        file.writelines(my_notes)
                    print('Note successfully deleted!')
                elif user_command == 'n':
                    print('You have cancelled the operation.')
                else:
                    print('Please try again and enter a valid input. (Y/N)')
            else:
                print('You entered an invalid number, please try again.')
        except ValueError:
            print('You entered an invalid number, please try again.')
    elif user_command in ['exit', 'quit']:
        print('Signing off...')
        break
    elif user_command == 'clear':
        userClear(user_command)
        print('Terminal successfully cleared!')
    elif user_command == 'secret':
        print('Wow, you really are desperate for easter eggs are you not?')
    else:
        print('Sorry, I do not understand that... Try something else')

    
    

