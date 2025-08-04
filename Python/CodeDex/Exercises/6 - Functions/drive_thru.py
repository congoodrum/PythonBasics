# Write code below 💖

menu = [
  'Cheeseburger',
  'Fries',
  'soda',
  'Ice Cream',
  'Cookie'
]

def get_item(x):
  return menu[x-1]

def welcome():
  print("""
  Welcome to our drive-thru :)

  Please take a look at the menu below, and input your order one item at a time.

  NOTE: When you have finished your order, enter -1
  """)

def main():
  welcome()
  for i in range(len(menu)):
    print(f"{i+1}) {menu[i]}")
  userInput = int(input("Please enter your choice: "))
  while userInput != -1:
    print(f"One {get_item(userInput)} added to your order")
    userInput = int(input("Please enter another choice: "))
    
  print("Thank you for coming to the Drive-Thru :)")

main()