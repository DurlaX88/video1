import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Turnaj se odehrává zde: http://bit.ly/gb_tclan_join a pravidla nalezneš zde: http://gbrothers.pageride.sk/turnaj/pravidla')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print("Ready, Freddy") 


@client.event
async def on_message(message):
    if message.content == '':
        await client.send_message(message.channel,'')
    if message.content == '/pravidla':
        await client.send_message(message.channel,'Pravidla turnaje nejdeš zde:  http://gbrothers.pageride.sk/turnaj')
    if ('piča') in message.content:
       await client.delete_message(message)
    if message.content == '/support':
        await client.send_message(message.channel,'Pro pomoc napiš zprávu zde: https://www.facebook.com/durlax88')
    if message.content == 'příkaz':
        await client.send_message(message.channel,'activity')        
    if message.content == '/příkazy':
        await client.send_message(message.channel,'/pravidla - pravidla turnaje a clanu   /support - podpora')
    if message.content.startswith('/web'):
        await client.send_message(message.channel,'web je http://gbrothers.pageride.cz')
    if message.content.startswith('royaleapi'):
        await client.send_message(message.channel,'https://royaleapi.com/clan/8V2CUQLU')
client.run('NTI4NjcwNTMzNTQyMzQ2NzU0.DwlqcQ.g5rWY8vOKE4TG4qwQZUunhgO0M8')

   
