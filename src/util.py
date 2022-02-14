import random
import re
from fuzzywuzzy import fuzz

card_name_index = "Card Name"
parallel_index = "Parallel"
rarity_index = "Rarity"
type_index = "Type"
function_index = "Function"

paragon_name_index = "Paragon Name"
paragon_parallel_index = "Parallel"
paragon_passive_index = "Passive"
paragon_active_index = "Active"

def format_card(card):
    name = f"Name: *{card[card_name_index]}*"
    faction = f"Parallel: *{card[parallel_index]}*"
    rarity = f"Rarity: *{card[rarity_index]}*"
    card_type = f"Type: *{card[type_index]}*"
    fn = f"Function: *{card[function_index]}*"
    formatted = "\n".join([name, faction, rarity, card_type, fn])
    return formatted

def format_paragon(paragon):
    name = f"Name: *{paragon[paragon_name_index]}*"
    faction = f"Parallel: *{paragon[paragon_parallel_index]}*"
    passive = f"Passive: *{paragon[paragon_passive_index]}*"
    active = f"Active: *{paragon[paragon_active_index]}*"
    formatted = "\n".join([name, faction, passive, active])
    return formatted

def get_card_url(card):
    hyphenated = hyphenate_card_name(card[card_name_index].lower())
    card_name = re.sub("[^a-zA-Z0-9-]", "", hyphenated)
    return f"https://parallel.life/cards/{card_name}"

def hyphenate_card_name(name):
    words = name.split()
    words_hyphenated = "-".join(words)
    return words_hyphenated

def fuzzy_find(name, set, name_index):
    best_score = 0
    best_item = None

    print("fuzzy_find: Searching", len(set), f"items for one named '{name}'")

    for key in set.keys():
        item = set[key]
        item_name = item[name_index]
        score = fuzz.token_sort_ratio(name.lower(), item_name)

        # this is the closest match we've seen so far
        if score > best_score:
            best_score = score
            best_item = item

    if best_item:
        print(f"fuzzy_find: The highest scoring item was '{best_item[name_index]}' with a score of {best_score}")

    # note, this can be None if there was no good match
    return best_item

def find_card(name, cards):
    return fuzzy_find(name, cards, card_name_index)

def find_paragon(name, paragons):
    return fuzzy_find(name, paragons, paragon_name_index)

def format_random_card_from_list(card_list):
    return format_card(random.choice(list(card_list.values())))

def format_multiple_paragons(paragons):
    accumulator = []
    for name, data in paragons.items():
        accumulator.append(format_paragon(data))
    formatted = "\n\n".join(accumulator)
    return formatted
