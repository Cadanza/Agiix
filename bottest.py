import discord
from discord.ext import commands

TOKEN = 'NTA3MTYzNzE2OTcwNzQxNzYw.DrsusA.oTMHmObNwyKjhjKcMAW2PONweyE'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('!site'):
        msg ='Ok you can connect into https://www.allgenda.com/'
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
