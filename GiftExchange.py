# Gift-assigner program
import random
numPeople = int(input("How many people are playing? "))
givers = []
receivers = []
print("Please enter their names: ")
# Get all of the players' names and add them to the list
for i in range(numPeople):
    givers.append(input(""))
# Randomly assign gift givers to gift receivers. Check to make sure that
# nobody is assigned themselves (which is no fun!), and that each person can
# only give one gift and can only receive one gift (no repeats). Keep trying
# (looping) until everyone is giving a gift to someone else.
for j in range(numPeople):
    receivers[j] = random.sample(givers, numPeople)
# Print results
print()
print("Gift Assignments...")
for k in range(numPeople):
    print(givers[k], "will buy a gift for", receivers[k])

print()