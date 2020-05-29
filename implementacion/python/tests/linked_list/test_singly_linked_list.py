from unittest import TestCase

from data_structures.linked_list.linear_singly import LinkedListLinearSingly

class TestLinkedListLinearSingly(TestCase):

  def setUp(self):
    self._linkedList = LinkedListLinearSingly()

  def test_insert_raise_ValueError(self):
    ll = self._linkedList

    with self.assertRaises(ValueError):
      ll.insert(200, 999)

  def test_remove(self):
    ll = self._linkedList

    key = ll.push(200)

    ll.remove(key)

    self.assertTrue(ll.is_empty())

  def test_size_decreased(self):
    ll = self._linkedList

    ll.push(200)
    ll.push(300)
    key = ll.append(500)

    ll.remove(key)

    self.assertEqual(2, len(ll))

  def test_search(self):
    ll = self._linkedList

    ll.push(200)

    node_data = ll.search(0)
    
    self.assertEqual(200, node_data._data)

  def test_search_raise_ValueError(self):
    ll = self._linkedList

    ll.push(1)

    with self.assertRaises(ValueError):
      ll.search(1)

  def test_search_raise_IndexError(self):
    ll = self._linkedList

    with self.assertRaises(IndexError):
      ll.search(1)

  def test_display(self):
    ll = self._linkedList

    ll.push(200)
    ll.append(300)

    list_data = ll.display()

    self.assertListEqual([200, 300], list_data)

  def test_display_raise_IndexError(self):
    ll = self._linkedList

    with self.assertRaises(IndexError):
      ll.display()


  def test_is_empty(self):
    ll = self._linkedList
    
    self.assertTrue(ll.is_empty())
    
    ll.append(9)
    
    self.assertFalse(ll.is_empty())

  def test_size(self):
    ll = self._linkedList

    self.assertEqual(0, len(ll))
    self.assertEqual(0, ll.size())
    
    ll.push(10)

    self.assertEqual(1, len(ll))
    self.assertEqual(1, ll.size())

    ll.insert(50, 0)

    self.assertEqual(2, len(ll))
    self.assertEqual(2, ll.size())

    ll.append(999)

    self.assertEqual(3, len(ll))
    self.assertEqual(3, ll.size())
