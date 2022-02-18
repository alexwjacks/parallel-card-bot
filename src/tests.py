from data import *
import util
import json
from Card import Card
from CardEditions import CardEditions

# card tests
card_json = """{
  "Name": "Pocket Dimension",
  "Parallel": "Shroud",
  "Editions": {
    "Concept_art": {
      "01": "https://parallel.life/cards/84",
      "02": "https://parallel.life/cards/83"
    },
    "Collectible_card": {
      "Day": "https://parallel.life/cards/pocket-dimension",
      "Night": "https://parallel.life/cards/pocket-dimension-2"
    },
    "Se": {
      "Day": "https://parallel.life/cards/pocket-dimension-se",
      "Night": "https://parallel.life/cards/pocket-dimension-se-2"
    },
    "Masterpiece": "https://parallel.life/cards/188"
  },
  "Rarity": "Rare",
  "Description": "They say its bark is so hard as to be nearly indestructible. It has stood here for thousands of years and will continue to for thousands more. Let it be a beacon for all those who stand for earth.",
  "Function": "At the Start of your turn, Create a 0/1 Defender. Intel: 3 Create a 2/1 Defender instead (Intel: X: X Enemy Bank Cards must be revealed)",
  "Type": "Relic",
  "Artist": "Oscar Mar"
}"""

data = json.loads(card_json)
card = Card(data)
#print(card)

card_json = """{
  "Name": "Cytokinesis",
  "Parallel": "Kathari",
  "Editions": {
    "Collectible_card": "https://parallel.life/cards/cytokinesis",
    "Se": "https://parallel.life/cards/cytokinesis-se",
    "Masterpiece": "https://parallel.life/cards/masterpiece-cytokinesis"
  },
  "Rarity": "Rare",
  "Description": "Imitation is flattery, but reproducing perfection is divine.",
  "Function": "At the Start of your turn, Create a 0/1 Defender. Intel: 3 Create a 2/1 Defender instead (Intel: X: X Enemy Bank Cards must be revealed)",
  "Type": "Relic",
  "Artist": "Oscar Mar"
}"""

data = json.loads(card_json)
card = Card(data)
#print(card)


print(list(filter(None, set([c.Artist for c in cards.values()]))))

# util.find_card("Archivist's Pride", data.cards)
# util.find_card("Archivist’s Pride", data.cards)
# util.find_card("Archivist", data.cards)
# util.find_card("Archive", data.cards)
# util.find_card("arkivist", data.cards)
# util.find_card("pride", data.cards)
# util.find_card("A P", data.cards)
# util.find_card("soleia disciple of gaffar", data.cards)
# util.find_card("soleea disciple gaffer", data.cards)
# util.find_card("soleia gaffer", data.cards)
# util.find_card("gaffar", data.cards)
# util.find_card("...", data.cards)

# # paragon tests
# util.find_paragon("skippius", data.paragons)
# util.find_paragon("aetio", data.paragons)
# util.find_paragon("atio", data.paragons)

