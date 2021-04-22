import discord
from discord.ext import commands
import json
from keep_alive import keep_alive

client = commands.Bot(command_prefix = "c!")

@client.event
async def on_ready():
  print("Logged in as ",client.user.name)
  
@client.event
async def on_guild_join(guild):
  with open("Channels.json", "r") as f:
    channels = json.load(f)
    
  channels[str(guild.id)] = "none"
  
  with open("Channels.json", "w") as f:
    json.dump(channels,f)
    
  with open("Numbers.json", "r") as f:
    numbers = json.load(f)
    
  numbers[str(guild.id)] = 0
  
  with open("Numbers.json", "w") as f:
    json.dump(numbers, f)
  
 
@client.command()
@commands.has_permissions(administrator = True)
async def channel(ctx, channel: discord.TextChannel):
  
  with open("Channels.json", "r") as f:
    channels = json.load(f)
    
  channels[str(ctx.guild.id)] = channel.id
  
  with open("Channels.json", "w") as f:
    json.dump(channels,f)
  
  await ctx.send(f"Successfuly set <#{channel.id}> as the counting channel")
  
@client.event
async def on_message(msg):
  with open("Channels.json", "r") as f:
    channels = json.load(f)
    
  channel = channels[str(msg.guild.id)]
  
  if msg.channel.id == channel:
    with open("Numbers.json", "r") as f:
      numbers = json.load(f)
  
    number = int(numbers[str(msg.guild.id)])
      
    try:
      num = int(msg.content)
    except:
      pass

    if num == number+1:
      with open("Numbers.json", "r") as f:
        bruh = json.load(f)
        
      bruh[str(msg.guild.id)] = int(msg.content)
      
      with open("Numbers.json","w") as f:
        json.dump(bruh, f)
        
    else:
      await msg.delete()
  await client.process_commands(msg)

keep_alive()
client.run("ODM0MzY1MzYyNjc3NjEyNTU0.YH_1TA.rf9lZauOImiYs1YKW8IDtat_LWs")