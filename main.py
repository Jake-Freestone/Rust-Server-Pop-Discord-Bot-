import discord
import asyncio
import time
from discord.ext import commands

import requests
from bs4 import BeautifulSoup
import string

client = commands.Bot(command_prefix='!')
client.remove_command("help")

file=open("token.txt","r")
line = file.readline()
file.close()
BotToken = str(line)

async def status_task():
    while True:
        time.sleep(5)
        file = open("url.txt","r")
        lines = file.readline()
        file.close()
        URL = str(lines)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        newsoup=str(soup)

        #finds the queue amount:
        resultant=(newsoup.find("rust_queued_players"))
        new=int(resultant)
        indexofqueue= new + 21
        Queued_Rust_Players = newsoup[indexofqueue:(indexofqueue+2)]
        Queued_Rust_Players = str(Queued_Rust_Players)

        #finds the players at the moment
        resultant2=(newsoup.find("players"))
        new2=int(resultant2)
        indexofplayers= new2 + 9
        Rust_Players = newsoup[indexofplayers:(indexofplayers+3)]
        Rust_Players = str(Rust_Players)
        Rust_Players = Rust_Players.replace(",","")
        Rust_Players = Rust_Players.replace('"',"")

        #finds status 
        resultant3=(newsoup.find("status"))
        new3=int(resultant3)
        indexofstatus= new3 + 9
        Server_Status = newsoup[indexofstatus:(indexofstatus+6)]
        Server_Status = str(Server_Status)
        if Server_Status == "online":
            #sets the status
            status = str(Rust_Players)+"/"+"250 + "+Queued_Rust_Players+ " In Queue"
            activity = discord.Activity(name=str(status), type=discord.ActivityType.playing,status=discord.Status.online)
            await client.change_presence(activity=activity)
            channel=client.get_channel(#SET TO THE ID OF A CHANNEL THAT WILL BE HIDDEN FOR EVERY OTHER USER)
            await channel.send ("Working")
            print("Server Online",status)
        else:
            print("Server Offline")
            channel=client.get_channel(#SET TO THE ID OF A CHANNEL THAT WILL BE HIDDEN FOR EVERY OTHER USER)
            await channel.send ("Working")

            activity = discord.Game(name="The Offline Server")
            await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_ready():
    client.loop.create_task(status_task())



client.run(BotToken)
