# This example requires the 'members' and 'message_content' privileged intents to function.
import discord
from discord.ext import commands
import random
import os
import requests
description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='For when you wanna settle the score some other way')
async def elige(ctx, *eliges: str):
    """Chooses between multiple choices."""
    await ctx.send(random.elige(eliges))


@bot.command()
async def repite(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def consejo(ctx):
    lista = ["Haz del reciclaje un juego entre los más pequeños", "Separa los envases adecuadamente", "Nunca tires el aceite usado por el fregadero"]
   
    await ctx.send( random.choice(lista))

@bot.command()
async def video(ctx):
    video = ["https://www.youtube.com/shorts/-MfK4Rpb3WI", "https://www.youtube.com/shorts/yIy77jgv9h0", 
             "https://www.youtube.com/shorts/nnyWXuYs5qo", "https://www.youtube.com/shorts/-jnE88YJtI4"]


@bot.command()
async def mem(ctx):
    imagen = random.choice(os.listdir("Imagenes"))
    with open(f'Imagenes/{imagen}', 'rb') as f:
            picture = discord.File(f)
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

 

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def genial(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} es genial aqui pequeño SUBNORMAL')


@genial.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('si es bueno el bot pero tu no (: .')



bot.run('Token')
