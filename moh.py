import discord
import requests
import json
import random
import math
from random import randint
from discord.ext import commands
from discord import Permissions
import time
TOKEN = "your_token"
link_invite = "https://discord.com/api/oauth2/authorize?client_id=950576892405219409&permissions=8&scope=bot"
client = commands.Bot(command_prefix="ml$", help_command=None)




#get quotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)


    

#print if logged in successfully
@client.event
async def on_ready():
    print("")
    print("{0.user} has logged in successfully".format(client))
    print("")
    print("===================================")
    print("")
    activity = discord.Game(name="Visual Studio Code")
    await client.change_presence(activity=activity)



@client.command()
async def hello(ctx):
    await ctx.send(f'Hello bro, have a nice day!')
    
@client.command()
async def bye(ctx):
    await ctx.send(f'Byeeeeeeeeeeeeeeeeeeeeee')

@client.command()
async def info(ctx):
    await ctx.send(f'Hi, My name is ML Bot, I am the second version of Moh. Moh was created by Matthew Lucastero at 7:41pm (GMT+7) 29 Jan 2022, then ML Bot was created at 9:13am (GMT+7) 9 March 2022')

@client.command()
async def quote(ctx):
    quote = get_quote()
    await ctx.send(quote)

@client.command()
async def help(ctx):
    embed = discord.Embed(title = "**Command list**", description = '''
        My prefix is: `ml%`
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        〔 ❓ 〕 **Help and invite commands**             ⎮ `help`, `invite`

        〔 🤪 〕 **Fun commands**             ⎮ `hello`, `bye`, `info`, `quote`, `cat`, `orange`, ` orange`, `rps`

        〔 🧮 〕 **Math commands**             ⎮ `calc`

        〔 😂 〕 **Emoji commands**             ⎮ `sus`, `egg`, `lmao`, `dark`

        〔 🧰 〕 **Other Commands**             ⎮ `disturb`, `spam`, `pw`
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ''',color=0xabedcc)
    await ctx.send(embed = embed)


@client.command()
async def cat(ctx):
    cat_gif = ['https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif', 
    'https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif', 
    'https://media.giphy.com/media/1iu8uG2cjYFZS6wTxv/giphy-downsized-large.gif',
    'https://media.giphy.com/media/Lq0h93752f6J9tijrh/giphy.gif',
    'https://media.giphy.com/media/Lq0h93752f6J9tijrh/giphy.gif',
    'https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif',
    'https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif',
    'https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif',
    'https://media.giphy.com/media/33OrjzUFwkwEg/giphy.gif',]
    embed = discord.Embed()
    random_cat = random.choice(cat_gif)
    embed.set_image(url=random_cat)
    await ctx.send(embed = embed)

@client.command()
async def orange(ctx):
    kt_orange = 'https://media.discordapp.net/attachments/930350335610986547/937204974369255504/IMG_20220123_122940.png'
    embed = discord.Embed(title="**You found an orange!🍊**" ,description="Here you are", color=0xff000)
    embed.set_image(url=kt_orange)
    await ctx.send(embed = embed)

@client.command()
async def angry(ctx):
    kt_angry = 'https://cdn.discordapp.com/attachments/932624418906206278/937632277494632548/received_693021038363615.jpeg'
    embed = discord.Embed(title="**Oh no, Khang is angry and he will come to your house**" ,description="grahhhh 😡", color=0xfc0303)
    embed.set_image(url=kt_angry)
    await ctx.send(embed = embed)

@client.command()
async def invite(ctx):
    await ctx.send(f'The link to invite the bot is ||https://discord.com/api/oauth2/authorize?client_id=950576892405219409&permissions=8&scope=bot||')

@client.command()
async def rps(ctx):
    embed = discord.Embed(title = "**This is how to play 'rock, paper, scissors' with Moh!**", description = '''
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ⌈ 👊 ⌋ **Rock!**     ⎮ `rps_rock`

        ⌈ 🖐 ⌋ **Paper!**    ⎮ `rps_paper`

        ⌈ ✌️ ⌋ **Scissors!** ⎮ `rps_scissors`
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ''', color=0x966bf2)
    await ctx.send(embed = embed)

@client.command()
async def rps_rock(ctx):
    computer = randint(0,2)
    if computer == 0:
        computer = "👊"
    if computer == 1:
         computer = "🖐"
    if computer == 2:
        computer = "✌️"
            
    if computer == "👊":
            await ctx.send(f'---')
            await ctx.send(computer)
            await ctx.send(f'---')
            await ctx.send(f'> **Draw!**')
        
    if computer == "✌️":
            await ctx.send(f'---')
            await ctx.send(computer)
            await ctx.send(f'---')
            await ctx.send(f'> **You win!**')

    if computer == "🖐":
            await ctx.send(f'---')
            await ctx.send(computer)
            await ctx.send(f'---')
            await ctx.send(f'> **You lose!**')

@client.command()
async def rps_paper(ctx):
    computer = randint(0,2)
    if computer == 0:
        computer = "👊"
    if computer == 1:
        computer = "🖐"
    if computer == 2:
        computer = "✌️"
            
    if computer == "👊":
        await ctx.send(f'---')
        await ctx.send(computer) 
        await ctx.send(f'---')
        await ctx.send(f'> **You win!**')
        
    if computer == "✌️":
        await ctx.send(f'---')
        await ctx.send(computer)
        await ctx.send(f'---')
        await ctx.send(f'> **You lose!**')
        
    if computer == "🖐":
        await ctx.send(f'---')
        await ctx.send(computer)
        await ctx.send(f'---')
        await ctx.send(f'> **Draw!**')


@client.command()
async def rps_scissors(ctx):
    computer = randint(0,2)
    if computer == 0:
        computer = "👊"
    if computer == 1:
        computer = "🖐"
    if computer == 2:
        computer = "✌️"
            
    if computer == "👊":
        await ctx.send(f'---')
        await ctx.send(computer)
        await ctx.send(f'---')
        await ctx.send(f'> **You lose!**')
        
    if computer == "✌️":
        await ctx.send(f'---')
        await ctx.send(computer)
        await ctx.send(f'---')
        await ctx.send(f'> **Draw!**')
        
    if computer == "🖐":
        await ctx.send(f'---')
        await ctx.send(computer)
        await ctx.send(f'---')
        await ctx.send(f'> **You win!**')

@client.command()
async def say(ctx, *,text):
    await ctx.message.delete()
    await ctx.send(f"{text}")



@client.command()
async def sudo_logout(ctx):
    if ctx.message.author.id == "your Discord ID":
        await ctx.message.delete()
        await client.close() 
        print("{0.user} has logged out successfully".format(client))
        print("") 
    
    else:
        await ctx.send(f'You are not the bot creator! You can not use this command!!!')

@client.command()
async def calc(ctx):
    embed = discord.Embed(title = "**Calculation Commands**", description = '''
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ⟪ 🧮 ⟫ **Solve the expression**          ⎮ `calc_exp <expression>`
            `NOTE`:
                ^ = \**
                x = *
                : = /
                
        ⟪ √ ⟫ **Calculate the squareroot**         ⎮ `calc_sqrt <number>`

        ⟪ ℉ ⟫ **Convert Fahrenheit to Celsius**        ⎮ `ftc <number>`

        ⟪ ℃ ⟫ **Convert Celsius to Fahrenheit**         ⎮ `ctf <number>`

        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ''', color = 0x0080ff)
    await ctx.send(embed = embed)

@client.command()
async def calc_exp(ctx,expression:str):
    calculate = eval(expression)
    embed = discord.Embed(title = "Result", description = '''

    **Input**
    ```python\n{}\n```
    ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    **Output**
    ```python\n{}\n```

    '''.format(expression, calculate), color = 0x00fff2)
    await ctx.send(embed = embed)

@client.command()
async def calc_sqrt(ctx, squareroot:float):
    await ctx.send(f'> **The answer is:** ' + str(math.sqrt(squareroot)))

@client.command()
async def ftc(ctx, fahrenheit: float):
    celsius = fahrenheit - 32 / 1.8
    embed = discord.Embed(title = "Result", description='''
    **From Fahrenheit**
    {}°F
    ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯    
    **To Celsius**
    {}°C 

    '''.format(fahrenheit, celsius), color=0x0be076)
    await ctx.send(embed = embed)

@client.command()
async def ctf(ctx, celsius: float): 
    fahrenheit = celsius * 1.8 + 32
    embed = discord.Embed(title = "Result", description='''
    **From Celsius** 
    {}°C
    ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
    **To Fahrenheit**
    {}°F

    '''.format(celsius, fahrenheit), color=0x0be076)
    await ctx.send(embed = embed)





@commands.has_permissions(administrator=True)
@client.command(pass_context=True)
async def purge(ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()
        print("Cleared successfully")

@client.command()
async def pw(ctx):
    embed = discord.Embed(title = "Welcome to Moh Password Generator!", description='''
    ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        ⌈ ⌨️ ⌋ **Generate a password**     ⎮ `gpw <length>`

        **HOW TO USE**
            moh gpw <length of the password>
     ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯''', color=0x27ab4a)
    await ctx.send(embed= embed)

@client.command()
async def gpw(ctx, length_of_password:int):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXWZ'
    low = 'abcdefghijklmnopqrstuvwxyz' 
    number = '0123456789'
    symbol = " !@#$%^&*()><[]"
    all = up + low + number + symbol
    password = "".join(random.sample(all, length_of_password))
    embed = discord.Embed(title = "Successfully generated", description = '''Password:
    || {} ||
    '''.format(password), color=0x03fc90)
    await ctx.message.delete()
    await ctx.author.send(embed=embed)

@client.command()
async def ping(ctx):
    ping = client.latency * 1000
    embed = discord.Embed(title = "**Latency**", description='''`{}` Millisecond'''.format(round(ping)), color =0xffd000)
    await ctx.send(embed=embed)

@client.command(name='lmao')
async def lmao(ctx):
    await ctx.message.delete()
    user = ctx.author
    lmao_emoji = ['<:lmao:932139118668947466>', '<:lmao:937946880053227530>', '<:lmao:941577955866451979>', '<:lmao:944521259335704606>', '<:lmao:941576846309478460>']
    await ctx.send(random.choice(lmao_emoji))

@client.command(name="sus")
async def sus(ctx):
    await ctx.message.delete()
    user = ctx.author
    sus = '<:sus:939907776392597514>'
    await ctx.send(sus)


@client.command(name="dark")
async def dark(ctx):
    await ctx.message.delete()
    user = ctx.author
    dark = '<:dark:930731883464110092>'
    await ctx.send(dark)

@client.command(name="egg")
async def egg(ctx): 
    await ctx.message.delete()
    user = ctx.author
    egg = '<:eggman2:918142972355301387>'
    await ctx.send(egg)

@client.command()
async def spam(ctx, message:str=None, *, int:int):
    if message == None:
        if amount == None:
            await ctx.send(f'Missing amount or message. Example: `ml$spam hello 20`')

    if "spam" in ctx.channel.name.lower():
        await ctx.message.delete() 
        for i in range(amount): 
            await ctx.send(message)
    
    else:
        await ctx.send(f'This is not a spam channel!')

@client.command()
async def disturb(ctx):
    await ctx.message.delete()
    for i in range(10):
        await ctx.message.author.send(f'အမိုက်စား ခွေးမိုက် ၊ မင်း အသားအရေ မည်းညစ် ညစ်ပတ်တယ်')

        



@client.command()
async def cc(ctx):
    embed = discord.Embed(title = "Currency coverter!", description='''
    Convert some currency units to Viet Nam Dong VND
    `ml@cc <money> <money_unit>`
        e.g: `ml@cc 100 USD`
    
    **Supports currency units**
    - [¥] Yen
    - [¥] Yuan
    - [$] USD
    - [€] Euro
    - [₩] Won
    
    ''', color = 0x03fc98)
    await ctx.send(embed = embed)


@client.command()
async def convert(ctx, money:float, money_unit:str):

    if money_unit == 'Yen':
        vnd = float(money)*198
        embed = discord.Embed(title = "Finished", description = '''
        **INPUT**
        {} ¥

        **OUTPUT**
        {} ₫
        '''.format(money, vnd), color =0x0091ff)
        await ctx.send(embed = embed)

    if money_unit == 'USD':
        vnd = float(money)*23000
        embed = discord.Embed(title = "Finished", description = '''
        **INPUT**
        {} $
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        **OUTPUT**
        {} ₫
        '''.format(money, vnd), color =0x0091ff)
        await ctx.send(embed = embed)

    if money_unit == 'Yuan':
        vnd = float(money)*3615
        embed = discord.Embed(title = "Finished", description = '''
        **INPUT**
        {} ¥ 
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        **OUTPUT**
        {} ₫
        '''.format(money, vnd), color =0x0091ff)
        await ctx.send(embed = embed)


    if money_unit == 'Euro':
        vnd = float(money)*25000
        embed = discord.Embed(title = "Finished", description = '''
        **INPUT**
        {} € 
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        **OUTPUT**
        {} ₫
        '''.format(money, vnd), color =0x0091ff)
        await ctx.send(embed = embed)

    if money_unit == 'Won':
        vnd = float(money)*19
        embed = discord.Embed(title = "Finished", description = '''
        **INPUT**
        {} ₩ 
        ⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
        **OUTPUT**
        {} ₫
        '''.format(money, vnd), color =0x0091ff)
        await ctx.send(embed = embed)



client.run(TOKEN, bot=True) 
