import funcions


while input('Поиграем?\n').lower() == 'да' or 'lf':
    count_players = funcions.set_number_of_players('Сколько игроков будет играть?:')
    funcions.greeting(count_players)
    if count_players == 1:
        funcions.single_player()
    elif count_players > 1:
        funcions.multiplayer(count_players)

print('Спасибо за игру.')
                