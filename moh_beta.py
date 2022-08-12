import os
import discord
import requests
import json
import random
import math
from random import randint
from discord.ext import commands
from discord import Permissions
TOKEN = "your_token"
client = discord.Client()



    

#print if logged in successfully
@client.event
async def on_ready():
    print("{0.user} has logged in successfully".format(client))
    print("===================================")
    terminal_input = input("Commands: ")
    if terminal_input == "test":
        user = await client.fetch_user("907986080312225802")
        await user.send("Hello there!")






    
client.run(TOKEN, bot=True)
