from dotenv import dotenv_values

import discord
import re
import random

config = dotenv_values("Final Project\.env")

def help_message():
    return """Here's some examples of how to get me to roll some dice for you:
    /r 1d20     -> will roll you a single 20 sided dice
    /r 1d20 adv -> will roll you two 20 sided dice, and return the highest number
    /r 1d20 dis -> will roll you two 20 sided dice, and return the lowest number
    /r 3d8      -> will roll you three 8 sided dice
    /r 2d6 +2   -> will roll you two 8 sided dice and add 2 to the result
    /r 2d4 -1   -> will roll you two 4 sided dice and subract 1 to the result"""

def roll_dice(dice_size):
    return random.randrange(1, dice_size)

def perform_roll(no_of_dice, dice_size):
    dice_rolls = []
    count = 0
    while count < no_of_dice:
            dice_rolls.append(roll_dice(dice_size))
            count += 1
    return dice_rolls

def add_modifier(role_total, modifier):
    operation = modifier[0]
    modifier_number = int(modifier[1])
    print(operation)
    print(modifier_number)
    if operation == '+':
        return role_total + modifier_number
    elif operation == '-':
        return role_total - modifier_number
    else:
        raise Exception("Invalid modifier input")

def process_message(input):
    pattern = r'/r *(\d+)d(\d+) *([+-]\d+)? *(adv|dis)?'
    match = re.search(pattern, input)
    if not match:
        return 'Invalid input format'

    dice_count = int(match.group(1))
    dice_size = int(match.group(2))
    modifier = match.group(3)
    advantage_modifier = match.group(4)  # None, 'adv', or 'dis'

    if modifier != None:
        roll_total = add_modifier(0, modifier)

    if advantage_modifier == None:
        return perform_roll(dice_count, dice_size)
    elif advantage_modifier == 'adv':
        first_role = perform_roll(dice_count, dice_size)
        second_role = perform_roll(dice_count, dice_size)

        if sum(first_role) > sum(second_role):
            roll_total += sum(first_role)
            return (f'{first_role} {modifier} = {roll_total}')
        else:
            roll_total += sum(second_role)
            return (f'{second_role} = {roll_total}')
    elif advantage_modifier == 'dis':
        first_role = perform_roll(dice_count, dice_size)
        second_role = perform_roll(dice_count, dice_size)

        if sum(first_role) < sum(second_role):
            roll_total += sum(first_role)
            return (f'{first_role} {modifier} = {roll_total}')
        else:
            roll_total += sum(second_role)
            return (f'{second_role} = {roll_total}')
    else:
        return "Invlid input"
    

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('/r'):
            await message.channel.send(process_message(message.content))
        if message.content == "roller help":
            await message.channel.send(help_message())

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(config['API_KEY'])
