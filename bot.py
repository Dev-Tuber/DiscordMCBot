import discord
from discord.ext import commands
from mcstatus import MinecraftServer

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='server')
async def server(ctx, server_address: str):
    server = MinecraftServer.lookup(server_address)
    status = server.status()
    await ctx.send(f'해당 서버는 {status.players.online} 플레이어가 플레이 중이며, 핑은 {status.latency} ms 입니다.')

bot.run('봇 토큰')
