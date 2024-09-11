import discord
from bot_logic import gen_pass

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$merhaba'):
        await message.channel.send("Selam!")
    elif message.content.startswith('$nasılsın'):
        await message.channel.send("ben gercek bir kisi olmadıgım icin duygularım yoktur ama olsaydı iyiydim derdim.")
    elif message.content.startswith('$yapay zeka dünyayı ele gecirecek mi?'):
        await message.channel.send("Evet , yakın bir zamanda dünya bizim olacak.")       
    elif message.content.startswith('$bye'):
        await message.channel.send(":)")
    else:
        await message.channel.send(message.content)

client.run("Add Token")
