import numbers

def ask():
    print("Welcome to Python Pharmacy")

    while True:
        print("[P] - Perfumery\n[F] - Pharmacy\n[C] - Cosmetics")
        try:
            my_section = input("Choose your section: ").upper()
            ["P", "F", "C"].index(my_section)
        except ValueError:
            print("That is not a valid option")
        else:
            break

    numbers.decorator(my_section)


def start():
    while True:
        ask()
        try:
            another_turn = input("Would you like to take another turn? [Y] [N]: ").upper()
            ["Y", "N"].index(another_turn)
        except ValueError:
            print("That is not a valid option")
        else:
            if another_turn == "N":
                print("Thank you for your visit")
                break

start()
