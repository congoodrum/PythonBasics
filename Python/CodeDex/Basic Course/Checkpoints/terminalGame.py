#  THIS NEEDS FINISHING TO BE BETTER

import random

enemyHealth = 10
playerHealth = 10


print("""Welcome to the terminal combat simulator!
      You arwe about to face off against an enemy where every action you make counts...
      Choose carefully, or you'll loose!
      
      Good luck, edventurer :)
      
      
      """)

while enemyHealth > 0 or playerHealth > 0:
    print(f"Player HP: {playerHealth}")
    print(f"Enemy HP: {enemyHealth}")
    playerAction = int(input("""Choose your action:
                             1) attack
                             2) defend
                             3) heal 1HP
"""))
    
    enemyAction = random.randint(1, 3)
    print(f"Enemy action: {enemyAction}")

    if playerAction == 1 and enemyAction != 2:
        enemyHealth -= 2
        print("You attack your enemy head on dealing 2 damage")
    elif playerAction == 1 and enemyAction == 2:
        print("You attack the enemy head on, but they deflect your blow") 
    elif playerAction == 2 and enemyAction == 1:
        print("You raise your guard as the enemy attacks you. You take 0 damage")
    elif playerAction == 2 and enemyAction != 1:
        print("You raise your guard, but the enemy does not attack")
    elif playerAction == 3 and enemyAction != 1:
        print("You take time to quickly heal some of your injuries. You regain 1HP.")
        playerHealth += 1
    elif playerAction == 3 and enemyAction == 1:
        print("You take time to quickly heal your wounds, but the enemy takes advantage of this and attacks you. You take 1 damage.")
        playerHealth -= 1
    

