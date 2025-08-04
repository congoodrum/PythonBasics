# Write code below 💖
import random

enteredWord = input("Please enter a word or phrase: ")
print(len(enteredWord))

print("Now let's make an array of random numbers between 0-100 and find the highest and lowest values")
numbersToGenerate = input("How many numbers should we create?: ")

numbersArray = []
count = 0

while count < int(numbersToGenerate):
  numbersArray.append(random.randint(0, 100))
  count += 1

print('The created array is: ', numbersArray)
print('The lowest value is: ', min(numbersArray))
print('The highest value is: ', max(numbersArray))

sortedNumberArray = sorted(numbersArray)

print("Here is the sorted array to prove the highest and lowest values:")
print(sortedNumberArray)