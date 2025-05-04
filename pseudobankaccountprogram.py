print('Welcome to your sign-in window! Please only use whole, numerical values.')
pin = 1234
max_pin_attempt = 2
pin_attempt_count = 0
balance = 10000

while True:
    user_password_attempt = int(input('Please enter your PIN code: '))
    if user_password_attempt == pin:
        print('Login successful, welcome to your bank account!')
        pin_attempt_count = 0    
        user_action = -1
        while user_action != 0:     
            user_action = int(input('Choose a number for your action (1 - Check Balance, 2 - Withdraw money, 3 - Deposit money): '))       
            if user_action == 1:
                print(f'You have {balance}TL')
            elif user_action == 2:
                money_withdrawn = int(input('Enter the amount of money you want to withdraw: ')).strip
                if balance >= money_withdrawn:
                    balance -= money_withdrawn
                    print('Withdraw successful!')
                else:
                    print('You do not have enough money in your account!')
            elif user_action == 3:
                money_deposited = int(input('Enter the amount of money you want to deposit: '))
                balance += money_deposited
                print('Deposit successful!')
            elif user_action == 0:
                print('Signing out...')
                quit()
            else:
                print('Invalid input...')        
    elif pin_attempt_count == max_pin_attempt:
        print('You entered the wrong PIN too many times, your account is blocked!')  
        break     
    else:
        print('Wrong PIN, please try again.')
        pin_attempt_count += 1