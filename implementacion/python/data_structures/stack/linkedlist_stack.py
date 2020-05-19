from data_structures.stack.istack import IStack


class Node:
  def __init__(self, data):
    self._data = data
    self._next = None


class LinkedListStack(IStack):

  def __init__(self):
    super().__init__()
    self._head = None

  def push(self, value):
    n = Node(value)

    if not self.is_empty():
      n._next = self._head

    self._head = n
    self._size += 1

  def pop(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')
    else:
      self._head = self._head._next
      self._size -= 1

  def peek(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')
    else:
      return self._head._data

  def is_empty(self):
    return self._head is None
    