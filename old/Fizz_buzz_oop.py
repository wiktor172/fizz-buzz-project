class FizzBuzz:
    def __init__(self, start, end):
        self.players = []
        self.game_over = False 
        self.currentNumber = start
        self.end = end
        self.currentPlayer = 0 

    def intro(self):
        print('welcome to FizzBuzz')
        print('the rules are you have to count up, from 1 to 100')
        print('if the number is divisible by 3 you say fizz')
        print('if the number is divisible by 5 you say buzz')
        print('if the number is divisible by 3 and 5 you say fizzbuzz')
        print('if the number is not divisible by 3 or 5 you say the number')
        print('the first player to get 10 points wins')
        print('good luck!')

    def check_answer(self, answer):
        correct_answer = self.fizzBuzzAnswer(self.currentNumber)
        return answer.lower() == correct_answer.lower()

    def add_player(self, player):
        self.players.append(player)

    def fizzBuzzAnswer(self, number):
        if number % 3 == 0 and number % 5 == 0:
            return "fizzbuzz"
        elif number % 3 == 0:
            return "fizz"
        elif number % 5 == 0:
            return "buzz"
        else:
            return str(number)

    def play_turn(self):
        if not self.players:
            print("No players added to the game!")
            return

        current_player = self.players[self.currentPlayer]
        print(f"\n{current_player.name}'s turn. Number is: {self.currentNumber}")
        
        player_answer = input("Your answer: ")
        if self.check_answer(player_answer):
            print("Correct!")
            current_player.score += 1
            if current_player.score >= 10:
                self.game_over = True
                print(f"\n🎉 {current_player.name} wins! 🎉")
        else:
            print(f"Wrong! The correct answer was: {self.fizzBuzzAnswer(self.currentNumber)}")

        self.currentNumber += 1
        self.currentPlayer = (self.currentPlayer + 1) % len(self.players)

        if self.currentNumber > self.end:
            self.game_over = True
            print("\nGame Over! Reached the end number.")

    def play_game(self):
        self.intro()
        while not self.game_over:
            self.play_turn()
        
        # Show final scores
        print("\nFinal Scores:")
        for player in self.players:
            print(f"{player.name}: {player.score} points")


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def get_answer(self, number):
        # Computer always gives correct answer
        return self.fizzBuzzAnswer(number)


    
        
