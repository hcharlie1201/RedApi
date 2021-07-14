from discord.ext import tasks
import discord
#from common import  get_new_memesThreads

#declares and initialize prevPost since 
#prevPost can't be in loop
#Why: prevPost would always be different if declared before "if prevPost == myPost:" inside loop so it spams

#loops
#channel client function stringthatspecifieswhichurl

class Repeater():
  def __init__(self, Channel:int, Function, UrlKey):
    self.channel = Channel
    self.getFunction = Function
    self.urlKey = UrlKey
    self.prevPost = ''

  @tasks.loop(seconds=5.0)
  async def repeater(self, client):
    myPost = self.getFunction(self.urlKey)
    print(self.channel)
    temp_channel = client.get_channel(self.channel) #test2 channel
    if self.prevPost == myPost:
      print('same post')
    else:
      await temp_channel.send(myPost)
      print(myPost)
    self.prevPost = myPost