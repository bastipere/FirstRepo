
#Import
import random
#Cachipun is what rock paper scissors is called in Chile
def game():
    print('=============================')
    print('        CACHIPUN GAME       ')
    print('\n1) ✊')
    print('2) ✋')
    print('3) ✌️')
    print('\n=============================')

    result = ''

    while result != 'player_wins':
        #Player
        def player():
            elec = int(input('\nSelect (1-3): '))
            if elec == 1:
                return '✊'
            elif elec == 2:
                return '✋'
            elif elec == 3:
                return '✌️'
            else:
                return 'Invalid option'
            return elec

        #CPU
        def cpu():
            cpuelec = random.randint(1,3)
            if cpuelec == 1:
                return '✊'
            elif cpuelec == 2:
                return '✋'
            elif cpuelec == 3:
                return '✌️'
            return cpuelec

        #Player and CPU choice
        player_select = player()
        print(f'\nPlayer: {player_select}')
        cpu_select = cpu()
        print(f'CPU: {cpu_select}')

        #Results
        if player_select == cpu_select:
            result = 'tie'
            print('\nTie')
        elif player_select == '✊' and cpu_select == '✌️':
            result = 'player_wins'
            print('\nPlayer wins')
        elif player_select == '✋' and cpu_select == '✊':
            result = 'player_wins'
            print('\nPlayer wins')
        elif player_select == '✌️' and cpu_select == '✋':
            result = 'player_wins'
            print('\nPlayer wins')
        else:
            result = 'cpu_wins'
            print('\nCPU wins')

    if result == 'player_wins':
        print('\nCongratulations, you won!')
    return

star_game = ''

while star_game.upper() != 'n':
    game()
    star_game = input('\nPlay Again? (Y/N): ')

print('\nThanks for playing!')




