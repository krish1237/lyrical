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
            try:
                text = message.content[1:].strip()
                lyrics = get_lyrics(text)
                if lyrics != "":
                    if(len(lyrics) >= 2000):
                        lyrics_1 = lyrics[:2000]
                        lyrics_2 = lyrics[2000:]
                        await message.channel.send(lyrics_1)
                        await message.channel.send(lyrics_2)
                    else:
                        await message.channel.send(lyrics)
            except Exception as e:
                logging.error(e)
                await message.channel.send("Some error occured. My developers are lazy asses who can't handle errors properly. Please try again")
        else:
            return

client = LyricalClient()

client.run(DISCORD_TOKEN)