from enum import Enum, unique

@unique
class CardEditions(Enum):
  # card back
  CardBack = "Collectible Card Back"
  # concept art
  ConceptArt = "Concept Art"
  # first edition 
  FirstEdition = "First Edition"
  # masterpiece
  Masterpiece = "Masterpiece"
  # perfect loop
  PerfectLoop = "Perfect Loop"
  # special edition
  SpecialEdition = "Special Edition"

  __aliases__ = {
    # card back
    "collectible_card_back" : CardBack,
    # concept art
    "concept_art" : ConceptArt,
    # first edition 
    "collectible_card" : FirstEdition,
    "fe" : FirstEdition,
    # masterpiece
    "masterpiece" : Masterpiece,
    # perfect loop
    "perfectloop" : PerfectLoop,
    "pl" : PerfectLoop,
    # special edition
    "se" : SpecialEdition
  }

  # look up the appropriate enum by alias
  @classmethod
  def from_alias(self, str):
    # wrapping the result in self() is required to return an actual enum instead of the string value
    try:
      item = self(self.__aliases__.get(str.lower()))
      return item
    except Exception as ex:
      print(f"CardEditions.from_alias: alias '{str}' was not recognized")
      return None

      
