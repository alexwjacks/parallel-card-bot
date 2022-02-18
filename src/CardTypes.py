from enum import Enum, unique

@unique
class CardTypes(Enum):
  Unknown = "unknown"
  Effect = "effect"
  Keyframing = "keyframing"
  Relic = "relic"
  Unit = "unit"
  Upgrade = "upgrade"
