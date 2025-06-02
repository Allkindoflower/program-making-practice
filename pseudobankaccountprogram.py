class BankAccount():
    def __init__(self, user_name, pin, balance):
        self.user_name = user_name
        self.pin = pin
        self.balance = balance
     
    def account_controls(self):
         pass
    
           
def login(user_name, user_password):
    max_pin_attempt = 3
    pin_attempt_count = 0
    while True:
        print('Please enter your account name: ')
        user_name = input('> ')
        if user_name not in accounts:
            print('There are no accounts matching that name, please try something else!')
            continue
        else:  
            print('Please enter your PIN code: ')
            user_password = int(input('> '))
        if pin_attempt_count == max_pin_attempt:
            print('You entered the wrong PIN too many times, your account is blocked!')       
        else:
            print('Wrong PIN, please try again.')
            pin_attempt_count += 1
        if user_name in BankAccount(user_name) and user_password == BankAccount(pin): 
            print('Login successful, welcome to your bank account!')
            pin_attempt_count = 0
            return True




def authenticate(user_name, user_password, max_pin_attempt):
    pass


accounts = {
    'namesurname': BankAccount('namesurname', 1234, 1000),
    'johnsmith': BankAccount('johnsmith', 4321, 5000)
}


pin = 1234

balance = 10000
print('Welcome to your sign-in window! Type "login" to log into an account.')
login_command = input('> ').lower().strip()


while True:
    if login_command == 'login':
        login(user_name, user_password) 
        user_action = int(input('Choose a number for your action (1 - Check Balance, 2 - Withdraw money, 3 - Deposit money): '))       
    elif user_action == 1:
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
