from unittest import TestCase

from data_structures.stack.array_stack import ArrayStack


class TestArrayStack(TestCase):
  
  def setUp(self):
    self._stack = ArrayStack()

  def test_push(self):
    s = self._stack
    
    # it should add the value from the parameter, into the stack
    s.push(1)
    self.assertEqual(s._array[s._size], 1)

  def test_pop(self):
    s = self._stack

    # it should remove the the first value from the stack
    s.push(1)
    s.pop()
    # should assert a list of size 10 None, values 
    self.assertListEqual(([None]*10), s._array)

  def test_peek(self):
    s = self._stack

    s.push(1)

    # it should return the last value (1)
    self.assertEqual(1, s.peek())

    # it should return the last value (300)
    s.push(300)
    self.assertEqual(300, s.peek())

  def test_size(self):
    s = self._stack
    
    # it should return the size of added values (0)
    self.assertEqual(0, s.size())

    # it should return the size of added values (1)
    s.push(200)
    self.assertEqual(1, s.size())
    
    # it should return the size of added values (3)
    s.push(89)
    s.push(3)
    self.assertEqual(3, s.size())

  def test_is_empty(self):
    s = self._stack

    # it should return a boolean value (False)
    self.assertTrue(s.is_empty())

    # it should return a boolean value (True)
    s.push(200)
    self.assertFalse(s.is_empty())

  def test_push_raise_indexException(self):
    s = self._stack
    
    for i in range(0, 10):
      s.push(i)

    # it should raise an Exception (IndexException), when there is not any value in the stack
    with self.assertRaises(IndexError):
      s.push(200)

  def test_pop_raise_indexException(self):
    s = self._stack

    # it should raise an Exception (IndexException), when there is not any value in the stack
    with self.assertRaises(IndexError):
      s.pop()

  def test_peek_raise_indexException(self):
    s = self._stack

    # it should raise an Exception (IndexException), when there is not any value in the stack
    with self.assertRaises(IndexError):
      s.peek()