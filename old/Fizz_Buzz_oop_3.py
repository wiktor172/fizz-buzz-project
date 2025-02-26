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
        print('welcome to FizzBuzz')
        print('the rules are you have to count up, from 1 to 100')
        print('if the number is divisible by 3 you say fizz')
        print('if the number is divisible by 5 you say buzz')
        print('if the number is divisible by 3 and 5 you say fizzbuzz')
        print('if the number is not divisible by 3 or 5 you say the number')
        print('if you get the wrong answer your point will be deducted')
        print('if you run out of time your points will be deducted')
        print('the first player to get 10 points wins')
        print('if the player gets below 10 points they get removed from the game')
        print('good luck!')

    def start_game(self):
        while True:
            choice = input(
                str('are you ready to play fizz buzz? (say yes if your ready) : ')).lower()
            if choice == 'yes':
                pvp = PvP()
                pvp.get_players()
                pvp.difficulty_level_seter()
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
        self.current_player = None
        self.customise_timer = None

    def difficulty_level_seter(self):
        # simple way of setting the timer to higher or Lower
        while True:
            self.customise_timer = 7
            print('\nhow hard do you want the game to be ?')
            print('the diffilculty level sets the countdown timer higher or lower')
            print('for the game difficulty to be set to hard type "hard"')
            print('for the game difficulty to be set to medium type "medium"')
            print('for the game difficulty to be set to easy type "easy"')
            user_difficulty = input('Type your perfered difficulty:').lower()
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
                print('please enter a valid input')
                continue

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

            if player_name.lower() == 'remove':
                remove_name = input('which name would you like to remove? : ')
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
        def handle_missed_turn(self):
            print(
                f"\n{self.current_player} loses 1 point for not answering in time.")
            self.scores[self.current_player] = max(
                0, self.scores[self.current_player] - 1)

        if self.scores[self.current_player] == 0:
            print(f"\n{self.current_player} has been eliminated!")
            self.players.remove(self.current_player)

        if len(self.players) == 1:  # If only one player is left, they win
            print(
                f"\n{self.players[0]} is the last player standing! They win!")
            exit()

        self.next_turn()  # Move to the next player

    def count_down_timer(self, seconds, stop_event):
        #  countdown timer stops when the player answers
        for i in range(seconds, 0, -1):
            if stop_event.is_set():
                return
            if i in {3, 1}:  # this reduces the ammount of if loops down to 1
                print(f'\n you have {i} seconds left')
                print(f"your current number is {self.current_number}")
                print(f"what is your answer {self.current_player}: ")
            time.sleep(1)

        # removes points to the player wich took to long
        if not stop_event.is_set():
            print(f'{self.current_player} ran out of time !!!')
            self.scores[self.current_player] = max(
                0, self.scores[self.current_player] - 1)
            print(f'{self.scores}')
            self.missed_turn()

            # removes the player if the scoere is 0
            if self.scores[self.current_player] == 0:
                print(f"{self.current_player} has been eliminated")
                self.players.remove(self.current_player)

            self.next_turn()  # skips to the next player

        print('time is up')

    def next_turn(self):
        if len(self.players) == 1:
            print(
                f"\n{self.players[0]} is the last player standing! They win!")
            exit()

        self.player_index += 1
        if self.player_index >= len(self.players):
            self.player_index = 0

        print(f"\nNext player: {self.players[self.player_index]}")

    def player_fizz_buzz(self):
        # handles the main game loop
        for i in range(1, 101):
            self.current_player = self.players[self.player_index]
            # also current player is a local variable
            # as it doesnt need to be stored anyware

            self.current_number = i

            print(f'\nhey {self.current_player} its your turn : ')
            print(f'The number is {i}')

            stop_event = threading.Event()

            timer_thread = threading.Thread(
                target=self.count_down_timer, args=(
                    self.customise_timer, stop_event)
            )
            timer_thread.start()

            player_answer = input(str('Please enter your answer : ')).lower()
            stop_event.set()  # stop the timer once the player answers.
            timer_thread.join()  # wait for the timer to finish

            if player_answer == '':
                continue

            self.check_answer(i)

            if player_answer == self.correct_answer:  # Checks for the correct answer
                print('\ncorrect !!!')
                # If player is correct 1 gets added to score
                self.scores[self.current_player] += 1
                print(self.scores)

                # if player gets 10 points they win
                if self.scores[self.current_player] >= 10:
                    print(f'\n{self.current_player} has won the game !!!')
                    return

            elif player_answer != self.correct_answer:  # checks for the incorrect answer
                print(f'\nWrong, the correct answer is {
                      self.correct_answer} ! ')
                # checks if the current player has a score above 0
                if self.scores[self.current_player] > 0:
                    # if player has score above 0 1 gets removed from the player score
                    self.scores[self.current_player] -= 1
                    print(f'\n{self.scores}')

                # ckecks if player has a score below or equal to 0
                elif self.scores[self.current_player] <= 0:
                    print(
                        f'\n{self.current_player} has ran out of points he is removed from the game !!')
                    # If so player gets removed form the game
                    self.players.remove(self.current_player)

                    # checks if there is only one player in the game, player would win
                    if len(self.players) == 1:
                        print(
                            f'\n{self.players[0]} is the last man standing!!!')
                        return
                continue

                self.next_turn()


if __name__ == '__main__':
    game = FizzBuzz()
    game.intro()
    game.start_game()
