import random

playerChoice = 0
playerWins = 0
botWins = 0

print("""
      =====================
      Rock, Paper, Scissors
      =====================
      Welcome to Rock, Paper, Scissors! 

      In this game you have to choose either Rock, Paper, or Scissors.
      Your opponent will also chose one of the options.
      To win the game, you must get to 3 wins before your opponent.

      Good luck! 
      """)

while playerWins < 3 and botWins < 3:

    playerChoice = int(input("""
      1) Rock
      2) Paper
      3) Scissors
      Pick a number: """))
    
    botChoice = random.randint(1,3)

    if playerChoice == 1:
        print("You chose Rock")
    elif playerChoice == 2:
        print("You chose Paper")
    elif playerChoice == 3:
        print("You chose Scissors")
    else:
        print("You chose an invalid option, opponent wins")

    if botChoice == 1:
        print("Opponent chose Rock")
    elif botChoice == 2:
        print("Opponent chose Paper")
    elif botChoice == 3:
        print("Opponent chose Scissors")

    if playerChoice == botChoice:
        print("It's a tie")
    elif playerChoice == 1 and botChoice == 2 or playerChoice == 2 and botChoice == 3 or playerChoice == 3 and botChoice == 1:
        print("You win! :)")
        playerWins += 1
    else:
        print("You lose! :(")
        botWins += 1
    
    print(f"""
    Current scores: 
    player: {playerWins}
    opponent: {botWins}
    """)

if playerWins > botWins:
    print("Congratulations, you win!")
else:
    print("You lose :(")