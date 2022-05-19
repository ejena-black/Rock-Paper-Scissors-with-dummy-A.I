from random import randint

print('...Rock... \n ...Paper... \n ...Scissors...')


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


if player:
    if player == computer:
        print('It\'s a tie')
    elif player == 'rock':
        if computer == 'paper':
            print('Computer Wins')
        elif computer == 'scissors':
            print('Player Wins')
    elif player == 'paper':
        if computer == 'rock':
            print('Player Wins')
        elif computer == 'scissors':
            print('Computer Wins')
    elif player == 'scissors':
        if computer == 'rock':
            print('Computer Wins')
        elif computer == 'paper':
            print('Player Wins')
else:
    print('You didn\'t make a move')