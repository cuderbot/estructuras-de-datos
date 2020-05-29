

class Node:
  def __init__(self, data, key):
    self._data = data
    self._key = key
    self._next = None

  def __repr__(self):
    return '<NODO ID: {} DATA: {}>'.format(self._key, self._data)

class LinkedListLinearSingly:

  def __init__(self):
    self._size = 0
    self._head = None

  def push(self, value):
    key = self._size
    n = Node(value, key)

    if not self.is_empty():
      n._next = self._head

    self._head = n
    self._size += 1
    return key

  def insert(self, value, key):
    newkey = self._size
    temp = self._head

    while temp is not None:
      if temp._key == key:
        break
      temp = temp._next


    if temp is None:
      raise ValueError('No se ha encontrado ningún nodo con ese ID.')
    else:
      n = Node(value, newkey)
      n._next = temp._next
      temp._next = n
      self._size += 1
      return newkey

  def append(self, value):
    key = self._size
    n = Node(value, key)
    if self.is_empty():
      self._head = n
    else:
      temp = self._head

      while temp._next is not None:
        temp = temp._next

      temp._next = n
    self._size += 1
    return key

  def remove(self, key):
    if self.is_empty():
      raise IndexError('Lista vacia.')
    else:
      if self._head._key == key:
        self._head = self._head._next
        self._size -= 1
      else:
        temp = self._head
        while temp._next is not None:
          if temp._next._key == key:
            break
          temp = temp._next

        if temp._next is None:
          raise ValueError('No se ha encontrado el nodo con esa llave.')
        else:
          temp._next = temp._next._next
          self._size -= 1

  def search(self, key):
    if self.is_empty():
      raise IndexError('Lista vacia.')
    else:
      temp = self._head

      while temp is not None:
        if temp._key == key:
          break
        temp = temp._next

      if temp is None or temp._key != key:
        raise ValueError('Nodo no encontrado.')
      else:
        return temp

  def display(self):
    if self.is_empty():
      raise IndexError('Lista vacia.')
    else:
      temp = self._head
      list_temp = list()
      while temp is not None:
        list_temp.append(temp)
        temp = temp._next
      return list_temp

  def is_empty(self):
    return self._head is None

  def size(self):
    return self._size

  def __len__(self):
    return self._size
