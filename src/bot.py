# bot.py
import os
from tkinter import N
from data import *
import util
from discord.ext import commands
from time import strftime
from dotenv import load_dotenv
import discord

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

@bot.command(name="card", help="Look up a card by name")
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

@bot.command(name="credits", help="New phone, who dis?")
async def give_credit(ctx, *args):
    credits = f"Lazergician made this bot all by himself with no help whatsoever,"
    credits += f" especially not by Deuce or that lazybones JERisBRISK."
    await ctx.send(credits)

@bot.command(name="disclaimer", help="Things are subject to change")
async def disclaim(ctx, *args):
    disclaimer = "Certain things spoken about in chat by team members are subject to change as this game and drops are in progress and in active development."
    await ctx.send(disclaimer)

@bot.command(name="echo", help="Test for echo")
async def test_for_echo(ctx, *args):
    required_role = discord.utils.get(ctx.guild.roles, name='Mad Scientist')
    authorized = required_role in ctx.author.roles
    if not authorized:
        print(f"echo: {ctx.author} attempted to use this command without the required role: {required_role}")
        return

    message = ' '.join(args)
    if not message:
        message = "You gotta give me something to work with, buddy."

    await ctx.send(message)

@bot.command(name="source", help="Visit the sausage factory")
async def source(ctx, *args):
    message = f"If you really want to see how the sausage is made, visit <https://github.com/alexwjacks/parallel-card-bot>"
    await ctx.send(message)

@bot.command(name="paragon", help="Look up a Paragon by name")
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

@bot.command(name="site", help="Get a link to the card")
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

@bot.command(name="random-card", help="Optionally provide a Parallel, Card Type, or Rarity")
async def random_card(ctx, *args):
    response = ""

    if len(args) == 0:
        response = util.format_random_card_from_list(cards)
    else:
        keyword = ' '.join(args).strip()

        list = cards_by_keyword.get(keyword.lower(), None)

        if not list:
            artistName = util.find_artist(keyword, cards_by_artist.keys())
            if artistName:
                list = cards_by_artist.get(artistName, None)

        if list:
            response = util.format_random_card_from_list(list)
        else:
            response = "\nUsage: `!random-card [keyword]` where the optional `keyword` is one of:"
            artists = filter(None, cards_by_artist.keys())
            response += "\n  Artists:" + '  '.join([f"`{a}`" for a in artists])
            response += "\n  Parallels: `" + ' '.join([p.name.lower() for p in Parallels if p.name.lower() != 'unknown']) + '`'
            response += "\n  Card Types: `" + ' '.join([t.name.lower() for t in CardTypes if t.name.lower() != 'unknown']) + '`'
            response += "\n  Card Rarities: `" + ' '.join([r.name.lower() for r in CardRarities if r.name.lower() != 'unknown']) + '`'

    await ctx.send(response)

@bot.command(name="list-paragons", help="List a Parallel's Paragons")
async def list_paragons(ctx, *args):
    if len(args) == 0:
        # list all the paragons without their details
        list = sorted([f"{util.emoji_by_parallel.get(v.Parallel)} {v.Name}" for k, v in paragons.items()])
        print(list)
        response = '\n'.join(list)
    else:
        keyword = args[0].strip().lower()
        list = paragons_by_keyword.get(keyword, None)

        if list:
            response = util.format_multiple_paragons(list)
        else:
            response = "\nUsage: `!list-paragons [keyword]` where the optional `paragon` is a Parallel:"
            response += "\n  Parallels: `" + ' '.join([p.name.lower() for p in Parallels if p.name.lower() != 'unknown']) + '`'
    
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
