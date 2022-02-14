# bot.py
import os
from data import *
import util
from discord.ext import commands
from time import strftime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

PARALLELS = ["earthen", "shroud", "augencore", "kathari", "marcolian", "universal"]
TYPES = ["unit", "effect", "relic", "upgrade"]

bot = commands.Bot("!", case_insensitive=True)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print("guilds are " + str(bot.guilds))
    for guild in bot.guilds:
        print(f'{bot.user} is connected to the following guild:\n'
              f'{guild.name}(id: {guild.id})')

@bot.command(name="card", help="Look up a card. Use quotes for card names with multiple words.")
async def card(ctx, arg):
    card = util.find_card(arg, cards)

    if not card:
        response = f"Sorry, I don't know the card {arg}"
    else:
        response = util.format_card(card)
    await ctx.send(response)

@bot.command(name="paragon", help="Look up a Paragon. Use quotes for Paragon names with multiple words.")
async def paragon(ctx, arg):
    paragon = util.find_paragon(arg, paragons)

    if not paragon:
        response = f"Sorry, I don't know the Paragon {arg}."
    else:
        response = util.format_paragon(paragon)
    await ctx.send(response)

@bot.command(name="site", help="Look up a card on parallel.life. Use quotes for card names with multiple words.")
async def site(ctx, arg):
    card = util.find_card(arg, cards)

    if not card:
        response = f"Sorry, I don't know the card {arg}"
    else:
        response = util.get_card_url(card)
    await ctx.send(response)

@bot.command(name="random-card", help="Get a random card. Can specify a Parallel or card type.")
async def random_card(ctx, arg):
    response = ""
    keyword = arg.lower()
    if keyword not in PARALLELS and keyword not in TYPES:
        response = "I don't know that keyword."
    else:
        if keyword == "kathari":
            response = util.format_random_card_from_list(kathari_cards)
        elif keyword == "marcolian":
            response = util.format_random_card_from_list(marcolian_cards)
        elif keyword == "earthen":
            response = util.format_random_card_from_list(earthen_cards)
        elif keyword == "shroud":
            response = util.format_random_card_from_list(shroud_cards)
        elif keyword == "augencore":
            response = util.format_random_card_from_list(augencore_cards)
        elif keyword == "universal":
            response = util.format_random_card_from_list(universal_cards)
        elif keyword == "unit":
            response = util.format_random_card_from_list(units)
        elif keyword == "effect":
            response = util.format_random_card_from_list(effects)
        elif keyword == "relic":
            response = util.format_random_card_from_list(relics)
        elif keyword == "upgrade":
            response = util.format_random_card_from_list(upgrades)
        else:
            # if we get here something went real wonky
            print(f"Arg {arg} didn't match any Parallel")
    await ctx.send(response)

@bot.command(name="list-paragons", help="List the Paragons for a given Parallel.")
async def list_paragons(ctx, arg):
    faction = arg.lower()
    response = ""
    if faction not in PARALLELS:
        response = f"Sorry, I don't know the faction {arg}"
    else:
        if faction == "kathari":
            response = util.format_multiple_paragons(kathari_paragons)
        elif faction == "marcolian":
            response = util.format_multiple_paragons(marcolian_paragons)
        elif faction == "earthen":
            response = util.format_multiple_paragons(earthen_paragons)
        elif faction == "shroud":
            response = util.format_multiple_paragons(shroud_paragons)
        elif faction == "augencore":
            response = util.format_multiple_paragons(augencore_paragons)
    await ctx.send(response)

@bot.event
# args and kwargs are the positional and keyword args from the original event handler that errored
async def on_error(event_method, *args, **kwargs):
    with open("resources/error.log", 'a') as f:
        if event_method == 'on_message':
            current_time = strftime("%Y-%m-%d %H:%M:%S")
            f.write(f'Unhandled message on {current_time}: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)
