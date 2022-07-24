import discord
import random
from discord.ext import commands
from dicAudio import audios

token = 'Token Goes Here'
pathFF = 'Path to FFMpeg.exe'

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'Bot online {format(bot.user)}')

@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await ctx.send(f'Entrando no canal {channel.name}')
    await channel.connect()        

@bot.command()
async def leave(ctx):
    await ctx.send(f'Saindo do canal {ctx.author.voice.channel.name}')
    await ctx.voice_client.disconnect()   

@bot.command()
async def play(ctx):
    guild = ctx.guild
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(executable=pathFF, source=f"audios/{audios[random.randint(1,len(audios))]}")
    if not voice_client.is_playing():
        voice_client.play(audio_source, after=None)

@bot.event
async def on_voice_state_update(member: discord.Member, before, after):
    guild = member.guild
    vc_before = before.channel
    vc_after = after.channel
    voice_client: discord.VoiceClient = discord.utils.get(bot.voice_clients, guild=guild)
    audio_source = discord.FFmpegPCMAudio(executable=pathFF, source="audios/olhaEleAi.mp3")
    
    if vc_before == vc_after:
        return
    if vc_before is None:
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)
    elif vc_after is None:
        return
    else:
        if not voice_client.is_playing():
            voice_client.play(audio_source, after=None)

    
bot.run(token)


