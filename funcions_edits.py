import random
import main_edits

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 1


def set_number_of_players(text: str) -> int:
    print(text)
    try:
        number = int(input())
        return number
    except ValueError:
        return set_number_of_players("Количетсво игроков должно быть натуральным числом:")







def  add_player(players:int):
    """Функция добавляет игроков. Возвращает cписок имен."""
    array_names = [input(f'Давайте знакомиться. Как зовут игрока №{i}: ') for i in range(1, players + 1)]
    players = dict.fromkeys(array_names, 0)
    return players
    
    
    
def checking_guess(guess, answer):
    """Сравнение пользовательского ввода с загаданным числом. Возвращает кол-во совершенных попыток"""
    if guess < answer:
        print('Загаданное число больше')
    elif guess > answer:
        print('Загаданное число меньше')
    else:
        print(f'Поздравляю, вы отгадали! Было загадано число {answer}.')
    

def choose_difficulty():
    """функция для определения уровня сложности. Возвращает кол_во попыток"""
    print(f'Для начала выберем уровень сложности: \n1.Легкий\n2.Сложный')
    difficulty = int(input('Выбор:'))
    if difficulty == 1:
        print(f'Вы выбрали уровень сложности: Легкий.')
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == 2:
        print(f'Вы выбрали уровень сложности: Сложный.')
        return HARD_LEVEL_ATTEMPTS
    
       
    
def greeting(number_of_players):
    """Приветствие в зависимости от количества игроков"""
    print('Добро пожаловать в игру «Угадай число».')
    print('Я загадал число от 1 до 100.')
    print('Вам предстоит его отгадать.')
    if number_of_players == 1:
        print('У вас будет два уровня сложности: легкий и тяжелый.\nВ легком у вас будет 10 попыток, в тяжелом - 5.')
    
def single_player():

    random_number = random.randint(1, 100)
    
    turns = choose_difficulty()
    user_guess = 0
    
    while  user_guess != random_number:
        print(f'У вас осталось {turns} попыток')
        user_guess = int(input('Введите ваше число: '))
        
        checking_guess(user_guess, random_number) # проверяем ввод
        turns -=1 #уменьшаем количество доступных попыток
        
        if turns == 0:
            print(f'Вы так и не смогли отгадать число {random_number}. Вы проиграли.')
            return
        print('Не угадали, давайте еще раз.')
        
#         while turns: # пока количетсво попыток больше или равно 1 - играем.
#             print('Не угадали, давайте еще раз.')
#         print(f'Вы так и не смогли отгадать число {random_number}. Вы проиграли.')
        
        
def multiplayer():

    players = add_player(main_edits.count_players)
  
    for name in (players):
        #Для каждого игрока будут разные случайные числа
        random_number = random.randint(1, 100)
        user_guess = 0
        print(f'Сейчас ходит {name}')
        while  user_guess != random_number:   
            players[name] += 1
            print(f'Количество совершенных ходов: {players[name]}.')
            user_guess = int(input('Введите ваше число: '))
            # функцией checking_guess проверяем ввод и загаданное число.
            checking_guess(user_guess, random_number)
            
            
    #Превращаем словарь в список и сортируем по кол-ву попыток.
    pairs = list(players.items())
    pairs.sort(key=lambda pairs: pairs[1])
    print(f'Побеждает {pairs[0][0]}. Количество ходов {pairs[0][1]}')
    
    
    
    