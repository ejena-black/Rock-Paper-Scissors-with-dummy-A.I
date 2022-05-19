from mimetypes import common_types
from random import randint

print('Rock \n Paper \n Scissors')


# Dummy computer A.I setup
computer = None

player = None
goal = int(input('Winning score: '))
player_score = 0
com_score = 0

print(f'You are playing to {goal}')

while player_score < goal and com_score < goal:
    
    # Dummy computer A.I setup
    computer = randint(0, 2)

    if computer == 0:
        computer = 'rock'
    elif computer == 1:
        computer = 'paper'
    elif computer == 2:
        computer = 'scissors'

    player = input('Make your move: ').lower()
    print(f'The computer plays: {computer}')


    # Game logic
    if player:
        if player == computer:
            print('It\'s a tie')
        elif player == 'rock':
            if computer == 'paper':
                print('Computer Wins')
                com_score += 1
            elif computer == 'scissors':
                print('Player Wins')
                player_score += 1
        elif player == 'paper':
            if computer == 'rock':
                print('Player Wins')
                player_score += 1
            elif computer == 'scissors':
                print('Computer Wins')
                com_score += 1
        elif player == 'scissors':
            if computer == 'rock':
                print('Computer Wins')
                com_score += 1
            elif computer == 'paper':
                print('Player Wins')  
                player_score += 1 
    else:
        print(f'Player has not made a move,')

    if player_score == goal:
        break
    elif com_score == goal:
        break

if player_score > com_score:
    print(f'Player wins')
else:
    print(f'Computer wins')

print(f'Final score: \n Player: {player_score} and Computer: {goal}')
