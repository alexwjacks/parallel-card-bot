import os
from imp import load_dynamic
import json
import util
from Card import Card
from CardTypes import CardTypes
from CardRarities import CardRarities
from Paragon import Paragon
from Parallels import Parallels
from dotenv import load_dotenv

load_dotenv()

# load the cards

# general
cards = {}

## indexes
cards_by_parallel = {
    Parallels.Augencore : {},
    Parallels.Earthen : {},
    Parallels.Kathari : {},
    Parallels.Marcolian : {},
    Parallels.Shroud : {},
    Parallels.Universal : {},
    Parallels.UnknownOrigins : {},
}

cards_by_type = {
    CardTypes.Effect : {},
    CardTypes.Keyframing : {},
    CardTypes.Relic : {},
    CardTypes.Unit : {},
    CardTypes.Upgrade : {},
}

cards_by_rarity = {
    CardRarities.Common: {},
    CardRarities.Uncommon: {},
    CardRarities.Rare: {},
    CardRarities.Legendary: {},
    CardRarities.Prime: {},
}

cards_by_artist = {}

cards_by_keyword = {
    # parallels
    "augencore" : cards_by_parallel[Parallels.Augencore],
    "earthen" : cards_by_parallel[Parallels.Earthen],
    "kathari": cards_by_parallel[Parallels.Kathari],
    "marcolian": cards_by_parallel[Parallels.Marcolian],
    "shroud" : cards_by_parallel[Parallels.Shroud],
    "universal" : cards_by_parallel[Parallels.Universal],
    "unknownorigins" : cards_by_parallel[Parallels.UnknownOrigins],
    # types
    "effect" : cards_by_type[CardTypes.Effect],
    "keyframing": cards_by_type[CardTypes.Keyframing],
    "relic" : cards_by_type[CardTypes.Relic],
    "unit" : cards_by_type[CardTypes.Unit],
    "upgrade" : cards_by_type[CardTypes.Upgrade],
    # rarities
    "common" : cards_by_rarity[CardRarities.Common],
    "uncommon" : cards_by_rarity[CardRarities.Uncommon],
    "rare" : cards_by_rarity[CardRarities.Rare],
    "legendary" : cards_by_rarity[CardRarities.Legendary],
    "prime" : cards_by_rarity[CardRarities.Prime],
}

CARD_DATA_FILE = os.getenv("CARD_DATA_FILE")
if not CARD_DATA_FILE:
    CARD_DATA_FILE = 'resources/cards.json'

with open(CARD_DATA_FILE, encoding='utf8') as cards_file:
    data = json.load(cards_file)
    for card_data in data:
        card = Card(card_data)

        card_name = card.Name.lower()
        # add to generic card lists
        cards[card_name] = card

        # add to parallel lists
        parallel_set = cards_by_parallel.get(card.Parallel)
        if not parallel_set == None:
            parallel_set[card_name] = card

        # add to card type list
        type_set = cards_by_type.get(card.Type)
        if not type_set == None:
            type_set[card_name] = card
            
        # add to card rarity list
        rarity_set = cards_by_rarity.get(card.Rarity)
        if not rarity_set == None:
            rarity_set[card_name] = card

        # add card to artist list
        artist = card.Artist
        if cards_by_artist.get(artist):
            cards_by_artist[artist].append(card)
        else:
            cards_by_artist[artist] = [card]

# load the paragons

paragons_by_parallel = {
    Parallels.Augencore: {},
    Parallels.Earthen: {},
    Parallels.Kathari: {},
    Parallels.Marcolian: {},
    Parallels.Shroud: {},
}

paragons_by_keyword = {
    "augencore": paragons_by_parallel[Parallels.Augencore],
    "earthen": paragons_by_parallel[Parallels.Earthen],
    "kathari": paragons_by_parallel[Parallels.Kathari],
    "marcolian": paragons_by_parallel[Parallels.Marcolian],
    "shroud": paragons_by_parallel[Parallels.Shroud],
}

paragons = {}

with open('resources/paragons.json', ) as paragons_file:
    data = json.load(paragons_file)
    for paragon_data in data:
        paragon = Paragon(paragon_data)
        name = paragon.Name.lower()

        # add to master paragon set
        paragons[name] = paragon

        # add to parallel lists
        paragon_set = paragons_by_parallel.get(paragon.Parallel)
        if not paragon_set == None:
            paragon_set[name] = paragon

