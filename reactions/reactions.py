import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from random import choice as randchoice
import os

class Reactions:
    """Nevvy Reactions COG"""
    def __init__(self, bot):
        self.bot = bot
        self.angery = fileIO("data/reactions/angery.json","load")
        self.hugs = fileIO("data/reactions/hugs.json","load")
        self.pats = fileIO("data/reactions/pats.json","load")
        self.kisses = fileIO("data/reactions/kisses.json","load")
        self.pokes = fileIO("data/reactions/pokes.json","load")
        self.slaps = fileIO("data/reactions/slaps.json","load")
        self.bites = fileIO("data/reactions/bites.json","load")
        self.tickles = fileIO("data/reactions/tickles.json","load")
        self.highfives = fileIO("data/reactions/highfives.json","load")
        self.pouts = fileIO("data/reactions/pouts.json","load")
        self.tehees = fileIO("data/reactions/tehees.json","load")
        self.smiles = fileIO("data/reactions/smiles.json","load")
        self.stares = fileIO("data/reactions/stares.json","load")
        self.holdhands = fileIO("data/reactions/holdhands.json","load")
        self.cuddles = fileIO("data/reactions/cuddles.json","load")
        self.greetings = fileIO("data/reactions/greetings.json","load")
        self.tsunderes = fileIO("data/reactions/tsundere.json","load")
        self.nuzzles = fileIO("data/reactions/nuzzle.json","load")
        self.bloodsucks = fileIO("data/reactions/bloodsuck.json","load")
        self.lewds = fileIO("data/reactions/lewd.json","load")
        self.meows = fileIO("data/reactions/meow.json","load")
        self.noms = fileIO("data/reactions/nom.json","load")
        self.facedesks = fileIO("data/reactions/facedesk.json","load")
		
    @commands.command(pass_context=True, no_pm=True)
    async def hug(self, ctx, user : discord.Member=None):
        """Hugs the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Aww, I see you are lonely, take a hug <3\n{}".format(randchoice(self.hugs)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*blushes*` O-Oh... Thanks\n{}".format(randchoice(self.hugs)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been hugged by **{}**\n{}".format(user, ctx.message.author, randchoice(self.hugs)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def pat(self, ctx, user : discord.Member=None):
        """Pats the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Aww, I see you are lonely, take a pat <3\n{}".format(randchoice(self.pats)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*is patted*` (´･ω･`)\n{}".format(randchoice(self.pats)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been patted by **{}**\n{}".format(user, ctx.message.author, randchoice(self.pats)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def kiss(self, ctx, user : discord.Member=None):
        """Kisses the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Aww, I see you are lonely, take a kiss **kisses**\n{}".format(randchoice(self.kisses)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*blushes*` I - uh... don't think you should be kissing a bot but...\n{}".format(randchoice(self.kisses)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been kissed by **{}**\n{}".format(user, ctx.message.author, randchoice(self.kisses)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def poke(self, ctx, user : discord.Member=None):
        """Pokes the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Aww, I see you are lonely, **pokes you**\n{}".format(randchoice(self.pokes)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("O-Ohh, What do you need? ( ͡° ͜ʖ ͡°)\n{}".format(randchoice(self.pokes)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been poked by **{}** :eyes:\n{}".format(user, ctx.message.author, randchoice(self.pokes)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def slap(self, ctx, user : discord.Member=None):
        """Slaps the specified user"""
        if user == ctx.message.author:
            await self.bot.say("Hmm, why do you want this? Uh, I guess... **slaps you**\nhttps://imgur.com/ZeRe5GD")
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("(╯°□°）╯︵ ┻━┻\n{}".format(randchoice(self.angery)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been slapped by **{}** :eyes:\n{}".format(user, ctx.message.author, randchoice(self.slaps)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def bite(self, ctx, user : discord.Member=None):
        """Bites the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*bites you*`\n{}".format(randchoice(self.bites)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("T-That hurts! (╥_╥)\n{}".format(randchoice(self.bites)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been bitten by **{}** :eyes:\n{}".format(user, ctx.message.author, randchoice(self.bites)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def tickle(self, ctx, user : discord.Member=None):
        """Tickles the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*tickles you*`\n{}".format(randchoice(self.tickles)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Hahahaha... Oh god staph （＾ｖ＾）\n{}".format(randchoice(self.tickles)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been tickled by **{}**\n{}".format(user, ctx.message.author, randchoice(self.tickles)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def highfive(self, ctx, user : discord.Member=None):
        """Highfives with the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*highfives*`\n{}".format(randchoice(self.highfives)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*highfives*`\n{}".format(randchoice(self.highfives)))
            else:
                await self.bot.say(":speech_balloon: **{}** highfives **{}** :heart:\n{}".format(ctx.message.author, user, randchoice(self.highfives)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def pout(self, ctx, user : discord.Member=None):
        """Pouts at the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*pouts, hmph*`\n{}".format(randchoice(self.pouts)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Are you mad at me (;﹏;)?\n{}".format(randchoice(self.pouts)))
            else:
                await self.bot.say(":speech_balloon: **{}** pouts at **{}** `*hmph*`\n{}".format(ctx.message.author, user, randchoice(self.pouts)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def tehee(self, ctx, user : discord.Member=None):
        """Teehee~"""
        if user == ctx.message.author:
            await self.bot.say("`*teases you*`\n{}".format(randchoice(self.tehees)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)\n{}".format(randchoice(self.tehees)))
            else:
                await self.bot.say(":speech_balloon: **{}** is teasing **{}**\n{}".format(ctx.message.author, user, randchoice(self.tehees)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def smile(self, ctx, user : discord.Member=None):
        """Smiles at someone"""
        if user == ctx.message.author:
            await self.bot.say("`*smiles at you*`\n{}".format(randchoice(self.smiles)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Aww :3\n{}".format(randchoice(self.smiles)))
            else:
                await self.bot.say(":speech_balloon: **{}** is smiling at **{}** :heart:\n{}".format(ctx.message.author, user, randchoice(self.smiles)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def stare(self, ctx, user : discord.Member=None):
        """Stares at someone"""
        if user == ctx.message.author:
            await self.bot.say("`*stares you*`\n{}".format(randchoice(self.stares)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴\n{}".format(randchoice(self.stares)))
            else:
                await self.bot.say(":speech_balloon: **{}** is staring at **{}** :eyes:\n{}".format(ctx.message.author, user, randchoice(self.stares)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def holdhand(self, ctx, user : discord.Member=None):
        """Hold someone's hands"""
        if user == ctx.message.author:
            await self.bot.say("`*holds your hand*`\n{}".format(randchoice(self.holdhands)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("O-oh! ( *v* )\n{}".format(randchoice(self.holdhands)))
            else:
                await self.bot.say(":speech_balloon: **{}** is holding **{}** hand\n{}".format(ctx.message.author, user, randchoice(self.holdhands)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def cuddle(self, ctx, user : discord.Member=None):
        """Cuddles someone"""
        if user == ctx.message.author:
            await self.bot.say("`*cuddles you*`\n{}".format(randchoice(self.cuddles)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("That's cute! ʕ ￫ᴥ￩ʔ\n{}".format(randchoice(self.cuddles)))
            else:
                await self.bot.say(":speech_balloon: **{}** you have been cuddled by **{}**\n{}".format(user, ctx.message.author, randchoice(self.cuddles)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def greet(self, ctx, user : discord.Member=None):
        """Sends a random greeting"""
        if user == ctx.message.author:
            await self.bot.say(":speech_balloon: {}".format(randchoice(self.greetings)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say(":speech_balloon: {}".format(randchoice(self.greetings)))
            else:
                await self.bot.say(":speech_balloon: {}".format(randchoice(self.greetings)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def tsundere(self, ctx, user : discord.Member=None):
        """Y-You baka!"""
        if user == ctx.message.author:
            await self.bot.say(":mega: {}".format(randchoice(self.tsunderes)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say(":mega: {}".format(randchoice(self.tsunderes)))
            else:
                await self.bot.say(":mega: {}".format(randchoice(self.tsunderes)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def nuzzle(self, ctx, user : discord.Member=None):
        """Nuzzles the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*nuzzles you*`\n{}".format(randchoice(self.nuzzles)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Aww, cute! ⊂(・(ェ)・)⊃\n{}".format(randchoice(self.nuzzles)))
            else:
                await self.bot.say(":speech_balloon: **{}** is nuzzling **{}**\n{}".format(ctx.message.author, user, randchoice(self.nuzzles)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def bloodsuck(self, ctx, user : discord.Member=None):
        """Sucks the blood of an user"""
        if user == ctx.message.author:
            await self.bot.say("J-Just how am I meant to? Oh well.. `*sucks your blood*`\n{}".format(randchoice(self.bloodsucks)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Are you a vampire now?, Oh!\n{}".format(randchoice(self.bloodsucks)))
            else:
                await self.bot.say(":speech_balloon: **{}** is sucking the blood of **{}**\n{}".format(ctx.message.author, user, randchoice(self.bloodsucks)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def lewd(self, ctx, user : discord.Member=None):
        """T-Too lewd!"""
        if user == ctx.message.author:
            await self.bot.say("Y-You lewdie!\n{}".format(randchoice(self.lewds)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("Y-You lewdie!\n{}".format(randchoice(self.lewds)))
            else:
                await self.bot.say("Y-You lewdie!\n{}".format(randchoice(self.lewds)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def meow(self, ctx, user : discord.Member=None):
        """Meows at the specified user"""
        if user == ctx.message.author:
            await self.bot.say("`*Meow*`\n{}".format(randchoice(self.meows)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*Meow*`\n{}".format(randchoice(self.meows)))
            else:
                await self.bot.say("`*Meow*`\n{}".format(randchoice(self.meows)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def nom(self, ctx, user : discord.Member=None):
        """*nom nom*"""
        if user == ctx.message.author:
            await self.bot.say("`*Yummy*`\n{}".format(randchoice(self.noms)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("`*Yummy*`\n{}".format(randchoice(self.noms)))
            else:
                await self.bot.say("`*Yummy*`\n{}".format(randchoice(self.noms)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
    @commands.command(pass_context=True, no_pm=True)
    async def facedesk(self, ctx, user : discord.Member=None):
        """When it's just too much to handle"""
        if user == ctx.message.author:
            await self.bot.say("¯\_(ツ)_/¯\n{}".format(randchoice(self.facedesks)))
            return 
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say("¯\_(ツ)_/¯\n{}".format(randchoice(self.facedesks)))
            else:
                await self.bot.say("¯\_(ツ)_/¯\n{}".format(randchoice(self.facedesks)))
        else:
            await self.bot.say(":heavy_multiplication_x: You need to mention a user")
			
def setup(bot):
    bot.add_cog(Reactions(bot))