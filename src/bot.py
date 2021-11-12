# bot.py

from discord.ext import commands
import json
from time import strftime
import util

# from dotenv import load_dotenv

# load_dotenv()

TOKEN = "FIXME WITH YOUR TOKEN"

card_names = []
cards = {}
with open('resources/cards.json', ) as fd:
    data = json.load(fd)
    for card in data:
        card_name = card[util.card_name_index].lower()
        card_names.append(card_name)
        cards[card_name] = card

bot = commands.Bot("!", case_insensitive=True)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print("guilds are " + str(bot.guilds))
    for guild in bot.guilds:
        print(f'{bot.user} is connected to the following guild:\n'
              f'{guild.name}(id: {guild.id})')


@bot.command(name="card")
async def card(ctx, arg):
    try:
        lookup = cards[arg.lower()]
        response = util.format_card(lookup)
    except KeyError:
        response = "Sorry, I don't know that card."
    await ctx.send(response)


@bot.command(name="site")
async def site(ctx, arg):
    name = util.hyphenate_card_name(arg)
    response = f"https://parallel.life/cards/{name}"
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
