# Write code below 💖

earth_weight = float(input("Please enter your weight: "))

planet = int(input("""
1) Mercury
2) Venus
3) Mars
4) Jupiter
5) Saturn
6) Uranus
7) Neptune

Please select a planet from the above list:
"""))


if planet == 1:
  destination_weight = earth_weight*0.38
  print(destination_weight)
elif planet == 2:
  destination_weight = earth_weight*0.91
  print(destination_weight)
elif planet == 3:
  destination_weight = earth_weight*0.38
  print(destination_weight)
elif planet == 4:
  destination_weight = earth_weight*2.53
  print(destination_weight)
elif planet == 5:
  destination_weight = earth_weight*1.07
  print(destination_weight)
elif planet == 6:
  destination_weight = earth_weight*0.89
  print(destination_weight)
elif planet == 7:
  destination_weight = earth_weight*1.14
  print(destination_weight)
else:
  print("Invalid planet number")

# THE BELOW WORKS AND IS A BETTER VERSION OF THE ABOVE

# if planet == 1:
#   print(f'You would weigh {earth_weight*0.38} on Mercury')
# elif planet == 2:
#   print(f'You would weigh {earth_weight*0.91} on Venus')
# elif planet == 3:
#   print(f'You would weigh {earth_weight*0.38} on Mars')
# elif planet == 4:
#   print(f'You would weigh {earth_weight*2.53} on Jupiter')
# elif planet == 5:
#   print(f'You would weigh {earth_weight*1.07} on Saturn')
# elif planet == 6:
#   print(f'You would weigh {earth_weight*0.89} on Uranus')
# elif planet == 7:
#   print(f'You would weigh {earth_weight*1.14} on Neptune')
# else:
#   print("Invalid planet number")