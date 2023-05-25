import time
import random
import single_game




# функция добавляет игроков, если игроков больше одного, возвращает cписок имен.
def  add_player(players):
    if players > 1:
        name_player = [input(f'Давайте знакомиться. Как зовут игрока №{i}: ') for i in range(1, players + 1)]
        return name_player
    else:
        name_player = [input('Давайте знакомиться. Как вас зовут?: ') for i in range(1, players + 1)]
        return name_player          

    
# Сравнение пользовательского ввода с загаданным числом. Возвращается оставшееся кол-во попыток 
def checking_guess(guess, answer, turn):
    if guess < answer:
        print('Загаданное число больше')
        return turn + 1
    elif guess > answer:
        print('Загаданное число меньше')
        return turn + 1
    else:
        print(f'Поздравляю, вы отгадали! Было загадано число {answer}.')
        return turn + 1


# Функция рекуссия 
def game():
    
    print('Добро пожаловать в игру «Угадай число».')
    time.sleep(1.5)
    print('Я загадал число от 1 до 100.')
    time.sleep(1.5)
    print('Вам предстоит его отгадать.')
    time.sleep(1.5)
    print('У вас будет два уровня сложности: легкий и тяжелый.\nВ легком у вас будет 10 попыток, в тяжелом - 5.')
    time.sleep(1.5)
       
    players = add_player(player_input)
            
    #Задаем в переменную turns кол-во попыток.
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
            turns = checking_guess(user_guess, random_number, turns)
            
            name_and_turns[players[name]] = turns
            
    #Превращаем словарь в список и сортируем по кол-ву попыток.
    pairs = list(name_and_turns.items())
    pairs.sort(key=lambda pairs: pairs[1])
    print(f'Побеждает {pairs[0][0]}. Количество ходов {pairs[0][1]}')


while input('Поиграем?\n').lower() == 'да':
    player_input = int(input('Сколько игроков будет играть?:\n'))
    if player_input == 1:
        #Если один игрок, то направляемся в файл одиночной игры: в нем ограниченное кол-во попыток 
        single_game.single()
    elif player_input > 1:
        game()
    
print('Спасибо за игру.')
                











