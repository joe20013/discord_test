import discord
from discord.ext import commands
import json

intents=discord.Intents.default()
intents.members=True

with open('setting.json','r',encoding='utf8') as jfile:
    jdate=json.load(jfile)

bot=commands.Bot(command_prefix='/',intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdate['Welcome_channel']))
    await channel.send(f'{member}join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdate['Leave_channel']))
    await channel.send(f'{member}leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.event
async def on_message(msg):
    if msg.content =='hi':
        await msg.channel.send('hello')

@bot.command()
async def say(self,ctx,*,msg):
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command()
async def clean(self,ctx,num:int):
    await ctx.channel.purge(limit=num+1)

bot.run(jdate['TOKEN'])