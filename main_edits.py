import funcions_edits




while input('Поиграем?\n').lower() == 'да':
    count_players = funcions_edits.set_number_of_players('Сколько игроков будет играть?:')
    funcions_edits.greeting(count_players)
    if count_players == 1:
        funcions_edits.single_player()
    elif count_players > 1:
        funcions_edits.multiplayer()
    
print('Спасибо за игру.')
                

