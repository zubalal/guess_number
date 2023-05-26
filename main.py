import random
import funcions
import time

def multiplayer():
    
    funcions.greeting(player_input)
       
    players = funcions.add_player(player_input)
            
    turns = 0
    
    name_and_turns = dict.fromkeys(players, turns)
    
    for name in range(len(players)):
        #Для каждого игрока будут разные случайные числа
        random_number = random.randint(1, 100)
        user_guess = 0
        turns = 0
        print(f'Сейчас ходит {players[name]}')
        while  user_guess != random_number:   
            print(f'Количество совершенных ходов: {turns}.')
            user_guess = int(input('Введите ваше число: '))
            
            # функцией checking_guess проверяем ввод и загаданное число.
            turns = funcions.checking_guess_multiplayer(user_guess, random_number, turns)
            
            name_and_turns[players[name]] = turns
            
    #Превращаем словарь в список и сортируем по кол-ву попыток.
    pairs = list(name_and_turns.items())
    pairs.sort(key=lambda pairs: pairs[1])
    print(f'Побеждает {pairs[0][0]}. Количество ходов {pairs[0][1]}')




def single_player():

    random_number = random.randint(1, 100)
    
    funcions.greeting(player_input)
    
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
    player_input = int(input('Сколько игроков будет играть?:\n'))
    if player_input == 1:
        single_player()
    elif player_input > 1:
        multiplayer()
    
print('Спасибо за игру.')
                

