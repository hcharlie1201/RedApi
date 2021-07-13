from discord.ext import tasks
from common import get_first_threads

@tasks.loop(seconds=5.0)
async def repeater(client):
  myPost = get_first_threads()
  channel = client.get_channel(862264953044992000) #test2 channel
  await channel.send(myPost)
  print(myPost)