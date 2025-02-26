import time
import threading


class FizzBuzz:
    def __init__(self):
        self.answer = ''
        self.correct_answer = ''
        self.players = []
        self.player_index = 0
        self.scores = {}

    def intro(self):
        print('Welcome to FizzBuzz!')
        print('Rules:')
        print('- Count from 1 to 100.')
        print('- Say "Fizz" if the number is divisible by 3.')
        print('- Say "Buzz" if the number is divisible by 5.')
        print('- Say "FizzBuzz" if divisible by both 3 and 5.')
        print('- Say the number if none of the above apply.')
        print('- Incorrect answers deduct a point.')
        print('- Running out of time also deducts a point.')
        print('- First player to reach 10 points wins.')
        print('- Players with 0 points are eliminated.')

    def start_game(self):
        while True:
            choice = input(
                'Are you ready to play Fizz Buzz? (Type "yes" to start): ').lower()
            if choice == 'yes':
                pvp = PvP()
                pvp.get_players()
                pvp.difficulty_level_setter()
                pvp.player_fizz_buzz()
                return
            else:
                print('Invalid choice, please type "yes".')

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

    def difficulty_level_setter(self):
        while True:
            print('\nSet the difficulty level:')
            print('- "hard" (5 sec)')
            print('- "medium" (7 sec)')
            print('- "easy" (10 sec)')
            user_difficulty = input('Choose difficulty: ').lower()

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
                print('Invalid input, please choose again.')

    def get_players(self):
        while True:
            player_name = input(
                '\nEnter a name (or type "done" to finish, "remove" to delete a name): ').lower()

            if player_name == 'done':
                if len(self.players) >= 2:
                    break
                else:
                    print('You need at least two players to start.')
                    continue

            if player_name == 'remove':
                remove_name = input(
                    'Which name would you like to remove? ').lower()
                if remove_name in self.players:
                    self.players.remove(remove_name)
                    del self.scores[remove_name]
                    print(f"{remove_name} has been removed.")
                else:
                    print('Player not found.')
                continue

            if player_name in self.players:
                print('That name is already taken, pick another.')
                continue

            self.players.append(player_name)
            self.scores[player_name] = 0
            print(f'{player_name} has been added.')

        print(f'\nPlayers: {self.players}')

    def missed_turn(self):
        print(f"\n{self.current_player} ran out of time and loses 1 point!")
        self.scores[self.current_player] = max(
            0, self.scores[self.current_player] - 1)

        if self.scores[self.current_player] == 0:
            print(f"{self.current_player} has been eliminated!")
            self.players.remove(self.current_player)

            if len(self.players) == 1:
                print(
                    f"\n{self.players[0]} is the last player standing! They win!")
                exit()

        self.next_turn()

    def count_down_timer(self, seconds, stop_event):
        for i in range(seconds, 0, -1):
            if stop_event.is_set():
                return
            if i in {3, 1}:
                print(f'\n{self.current_player}, {i} seconds left!')
            time.sleep(1)

        if not stop_event.is_set():
            self.missed_turn()

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
        for i in range(1, 101):
            if len(self.players) == 1:
                print(
                    f"\n{self.players[0]} is the last player standing! They win!")
                return

            self.current_player = self.players[self.player_index]
            self.current_number = i

            print(f'\n{self.current_player}, it\'s your turn! The number is {i}.')

            stop_event = threading.Event()
            timer_thread = threading.Thread(
                target=self.count_down_timer, args=(
                    self.customise_timer, stop_event)
            )
            timer_thread.start()

            try:
                player_answer = input('Your answer: ').lower()
                stop_event.set()
                timer_thread.join()
            except:
                stop_event.set()
                timer_thread.join()
                self.missed_turn()
                continue

            if player_answer == '':
                self.missed_turn()
                continue

            self.check_answer(i)

            if player_answer == self.correct_answer:
                print('\nCorrect!')
                self.scores[self.current_player] += 1

                if self.scores[self.current_player] >= 10:
                    print(f'\n{self.current_player} has won the game!')
                    return
            else:
                print(f'\nWrong! The correct answer was {
                      self.correct_answer}.')
                self.scores[self.current_player] = max(
                    0, self.scores[self.current_player] - 1)

                if self.scores[self.current_player] == 0:
                    print(f"\n{self.current_player} has been eliminated!")
                    self.players.remove(self.current_player)

                    if len(self.players) == 1:
                        print(
                            f"\n{self.players[0]} is the last player standing! They win!")
                        return

            self.next_turn()


if __name__ == '__main__':
    game = FizzBuzz()
    game.intro()
    game.start_game()
