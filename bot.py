from settings import DISCORD_TOKEN

import discord
import logging

logging.basicConfig(level=logging.INFO)

class LyricalClient(discord.Client):

    async def on_ready(self):
        logging.info(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        text = message.content
        if(message.author == self.user):
            return
        if(text.startswith("&")):
            text = message.content[1:].strip()
            await message.channel.send("I have seen what you said and choose to ignore it :)")
            # print(text)
        else:
            return
            # await message.channel.send("I don't eavesdrop! Or do I?")
            # print("I don't eavesdrop!")

client = LyricalClient()

client.run(DISCORD_TOKEN)