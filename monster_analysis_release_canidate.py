import random


def main():
    print('-----------------------------')
    print('Welcome to Skeleton Scuffle!')
    print('-----------------------------')

    class_num = 1
    class1_wins = 0
    class2_wins = 0
    class3_wins = 0
    class4_wins = 0
    class5_wins = 0

    while class_num <= 5:
        num_of_games = 0
        while num_of_games < 100:
            class_name, user_health, max_damage, damage_chance = player_generator(class_num)
            monster_health = 33

            while check_for_winner(user_health, monster_health) == True:
                dodged_damage, user_damage = user_turn_damage(max_damage)
                monster_damage = computer_turn_damage()
                if dodged_damage == 0:
                    if hit_check(damage_chance) == True:
                        user_health -= monster_damage
                        monster_health -= user_damage
                    else:
                        monster_health -= user_damage
                else:
                    if hit_check(damage_chance) == True:
                        user_health -= monster_damage
                        monster_health -= user_damage - dodged_damage
                    else:
                        monster_health -= user_damage - dodged_damage

            if user_health > monster_health and user_health > 0:
                num_of_games += 1
                if class_num == 1:
                    class1_wins += 1
                elif class_num == 2:
                    class2_wins += 1
                elif class_num == 3:
                    class3_wins += 1
                elif class_num == 4:
                    class4_wins += 1
                else:
                    class5_wins += 1
            else:
                num_of_games += 1

        class_num += 1

    print('Here is each classes number of wins!')
    print(f'Fighter: {class1_wins}')
    print(f'Mage: {class2_wins}')
    print(f'Thief: {class3_wins}')
    print(f'Engineer: {class4_wins}')
    print(f'Bacteria: {class5_wins}')


def computer_turn_damage():
    monster_damage = random.randint(1, 8)
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


def player_generator(player_class):
            if player_class == 1:
                return 'Fighter', 25, 10, 70
            elif player_class == 2:
                return 'Mage', 18, 14, 60
            elif player_class == 3:
                return 'Thief', 18, 10, 50
            elif player_class == 4:
                return 'Engineer', 16, 18, 65
            else:
                return 'Bacteria', 1, 1000, 99


main()