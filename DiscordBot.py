import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

@client.event
async def on_message(message):
	if message.content.startswith('!tekken'):
		await client.send_message(message.channel, 'Gets me off fuck up!!')

client.run('MzY1OTg2NTk2Mjc0NzAwMjkw.DL4JbA.aZw16I8TDvedyajIyHHhahzc3Xw')
