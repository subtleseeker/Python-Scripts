import random

    
def print_word(letter, l, list_letters, guessed_list, moves):
    flag = True
    for i in range(l):
        if list_letters[i] in guessed_list:
            print(list_letters[i].upper() + " ", end="")
        else:
            print("_ ", end="")
            flag = False
    print("     Moves left = " + str(moves))

    print("You have guessed the letters:", end = "")
    for i in guessed_list:
        print(i.upper() + " ", end = "")
    print("\n")
    return flag


def hangman(letter, l, list_letters, guessed_list, moves, game_completed):
    if letter in guessed_list:
        print("Already tried letter " + str(letter) + "\n")
        return (letter, l, list_letters, guessed_list, moves, game_completed)

    guessed_list.append(letter)

    if letter in list_letters:
        print("Yeh, you have guessed the correct letter!")
        game_completed = print_word(letter, l, list_letters, guessed_list, moves)
    else:
        print("Oops, the letter " + letter.upper() + " is not present.")
        moves -= 1
        game_completed = print_word(letter, l, list_letters, guessed_list, moves)
    return (letter, l, list_letters, guessed_list, moves, game_completed)


def check_letter(letter):
    if len(letter) == 1 and 'A' <= letter <= 'z':
        return True
    elif len(letter) == 0:
        print("Error: You need to enter a character.\n")
    elif len(letter) > 1:
        print("Error: You need to enter a single alphabet.\n")
    elif len(letter) == 1:
        print("You need to enter a letter between A to Z.\n")
    else:
        print("Unknown error.\n")
    return False


def main():
    print("Welcome to hangman")
    words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
             "computer", "python", "program", "glasses", "sweatshirt",
             "sweatpants", "mattress", "friends", "clocks", "biology",
             "algebra", "suitcase", "knives", "ninjas", "shampoo"
             ]

    while True:
        game_completed = False
        moves_left = 7
        guessed_list = []

        word = random.choice(words).lower()
        l = len(word)
        list_letters = list(word)
        #print(list_letters)

        print('Guess a ' + str(l) + ' letter word')
        for i in range(l):
            print("_ ",end = "")
        print("     Moves = " + str(moves_left) + '\n')

        while True:
            if moves_left < 1:
                print("Awwww! You are out of moves. You lose...\n")
                break

            letter = input('Guess a letter:')
            if check_letter(letter):
                letter = letter.lower()
                (letter, l, list_letters, guessed_list, moves_left, game_completed) = hangman(letter, l, list_letters, guessed_list, moves_left, game_completed)

            if game_completed:
                print("Woow! You are a genius. You win!\n")
                break

        play_again = input("Do you want to play again?\nPress \'y\' for yes or enter for no:")
        while play_again != 'y' and play_again != "":
            print('Invalid response. Try again:')
            play_again = input()
        if play_again == "":
            break


if __name__ == '__main__':
    main()