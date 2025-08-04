# Write code below 💖

tries = 0
guess = 0

while guess != 6 and tries < 3:
  tries += 1
  guess = int(input("Guess the number:  "))

print("You got it!")