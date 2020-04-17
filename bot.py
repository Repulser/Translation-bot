from datetime import datetime

import discord
from googletrans import Translator

SOURCE_CHANNEL = 700741481920462939  # Channel ID
TARGET_CHANNEL = 700741544566587422  # Channel ID


def strip(input):
    return input.replace("*", "").replace("`", "").replace("_", "").replace("@", "@\u200b")


class TranslateBot(discord.Client):
    def __init__(self, **options):
        super().__init__(**options)
        self.translator = Translator()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.channel.id != SOURCE_CHANNEL:
            return
        target_channel = message.guild.get_channel(TARGET_CHANNEL)
        if not target_channel:
            return
        time = datetime.utcnow().strftime("%H:%M:%S")
        author = message.author
        translated = self.translator.translate(strip(message.content))
        await target_channel.send(f"`[{time}]` ({translated.src}) **{author.name}#{author.discriminator}** - {translated.text}")


client = TranslateBot()
client.run('token')
