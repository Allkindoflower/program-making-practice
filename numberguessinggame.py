import random


print('Welcome to number guessing game! 1 through 10')
secret_number = random.randint(1, 10)
guess = 0
guess_count = 0
max_guess = 3

while guess != secret_number:     
    guess = int(input('Your guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You win!')
        break
    elif guess_count == max_guess:
        print('You lose!')
        break
    else:
        print('Try again!')
        

    
   
    


    