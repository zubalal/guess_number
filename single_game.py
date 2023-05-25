import time
import random


# константы с кол-вом попыток
HARD_LEVEL_ATTEMPTS = 5
EASY_LEVEL_ATTEMPTS = 1

def cls():
    print ("\n" * 100)


# функция для определения уровня сложности. Возвращает кол_во попыток
def choose_difficulty():
    level = input('Для начала выберем уровень сложности. Сложный/Легкий:').lower()
    if level == 'сложный':
        print(f'Вы выбрали уровень сложности: {level.title()}.')
        return HARD_LEVEL_ATTEMPTS
    elif level == 'легкий':
        print(f'Вы выбрали уровень сложности: {level.title()}.')
        return EASY_LEVEL_ATTEMPTS
    
    
# Сравнение пользовательского ввода с загаданным числом. Возвращается оставшееся кол-во попыток 
def checking_guess(guess, answer, turn):
    if guess < answer:
        print('Загаданное число больше')
        return turn - 1
    elif guess > answer:
        print('Загаданное число меньше')
        return turn - 1
    else:
        print(f'Поздравляю, вы отгадали! Было загадано число {answer}.')
      

# Функция рекуссия 
def single():
    
    random_number = random.randint(1, 100)
    
    print('Добро пожаловать в игру «Угадай число».')
    time.sleep(1.5)
    print('Я загадал число от 1 до 100.')
    time.sleep(1.5)
    print('Вам предстоит его отгадать.')
    time.sleep(1.5)
    print('У вас будет два уровня сложности: легкий и тяжелый.\nВ легком у вас будет 10 попыток, в тяжелом - 5.')
    time.sleep(1.5)
    cls()
    
    #print(f'Текст для отладки: загаданное число - {random_number}')
    
    #Задаем в переменную turns кол-во попыток.
    turns = choose_difficulty() 
    user_guess = 0
    
    while  user_guess != random_number:
        print(f'У вас осталось {turns} попыток')
        user_guess = int(input('Введите ваше число: '))
        
        # функцией checking_guess проверяем ввод и загаданное число.
        # Так как возвращается кол-во попыток, перезаписываем переменную turns
        turns = checking_guess(user_guess, random_number, turns)
        if turns == 0:
            print(f'Вы так и не смогли отгадать число {random_number}. Вы проиграли.')
            return
        elif user_guess != random_number:
            print('Не угадали, давайте еще раз.')
            

if __name__ == "__main__": 
    single()
#while input('Поиграем?\n').lower() == 'да':
#abc = single()
    
    
#print('Спасибо за игру.')
                











