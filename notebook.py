
print('Your personal notepad, type "help" for a list of commands. Do not worry, there are no SECRETs here...')

user_notes = []
user_command = ''


while input != 'exit':
    user_command = input('> ').lower().strip()
    if user_command == 'help':
        print(''' exit - to quit program
note - add note
read - read all notes       
''')
    elif user_command == 'note':
        note = input('Please enter your note: ')
        if note == 'secret':
            print('Holy Moly, you went above and beyond for this one! Props!')
        sure = input('Are you sure you want to add this note? (Y/N)').upper()
        if sure == 'Y':
            user_notes.append(note)
            print('Note added successfully!')
        elif sure == 'N':
            print('You cancelled your note addition...')
            continue
    elif user_command == 'read':
        print('Here are your notes so far:')
        print(user_notes)
    elif user_command == 'exit' or 'quit':
        print('Signing off...')
        break
    elif user_command == 'secret':
        print('Wow, you really are desperate for easter eggs are you not?')
    else:
        print('Sorry, I do not understand that... Try something else')

    
    

