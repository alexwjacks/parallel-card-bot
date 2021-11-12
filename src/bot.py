# bot.py
import os
from discord.ext import commands
import json
from time import strftime
import util
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

card_names = []
cards = {}
with open('resources/cards.json', ) as fd:
    data = json.load(fd)
    for card in data:
        card_name = card[util.card_name_index].lower()
        card_names.append(card_name)
        cards[card_name] = card

paragon_names = []
paragons = {}
with open('resources/paragons.json', ) as fd:
    data = json.load(fd)
    for paragon in data:
        paragon_name = paragon[util.paragon_name_index].lower()
        paragon_names.append(paragon_name)
        paragons[paragon_name] = paragon

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
