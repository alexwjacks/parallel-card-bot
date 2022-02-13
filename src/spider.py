# Spider.py scrapes the Parallel.Life website cards list
# and generates spider.json from the data it finds there
import sys
import requests
import json
from bs4 import BeautifulSoup

# constants
DEFAULT_OUTPUT_PATH = 'resources/spider.json'
BASE_URL = "https://parallel.life"
URL = BASE_URL + "/cards/"

# usage
def print_usage():
  print("Usage:")
  print("python spider.py [output]")
  print(f"    output:  optional. The path to the desired output file. Default: {DEFAULT_OUTPUT_PATH}")

# process command-line arguments

# see if help was requested
for arg in sys.argv:
  if arg == '/?' or arg.lower() == '/help':
    print_usage()
    exit()

outputFile = ""

if len(sys.argv) > 1:
  outputFile = sys.argv[1]
else:
  outputFile = DEFAULT_OUTPUT_PATH

print("Output will be written to:", outputFile)

# do the work
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

cardLinks = soup.find_all("a", class_=lambda c: "card" in c)

cards = []

for card in cardLinks:
  c = {}

  # a string like 'Ashes to Ashes rare shroud collectible_card'
  id = card.attrs['id'].lower()

  # a string like 'shroud'
  faction = card.attrs['data-faction']

  # a string like 'collectible_card'
  type = card.attrs['data-cardtype']

  c['Parallel'] = faction.capitalize()
  c['URL'] = BASE_URL + card['href']

  print(f"Requesting {c['URL']} ...")

  cardPage = requests.get(c['URL'])
  cardSoup = BeautifulSoup(cardPage.content, "html.parser")

  #<meta content="Ashes To Ashes" name="title"/>
  cardName = cardSoup.find('meta', attrs={'name' : 'title'})
  c['Card Name'] = cardName['content']

  c['Rarity'] = id.replace(c['Card Name'].lower(), "") \
                  .replace(faction, "") \
                  .replace(type, "") \
                  .strip() \
                  .capitalize()

  #<meta content="What we become, is what we came from." name="description"/>
  cardDescription = cardSoup.find('meta', attrs={'name' : 'description'})
  c['Description'] = cardDescription['content']

  # {
  #   "Card Name": "Trigger-Happy Trooper",
  #   "Parallel": "Marcolian",
  #   "Rarity": "Uncommon",
  #   "Type": "Unit",
  #   "Function": "When this Unit attacks, deal 1 damage to both players."
  # },

  cards.append(c)
  print(c)

print (f"Writing output to {outputFile}")

with open(outputFile, 'w', encoding='utf-8') as f:
  json.dump(cards, f, ensure_ascii=False, indent=2)

