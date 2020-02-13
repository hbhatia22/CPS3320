score = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
    'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1,
    'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
word = input("Enter you word: ")
# def letterScore(word, total=0):
#   for i in word:
#       i = i.lower()
#       total += score[i]
#   return total


def letterScore(i):
    if i in 'aeilnorstuv':
        return 1
    elif i in 'dg':
        return 2
    elif i in 'bcmp':
        return 3
    elif i in 'fhwy':
        return 4
    elif i in 'k':
        return 5
    elif i in 'jx':
        return 8
    elif i in 'qz':
        return 10
    else:
        return 0


def wordScore(letter):
    total = 0
    for i in letter:
        i = i.lower()
        num = letterScore(i)
        total += num
    return total


totalScore = wordScore(word)

print("word score: ", totalScore)
