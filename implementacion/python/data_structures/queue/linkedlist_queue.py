from .iqueue import IQueue


class Node:

  def __init__(self, data):
    self._data = data
    self._next = None


class LinkedListQueue(IQueue):

  def __init__(self):
    self._head = None
    self._tail = None

  def add(self, value):
    n = Node(value)
    if self.is_empty():
      self._head = n
    else:
      self._tail._next = n
    self._tail = n
    self._size += 1

  def remove(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')

    if self._front is self._rear:
      self._front = None
      self._rear = None
    else:
      self._front = self._front._next
    self._size -= 1

  def peek(self):
    if self.is_empty():
      raise IndexError('La cola esta vacía.')
    else:
      return self._head._data

  def is_empty(self):
    return self._head is None