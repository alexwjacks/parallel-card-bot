# Adds available card function and type data to spider data
import sys
import json

# constants
DEFAULT_SPIDER_DATA_PATH = 'resources/spider.json'
DEFAULT_CARD_DATA_PATH = 'resources/cards.json'
DEFAULT_OUTPUT_PATH = 'resources/merged.json'

# usage
def print_usage():
  print("Usage:")
  print("python merge.py [spider_data] [function_data] [output]")
  print(f"    spider_data: optional. The path to the desired output file. Default: {DEFAULT_SPIDER_DATA_PATH}")
  print(f"  function_data: optional. The path to the desired output file. Default: {DEFAULT_CARD_DATA_PATH}")
  print(f"         output: optional. The path to the desired output file. Default: {DEFAULT_OUTPUT_PATH}")

# process command-line arguments

# see if help was requested
for arg in sys.argv:
  if arg == '/?' or arg.lower() == '/help':
    print_usage()
    exit()

outputFile = ""
spiderDataFile = ""
cardsDataFile = ""

if len(sys.argv) > 3:
  outputFile = sys.argv[3]
  spiderDataFile = sys.argv[2]
  cardsDataFile = sys.argv[1]
else:
  outputFile = DEFAULT_OUTPUT_PATH
  spiderDataFile = DEFAULT_SPIDER_DATA_PATH
  cardsDataFile = DEFAULT_CARD_DATA_PATH

print("Merging (spider data):", spiderDataFile)
print("  And (function data):", cardsDataFile)
print("        Into (output):", outputFile)

# search the json_object for a given value
# using the provided key on each element in the object
def find_element(json_object, key, value):
  return [o for o in json_object if o.get(key) and o.get(key).lower() == value.lower()]

with open(spiderDataFile, encoding='utf8') as spider_file:
    spider_data = json.load(spider_file)

with open(cardsDataFile, encoding='utf8') as cards_file:
    cards_data = json.load(cards_file)

print("Spider", len(spider_data))
print("Cards", len(cards_data))

# calc the intersection
# i = { key: [o, cards_data[key]] for key, o in spider_data.items() if key in cards_data }
# print(i)
# exit()

card_name_index = 'Card Name'
function_index = 'Function'
type_index = 'Type'

for sr in spider_data:
  name = sr[card_name_index]
  o = find_element(cards_data, card_name_index, name)
  if o:
    sr[function_index] = o[0].get(function_index, "")
    sr[type_index] = o[0].get(type_index, "")
    print(f"Adding {function_index} '{sr[function_index]}' to {name}")
    print(f"Adding {type_index} '{sr[type_index]}' to {name}")
  else:
    sr[function_index] = "(coming soon)"
    sr[type_index] = "(coming soon)"

print (f"Writing output to {outputFile}")

with open(outputFile, 'w', encoding='utf-8') as f:
  json.dump(spider_data, f, ensure_ascii=False, indent=2)

