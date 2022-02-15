import json
import util

# load the cards

# parallels
earthen_cards = {}
kathari_cards = {}
marcolian_cards = {}
augencore_cards = {}
shroud_cards = {}
universal_cards = {}

# types
units = {}
relics = {}
effects = {}
upgrades = {}

# rarities
rarities = {
  "common": {},
  "uncommon": {},
  "rare": {},
  "legendary": {},
  "prime": {},
}

# general
card_names = []
cards = {}

with open('resources/cards.json', encoding='utf8') as cards_file:
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
            print(f"Card '{card[util.card_name_index]}' with Parallel '{card[util.parallel_index]}' didn't match any Parallel")

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
            print(f"Card '{card[util.card_name_index]}' with Type '{card[util.type_index]}' didn't match any card type")

        # add to card rarity list
        rarity_set = rarities.get(card[util.rarity_index].lower())
        if not rarity_set == None:
          rarity_set[card_name] = card
        else:
          print(f"Card '{card[util.card_name_index]}' with Rarity '{card[util.rarity_index]}' didn't match any card rarity")

# load the paragons

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

