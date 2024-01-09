import discord
from discord.ext import commands

DISCORD_TOKEN = "MTE1MTk5NTAzNzk5MTgzMzYyMQ.GxQ7kP.lumWzHKt8CnCtbcyqrxjzUF-x1ZkDKu5XFeH9w"
PREFIX = "!"

bot = commands.Bot(command_prefix=PREFIX, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Meu bot {bot.user.name} conectou)")

@bot.command()
async def ping(ctx):
    await ctx.send(f"pong{round(bot.latency * 1000)}ms")

@bot.command("Darminha")
async def ping(ctx):
    print("Ama a Giovanna")
    await ctx.send("Ama a Giovanna")

bot.run(DISCORD_TOKEN)
