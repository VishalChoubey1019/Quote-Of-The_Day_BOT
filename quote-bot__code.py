from keep_alive import keep_alive

import discord
from discord.ext import commands, tasks
import requests
import json
import time

client = commands.Bot(command_prefix = 'q_') #you can have any prefix as per your choice
#here you can use anything except client too but make sure that everytime i have written client.____ u write yourvariable._____

def find_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@tasks.loop(seconds=43200)
async def play_quotes(ctx):
  name = ' '
  quote_with_name    = find_quote()

  quote_without_name = quote_with_name.split('-')[0]
  b = 0

  for i in range(0,len(quote_with_name)):
    if quote_with_name[i] == '-':
      b = 1
    if b==1:
      name = name + quote_with_name[i]     
  channel = client.get_channel(813744487758796822794) #CHANNEL ID(it has 18 digits)
  await channel.send(f'**"{quote_without_name}" {name}**') 

@client.command()
async def stop(ctx):
  print_quote.cancel()
  await ctx.send("Okay! I'll Stop :(")

@client.command()
async def ping(ctx):
  await ctx.send(f'pong : {round(client.latency * 1000)} ms')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command Used. Type q_help to know the commands'
                       )
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Give proper values to the command an argument is missing')

@client.event 
async def on_ready():
  print('Hey m turned on :p')


@client.command()
async def inspire(ctx):
  play_quotes.start(ctx)


keep_alive()

client.run('ODM4NTfas325MjgysdfTcsfsaNjc0.Yjfks8bQA.QVh7UtbVrUtCiRZ5hasi7fkaSGnjlymiU')  #THIS IS WRONG YOU CAN ADD YOUR SERVER's TOKEN HERE.


