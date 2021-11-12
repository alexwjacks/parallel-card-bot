card_name_index = "Card Name"
parallel_index = "Parallel"
rarity_index = "Rarity"
type_index = "Type"
function_index = "Function"

def format_card(card):
    name = f"Name: *{card[card_name_index]}*"
    faction = f"Parallel: *{card[parallel_index]}*"
    rarity = f"Rarity: *{card[rarity_index]}*"
    card_type = f"Type: *{card[type_index]}*"
    fn = f"Function: *{card[function_index]}*"
    formatted = "\n".join([name, faction, rarity, card_type, fn])
    return formatted

def hyphenate_card_name(name):
    words = name.split()
    words_hyphenated = "-".join(words)
    return words_hyphenated