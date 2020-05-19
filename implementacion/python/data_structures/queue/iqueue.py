from abc import ABCMeta, abstractmethod

class IQueue(metaclass=ABCMeta):

  def __init__(self):
    self._size = 0

  @abstractmethod
  def add(self, value):
    pass

  @abstractmethod
  def remove(self):
    pass

  @abstractmethod
  def peek(self):
    pass

  @abstractmethod
  def is_empty(self):
    pass

  def size(self):
    return self._size

  def __len__(self):
    return self._size