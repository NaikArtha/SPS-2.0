import numpy as np

print("----------------------Welcome To SPS-2.0----------------------")
print("To continue please fill up the following details.")

while True:
    number_of_players = input("Enter the number of players: ")  # Number of players who will play the game
    try:
        number_of_players = int(number_of_players)
    except Exception as e:
        print("Note: Input must be a number.")
    if type(number_of_players) == type(1):
        break
print("")
print("")
Codes = np.empty((number_of_players, 3), int)
countPlayer = 0
for i in range(1, number_of_players + 1):
    countCode = 0
    print("Player", i, "enter the code for the following:")
    Codes[countPlayer, countCode] = input("Stone: ")

    countCode += 1

    Codes[countPlayer, countCode] = input("Paper:")
    countCode += 1

    Codes[countPlayer, countCode] = input("Scissors: ")
    countPlayer += 1

    print("")
    print("")

InputCode = np.empty(number_of_players, int)

for i in range(number_of_players):
    print("Player", i + 1, ": Enter your choice in terms of code")
    InputCode[i] = input()

sps = np.empty(number_of_players, int)
for i in range(number_of_players):
    if InputCode[i] == Codes[i][0]:
        sps[i] = 1  # Stone

    elif InputCode[i] == Codes[i][1]:
        sps[i] = 2  # Paper

    elif InputCode[i] == Codes[i][2]:
        sps[i] = 3  # Scissors

score = np.empty(number_of_players, int)

for i in range(number_of_players):
    for j in range(number_of_players):
        if j != i:
            if sps[i] == sps[j]:
                score[i] = 0
            elif sps[i] == 1 and sps[j] == 2:
                score[i] = 0
            elif sps[i] == 1 and sps[j] == 3:
                score[i] = 1
            elif sps[i] == 2 and sps[j] == 3:
                score[i] = 0
print("\n\n")

for i in range(number_of_players):
    if score[i] != 0:
        print("Player", i+1, "WINS!!!")

doesntWin = 0

for i in range(number_of_players):
    if score[i] == 0:
        doesntWin+=1

if doesntWin == number_of_players:
    print("OOPS!! NO ONE WON")

print("\n\nGame ends!")
