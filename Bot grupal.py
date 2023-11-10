import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def enviroment(ctx, count_enviroment = 1):
    await ctx.send("Ideas para cuidar el medio ambiente:\n-Recicla en ves de botar la basura\n-Planta àrboles\n-No uses productos contaminantes\n-No compres cosas innecesarias\n-Ahorra la luz\n-Cierra el caño mientras te estas cepillando " * count_enviroment)


@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

bot.run("MTE2NzI0MzMyNjI2MTU3MTc0NQ.GNsRxr.IGPDz-Y9J_coxRektf0kPAb3pcEoyyjBvffWJ8")