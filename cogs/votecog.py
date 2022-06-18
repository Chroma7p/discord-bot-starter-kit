from discord.ext import commands

#votecogクラス
class VoteCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    #コマンドの記述
    @commands.command()
    async def chkcog(self,ctx):
        await ctx.send("using cog!")

#Cogとして使うのに必要なsetup関数
def setup(bot):
    print("checkcog OK")
    return bot.add_cog(VoteCog(bot))