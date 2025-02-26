class FizzBuzz():
    
    def __init__(self):
        self.choice = input('Do you want ot play with computer or player? (c for computer): ')
        self.correct_answer = ''

    def intro(self):
        print('welcome to FizzBuzz')
        print('the rules are you have to count up, from 1 to 100')
        print('if the number is divisible by 3 you say fizz')
        print('if the number is divisible by 5 you say buzz')
        print('if the number is divisible by 3 and 5 you say fizzbuzz')
        print('if the number is not divisible by 3 or 5 you say the number')
        print('the first player to get 10 points wins')
        print('good luck!')

    def CheckChoice(self):
        if self.choice == 'c':
            break
        elif self.choice == 'p':
            break



    def checkAnswer(self, checkAnswer):
        if 
        


    def Main_Game(self):
        

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

        return super().Main_Game()



        

class Player(FizzBuzz):
    player_one = None
    player_two = None
    players = [player_one, player_two]
    current_player = 0


    player_index = 0 #This is used to switch between player 1 and player 2
    def __init__(self):
        super().__init__(self, self.choice)
        
        self.player_one = input
        self.player_two =
        self.current_player = 

    
    def playerSwitch(self):
        self.player_index = (player_index + 1) % 2
        self.current_player = players[self.player_index]
        

    

    class Computer(FizzBuzz):
    
    def __init__(self):
        super().__init__(self)
