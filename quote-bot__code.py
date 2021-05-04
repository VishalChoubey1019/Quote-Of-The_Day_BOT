from keep_alive import keep_alive

import discord
from discord.ext import commands, tasks
import requests
import json
import time

client = commands.Bot(command_prefix = 'q_')

# Function to find quote # 
def find_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return (quote)


@client.event 
async def on_ready():
  print('Hey m turned on :p')    #this is printed on my terminal


@client.command()
async def inspire(ctx):
  while True:
    
    name = ' '
    quote_with_name    = find_quote()     

    quote_without_name = quote_with_name.split('-')[0] 
    b = 0

    for i in range(0,len(quote_with_name)):
      if quote_with_name[i] == '-':
        b = 1
      if b==1:
        name = name + quote_with_name[i]
      

    await ctx.send(f'**"{quote_without_name}" {name}**') 
    time.sleep(43200) #12 hours, you can set it to any amount of time(in seconds)


keep_alive()

client.run('ODM4NTI5MjgayNTUxNTc4Njo0.YI8bQA.CJOxT9T_IQq9DFkoFoOT_ursky')  #this token is not correct :p . You can paste your bot's token here to make it run.
