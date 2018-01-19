from itertools import permutations

f = open("words.txt")
dict = f.readlines()
dict = [i.strip() for i in dict]
playAgain = True

while playAgain:
    playAgain = False
    print("Welcome to SCRABBLE")
    # l = int(input("Enter the number of letters you have:"))
    # add exception
    # letters = []
    values = {}

    print("Enter the letters:")
    # x = input() #input each letter if written in a line
    # letters.extend(x.split().lower())
    letters = [x for x in input().lower().split()]

    boolValue = input("Do you want to assign values to each letter(y/n):")
    if boolValue == 'y':
        for i in set(letters):
            values[i] = input(i+":")
    else:
        for i in set(letters):
            values[i] = 1

    # print(values)