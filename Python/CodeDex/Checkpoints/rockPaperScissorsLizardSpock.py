import random

playerChoice = 0
playerWins = 0
botWins = 0

print("""
      ====================================
      Rock, Paper, Scissors, Lizard, Spock
      ====================================
      Welcome to Rock, Paper, Scissors, Lizard, Spock! 

      In this game you have to choose either Rock, Paper, Scissors, Lizard or Spock.
      Your opponent will also chose one of the options.

      Remember:
        - Scissors cut Paper.
        - Paper covers Rock.
        - Rock crushes Lizard.
        - Lizard poisons Spock.
        - Spock smashes Scissors.
        - Scissors beat Lizard.
        - Lizard eats Paper.
        - Paper disproves Spock.
        - Spock vaporizes Rock.
        - Rock breaks Scissors.

      To win the game, you must get to 3 wins before your opponent.

      Good luck! 
      """)

while playerWins < 3 and botWins < 3:

    playerChoice = int(input("""
      1) Rock
      2) Paper
      3) Scissors
      4) Lizard
      5) Spock
      Pick a number: """))
    
    botChoice = random.randint(1,5)

    if playerChoice == 1:
        print("You chose Rock")
    elif playerChoice == 2:
        print("You chose Paper")
    elif playerChoice == 3:
        print("You chose Scissors")
    elif playerChoice == 4:
        print("You chose Lizard")
    elif playerChoice == 5:
        print("You chose Spock")
    else:
        print("You chose an invalid option, opponent wins")

    if botChoice == 1:
        print("Opponent chose Rock")
    elif botChoice == 2:
        print("Opponent chose Paper")
    elif botChoice == 3:
        print("Opponent chose Scissors")
    elif botChoice == 4:
        print("Opponent chose Lizard")
    elif botChoice == 5:
        print("Opponent chose Spock")
    else:
        print("You chose an invalid option, opponent wins")


    if playerChoice == botChoice:
        print("It's a tie")
    elif (playerChoice == 3 and botChoice == 2
          or playerChoice == 2 and botChoice == 1
          or playerChoice == 1 and botChoice == 4
          or playerChoice == 4 and botChoice == 5
          or playerChoice == 5 and botChoice == 3
          or playerChoice == 3 and botChoice == 4
          or playerChoice == 4 and botChoice == 2
          or playerChoice == 2 and botChoice == 5
          or playerChoice == 5 and botChoice == 1
          or playerChoice == 1 and botChoice == 3
          ):
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