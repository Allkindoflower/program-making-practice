print('Welcome to the car game! Type "help" for commands.')
user_input = ''
engine = False
while True: 
    user_input = input('> ').lower()      
    if user_input == 'start':
        if not engine:
            print('car started, ready to go!')
            engine = True
        else:
            print('car already running')                  
    elif user_input == 'stop':
        if engine:
            print('car is stopped')
            engine = False
        else:
            print('car is already stopped')
    elif user_input == 'help':
        print('''start - to start car
stop - to stop car
quit - to exit ''')
    elif user_input == 'quit':
        break
    else:
        print('I do not understand that...')


    


        


