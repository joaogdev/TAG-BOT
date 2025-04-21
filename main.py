import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print("Bot Inicializado Com Sucesso!")  

@bot.command()
async def botinfo(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"Olá,{nome}! eu sou um bot de criado pelo joão! Estou aqui para ajudar você com suas necessidades de automação interação no Discord. Se precisar de algo, é só me chamar!")
    
@bot.command()
async def gay(ctx:commands.Context):
    nome = ctx.author.name
    await ctx.reply(f"@everyone o {nome} é o mais gay do grupo!")

@bot.command()
async def ping(ctx:commands.Context):
    await ctx.reply("Pong!")

   
@bot.command()
async def avatar(ctx: commands.Context, member: commands.MemberConverter = None):
    member = member or ctx.author  # Se ninguém for mencionado, usa quem chamou
    await ctx.reply(member.avatar.url)

@bot.command()
async def tagios(ctx:commands.Context):
    await ctx.reply("https://discord.gg/Uht9rp6qMn")

@bot.command()
async def tagdev(ctx:commands.Context):
    await ctx.reply("https://discord.gg/reactionroles")

@bot.command()
async def tagowo(ctx:commands.Context):
    await ctx.reply("https://discord.gg/X4DAytX6TM")


@bot.command() 
async def tagez(ctx:commands.Context):
    await ctx.reply("https://discord.gg/valorantil")

@bot.command()
async def taglgbt(ctx:commands.Context):
    await ctx.reply("https://discord.gg/lgbtqia")

@bot.command()
async def tagdual(ctx:commands.Context):
    await ctx.reply("https://discord.gg/dualview")

@bot.command()
async def tagtit(ctx:commands.Context):
    await ctx.reply("https://discord.gg/titsrp")

@bot.command()  
async def tagmeow(ctx:commands.Context):
    await ctx.reply("https://discord.gg/8wJKvYmEwc")

@bot.command()
async def tagbruh(ctx:commands.Context):
    await ctx.reply("https://discord.gg/la-cueva-de-cosi-844285068275875890")

@bot.command()
async def tagvip(ctx:commands.Context):
    await ctx.reply("https://discord.gg/Axb7ThUY5y")

@bot.command()
async def taggca(ctx:commands.Context):
    await ctx.reply("https://discord.gg/gca")

@bot.command()  
async def tagvalc(ctx:commands.Context):
    await ctx.reply("https://discord.gg/mqGmVhntRt")

@bot.command()
async def tagrawr(ctx:commands.Context):
    await ctx.reply("https://discord.gg/kCh734XdZv")

@bot.command()
async def tagmoco(ctx:commands.Context):
    await ctx.reply("https://discord.gg/moco")

@bot.command()
async def tagcybr(ctx:commands.Context):
    await ctx.reply("https://discord.gg/cyberinfo")

@bot.command()
async def tagstar(ctx:commands.Context):
    await ctx.reply("https://discord.gg/solarballs")

@bot.command()
async def tagsoul(ctx:commands.Context):
    await ctx.reply("https://discord.gg/soulobby")

@bot.command()
async def tagemh(ctx:commands.Context):
    await ctx.reply("https://discord.gg/emh")

@bot.command()
async def tagwtds(ctx:commands.Context):
    await ctx.reply("https://discord.gg/wtuds") 
    
    
bot.run("MTM2MzM0MDU3NTU1ODA3ODU1Ng.GuFhCf.jitS1GbB3S8drfC_JCwVARtk96kvsNXuLXRVbk")