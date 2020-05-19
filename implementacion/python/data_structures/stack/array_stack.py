from .istack import IStack


class ArrayStack(IStack):

  def __init__(self, size=10):
    super().__init__()
    self._array = [None] * size

  def push(self, value):
    self._size += 1
    self._array[self._size] = value

  def pop(self):
    if self.is_empty():
      raise IndexError('La pila esta vacía.')

    self._array[self._size] = None
    self._size -= 1

  def peek(self):
    if self.is_empty():
      raise IndexError('La pila esta vacía.')

    return self._array[self._size]

  def is_empty(self):
    return self._size == -1
