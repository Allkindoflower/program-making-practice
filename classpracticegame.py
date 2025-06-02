import random
import time


class Character():
    def __init__(self, name, current_hp, max_hp, damage, speed, role, status):
        self.name = name
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.damage = damage
        self.speed = speed
        self.role = role
        self.status = status
        self.status_effects = {}
    def attack(self, target):
        print(f"{self.name} attacks...")
        self.deal_damage(target)
    def cast_spell(self, target):
        print(f"{self.name} casts Hurt...")
        target.current_hp -= self.damage
        target.check_death()
    def take_damage(self, damage):
        self.current_hp -= damage
        print(f'{self.name} takes {damage} damage!')  
        self.check_death()
    def deal_damage(self, target):
        target.current_hp -= self.damage
        print(f'{self.name} deals {self.damage} damage!')
        target.check_death()
    def check_death(self):
        if self.current_hp <= 0:
            self.status = 'dead'
            self.current_hp = 0
    
   
class FireMage(Character):
    def __init__(self, name, current_hp, max_hp, damage, dot, speed, role, status):
        self.dot = dot
        super().__init__(name, current_hp, max_hp, damage, speed, role, status)
    def cast_fireball(self, target):
        target.take_damage(self.damage)
        print(f'{self.name} casts fireball for {self.damage} fire damage!')
    def ablaze(self, dot, target):
        target.take_damage(dot)


class Berserker(Character):
    def __init__(self, name, current_hp, max_hp, damage, speed, role, status):
        super().__init__(name, current_hp, max_hp, damage, speed, role, status)
    def cast_rage(self):
        self.damage *= 2
        self.max_hp += 25
        print(f'{self.name} casts rage! Damage and Maximum Health increased!')

class Ninja(Character):
    def __init__(self, name, current_hp, max_hp, damage, speed, role, status):
        super().__init__(name, current_hp, max_hp, damage, speed, role, status)
    def backstab(self, target):
        if turn_count == 1:
            self.deal_damage(target)
            print(f'{self.name} backstabs for {self.damage * 2}!')
            target.check_death()
        else:
            self.deal_damage(target)
            print(f'{self.name} deals {self.damage} damage!')
            target.check_death()
    def attack(self, target):
        if turn_count == 1:
            self.backstab(target)
        else:
            super().attack(target)

            

def flip_coin(char1, char2):
    return random.choice([char1, char2])

def whose_turn(char1, char2):
    if char1.speed > char2.speed:
        print(f"{char1.name}'s turn!")
        time.sleep(1)
        return char1
    elif char2.speed > char1.speed:
        print(f"{char2.name}'s turn!")
        time.sleep(1)
        return char2
    else:
        return flip_coin(char1, char2)

        
char1 = Character('Jimmy', 150, 150, 25, 3, 'warrior', 'alive')

char3 = Character('Luna', 75, 75, 50, 2, 'mage', 'alive')

char4 = FireMage('Zara-el', 80, 80, 75, 5, 2, 'fire mage', 'alive')

char2 = Ninja('Kage', 50, 50, 75, 5, 'ninja', 'alive')

def choose_attacker_and_defender(char1, char2):
    first = whose_turn(char1, char2)
    if first == char1:
        second = char2
    else:
        second = char1
    return first, second

def switch_turns(attacker, defender):
    return defender, attacker

attacker, defender = choose_attacker_and_defender(char1, char2)
turn_count = 0
while char1.current_hp > 0 and char2.current_hp > 0:
    turn_count += 1
    if isinstance(attacker, Ninja) and turn_count == 1:
        attacker.backstab(defender)
        defender.check_death()
        if defender.status == 'dead':
            print(f'{defender.name} meets their demise, {attacker.name} wins!')
            break
        else:
            attacker, defender = switch_turns(attacker, defender) 
    else:
        attacker.attack(defender)
        if defender.status == 'dead':
            print(f'{defender.name} meets their demise, {attacker.name} wins!')
            time.sleep(2)
            break
        else:
            time.sleep(1)
            attacker, defender = switch_turns(attacker, defender)  
            time.sleep(1)
    
    
def ablaze(self, target):
    pass
        


    