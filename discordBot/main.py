import os

import mafic
import nextcord
from nextcord.ext import commands

print("Бот запущен!")


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.pool = mafic.NodePool(self)
        self.loop.create_task(self.add_nodes())

    async def add_nodes(self):
        await self.pool.create_node(
            host="127.0.0.1",
            port=2333,
            label="MAIN",
            password="youshallnotpass",
        )


bot = MyBot(intents=nextcord.Intents(guilds=True, voice_states=True))


@bot.slash_command(dm_permission=False)
async def play(inter: nextcord.Interaction, query: str):
    if not inter.guild.voice_client:
        player = await inter.user.voice.channel.connect(cls=mafic.Player)
    else:
        player = inter.guild.voice_client

    tracks = await player.fetch_tracks(query, search_type="ymsearch")

    if not tracks:
        return await inter.send("No tracks found.")

    track = tracks[0]

    await player.play(track)

    await inter.send(f"Playing {track.title}.")


bot.run("MTE4MjU3OTMwMTU2MDg5NzYxNw.Gm8Lv8.6t6_KSf840kSDarJER3-vJ16xZ4Gom2RHf9xfg")
