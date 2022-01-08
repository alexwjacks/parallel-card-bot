# bot.py
import os

from discord.ext import commands
import json
from time import strftime
import util
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

PARALLELS = ["earthen", "shroud", "augencore", "kathari", "marcolian", "universal"]
TYPES = ["unit", "effect", "relic", "upgrade"]

# precompute all these organizational lists on start up
earthen_cards = {}
kathari_cards = {}
marcolian_cards = {}
augencore_cards = {}
shroud_cards = {}
universal_cards = {}
units = {}
relics = {}
effects = {}
upgrades = {}
card_names = []
cards = {}
with open('resources/cards.json', ) as cards_file:
    data = json.load(cards_file)
    for card in data:
        card_name = card[util.card_name_index].lower()
        # add to generic card lists
        card_names.append(card_name)
        cards[card_name] = card

        # add to parallel specific list
        if card["Parallel"] == "Kathari":
            kathari_cards[card_name] = card
        elif card["Parallel"] == "Marcolian":
            marcolian_cards[card_name] = card
        elif card["Parallel"] == "Earthen":
            earthen_cards[card_name] = card
        elif card["Parallel"] == "Shroud":
            shroud_cards[card_name] = card
        elif card["Parallel"] == "Augencore":
            augencore_cards[card_name] = card
        elif card["Parallel"] == "Universal":
            universal_cards[card_name] = card
        else:
            print(f"Card % didn't match any Parallel", card)

        # add to card type list
        if card["Type"] == "Relic":
            relics[card_name] = card
        elif card["Type"] == "Unit":
            units[card_name] = card
        elif card["Type"] == "Effect":
            effects[card_name] = card
        elif card["Type"] == "Upgrade":
            upgrades[card_name] = card
        else:
            print(f"Card % didn't match any card type", card)

# and do the same for the paragons
earthen_paragons = {}
kathari_paragons = {}
marcolian_paragons = {}
augencore_paragons = {}
shroud_paragons = {}
paragon_names = []
paragons = {}
with open('resources/paragons.json', ) as paragons_file:
    data = json.load(paragons_file)
    for paragon in data:
        paragon_name = paragon[util.paragon_name_index].lower()
        paragon_names.append(paragon_name)
        paragons[paragon_name] = paragon
        if paragon["Parallel"] == "Kathari":
            kathari_paragons[paragon_name] = paragon
        elif paragon["Parallel"] == "Marcolian":
            marcolian_paragons[paragon_name] = paragon
        elif paragon["Parallel"] == "Earthen":
            earthen_paragons[paragon_name] = paragon
        elif paragon["Parallel"] == "Shroud":
            shroud_paragons[paragon_name] = paragon
        elif paragon["Parallel"] == "Augencore":
            augencore_paragons[paragon_name] = paragon
        else:
            print(f"Paragon % didn't match any Parallel", paragon)

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
    name = arg.lower()
    if name not in card_names:
        response = f"Sorry, I don't know the card {arg}"
    else:
        response = util.format_card(cards[name])
    await ctx.send(response)


@bot.command(name="paragon", help="Look up a Paragon. Use quotes for Paragon names with multiple words.")
async def paragon(ctx, arg):
    name = arg.lower()
    if name not in paragon_names:
        response = "fSorry, I don't know the Paragon {arg}."
    else:
        response = util.format_paragon(paragons[name])
    await ctx.send(response)


@bot.command(name="site", help="Look up a card on parallel.life. Use quotes for card names with multiple words.")
async def site(ctx, arg):
    name = arg.lower()
    if name not in card_names:
        response = f"Sorry, I don't know the card {arg}"
    else:
        response = f"https://parallel.life/cards/{util.hyphenate_card_name(name)}"
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
            print(f"Arg % didn't match any Parallel", arg)
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
