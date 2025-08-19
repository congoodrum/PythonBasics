# Write code below 💖
import random

def play():
    symbols = ['🍒','🍇', '🍉', '7️⃣']

    results = random.choices(symbols, k=3)

    print(f'{results[0]} | {results[1]} | {results[2]}')

    if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
        print('Jackpot! 💰')
    else:
        print('Thanks for playing!')


def main():
    print('Welcome to the slot machine!')
    playerInput = input('Do you want to play? (Y/N): ')

    while playerInput != 'N':
        if playerInput == 'Y':
            play()
            playerInput = input('Do you want to play again? (Y/N): ')
        else:
            playerInput = input('Invalid input. Do you want to  play? (Y/N): ')
    
    print('Thank you for playing :)')

main()