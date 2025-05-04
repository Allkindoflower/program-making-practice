import os
import platform
import time


game_state = {
    'started': False,
    'burden': 0
}


inventory = []

def restart():
    inventory.clear()
    clear()
    gameStart()
    game_state['burden'] = 0
    

def secondChoice():
    time.sleep(2)
    print('''With the creature out of the way, you blankly push forward,
deep in thought, how you appeared here, or if someone brought you here.
''')
    time.sleep(5)
    print('''You feel a disturbance, as someone was watching you behind the trees,
but you can't quite be sure because of the heavy fog blocking your sight.
''')
    print('''You feel uneasy. You feel like you have to take action right now.
1- Stop and prepare to attack whatever comes out of the fog
2- Calmly keep walking
''')
    user_input = input('> ')
    while True:
        if user_input == '1':
            clear()
            game_state['burden'] += 1
            print('Several goblins appear behind the trees and attack you simultaneously.')
            time.sleep(3)
            print('You focus, then dash between the goblins, slitting their throats one by one.')
            time.sleep(3)
            print('They fall before they can realize what was going on.')
            time.sleep(3)
            print('You press on.')
            break
        elif user_input == '2':
            clear()
            print('''Keeping your composure, you keep walking. Your eye catches movement behind the trees,
but nothing worthwile happens.''')
            break
        elif user_input == 'quit':
            print('You cannot escape your burden forever.')
            time.sleep(2)
            quit()
        else:
            print('I do not understand that input, try something else.')

def firstChoice():
    while True:
        choice = input('> ')
        if choice == '1' and hasBlade(inventory):
            game_state['burden'] += 1
            clear()
            print('You kill the creature in one swift motion of your Rusty Switchblade.')
            secondChoice()
        elif choice == '1' and not hasBlade(inventory):
            print('''You attack the creature, but you do not have a weapon.
The creature quickly overpowers and slits your throat with a sharp objects.
The creature then flees, whereas you bleed to death, wondering what kind of mistake you made.''')
            time.sleep(3)
            clear()
            heroDeath()
        elif choice == '3' and hasBlade(inventory):
            clear()
            print('''You approach the creature, attempting to communicate. 
As soon as you are in range of it, it smells violence on you and suddenly leaps on you, and slices your throat out with a sharp object you could not register.
The creature then flees, whereas you bleed to death where you stand, wondering what you did wrong.
''')    
            heroDeath()    
        elif choice == '2':
            clear()
            print('''You avoid the creature, circling around it, you find the rest of the path.''')
            secondChoice()
        elif choice == '3' and not hasBlade(inventory):
            print('''You attempt to communicate with the creature, but it gets startled and flees deeper into the woods,
you are left alone for once more.''')
            secondChoice()
        elif choice == 'quit':
            print('You cannot escape your burden forever.')
            time.sleep(2)
            quit()
        else:    
            print('I do not understand that input, try something else.')          

def bladePickupChoice():
    while True:
            y_or_n = input('Do you pick it up? (Y/N)' ).lower().strip()
            if y_or_n == 'y':
                    game_state['burden'] += 1
                    inventory.append('Rusty Switchblade')
                    clear()
                    print('You disregarded the note and have obtained the Rusty Switchblade.')
                    time.sleep(2)
                    print('You press on.')
                    time.sleep(1)
                    break
            elif y_or_n == 'n':
                    print('You step over the blade.')
                    time.sleep(2)
                    print('You continue on.')
                    time.sleep(1)
                    break
            elif y_or_n == 'quit':
                print('You cannot escape your burden forever.')
                time.sleep(3)
                quit()
            else:
                print('Please choose a valid option(yes or no).')

def gameStart():
    if game_state['started'] == True:
        print('Game already started.')
    else:
        game_state['started'] = True
        print('''You find yourself inside of an abandoned cabin in the woods. You look around the cabin, the interior is devastated, 
as it looks like there was a huge struggle here. You notice a rusty switchblade on the floor with a bloody note next to it:
'I know why I did this, but still, my burden is too much to bear.' ''')
        bladePickupChoice()        
        print('''You open the door and go out. It's raining on you, getting you colder.
You walk on the path leading out of the cabin. Between the trees, you can make the shape
of a humanoid creature. It's digging the ground for no reason.
''')
        print ('''1. Attack
2. Avoid it
3. Attempt to communicate
''')
        firstChoice()

def printHelp():
    clear()
    print('''start - to shoulder your burden
            
help - for help
            
Y or N - yes or no
            
Number choices - Choose an action

inv - to check your inventory
          
res - restart the game from the beginning
            
quit - to avoid your burden
''')
    
def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    
def hasBlade(inventory):
    #checks if player has the blade 
    if 'Rusty Switchblade' in inventory:
        return True
    else:
        return False
    
def heroDeath():
    #hero dies, replay logic
    inventory.clear()
    while True:
        replay = input('You died. Play again? (Y/N)').lower()
        if replay == 'y':
            clear()
            restart()
        elif replay == 'n':
            print('You cannot escape your burden forever.')
            print('Signing off...')
            quit()

def checkInventory(inventory):
    if not game_state['started']: 
        print('You have not shouldered you burden yet...(Game has not started yet)')
    elif not inventory:
        print('You do not have anything at hand.')    
    elif game_state['started']:
        print(''.join(inventory))


print("A Hero's Burden")
print('Type "start" to shoulder your burden. Or "help", if you need some.')
user_input = ''
while True:        
    user_input = input('> ').lower().strip()
    if user_input == 'help':
        printHelp()
    elif user_input == 'quit':
        clear()
        print('You cannot escape your burden forever.')
        print('Signing off...')
        time.sleep(3)
        quit()    
    elif user_input == 'inv':
        checkInventory(inventory)
    elif user_input == 'start':
        clear()
        gameStart()
    elif user_input == 'res':
        restart()
    else:
        print('I do not understand that input...')
        
            
            
             
        






