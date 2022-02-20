from Parallels import Parallels

class Paragon:
  def __init__(self, data:dict):
    # load the name first so we can use it for error reporting
    self.Name = data.get('Name', '')
    self.Active = data.get('Active', '')
    self.Passive = data.get('Passive', '')

    try:
      self.Parallel = Parallels.from_alias(data.get('Parallel', '').lower())

    except Exception as ex:
      self.__printException__(ex)
      self.Parallel = Parallels.Unknown
    