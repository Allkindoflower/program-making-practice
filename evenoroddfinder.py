user_input = ''
def evenOrOdd(user_input): 
    while user_input != 'exit':
        user_input = input('Enter a number to see if it is even or odd, or type exit to exit: ').lower()
        if user_input == 'exit':
            print('Exiting...')
            break
        else:
            try:
                user_input = int(user_input)
            except ValueError:
                    print('Your input is not correct, try again')
                    continue
            if user_input == 0:
                print('You typed 0, you rapscallion, 0 is neither even nor odd')
            elif (user_input % 2 == 0):
                print('Even')
            elif (user_input % 2 != 0):
                print('Odd')
            
                
                                        
evenOrOdd(user_input)