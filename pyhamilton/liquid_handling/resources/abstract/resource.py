from abc import ABCMeta, abstractmethod

from .coordinate import Coordinate


class Resource(object, metaclass=ABCMeta):
  """ Abstract base class for deck resources. """

  @abstractmethod
  def __init__(
    self,
    name: str,
    size_x: float,
    size_y: float,
    size_z: float,
    location=Coordinate(None, None, None)
  ):
    self.name = name
    self.size_x = size_x
    self.size_y = size_y
    self.size_z = size_z
    self.location = location
