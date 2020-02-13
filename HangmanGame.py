from random_word import RandomWords

# Hangman game!
# Assume the answer is "hangman"

# read the input file

with open("words.txt") as f:
    words = f.read().split(" ")

# get the length of words available for the game
length = len(words)

# let the user choose the word they want to try guess from the list of words
print("Pick a number between 1 to", length, ": ")
choice = int(input())

if 0 < choice < length:
    A = list(words[choice - 1])

# importing words from python package random-words
w = RandomWords()

# get any random word from the dictionary
word = w.get_random_word()

# create a list out of the selected random word
A = list(word)

L = []
for char in A:
    L.append('-')

play = True
count = 0

while play == True:
    # Ask the user to guess a letter
    letter = str(input("Guess a letter: "))
    letter = letter.lower()
    # Check to see if that letter is in the Answer
    i = 0
    if letter in A:
        for currentletter in A:
            # If the letter the user guessed is found in the answer,
            # set the underscore in the user's answer to that letter

            if letter == currentletter:
                L[i] = letter
            i = i + 1
        # Display what the player has thus far (L) with a space
        # separating each letter
        print(' '.join(str(n) for n in L))
    else:
        print("BAD GUESS!")
        count += 1
        print("Wrong turn number: ", count)
        if count == 6:
            play = False
            print("Game Over!")
            print("The correct answer is: ", A)
    # Test to see if the word has been successfully completed,
    # and if so, end the loop
    if A == L:
        play = False
        print("GREAT JOB!")
