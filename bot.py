import discord
import requests
from discord.ext import commands
 
client = discord.Client()
TOKEN = 'ENTER_TOKEN_HERE'
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    request = requests.get('https://api.etherscan.io')
    print(request.status_code)
    request = requests.get('https://ticker.saturn.network/')
    print(request.status_code)
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == 'off-topic':
        if message.content.startswith('!help'):
            embed = discord.Embed(title="Commands: ",color=0x000000) #bar color
            embed.add_field(value='!price', name="Gets average price from Saturn Network", inline=False)
            embed.add_field(value='!24hr', name="Gets 24 hr price from Saturn Network", inline=False)
            embed.add_field(value='!volume', name="Gets trade volume from Saturn Network", inline=False)
            embed.add_field(value='!address', name="Gets token contract address", inline=False)
            embed.add_field(value='!contract', name="Gets token EtherScan link", inline=False)
            embed.add_field(value='!saturn', name="Gets Saturn exchange link", inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('!address'):
            embed = discord.Embed(title="0xb9440022a095343b440d590fcd2d7a3794bd76c8",color=0x000000) #bar color
            await message.channel.send(embed=embed)
            
        if message.content.startswith('!contract'):
            embed = discord.Embed(title="https://etherscan.io/address/0xb9440022a095343b440d590fcd2d7a3794bd76c8",color=0x000000) #bar color
            await message.channel.send(embed=embed)

        if message.content.startswith('!saturn'):
            embed = discord.Embed(title="https://www.saturn.network/exchange/ETH/order-book/0xb9440022a095343b440d590fcd2d7a3794bd76c8",color=0x000000) #bar color
            await message.channel.send(embed=embed)
            
        if message.content.startswith('!24hr'):
            tkninfo = requests.get('https://ticker.saturn.network/api/v2/tokens/show/eth/0xb9440022a095343b440d590fcd2d7a3794bd76c8.json')
            tkninfo_json = tkninfo.json()
            embed = discord.Embed(title="Saturn Network",color=0x000000) #bar color
            price = '{0:.10f}'.format(float(tkninfo_json['price24hr']))
            embed.add_field(name="24 HR Price: ", value="{} ETH".format(price), inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('!price'):
            tkninfo = requests.get('https://ticker.saturn.network/api/v2/tokens/show/eth/0xb9440022a095343b440d590fcd2d7a3794bd76c8.json')
            tkninfo_json = tkninfo.json()
            embed = discord.Embed(title="Saturn Network",color=0x000000) #bar color
            price = '{0:.10f}'.format(float(tkninfo_json['dashboard_price']))
            embed.add_field(name="Average Price: ", value="{} ETH".format(price), inline=False)
            await message.channel.send(embed=embed)

        if message.content.startswith('!volume'):
            tkninfo = requests.get('https://ticker.saturn.network/api/v2/tokens/show/eth/0xb9440022a095343b440d590fcd2d7a3794bd76c8.json')
            tkninfo_json = tkninfo.json()
            embed = discord.Embed(title="Saturn Network",color=0x000000) #bar color
            vol = '{0:.2f}'.format(float(tkninfo_json['volume24hr']))
            embed.add_field(name="24 HR Volume: ", value="{} ETH".format(vol), inline=False)
            await message.channel.send(embed=embed)
        
client.run(TOKEN)