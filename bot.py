from settings import DISCORD_TOKEN
from lyrics import get_lyrics

import discord
import logging

logging.basicConfig(level=logging.INFO)

#TODO Handle Errors
class LyricalClient(discord.Client):

    async def on_ready(self):
        logging.info(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        text = message.content
        if(message.author == self.user):
            return
        if(text.startswith("&")):
            text = message.content[1:].strip()
            lyrics = get_lyrics(text)
            await message.channel.send(lyrics)
            # print(text)
        else:
            return
            # await message.channel.send("I don't eavesdrop! Or do I?")
            # print("I don't eavesdrop!")

client = LyricalClient()

client.run(DISCORD_TOKEN)