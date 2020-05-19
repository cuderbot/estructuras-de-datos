from unittest import TestCase

from data_structures.stack.linkedlist_stack import LinkedListStack


class TestLinkedListStack(TestCase):

  def setUp(self):
    self._stack = LinkedListStack()

  def test_push(self):
    s = self._stack

    # it should push the value into the head in the stack
    s.push(99)
    self.assertEqual(s._head._data, 99)

    # it should push the value into the next to the head in the stack
    s.push(200)
    self.assertEqual(s._head._data, 200)

  def test_pop(self):
    s = self._stack

    s.push(200)
    self.assertEqual(s._head._data, 200)

    s.pop()
    # it should pop out the node from the stack, so the node head has to be None
    self.assertIsNone(s._head)

    s.push(10)
    s.push(500)
    s.pop()
    # it should pop out the last value, so the node value it has to be 10
    self.assertEqual(10, s._head._data)

  def test_peek(self):
    s = self._stack

    s.push(88)
    # it should give the last value pushed into the stack
    self.assertEqual(88, s.peek())

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

    # it should be True, because there is any value into the stack
    self.assertTrue(s.is_empty())

    # it should be False, because there is a value into the stack
    s.push(0)
    self.assertFalse(s.is_empty())

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