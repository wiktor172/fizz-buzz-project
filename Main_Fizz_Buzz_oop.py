import time  # I used time libary as its preinstalled in python
import threading  # I use the threading module as it works on all operating systems and its preinstalled in python


class FizzBuzz:

    def __init__(self):
        self.answer = ''
        self.correct_answer = ''
        self.players = []
        self.player_index = 0
        self.scores = {}

    def intro(self):
        print('-------------------------')
        print('\n1.play game, \n2.rules , \n3.credits')
        print('-------------------------')

        while True:
            choice = input('Pick 1, 2, or 3: ')
            if choice == '1':
                pvp = PvP()
                pvp.get_players()
                pvp.difficulty_level_setter()
                pvp.player_fizz_buzz()
                return
            elif choice == '2':
                self.rules()
            elif choice == '3':
                self.credits()
            else:
                print('Invalid choice, please enter 1, 2, or 3.')

    def rules(self):
        print('welcome to FizzBuzz')
        print('Rules :')
        print('- Count from 1 to 100.')
        print('- You will be presented with a number')
        print('- When prompted to respond only refer to the number shown')
        print('- Say "Fizz" if the number is divisible by 3.')
        print('- Say "Buzz" if the number is divisible by 5.')
        print('- Say "FizzBuzz" if divisible by both 3 and 5.')
        print('- Say the number if none of the above apply.')
        print('- Incorrect answers deduct a point.')
        print('- Running out of time also deducts a point.')
        print('- First player to reach 10 points wins.')
        print('- Players with 0 points are eliminated.')
        print('Good Luck!!!')


    def credits(self):
        print('Game developed by : Wiktor Wardziak :)')


    def start_game(self):
        while True:
            choice = input(
                str('are you ready to play fizz buzz? (say yes if your ready) : ')).lower()
            if choice == 'yes':
                pvp = PvP()
                pvp.get_players()
                pvp.difficulty_level_setter()
                pvp.player_fizz_buzz()
                return
            else:
                print('invalid choice, please type "yes" ')

    def check_answer(self, current_number):
        if current_number % 3 == 0 and current_number % 5 == 0:
            self.correct_answer = 'fizzbuzz'
        elif current_number % 3 == 0:
            self.correct_answer = 'fizz'
        elif current_number % 5 == 0:
            self.correct_answer = 'buzz'
        else:
            self.correct_answer = str(current_number)


class PvP(FizzBuzz):
    def __init__(self):
        super().__init__()
        self.current_number = None
        self.customise_timer = None

    def difficulty_level_setter(self):
        # simple way of setting the timer to higher or Lower
        while True:
            print('\nSet the difficulty level:')
            print('- "hard" (5 sec)')
            print('- "medium" (7 sec)')
            print('- "easy" (10 sec)')
            user_difficulty = input('Choose difficulty: ').lower()
            # Sets the self.customise_timer to the corresponding attibute
            if user_difficulty == 'hard':
                self.customise_timer = 5
                break
            elif user_difficulty == 'medium':
                self.customise_timer = 7
                break
            elif user_difficulty == 'easy':
                self.customise_timer = 10
                break
            else:
                print('Invalid input, please enter a valid input')

    def get_players(self):
        while True:
            player_name = input(
                '\nPlease enter your name or type "done" to finish or "remove" if you want to remove a name: ')

            if player_name.lower() == 'done':
                if len(self.players) >= 2:
                    break  # This sets the lowest amount of players 2
                else:
                    print('\nyou need at least two players to start')
                    continue
            # prompt to remove a player
            if player_name.lower() == 'remove':
                remove_name = input('which name would you like to remove? : ')
                # checks if name is in list to prevent error
                if remove_name in self.players:
                    self.players.remove(remove_name)
                else:
                    print('The player you would like to remove is not in the list')
                    break

            elif player_name.lower() in self.players:  # Checks if player is in list
                print('This name has all ready been taken \nPick another name')

            elif player_name.lower() not in ['done', 'remove']:
                self.players.append(player_name)
                self.scores[player_name] = 0
                print(f'{player_name} has been added')

            print(f'\nCurrent Players , {self.players}')

    def missed_turn(self):
        print(f"\n{self.current_player} loses 1 point for not answering in time.")
        self.scores[self.current_player] = max(0, self.scores[self.current_player] - 1)
        print(self.scores)
        print('click ENTER to continue')

        if self.scores[self.current_player] == 0:
            print(f"\n{self.current_player} has been eliminated!")
            self.players.remove(self.current_player)

        # Check if there are still players left
        if len(self.players) == 0:
            print("No players left in the game.")
            exit()  # Exit if there are no players

        if len(self.players) == 1:  # If only one player is left, they win
            print(f"\n{self.players[0]} is the last player standing! They win!")
            exit()

        self.next_turn()  # Move to the next player

    def count_down_timer(self, seconds, stop_event):
        for i in range(seconds, 0, -1):
            if stop_event.is_set():
                return  # Exit if the player has answered
            if i in {3, 1}:  # this reduces the ammount of if loops down to 1
                print(f'\n you have {i} seconds left')
                print(f"what is your answer {self.current_player}: ")
            time.sleep(1)

        # If the timer runs out and the player hasn't answered
        if not stop_event.is_set():
            print(f"\nTime's up! {self.current_player} loses their turn.")
            self.missed_turn()  # Call missed_turn if the player didn't answer

    def next_turn(self):
        # changes the player index so the players can switch turns between one and other
        if len(self.players) == 0:
            print("No players left in the game.")
            exit()  # Exit if there are no players

        self.player_index = (self.player_index + 1) % len(self.players)  # Wrap around using modulo

    def player_fizz_buzz(self):
        for i in range(1, 101):
            if len(self.players) == 0:
                print("No players left in the game.")
                exit()

            self.current_player = self.players[self.player_index] # also current player is a local variable
            # as it doesnt need to be stored anyware
            self.current_number = i 

            print(f'\nNext Player: {self.current_player} ')
            print(f'The number is {i}. What is your answer?')

            stop_event = threading.Event() # this is used to stop the timer but is still laggy
            timer_thread = threading.Thread(target=self.count_down_timer, args=(self.customise_timer, stop_event))
            # this is used to start the timer
            timer_thread.start() # this is used to start the timer

            player_answer = input('Please enter your answer: ').lower() # i like this becuase it sets it to lower case
            stop_event.set()  # Stop the timer once the player answers.
            timer_thread.join()  # Wait for the timer to finish

            if player_answer == '': # this is used to check if the player has answered
                print(f'{self.current_player} loses 1 point for not answering.')
                self.scores[self.current_player] = max(0, self.scores[self.current_player] - 1)
                print(self.scores) 

                if self.scores[self.current_player] == 0: # this is used to check if the player has 0 points
                    print(f"\n{self.current_player} has been eliminated!")
                    self.players.remove(self.current_player)
                    if len(self.players) == 1: # this is used to check if there is only one player left
                        print(f"\n{self.players[0]} is the last player standing! They win!")
                        exit()
                continue

            self.check_answer(i)

            if player_answer == self.correct_answer: # this is used to check if the player has answered correctly
                print('\nCorrect!!!')
                self.scores[self.current_player] += 1 # this is used to add 1 point to the player's score if thr player is correct
                print(self.scores)

                if self.scores[self.current_player] >= 10: # playuer wins if thry have 10 points
                    print(f'\n{self.current_player} has won the game!!!')
                    return

            elif player_answer != self.correct_answer:
                print(f'\nWrong, the correct answer is {self.correct_answer}!')
                if self.scores[self.current_player] > 0: # check to prevent negative points
                    self.scores[self.current_player] -= 1
                    print(f'\n{self.scores}')

                if self.scores[self.current_player] <= 0: # player looses if they have 0 points
                    print(f'\n{self.current_player} has run out of points and is removed from the game!')
                    self.players.remove(self.current_player)

                    if len(self.players) == 1: # if there is only one player left they win
                        print(f'\n{self.players[0]} is the last player standing!!!')
                        exit()
                continue

            self.next_turn()


if __name__ == '__main__':
    game = FizzBuzz()
    game.intro()
    game.start_game()
