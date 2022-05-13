import asyncio
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice
import discord
from discord.ext import commands
from random import randint
import time
import requests as rq
import os
import random
from random import choice

# Washno # 

Self_botik = True # Если вы создали бота на сайте discord developers portal то пишите False

# Imports ✓ #

client = commands.Bot(command_prefix='/', intents=discord.Intents.all(), self_bot=Self_botik)
client.remove_command('help')

# Vars ↓ #



Token = ("# ваш токен #")
wait = time.sleep

# On start ⌀ #

@client.event
async def on_ready():
    randomik = ["Я запустился, надеюсь ты меня обслужил! 💚", "Обслужи пожалуйста, я уже пыльный..", "Перепиши пару строчек моего кода, ато я уже старый..", "Наконецто я дождался, я готов к работе! <3"]

    await client.change_presence(status=discord.Status.online)

    print(f"Start\n\n\n\n\n\n\n\n")
    print(random.choice(randomik))

# Commands ⁜ #

@client.command()
async def help(ctx):
    await ctx.send(f"`Привет! Это asyncbot.`")
    wait(0.8)
    await ctx.send(f"`Все мои команды ты сможешь узнать написав` -> /help_ready")

@client.command()
async def help_ready(ctx):
    await ctx.send(f"/1")
    await ctx.send(f"/2")
    await ctx.send(f"/3")
    await ctx.send(f"/4")
    await ctx.send(f"/5")








client.run(Token, bot=Self_botik)