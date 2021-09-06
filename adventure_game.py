import time
import random


def print_pause(print_this, delay=2):
    # I have used this expresion 'flush=True' because in my Git Bash
    # the delay between the print strings was not displaying, so I
    # see in the Udacity questions that someone had the same problem
    # and for making the delay work in the Git Bash you have to add
    # this expresion. But I would like to know why when I add this
    # 'flush=True' the delay works.
    print(print_this, flush=True)
    time.sleep(delay)


def text_color(message, color, background=False):
    soc = '\33[48;5;' if background else '\33[38;5;'
    eoc = '\033[0m'
    return f"{soc}{color}m{message}{eoc}"


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
    return response


def intro(enemy):
    color = 10
    fg_color = text_color('Welcome to the Ultimate Adventure Game', color)
    print_pause(f'{fg_color}')
    name = input("For starting. Insert your nickname:\n")
    print_pause("\nSome strange things have been"
                " happening in the village of a lonely island.")
    print_pause(f"And you {name} have been chosen to find the"
                " cause of these misteries.")
    print_pause("After some search you found that the responsable"
                f" of this is a {enemy}.")
    print_pause(f"{name} concluded that the {enemy} is hiding in the "
                "ruins of a graveyard or in a hovel near the village.", 3)
    print_pause("In front of you is the hovel.")
    print_pause("To your right is the old graveyard.")
    print_pause("But you have a problem, your only weapon at the"
                " moment is a small dull knife.", 3)


def village(enemy, weapon, damage, items):
    print_pause("\nEnter 1 to peer into the graveyard ruins.")
    print_pause("Enter 2 to knock on the door of the hovel.")
    print_pause("What would you like to do?", 1)
    choice = valid_input("(Please enter 1 or 2).\n", "1", "2")
    if choice == '1':
        print_pause("You peer cautiously into the ruins.", 1)
        print_pause("There is too much dust and you can hardly see.")
        print_pause(f"Suddenly, behind some small walls, the {enemy} appears.")
        print_pause(f"The {enemy} attacks you.")
        if weapon in items:
            print_pause(f"With these new {weapon} you can give"
                        f" battle to the {enemy}.")
        else:
            print_pause("Oh no!! You are in trouble, your weapon might be not"
                        f" enough for finishing with the {enemy}.", 3)
        fight(enemy, weapon, damage, items)
    elif choice == '2':
        if weapon in items:
            print_pause("You have already been here.")
            print_pause("There doesn't seem to be anything else to do here.")
        else:
            print_pause("You knock the door of the hovel.")
            print_pause("There doesn't seem to be anyone in the hovel.")
            print_pause("You enter carfully to the hovel")
            print_pause("Behind a dusty sofa there is something shyning.")
            print_pause(f"Oh this is the {weapon}.")
            print_pause(f"With this {weapon} you can surely"
                        f" deafet the {enemy}.")
            items.append(weapon)
        village(enemy, weapon, damage, items)


def fight(enemy, weapon, damage, items):
    quarrel = valid_input("Would you like to (1)fight"
                          " or (2)run away? ", "1", "2")
    if quarrel == '1':
        print_pause(f"You counter-attack the {enemy}.")
        if weapon in items:
            print_pause(f"With the counter-attack you made {damage}"
                        " points of damage.")
            print_pause(f"You do a second attack with the {weapon},"
                        " this one made " + str(100 - damage) +
                        " points of damage.", 4)
            print_pause("With these two attacks you made 100"
                        " points of damage.")
            print_pause(f"This was the total health points of the {enemy}.")
            print_pause(f"The damage you made with the {weapon} was enough"
                        f" for defeating the {enemy}.", 3)
            print_pause(f"Good Game.")
            print_pause("GG WP :)")
        # The 'elif' that is coming is giving the chance of wining with
        # out having the weapon. This is an small chance but I think
        # is a cool way of making the game more fun.
        elif random.randint(1, 100) <= 15:
            print_pause(f"You attack the {enemy} with the dull knife")
            print_pause("Ohh! You are lucky you connected a critical"
                        f" hit to the {enemy}.")
            print_pause(f"You defeated the {enemy} with this hit.")
            print_pause("Who would have said that it was"
                        f" possible to defeat the {enemy} with"
                        " that dull knife?", 4)
            print_pause(f"Good Game.")
            print_pause("GG WP :)")
        else:
            print_pause("You try to attack with the dull knife.")
            print_pause("With the counter-attack you made "
                        + str(random.randint(2, 22)) + " points of damage.", 4)
            print_pause(f"But it is not effective enough to end"
                        f" with the {enemy}.")
            print_pause("Nice try. Your weapon was not enough to"
                        " finish victorious.")
            print_pause("Try it again another time.")
            print_pause("GAME OVER!!")
    elif quarrel == '2':
        print_pause(f"After a long run the {enemy} got tired of"
                    " following you.")
        print_pause("Now you are back in the village.")
        village(enemy, weapon, damage, items)


def play_game():
    enemies = ["thief", "big dragon", "mad Shrek", "troll", "pirate"]
    weapons = ["legendary sword", "magic stick", "rusty knife"]

    enemy = random.choice(enemies)
    weapon = random.choice(weapons)
    damage = random.randint(60, 99)
    items = []

    intro(enemy)
    village(enemy, weapon, damage, items)


def play_again():
    choice = valid_input("\nWould you like to play again? (y/n) ", "y", "n")
    if choice == 'n':
        print('Thanks for playing! Goodbye!')
        exit(0)


def game():
    # Infinite loop.
    while True:
        # All logic to play.
        play_game()

        # The stop condition.
        play_again()


if __name__ == '__main__':
    game()
