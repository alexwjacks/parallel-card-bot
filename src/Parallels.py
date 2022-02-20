from enum import Enum, unique

@unique
class Parallels(Enum):
  # we actually don't know
  Unknown = "unknown"

  # actual parallels
  Augencore = "augencore"
  Earthen = "earthen"
  Kathari = "kathari"
  Marcolian = "marcolian"
  Shroud = "shroud"
  Universal = "universal"
  UnknownOrigins = "unknownorigins"

  __aliases__ = {
    # unknown
    "unknown" : Unknown,
    "" : Unknown,
    # augencore
    "augencore" : Augencore,
    # augencore
    "earthen" : Earthen,
    # kathari
    "kathari" : Kathari,
    # marcolian
    "marcolian" : Marcolian,
    # shroud
    "shroud" : Shroud,
    # universal
    "universal" : Universal,
    # unknown origins
    "unknownorigins" : UnknownOrigins,
    "unknown origins" : UnknownOrigins,
    "uo" : UnknownOrigins,
  }

  # look up the appropriate enum by alias
  @classmethod
  def from_alias(self, str):
    # wrapping the result in self() is required to return an actual enum instead of the string value
    item = self(self.__aliases__.get(str.lower()))
    if not item:
      print(f"Parallels.from_alias: alias '{str}' was not recognized")
    return item  