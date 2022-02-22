import random
from Card import Card
from Paragon import Paragon
from Parallels import Parallels
from fuzzywuzzy import fuzz

paragon_name_index = "Name"
paragon_parallel_index = "Parallel"
paragon_passive_index = "Passive"
paragon_active_index = "Active"

emoji_by_parallel = {
    Parallels.Unknown : "",
    Parallels.Augencore : "<:color_augencore:850233294971994123>",
    Parallels.Kathari : "<:color_kathari:850233295362850816>",
    Parallels.Marcolian : "<:color_marcolian:850233295501262899>",
    Parallels.Shroud : "<:color_shroud:850233295501000704>",
    Parallels.Earthen : "<:color_earthen:850233295371632670>",
    Parallels.Universal : ":white_circle:",
}

def format_card(card:Card):
    name = ""
    artist = ""
    parallel = ""
    rarity = ""
    cardType = ""
    fn = ""

    if card.Name:
        name = f"**{card.Name.upper()}**"

    if card.Artist:
        artist = f"(Art by {card.Artist})"

    if card.Parallel:
        parallel = emoji_by_parallel.get(card.Parallel, "")

    if card.Rarity:
        rarity = f"{card.Rarity.value.upper()} // "
    
    cardType = card.Type.value.upper()

    if card.Function:
        fn = f"*{card.Function}*"

    formatted = f"{parallel} {name} {artist}\n"
    formatted += f"{rarity}{cardType}\n"
    formatted += f"{fn}"

    return formatted

def format_paragon(paragon:Paragon):
    name = ""
    parallel = ""
    passive = ""
    active = ""
    
    if paragon.Name:
        name = f"**{paragon.Name.upper()}**"
    
    if paragon.Parallel:
        parallel = emoji_by_parallel.get(paragon.Parallel, "")

    passive = f"Passive: *{paragon.Passive}*"
    active = f"Active: *{paragon.Active}*"

    formatted = f"{parallel} {name}\n"
    formatted += f"{passive}\n{active}\n"

    return formatted

def get_card_url(card:Card):
    s = "Sorry, I don't have any URLs for this card."
    if isinstance(card.Editions, dict) and len(card.Editions):
        s = 'Editions :\n'
        for k, v in card.Editions.items():
            # e.g. Concept Art, First Edition, Special Edition, Masterpiece, etc.
            s += f"  {k.value} :"
            if isinstance(v, dict):
                # e.g. 01, 02, Day, Night, etc.
                s += '\n'
                # wrapping links in < > cancels the embedded preview
                s += '\n'.join({f"    {k2} : <{v2}>" for k2, v2 in v.items()})
                s += '\n'
            if isinstance(v, str):
                s += f" <{v}>\n"
    return s
    

def fuzzy_find(name, set, attribute):
    best_score = 0
    best_item = None

    print("fuzzy_find: Searching", len(set), f"items for one with '{attribute}' like '{name}'")

    for key in set.keys():
        item = set[key]
        item_name = getattr(item, attribute)

        score = fuzz.token_sort_ratio(name.lower(), item_name)

        # this is the closest match we've seen so far
        if score > best_score:
            best_score = score
            best_item = item

    if best_item:
        print(f"fuzzy_find: The highest scoring item was '{getattr(best_item, attribute)}' with a score of {best_score}")

    # note, this can be None if there was no good match
    return best_item

def find_card(name, cards):
    return fuzzy_find(name, cards, 'Name')

def find_paragon(name, paragons):
    return fuzzy_find(name, paragons, 'Name')

def find_artist(name, artists):
    artist = None
    print(f"find_artist: Looking for '{name}' among '{artists}'")
    scores = [(a, fuzz.token_sort_ratio(name.lower(), a)) for a in artists]
    match, score = max(scores, key=lambda x: x[1])
    print(f"find_artist: The closest artist name was '{match}' with a score of {score}")

    if score >= 40:
        artist = match
    else:
        print("find_artist: Could not find a match with high enough confidence.")

    return artist

def format_random_card_from_list(card_list):
    if isinstance(card_list, list):
        return format_card(random.choice(card_list))
    else:
        return format_card(random.choice(list(card_list.values())))

def format_multiple_paragons(paragons):
    accumulator = []
    for name, data in paragons.items():
        accumulator.append(format_paragon(data))
    formatted = "\n".join(accumulator)
    return formatted
