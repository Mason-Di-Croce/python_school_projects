import random


def main():
    print('-----------------------------')
    print('Welcome to Skeleton Scuffle!')
    print('-----------------------------')

    class_name, user_health, max_damage, damage_chance = player_generator()
    monster_health = 33
    round = 1
    print(f'Good luck, mighty {class_name}!')

    while check_for_winner(user_health, monster_health) == True:
        dodged_damage, user_damage = user_turn_damage(max_damage)
        monster_damage = computer_turn_damage()
        if dodged_damage == 0:
            if hit_check(damage_chance) == True:
                print(f'Round {round}:')
                print(f'Your {class_name} hits the skeleton for {user_damage} points of damage')
                print(f'The skeleton hits your {class_name} for {monster_damage} points of damage')
                user_health -= monster_damage
                monster_health -= user_damage
                print(f'Results: {class_name} - {user_health} health, Skeleton - {monster_health} health')
                round += 1
                print('1')
            else:
                print(f'Round {round}:')
                print(f'Your {class_name} hits the skeleton for {user_damage} points of damage')
                print(f'The skeleton misses your {class_name} this turn.')
                monster_health -= user_damage
                print(f'Results: {class_name} - {user_health} health, Skeleton - {monster_health} health')
                round += 1
                print('2')
        else:
            if hit_check(damage_chance) == True:
                print(f'Round {round}:')
                print(f'Your {class_name} hits the skeleton for {user_damage} points of damage')
                print(f'The skeleton dodged {dodged_damage} points of that damage')
                print(f'The skeleton hits your {class_name} for {monster_damage} points of damage')
                user_health -= monster_damage
                monster_health -= user_damage - dodged_damage
                print(f'Results: {class_name} - {user_health} health, Skeleton - {monster_health} health')
                round += 1
                print('3')
            else:
                print(f'Round {round}:')
                print(f'Your {class_name} hits the skeleton for {user_damage} points of damage')
                print(f'The skeleton dodged {dodged_damage} points of that damage')
                print(f'The skeleton misses your {class_name} this turn.')
                monster_health -= user_damage - dodged_damage
                print(f'Results: {class_name} - {user_health} health, Skeleton - {monster_health} health')
                round += 1
                print('4')

    if class_name == 'Bacteria':
        if user_health > monster_health:
            print('*************************************************')
            print(f"Your {class_name} has won the battle, I don't know how but congratulations!")
            print('*************************************************')
        else:
            print('*************************************************')
            print(f"Your {class_name} has lost the battle, it's a bacteria what else did you expect!")
            print('*************************************************')
    else:
        if user_health > monster_health and user_health > 0:
            print('*************************************************')
            print(f'Your {class_name} has won the battle, congratulations!')
            print('*************************************************')
        else:
            print('*************************************************')
            print(f'Your {class_name} has lost the battle, sorry try again!')
            print('*************************************************')


def computer_turn_damage():
    monster_damage = random.randint(1, 4)
    return monster_damage


def user_turn_damage(max_damage):
    user_damage = die_roll(max_damage)
    dodged_damage = 0
    if random.randint(1, 10) == 1:
        dodged_damage += int(user_damage * 0.25)
        return dodged_damage, user_damage
    else:
        return dodged_damage, user_damage


def die_roll(max_damage):
    return random.randint(1, max_damage)


def hit_check(damage_chance):
    if random.randint(1, 100) <= damage_chance:
        return True
    else:
        return False


def check_for_winner(user_health, monster_health):
    if user_health <= 0 or monster_health <= 0:
        return False
    else:
        return True


def player_generator():
    print('1. Fighter  2. Mage  3. Thief  4. Engineer 5. Bacteria')
    while True:
        try:
            player_class = int(input('Choose your character class (1, 2, 3, 4, or 5): '))
            if player_class == 1:
                return 'Fighter', 25, 10, 70
            elif player_class == 2:
                return 'Mage', 18, 14, 60
            elif player_class == 3:
                return 'Thief', 18, 10, 50
            elif player_class == 4:
                return 'Engineer', 16, 18, 65
            elif player_class == 5:
                return 'Bacteria', 1, 1000, 99
            else:
                print('Please enter a valid class')
                continue
        except:
            print('Please enter a valid class')
            continue

main()