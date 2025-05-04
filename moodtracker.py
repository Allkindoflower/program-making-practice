
print('This is your mood tracker. ')

mood_entry_counter = 0
print('Type "mood" to record your mood today, or "view" to view your mood history. "quit" to quit the program')
while True:   
    user_command = input('> ').lower().strip() 
    if user_command == 'mood':
        user_mood = input('How are you feeling today? ')
        while True:
            sure = input('Are you sure this is your current mood today? (Y/N)').lower().strip()
            if sure == 'y':
                print(f'You are feeling {user_mood} today, your mood has been saved to your history')
                with open('mood_history.txt', 'a') as file:
                    file.write(user_mood + '\n')
                break
            elif sure == 'n':
                print('You cancelled the operation.')
                break
            else:
                print('Please enter a valid input.')    
    elif user_command == 'view':
        try:
            with open('mood_history.txt', 'r') as file:
                lines = file.readlines()
                if not lines:
                    print('You have no saved moods.')
                else:
                    for i, mood in enumerate(lines, start=1):
                        print(f"Day {i}. {mood.strip()}")
        except FileNotFoundError:
            print("No mood history file found yet.")       
    elif user_command == 'quit':
        print('Signing off, see you tomorrow!')
        break
    else:
        print('I do not understand that command, please try "mood" or "view".')