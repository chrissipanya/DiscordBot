import discord
import asyncio
import random
import os


client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


#messing around with classes
class Bot:

	def __init__(self,response,tok):
		self.response = response
		self.tok = tok

msg1 = Bot('Git Good Scrub!!','!tekken')
msg2 = Bot('Eat this SPD!!!!','!sfv')

@client.event
async def on_message(message):
	if message.content.startswith(msg1.tok):
		await client.send_message(message.channel,msg1.response)
	elif message.content.startswith(msg2.tok):
		await client.send_message(message.channel,msg2.response)


client.run('MzY1OTg2NTk2Mjc0NzAwMjkw.DL4JbA.aZw16I8TDvedyajIyHHhahzc3Xw')
