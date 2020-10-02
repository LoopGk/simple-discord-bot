import os
import math

import discord
from discord.ext import commands
from discord.voice_client import VoiceClient

from dotenv import load_dotenv

bot = commands.Bot(command_prefix=">", description="I'm Gk Bot")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Among us", url="https://youtube.com/anywhere"))
    print("Bot Gk Online")

@bot.command(name='loop', help="Este comando nos avisa que el bot está vivo")
async def loop(ctx):
    await ctx.send('gk')

@bot.command(name='ping', help="Este comando nos indica la latencia")
async def ping(ctx):
    await ctx.send(f"¡PONG! Latencia {round(bot.latency*1000)} ms")

@bot.command()
async def elevar(ctx, base:float, exponent:int):
    await ctx.send(math.pow(base,exponent))

@bot.listen()
async def on_message(message):
    if "mejores cursos de programacion" in message.content.lower():
        await message.channel.send("Tal vez quisiste decir LoopGk https://facebook.com/loopgk")
        await bot.process_commands(message)
    elif "¿quien eres?" in message.content.lower():
        await message.channel.send("Soy un bot de discord hecho en Python")
        await bot.process_commands(message)

@bot.command(name='join', help="Este comando hace que se una nuestro bot al canal de voz en el que estemos")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("No estás conectado a ningún canal, ingresa y reintenta")
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

    

load_dotenv()

TOKEN = os.getenv('TOKEN-DISCORD')

bot.run(TOKEN)
