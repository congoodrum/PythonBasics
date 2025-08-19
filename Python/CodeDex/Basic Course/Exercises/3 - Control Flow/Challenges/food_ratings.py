# Write code below 💖
import random

rating = random.randint(0,50)/10

print(rating)

if rating > 4.5:
  print("Extraordinary")
elif rating > 4:
  print("Excellent")
elif rating > 3:
  print("Good")
elif rating > 2:
  print("fair")
else:
  print("Poor")