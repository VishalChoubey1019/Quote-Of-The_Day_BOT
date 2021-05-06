from keep_alive import keep_alive

import discord
from discord.ext import commands, tasks
import requests
import json
import time

client = commands.Bot(command_prefix = 'q_')

def find_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@tasks.loop(seconds=43200)   #43200 = 12*60*60 secs = 12 hours, you can change it to any amount of time
async def play_quotes(ctx):
  name = ' '
  quote_with_name    = find_quote()

  quote_without_name = quote_with_name.split('-')[0]
  b = 0

  for i in range(0,len(quote_with_name)):  # This thing is only for adding quotes(" ") in the part without the name of the writer/speaker.
                                           # But this feature fails when sometimes the quote has a ' - ' before writer/speaker's name.
    if quote_with_name[i] == '-':
      b = 1                       
    if b==1:
      name = name + quote_with_name[i]     

  await ctx.send(f'**"{quote_without_name}" {name}**') 

@client.command()                          # You can check the ping here.
async def ping(ctx):
  await ctx.send(f'Ping : {round(client.latency * 1000)} ms')  # ms is milisecond. 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid Command Used. Type q_help to know the commands')
                       
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Give proper values to the command an argument is missing')

@client.event 
async def on_ready():
  print('Hey m turned on :p')   # This is printed on the website i host it on.


@client.command()
async def inspire(ctx):
  play_quotes.start(ctx)


keep_alive()

client.run('ODMsd5MjgyNTUxNTcfds0.YI232sdA.sdfUtCADIAZnsfdnjlymiU')  #this token is not correct :p . You can paste your bot's token here to make it run.
