from CardEditions import CardEditions
from CardRarities import CardRarities
from CardTypes import CardTypes
from Parallels import Parallels

class Card:
  def __init__(self, data:dict):
    # load the name first so we can use it for error reporting
    self.Name = data.get('Name', '')

    # load the remaining data
    self.Artist = data.get('Artist', '')
    self.Description = data.get('Description', '')
    self.Function = data.get('Function', '')

    try:
      self.Parallel = Parallels.from_alias(data.get('Parallel', '').lower())
    except Exception as ex:
      self.__printException__(ex)
      self.Parallel = Parallels.Unknown
    
    try:
      self.Rarity = CardRarities(data.get('Rarity', '').lower())
    except Exception as ex:
      self.__printException__(ex)
      self.Rarity = CardRarities.Unknown

    try:
      self.Type = CardTypes(data.get('Type', '').lower())
    except Exception as ex:
      self.__printException__(ex)
      self.Type = CardTypes.Unknown

    # load editions, e.g.
    #  "Editions": {
    #    "Se": {
    #      "Day": "https://parallel.life/cards/pocket-dimension-se",
    #      "Night": "https://parallel.life/cards/pocket-dimension-se-2"
    #    },
    #    "Masterpiece": "https://parallel.life/cards/188"
    #  }
    self.Editions = {}
    editions = data.get('Editions', {})

    for k, v in editions.items():
      ed = CardEditions.from_alias(k)
      if ed:
        self.Editions[ed] = v

  def __printException__(self, ex:Exception):
    print(f"Card.__init__: warning loading card named '{self.Name}' : {ex}")

  def __str__(self):
    s = ''
    # get a sorted list of properties for this class
    members = dir(self)
    properties = sorted(
      filter(
        lambda x: not x.startswith('__') and x != 'Editions',
        members
      )
    )

    # print the properties (except Editions)
    s += '\n'.join([f"{p} : {getattr(self, p)}" for p in properties])
    s += '\n'

    # print the Editions
    s += 'Editions :\n'
    for k, v in self.Editions.items():
      s += f"  {k} :"
      if isinstance(v, dict):
        s += '\n'
        s += '\n'.join({f"    {k2} : {v2}" for k2, v2 in v.items()})
        s += '\n'
      if isinstance(v, str):
        s += f" {v}\n"
    return s
