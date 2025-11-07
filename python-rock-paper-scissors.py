import random



print("sang...")
print("kaghaz...")
print("ghychi...")


player_1_wins = 0
player_2_wins = 0
winning_score = 3
while player_1_wins < winning_score and player_2_wins < winning_score:
    print(f"player_1 wins : {player_1_wins} | player_2 wins : {player_2_wins}")
    randomNumber =  random.randint(0,2)
    if randomNumber == 0:
        computerMove = 'sang'
    elif randomNumber == 1:
        computerMove = "kaghaz"
    elif randomNumber == 2:
        computerMove = "ghychi"
    
    player_1 = str(input('player_1 , make your move: '))
    player_2 = computerMove
    print(f'player_2 , make your move: {player_2}')

    if player_1 == 'q' or player_1 == 'quit':
        break


    if player_1 == 'sang' and player_2 == 'kaghaz':
        print('player_2 wins! ')
        player_2_wins += 1

    elif player_1 == 'sang' and player_2 == 'ghychi':
        print('player_1 wins!')
        player_1_wins += 1

    elif player_1 == 'kaghaz' and player_2 == 'sang':
        print('player_1 wins!')
        player_1_wins += 1

    elif player_1 == 'kaghaz' and player_2 == 'ghychi':
        print('player_2 wins!')
        player_2_wins += 1

    elif player_1 == 'ghychi' and player_2 == 'sang':
        print('player_2 wins!')
        player_2_wins += 1

    elif player_1 == 'ghychi' and player_2 == 'kaghaz':
        print('player_1 wins!')
        player_1_wins += 1

    elif player_1 == player_2:
        print('thats a tie...')
    else:
        print('somthing wants...')



print(f"player_1 wins : {player_1_wins} | player_2 wins : {player_2_wins}")

print('this final score player')

if player_1_wins == 3:
    print('player_1 wins =)')

elif player_2_wins == 3:
    print('player_2 wins =)')
    
else:
    print('player_1 tie this player_2...')