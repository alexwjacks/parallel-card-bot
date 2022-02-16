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

@bot.command(name="card", help="Look up a card by name.")
async def card(ctx, *args):
    name = ' '.join(args).strip()

    if not name:
        response = f"Please give me something to work with. Usage: `!card name`"
    else:
        card = util.find_card(name, cards)

        if not card:
            response = f"Sorry, I couldn't find a card that even slightly resembled '{name}'"
        else:
            response = util.format_card(card)

    await ctx.send(response)

@bot.command(name="paragon", help="Look up a Paragon by name.")
async def paragon(ctx, *args):
    name = ' '.join(args).strip()

    if not name:
        response = f"Please give me something to work with. Usage: `!paragon name`"
    else:
        paragon = util.find_paragon(name, paragons)

        if not paragon:
            response = f"Sorry, I couldn't find a paragon that even slightly resembled '{name}'"
        else:
            response = util.format_paragon(paragon)

    await ctx.send(response)

@bot.command(name="site", help="Get a link to the card on the parallel website.")
async def site(ctx, *args):
    name = ' '.join(args).strip()

    if not name:
        response = f"Sorry, I couldn't find a card that even slightly resembled '{name}' in my data banks."
        response += "Try searching for it on https://parallel.life/cards/"
    else:
        card = util.find_card(name, cards)

        if not card:
            response = f"Sorry, I couldn't find a card that even slightly resembled '{name}'"
        else:
            response = util.get_card_url(card)

    await ctx.send(response)

@bot.command(name="random-card", help="Get a random card. Optionally specify a Parallel, Card Type, or Rarity.")
async def random_card(ctx, *args):
    response = ""

    if len(args) == 0:
        response = util.format_random_card_from_list(cards)
    else:
        keyword = args[0].strip().lower()
        switch = {
            # parallels
            "kathari": kathari_cards,
            "marcolian": marcolian_cards,
            "earthen" : earthen_cards,
            "shroud" : shroud_cards,
            "augencore" : augencore_cards,
            "universal" : universal_cards,
            # types
            "unit" : units,
            "effect" : effects,
            "relic" : relics,
            "upgrade" : upgrades,
            # rarities
            "common" : rarities[util.common_index],
            "uncommon" : rarities[util.uncommon_index],            
            "rare" : rarities[util.rare_index],            
            "legendary" : rarities[util.legendary_index],            
            "prime" : rarities[util.prime_index],            
        }

        list = switch.get(keyword, None)

        if list:
            response = util.format_random_card_from_list(list)
        else:
            response = "\nUsage: `!random-card [keyword]` where the optional `keyword` is a Parallel, Card Type, or Rarity:"
            response += "\n  Parallels: `" + ' '.join(PARALLELS) + '`'
            response += "\n  Card Types: `" + ' '.join(TYPES) + '`'
            response += "\n  Card Rarities: `" + ' '.join(rarities.keys()) + '`'

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
