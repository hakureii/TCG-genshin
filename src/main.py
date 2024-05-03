import random, discord, asyncio, os
from head import getAsset, getAssetList, getColor, getToken, getIntents, resizeImage, getColor
from discord.ext.commands import Bot

bot = Bot(["!"], intents=getIntents())

@bot.event
async def on_ready():
    await asyncio.sleep(5*60*60)
    os.remove(os.environ["CONDITION"])
    await bot.close()

@bot.command(name="refresh")
async def refresh(ctx):
    await ctx.send("rebooting")
    await bot.close()

@bot.command(name="pull")
async def pull(ctx):
    card_type = "Character Cards"
    assetList = getAssetList()
    pulled = random.choice(list(assetList[card_type].keys()))
    resizedImage = resizeImage(getAsset(assetList[card_type][pulled]))
    filename = assetList[card_type][pulled].replace(card_type + "/", "")
    embed = discord.Embed(title=pulled, color=getColor("diamond"))
    embed.set_image(url=f"attachment://{filename}")
    await ctx.send(embed=embed, file=discord.File(resizedImage, filename=filename))

bot.run(getToken())
