import discord
from discord.ext import commands
import youtube_dl
class music (commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def join (self,ctx):
        if ctx.author.voice is None:
            await ctx.send("anh co o trong phong voice chat nao dau >.<")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else: 
            await ctx.voice_client.move_to(voice_channel)
    @commands.command()
    async def disconnect (self,ctx):
        await ctx.voice_client.disconnect()
    @commands.command()
    async def play (self,ctx,url):
        ctx.voice_client.stop()
        ffmpeg_ops = {'before_options': '-reconnect 1 -reconnect_streamed 1-reconnect_delay_max 5', 'options':'-vn'}
        ydl_ops = {'format':'bestaudio'}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(ydl_ops) as ydl:
            info =ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source =await discord.FFmpegOpusAudio.from_probe(url2,**ffmpeg_ops)
            vc.play(source)
    @commands.command()
    async def pause (self,ctx):
        await ctx.voice_client.pause()
        await ctx.send("nhac da dung ;-;")
    @commands.command()
    async def resume (self,ctx):
        await ctx.voice_client.resume()
        await ctx.send("~tiep tuc choi nhac nhaa ^-^")
def setup(client):
    client.add_cog(music(client))
