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


@client.event 
async def on_ready():
  print('hey m turned on :p')


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
    time.sleep(43200)

@client.command()
async def clear(ctx , num= 1):
  await ctx.channel.purge(limit= num+1)    


keep_alive()

client.run('ODM4NTI5MjgyNTUxNTc4Njc0.YI8bQA.CJOxzT9T_IQq9VFkmFoQI_vckjk')  