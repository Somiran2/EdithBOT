import discord
from discord.ext import commands

class badwords(commands.Cog):
    def __init__(self, bot):
        self.bot = bot     
      

    @commands.Cog.listener()
    async def on_message(self,ctx):
        keywords = [
        "abortion",
        "anal",
        "anus",
        "arse",
        "ass",
        "ass-fucker",
        "asses",
        "asshole",
        "assholes",
        "ballbag",
        "balls",
        "bastard",
        "bellend",
        "bestial",
        "bestiality",
        "bitch",
        "bitches",
        "bitching",
        "bloody",
        "blowjob",
        "bollok",
        "boob",
        "boobs",
        "breasts",
        "buceta",
        "bum",
        "butt",
        "carpet muncher",
        "chink",
        "cipa",
        "clitoris",
        "cock",
        "cock-sucker",
        "cocks",
        "coon",
        "crap",
        "cum",
        "cumshot",
        "cunillingus",
        "cunt",
        "damn",
        "dick",
        "dildo",
        "dildos",
        "dink",
        "dog-fucker",
        "duche",
        "dyke",
        "ejaculate",
        "ejaculated",
        "ejaculates",
        "ejaculating",
        "ejaculation",
        "fag",
        "fagging",
        "faggot",
        "fagot",
        "fagots",
        "fanny",
        "felching",
        "fellatio",
        "flange",
        "fuck",
        "fucked",
        "fucker",
        "fuckers",
        "fucking",
        "fuckings",
        "fucks",
        "fudge packer",
        "god-damned",
        "goddamn",
        "hell",
        "hore",
        "horny",
        "jerk-off",
        "kock",
        "labia",
        "lust",
        "lusting",
        "masochist",
        "masturbate",
        "mother fucker",
        "nazi",
        "nigga",
        "nigger",
        "niggers",
        "orgasim",
        "orgasm",
        "orgasms",
        "pecker",
        "penis",
        "piss",
        "pissed",
        "pisser",
        "pisses",
        "pissing",
        "pissoff",
        "poop",
        "porn",
        "porno",
        "pornography",
        "prick",
        "pricks",
        "pube",
        "pussies",
        "pussy",
        "rape",
        "rapist",
        "rectum",
        "retard",
        "rimming",
        "sadist",
        "screwing",
        "scrotum",
        "semen",
        "sex",
        "shag",
        "shagging",
        "shemale",
        "shit",
        "shite",
        "shits",
        "shitted",
        "shitting",
        "shitty",
        "skank",
        "slut",
        "sluts",
        "smegma",
        "smut",
        "snatch",
        "son-of-a-bitch",
        "spac",
        "spunk",
        "testicle",
        "tit",
        "tits",
        "titt",
        "turd",
        "vagina",
        "viagra",
        "vulva",
        "wang",
        "wank",
        "whore",
        "x rated",
        "xxx"]
        for i in range(len(keywords)):
            msg = ctx.content
            if keywords[i] in msg.lower():
                await ctx.channel.purge(limit=1)
        


def setup(bot):
  bot.add_cog(badwords(bot))