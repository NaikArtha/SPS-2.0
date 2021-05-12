import numpy as np, getpass, os

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
    Codes[countPlayer, countCode] = getpass.getpass("Stone: ")
    os.system('cls')
    countCode += 1
    print("Player", i, "enter the code for the following:")
    Codes[countPlayer, countCode] = getpass.getpass("Paper: ")
    countCode += 1
    os.system('cls')
    print("Player", i, "enter the code for the following:")
    Codes[countPlayer, countCode] = getpass.getpass("Scissors: ")
    countPlayer += 1
    os.system('cls')
    print("")
    print("")

for count in Codes:
    for i in count:
        print(i, end=" ")
    print(" \n ")
    

