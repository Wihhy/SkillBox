from random import randint


def dicer(game_1, game_2):

    game_1_counter = 0
    game_2_counter = 0
    iteration = 0
    while True:
        dice = randint(0, 10)
        res = dice % 2
        iteration += 1
        if res == 0:
            game_1_counter += 1
            game_2_counter = 0
        if res == 1:
            game_2_counter +=1
            game_1_counter = 0
        if game_1_counter == 10:
            print(f'Победила {game_1}!')
            break
        if game_2_counter == 10:
            print(f'Победила {game_2}!')
            break
        print(f'Круг: {iteration}')


dicer(game_1='Идём по шаурму и к воде', game_2='К воде без шаурмы')
