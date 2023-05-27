import time

HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 1


def set_number_of_players(text: str) -> int:
    print(text)
    try:
        number = int(input())
        return number
    except ValueError:
        return set_number_of_players("Количетсво игроков должно быть натуральным числом:")


def  add_player(players):
    """Функция добавляет игроков. Возвращает cписок имен."""
    if players > 1:
        name_player = [input(f'Давайте знакомиться. Как зовут игрока №{i}: ') for i in range(1, players + 1)]
        return name_player
    else:
        name_player = [input('Давайте знакомиться. Как вас зовут?: ') for i in range(1, players + 1)]
        return name_player
    
    
    
def checking_guess_multiplayer(guess, answer, turn):
    """Сравнение пользовательского ввода с загаданным числом. Возвращает кол-во совершенных попыток"""
    if guess < answer:
        print('Загаданное число больше')
        return turn + 1
    elif guess > answer:
        print('Загаданное число меньше')
        return turn + 1
    else:
        print(f'Поздравляю, вы отгадали! Было загадано число {answer}.')
        return turn + 1
    

def choose_difficulty():
    """функция для определения уровня сложности. Возвращает кол_во попыток"""
    level = input('Для начала выберем уровень сложности. Сложный/Легкий:\n').lower()
    if level == 'сложный':
        print(f'Вы выбрали уровень сложности: {level.title()}.')
        return HARD_LEVEL_ATTEMPTS
    elif level == 'легкий':
        print(f'Вы выбрали уровень сложности: {level.title()}.')
        return EASY_LEVEL_ATTEMPTS
    
    
def checking_guess_singleplayer(guess, answer, turn):
    """Сравнение пользовательского ввода с загаданным числом. Возвращается оставшееся кол-во попыток."""
    if guess < answer:
        print('Загаданное число больше')
        return turn - 1
    elif guess > answer:
        print('Загаданное число меньше')
        return turn - 1
    else:
        print(f'Поздравляю, вы отгадали! Было загадано число {answer}.')    
    
    
def greeting(number_of_players):
    """Приветствие в зависимости от количества игроков"""
    if number_of_players == 1:
        print('Добро пожаловать в игру «Угадай число».')
        time.sleep(1.5)
        print('Я загадал число от 1 до 100.')
        time.sleep(1.5)
        print('Вам предстоит его отгадать.')
        time.sleep(1.5)
        print('У вас будет два уровня сложности: легкий и тяжелый.\nВ легком у вас будет 10 попыток, в тяжелом - 5.')
        time.sleep(1.5)
    elif number_of_players > 1:
        print('Добро пожаловать в игру «Угадай число».')
        time.sleep(1.5)
        print('Я загадал число от 1 до 100.')
        time.sleep(1.5)
        print('Вам предстоит его отгадать.')
        time.sleep(1.5)
    
    
    
    
    
    