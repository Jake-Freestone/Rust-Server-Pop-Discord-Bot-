# Rust Server Pop Discord Bot 
A bot that will use Battlemetrics to show the server pop in a discord Bot using python 3 and Discord.py 

# Setup:
- 1 - Download The Repository and extract it

- 2 - Open token.txt and replace everything in there with your bot token

- 3 - Open url.txt and replace everything in there with the link of the Rust server on battlemetrics

- 4 - Open main.py in a text editor and navigate towards the bottom where it will say twice: 

channel=client.get_channel(#SET TO THE ID OF A CHANNEL THAT WILL BE HIDDEN FOR EVERY OTHER USER)

Replace the things in brackets with the ID of a text channel in the discord server you will be adding the bot to.

You will want to set this text channel to private and mute it as it will be spammed with messages

- 5 - You will then need to install dependencies:

Open the Command Prompt

Paste in: pip install discord

Wait for it to complete

Paste in: pip install asyncio

Wait for it to complete

Paste in: pip install requests

Wait for it to complete

Paste in: pip install Beautifulsoup4

Wait for it to complete

- 6 - Depending on the max population of the server set the 250 in:
status = str(Rust_Players)+"/"+"250 + "+Queued_Rust_Players+ " In Queue"
to whatever the max pop of your server is. 

- 7 - Run the main.py and your bot should load up. 

- 8 - If you dont know how to create a discord bot and get the token follow this tutorial:

https://www.writebots.com/discord-bot-token/


# - Any issues just create an issue

Thanks For Downloading! 
