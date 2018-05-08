import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os

class Insults:
    """Nevvy Insults Cog"""
    def __init__(self, bot):
        self.bot = bot
        self.insults = fileIO("data/insults/insults.json","load")
        self.angery = fileIO("data/insults/angry.json","load")

    @commands.command(aliases=['insult'], pass_context=True, no_pm=True)
    async def szkaluj(self, ctx, user : discord.Member=None):
        """Insults the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Hmm, why do you want this?\nhttps://imgur.com/ZeRe5GD")
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("(╯°□°）╯︵ ┻━┻\n{}".format(randchoice(self.angery)))
            else:
                await self.bot.say(":mega: **{}** {}".format(user.display_name, randchoice(self.insults)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
		
def setup(bot):
    bot.add_cog(Insults(bot))