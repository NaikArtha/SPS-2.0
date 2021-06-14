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
   
    countCode += 1
    print("Player", i, "enter the code for the following:")
    Codes[countPlayer, countCode] = getpass.getpass("Paper: ")
    countCode += 1
    
    print("Player", i, "enter the code for the following:")
    Codes[countPlayer, countCode] = getpass.getpass("Scissors: ")
    countPlayer += 1
    
    print("")
    print("")

    
player1 = {
  Codes[0][0] : 'Stone',
  Codes[0][1] : 'Paper',
  Codes[0][2] : 'Scissor',
}
player2 = {
  Codes[1][0] : 'Stone',
  Codes[1][1] : 'Paper',
  Codes[1][2] : 'Scissor',
}


#print(player1[player1Code])
#print(player2[player2Code])



RESULTS = {
    ("Stone", "Scissor"): "Stone beats scissors, Player 1 wins! ",
    ("Paper", "Stone"): "Paper beats stone, tough luck! Player 1 wins! ",
    ("Scissor", "Paper"): "Scissors me timbers! Scissors cuts paper! Player 1 wins",
    ("Scissor", "Stone"): "Stone beats scissors,  Player 2 wins!",
    ("Stone","Paper"): "Paper beats stone, Player 2 wins!",
    ("Paper", "Scissor"): "Scissors me timbers! Scissors cuts paper! Player 2 wins"
}

def game_play(input1, input2):
  
  print(RESULTS.get((input1, input2), "It's a draw!"))


while True:
  player1Code = int(input("Enter your code: "))
  player2Code = int(input("Enter your code: "))
  game_play(player1[player1Code], player2[player2Code])
  if input("Do you want to quit? Else press Enter to continue").lower() in {"y", "yes"}:
    break