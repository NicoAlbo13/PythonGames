#import time

#print("Hello! I am Bob, the Breakfast Bot.")
#time.sleep(2)
#print("Today we have two breakfasts available.")
#time.sleep(2)
#print("The first is waffles with strawberries and whipped cream.")
#time.sleep(2)
#print("The second is sweet potato pancakes with butter and syrup.")
#time.sleep(2)

#while True:
#    while True:
#        response = input("Please place your order. "
#                         "Would you like waffles or pancakes?\n").lower()
#        if "waffles" in response:
#            print("Waffles it is!")
#            time.sleep(2)
#            break
#        elif "pancakes" in response:
#            print("Pancakes it is!")
#            time.sleep(2)
#            break
#        else:
#            print("Sorry, I don't understand.")
#            time.sleep(2)
#    print("Your order will be ready shortly.")
#    time.sleep(2)
#    while True:
#        order_again = input("Would you like to place another order? "
#                            "Please say 'yes' or 'no'.\n").lower()
#        if 'no' in order_again:
#            print("OK, goodbye!")
#            time.sleep(2)
#            break
#        elif 'yes' in order_again:
#            print("Very good, I'm happy to take another order.")
#            time.sleep(2)
#            break
#        else:
#            print("Sorry, I don't understand.")
#            time.sleep(2)
#    if 'no' in order_again: 
#        break


# Now we have the same code but this is easy to read
import time

def print_pause(message_to_print):
    print(message_to_print, flush=True)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def get_order():
    response = valid_input("Please place your order. "
                           "Would you like waffles or pancakes?\n",
                           "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")
    order_again()


def order_again():
    response = valid_input("Would you like to place another order? "
                              "Please say 'yes' or 'no'.\n",
                              "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
    elif "yes" in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()


def order_breakfast():
    intro()
    get_order()


if __name__ == '__main__':
    order_breakfast()
