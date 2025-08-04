# Write code below 💖

hufflepuff = 0
slytherin = 0
gryffindor = 0
ravenclaw = 0

print("""Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk""")

answer = int(input())

if answer == 1:
  gryffindor += 1
  ravenclaw += 1
elif answer == 2:
  slytherin += 1
  hufflepuff += 1
else:
  print('Wrong input.')

print('')
print("""Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold""")

answer = int(input())

if answer == 1:
  hufflepuff += 2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor += 2
else:
  print('Wrong input.')

print('')
print("""Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum""")

answer = int(input())

if answer == 1:
  slytherin += 4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print('Wrong input.')

print('')

if hufflepuff > slytherin and hufflepuff > gryffindor and hufflepuff > ravenclaw:
  print("You belong in Hufflepuff")
elif slytherin > hufflepuff and slytherin > gryffindor and slytherin > ravenclaw:
  print("You belong in Slytherin")
elif gryffindor > slytherin and gryffindor > hufflepuff and gryffindor > ravenclaw:
  print("You belong in Gryffindor")
else:
  print("You belong in Ravenclaw")

print('')

print("Scores:")
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)
print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)