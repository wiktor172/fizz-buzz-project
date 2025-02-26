# This is the basic premis of fizzbuzz without the user imput
#fori in range(1, 101): # for loop counts from 1 to 101
#    if i % 3 and i % 5: # if the number is divisible by 3 and 5 the program will print fizzbuzz
#        print('fizzbuzz') 
#    elif i % 3: # if the number is divided by 3 the program will print fizz
#        print('fizz')
#    elif i & 5: # if the number is divided by 5 the program will print fuzz
#        print('fuzz')
#    else: # if the number is not divisible by 3 or 5 the program will print the number
#        print(i)



print('are you ready to play FIZZ BUZZ')
computer_or_player = int(input('do you want to play against another player or a computer, please imput 0 for computer or 1 for another player :'))
player1 = None
player2 = None
game_over = False

if computer_or_player == 0:
    player1 = "Player"
    player2 = "Computer"
elif computer_or_player == 1:
    player1 = str(input('player 1 please imput your name : '))
    player2 = str(input('player 2 please imput your name : '))
else:
    print('invalid input')
    exit()

players = [player1, player2]
print(f'The players are {player1} and {player2}')
current_player_idx = 0
current_player = players[current_player_idx]

for i in range(1, 101):
    print(f'{current_player} its your turn')
    print(f'Number is: {i}')
    answer = input('please enter your answer: ').lower()

    correct_answer = ''
    if i % 3 == 0 and i % 5 == 0:
        correct_answer = 'fizzbuzz'
    elif i % 3 == 0:
        correct_answer = 'fizz'
    elif i % 5 == 0:
        correct_answer = 'buzz'
    else:
        correct_answer = str(i)

    if answer == correct_answer:
        print('correct')
        # Switch to other player
        current_player_idx = (current_player_idx + 1) % 2
        current_player = players[current_player_idx]
    else:
        print('incorrect')
        print(f'The correct answer was: {correct_answer}')
        # Current player lost, so other player wins
        
        current_player = players[current_player_idx]
        print(f'{current_player} has won!')
        break
            


