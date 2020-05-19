from abc import ABCMeta, abstractmethod

class IStack(metaclass=ABCMeta):

  def __init__(self):
    self._size = -1

  @abstractmethod
  def push(self, value):
    """
      coloca un dato en la pila.
    """
    pass

  @abstractmethod
  def pop(self):
    """
      retira el ultimo dato en la pila.
    """
    pass

  @abstractmethod
  def peek(self):
    """
      lee el ultimo dato de la pila sin retirarlo.
    """
    pass

  @abstractmethod
  def is_empty(self):
    """
      devuelve si la pila esta vacia o no
    """
    pass

  def size(self):
    """
      devuelve la cantidad de datos en la pila.
    """
    return self._size + 1

  def __len__(self):
    return self._size + 1