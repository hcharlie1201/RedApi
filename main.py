import os
import discord
from repeat import repeater

#############################################################################################
#
#discord
client = discord.Client()


@client.event
async def on_ready():
	print('We have login in as {0.user}'.format(client))
	repeater.start(client)


# @client.event
# async def on_message(message):
#   if message.author == client.user:
#     return

#   if any(word in message.content.lower() for word in twords):
#     myPost = await get_first_threads()
#     channel = client.get_channel(862264953044992000) #test2 channel
#     await channel.send(myPost)

# client.loop.create_task(get_first_threads())

#channel = client.get_channel(862264953044992000)
# @client.command()
# async def announce(ctx, channel: discord.TextChannel):
# 		await channel.send("My text")
# def printit():
#   threading.Timer(5.0, printit).start()
#   print ("Hello, World!")
#   channel.send('hi')

# printit()
#@client.event
##async def client.on(mess#

#lient.channels.get('862264953044992000').send('Hello here!')
#   #if message.content.startswith('inspire'):
#   if any(word in message.content for word in zen_words):
#     quote = get_quote()
#     await message.channel.send(quote)
#     #await message.channel.send('hello! boba plz')
#   if any(word in message.content for word in shutupflag):
#     await message.channel.send(random.choice(shutupoutput))
#   if any(word in message.content for word in remind):
#     await message.channel.send(random.choice(remindoutput))
#   if any(word in message.content for word in counterflag_words):
#     await message.channel.send(random.choice(output_words))

client.run(os.getenv('tok'))
