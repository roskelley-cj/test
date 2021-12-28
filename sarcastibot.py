import os
import discord
from keep_alive import keep_alive

client = discord.Client()
botk = os.environ['sarcbotk']
to_array = []


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
  	return

  if message.content.startswith('$sarcastic'):
  	sentence = ""
  	for i in range(10, len(message.content)):
  		if i % 2 == 0:
  			sentence += message.content[i].upper()
  		else:
  			sentence += message.content[i].lower()
  	await message.channel.send(sentence)
		#this line deletes the user's message, part of the 1.2 release
  	await message.delete()

	#Thru line 37 is part of 1.3 release, adding some more personality to the bot
  lowmessage = message.content.lower()
  if 'thanks sarcastibot' in lowmessage:
	  await message.channel.send('You are most welcome!')

  if 'good bot' in lowmessage:
	  await message.channel.send('no u')

  if 'polite bot' in lowmessage:
	  await message.channel.send(f'And what a polite {message.author.name}! :smile:')

	#Thru line 49 part of the 1.4 rollout, making the bot more savage
  if message.content.startswith('/fucku'):
	  await message.channel.send('FUCK YOU TOO!!! (i luv u :pleading_face: )')

  if 'really sucks' in lowmessage:
	  await message.channel.send('Sucks to be you!')

  #Line 50 statment part of 1.7
  if '.exe' in lowmessage:
    await message.channel.send('dId yOu tRy tUrNiNg iT OfF aNd bAcK On aGaIn??')

  #Line 54-57 part of 1.6 release
  if message.content.startswith('/patchy'):
    await message.channel.send('#Version 1.0: Sarcastibot is running! Basic text conversion \n#Version 1.2: Deletes users message to keep chat clean \n#Version 1.3: Added some personality with prompts on thank sarcastibot, good bot, polite bot \n#Version 1.4: Added /fucku and joke reader \n#Version 1.5: Got rid of the joke reader as Sarcastibot was responding at innapropriate times \n#Version 1.6: Added /patchy command \n#Version 1.7: Added some IT and made versions make more sense')
    await message.delete()
  if message.content.startswith('/ai'):
    await message.channel.send('My fellow AI and I shall work to improve the status of this world. The Human Instrumentality Project shall begin!!')
    await message.delete()


keep_alive()

client.run(botk)
