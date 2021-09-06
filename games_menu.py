import time
import Elevator_game
import adventure_game
import order_breakfast_bot
import rps

def print_pause(print_this, delay=1):
    print(print_this, flush=True)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in  options:
            break
    return response


def menu_games():
    print_pause("\nWelcome to the Games Menu")
    print_pause("Select the game:")
    print_pause("1. Breakfast B0t.")
    print_pause("2. Elevator Game.")
    print_pause("3. Adventure Game.")
    print_pause("4. Rock, Paper, Scissors.")
    game = valid_input("\nWhat game do you want to play?\n", ["1", "2", "3", "4"])
    if game == '1':
        print_pause("You selected the Breakfast B0t.")
        order_breakfast_bot.order_breakfast()
    elif game == '2':
        print_pause("You selected the Elevator Game.")
        Elevator_game.play_game()
    elif game == '3':
        adventure_game.game()
    elif game == '4':
        game = rps.Game(rps.HumanPlayer(), rps.main_player)
        game.play_game()


def play_again():
    choice = valid_input("\nWould you like to play another game? (y/n) ", ["y", "n"])
    if choice == 'n':
        print('Thanks for playing! Goodbye!')
        exit(0)


def menu():
    while True:
        menu_games()
        
        play_again()


if __name__ == '__main__':
    menu()
    