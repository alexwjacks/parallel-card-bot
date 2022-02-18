from enum import Enum, unique

@unique
class CardRarities(Enum):
  Unknown = "unknown"
  Common = "common"
  Uncommon = "uncommon"
  Rare = "rare"
  Legendary = "legendary"
  Prime = "prime"
