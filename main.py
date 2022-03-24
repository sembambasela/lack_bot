'''
Lack BOT 

'''
import discord
import os 
import gcsa 

import asyncio


 

@client.event 
async def on_ready():
  print('We have logged in as {0.user}'.format(client))  
  

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  if message.channel.send('$lack'):
    await message.channel.send('Morning Lacker! Time to Start grinding you know what I meaaan')

async def my_repeated_message():
  await client.wait_until_ready()
  counter = 0; 
  channel = client.getchannel(id = '947661666668130354') 
  while not client.isclosed():
    counter += 1
    await channel.send_message(print(),counter)
    await asyncio.sleep(60) #
  
#Task:make a function that returns calendar events

client.loop.create_task(my_repeated_message())
client.run(os.getenv('TOKEN'))