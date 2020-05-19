from .iqueue import IQueue

class ArrayQueue(IQueue):

  def __init__(self, size=10):
    super().__init__()
    self._array = [None] * size
    self._head = 0
    self._tail = 0

  def add(self, value):
    self._array[self._tail] = value
    self._tail += 1
    self._size += 1

  def remove(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')
    else:
      self._array[self._head] = None
      self._head += 1
      self._size -= 1

  def peek(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')
    else:
      return self._array[self._head]

  def is_empty(self):
    return self._size == 0