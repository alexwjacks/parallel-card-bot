# parallel-card-bot

This is an unofficial Discord bot for fetching cards from the upcoming card game Parallel.

Learn more at:
* Website: https://parallel.life/
* Twitter: https://twitter.com/ParallelNFT
* The Discord server: https://discord.gg/Ux62xbpTYQ

# Dependencies
The following py packages are required:

## bot.py (the Discord bot)
* [discord.py](https://pypi.org/project/discord.py/)
* [dotenv](https://pypi.org/project/dotenv/)
* [fuzzywuzzy](https://pypi.org/project/fuzzywuzzy/)
  * [python-Levenshtein](https://pypi.org/project/python-Levenshtein/)
    * This is optional, but provides a 4-10x perf enhancement
    * This may also require platform-dependent C++ tooling. It will tell you during installation.

## spider.py (a web scraper for acquiring card data)
* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

# TODO
* Change data representation into one dict of {faction1: [cards, paragons], faction2: [cards, paragons], etc} so that we can do `data.faction.cards`, for example
* Attach pictures of the cards
* Fuzzy matching

# Known Issues
* Plenty of revealed cards still missing

