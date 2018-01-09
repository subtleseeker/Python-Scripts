import random


def roll_dice(l, r):
    for i in range(10):
        print(random.randint(l, r))


def main():
    print("This is a Dice Rolling Simulator\n")

    while True:
        choice = input("If you want a custom dice, enter \"y\"\nPress enter for a normal die(1-6):")

        if choice == "":
            left = 1
            right = 6
            break

        elif choice == 'y' or choice == 'Y':
            while True:
                left = int(input("Enter minimum number:"))
                right = int(input("Enter maximum number:"))

                if left > right:
                    print("\nERROR:The minimum number cannot be greater than the maximum number.\n")
                    continue
                else:
                    break
            break

        else:
            print("This is not recognized. ")

    roll_dice(left, right)


if __name__ == "__main__":
    main()
