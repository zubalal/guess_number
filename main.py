import random
import funcions
import time

def multiplayer():
    players = funcions.add_player(count_players, 0 )
    for name in players:
        #Для каждого игрока будут разные случайные числа
        print(f'Ход игрока {name}')
        random_number = random.randint(1, 100)
        user_guess = 0
        while user_guess != random_number:
            players[name] += 1
            print(f'Количество совершенных ходов: {players[name]}.')
            user_guess = int(input('Введите ваше число: '))
            funcions.checking_guess_multiplayer(user_guess, random_number)
  
    #Превращаем словарь в список и сортируем по кол-ву попыток.
    pairs = list(players.items())
    pairs.sort(key=lambda pairs: pairs[1])
    print(f'Побеждает {pairs[0][0]}. Количество ходов {pairs[0][1]}')




def single_player():

    random_number = random.randint(1, 100)
    
    turns = funcions.choose_difficulty()
    user_guess = 0
    
    while  user_guess != random_number:
        print(f'У вас осталось {turns} попыток')
        user_guess = int(input('Введите ваше число: '))
        
        turns = funcions.checking_guess_singleplayer(user_guess, random_number, turns)
        if turns == 0:
            print(f'Вы так и не смогли отгадать число {random_number}. Вы проиграли.')
            return
        elif user_guess != random_number:
            print('Не угадали, давайте еще раз.')





while input('Поиграем?\n').lower() == 'да' or 'lf':
    count_players = funcions.set_number_of_players('Сколько игроков будет играть?:')
    funcions.greeting(count_players)
    if count_players == 1:
        single_player()
    elif count_players > 1:
        multiplayer()
    
print('Спасибо за игру.')
                

