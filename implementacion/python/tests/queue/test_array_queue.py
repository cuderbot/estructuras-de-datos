from unittest import TestCase

from data_structures.queue.array_queue import ArrayQueue

class TestArrayQueue(TestCase):
  
  def setUp(self):
    self._queue = ArrayQueue()

  def test_add(self):
    q = self._queue

    # it should add the value into the queue
    q.add(2)
    self.assertEqual(q._array[q._head], 2)

  def test_remove(self):
    q = self._queue

    # it should remove the value into the queue
    q.add(200)
    q.remove()
    # should assert a list of size 10 None, values 
    self.assertListEqual(([None]*10), q._array)

  def test_peek(self):
    q = self._queue

    q.add(1)

    # it should return the last value (1)
    self.assertEqual(1, q.peek())

    # it should return the last value (300)
    q.remove()
    q.add(300)
    self.assertEqual(300, q.peek())

  def test_size(self):
    q = self._queue
    
    # it should return the size of the queue (0)
    self.assertEqual(0, q.size())

    # it should return the size of the queue (1)
    q.add(200)
    self.assertEqual(1, q.size())
    
    # it should return the size of the queue (3)
    q.add(89)
    q.add(3)
    self.assertEqual(3, q.size())

  def test_is_empty(self):
    q = self._queue

    # it should return a boolean value (False)
    self.assertTrue(q.is_empty())

    # it should return a boolean value (True)
    q.add(200)
    self.assertFalse(q.is_empty())

  def test_push_raise_indexException(self):
    q = self._queue
    
    for i in range(0, 10):
      q.add(i)

    # it should raise an Exception (IndexException), when there is not any value in the queue
    with self.assertRaises(IndexError):
      q.add(200)

  def test_pop_raise_indexException(self):
    q = self._queue

    # it should raise an Exception (IndexException), when there is not any value in the queue
    with self.assertRaises(IndexError):
      q.remove()

  def test_peek_raise_indexException(self):
    q = self._queue

    # it should raise an Exception (IndexException), when there is not any value in the queue
    with self.assertRaises(IndexError):
      q.peek()