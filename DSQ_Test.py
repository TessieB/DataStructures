import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()
  
  def test_empty_list_string(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')

  def test_front_end_to_back_end_string(self):
    self.__deque.push_back('Testing')
    self.__deque.push_back('is')
    self.__deque.push_back('the')
    self.__deque.push_back('best')
    self.__deque.push_back('!')
    self.assertEqual('[ Testing, is, the, best, ! ]', str(self.__deque))

  def test_back_end_to_front_end_string(self):
    self.__deque.push_back('is')
    self.__deque.push_back('bright')
    self.__deque.push_front('sun')
    self.__deque.push_front('The')
    self.assertEqual('[ The, sun, is, bright ]', str(self.__deque))

  def test_get_length_of_empty_deque(self):
    self.assertEqual(0, len(self.__deque))
  
  def test_get_one_length_push_front(self):
    self.__deque.push_front('one')
    self.assertEqual(1, len(self.__deque))

  def test_get_two_length_push_front(self):
    self.__deque.push_front('one')
    self.__deque.push_front('two')
    self.assertEqual(2, len(self.__deque))
  
  def test_get_two_length_push_back(self):
    self.__deque.push_back('one')
    self.__deque.push_back('two')
    self.assertEqual(2, len(self.__deque))
  
  def test_get_three_length_push_back(self):
    self.__deque.push_back('one')
    self.__deque.push_back('two')
    self.__deque.push_back('three')
    self.assertEqual(3, len(self.__deque))

  def test_one_element_push_front(self):
    self.__deque.push_front('one')
    self.assertEqual('[ one ]', str(self.__deque))

  def test_push_front(self):
    self.__deque.push_front(5)
    self.__deque.push_front(6)
    self.__deque.push_front(7)
    self.assertEqual('[ 7, 6, 5 ]', str(self.__deque))

  def test_push_front_None(self):
    self.__deque.push_front(None)
    self.assertEqual('[ None ]', str(self.__deque))
  
  def test_pop_front_empty_deque(self):
    try:
      returned = self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_all_values_plus_from_empty_string(self):
    try:
      self.__deque.push_back('one')
      self.__deque.push_back('two')
      self.__deque.push_front('three')
      returned1 = self.__deque.pop_front()
      returned2 = self.__deque.pop_front()
      returned3 = self.__deque.pop_front()
      returned4 = self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
    except IndexError:
      with self.assertRaises(IndexError):
        self.__deque.push_back('one')
        self.__deque.push_back('two')
        self.__deque.push_front('three')
        returned1 = self.__deque.pop_front()
        returned2 = self.__deque.pop_front()
        returned3 = self.__deque.pop_front()
        returned4 = self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_three_element_deque(self):
    self.__deque.push_front(5)
    self.__deque.push_front(6)
    self.__deque.push_front(7)
    returned = self.__deque.pop_front()
    self.assertEqual('[ 6, 5 ]', str(self.__deque))
  
  def test_peek_front_empty_deque(self):
    try:
      returned = self.__deque.peek_front()
      self.assertEqual('None', str(self.__deque.peek_front()))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__deque.peek_front()

  def test_peek_front_three_entry_deque(self):
    self.__deque.push_back('one')
    self.__deque.push_back('two')
    self.__deque.push_back('three')
    returned = self.__deque.peek_front()
    self.assertEqual('one', str(self.__deque.peek_front()))

  def test_push_back_one_element(self):
    self.__deque.push_back('one')
    self.assertEqual('[ one ]', str(self.__deque))
  
  def test_push_back_three_elements(self):
    self.__deque.push_back(5)
    self.__deque.push_back(6)
    self.__deque.push_back(7)
    self.assertEqual('[ 5, 6, 7 ]', str(self.__deque))

  def test_push_back_None(self):
    self.__deque.push_back(None)
    self.assertEqual('[ None ]', str(self.__deque))
  
  def test_pop_back_on_three_element_deque(self):
    self.__deque.push_back(5)
    self.__deque.push_back(6)
    self.__deque.push_back(7)
    returned = self.__deque.pop_back()
    self.assertEqual('[ 5, 6 ]', str(self.__deque))
  
  def test_pop_back_from_empty_deque(self):
    try:
      returned = self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_back_all_values_plus_from_empty_string(self):
    try:
      self.__deque.push_back('one')
      self.__deque.push_back('two')
      self.__deque.push_front('three')
      returned1 = self.__deque.pop_back()
      returned2 = self.__deque.pop_back()
      returned3 = self.__deque.pop_back()
      returned4 = self.__deque.pop_back() 
      self.assertEqual('[ ]', str(self.__deque))
    except IndexError:
      with self.assertRaises(IndexError):
        self.__deque.push_back('one')
        self.__deque.push_back('two')
        self.__deque.push_front('three')
        returned1 = self.__deque.pop_back()
        returned2 = self.__deque.pop_back()
        returned3 = self.__deque.pop_back()
        returned4 = self.__deque.pop_back() 
      self.assertEqual('[ ]', str(self.__deque))
  
  def test_peek_back_empty_deque(self):
    try:
      returned = self.__deque.peek_back()
      self.assertEqual('None', str(self.__deque.peek_back()))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__deque.peek_back()

  def test_peek_back_three_entry_deque(self):
    self.__deque.push_back('one')
    self.__deque.push_back('two')
    self.__deque.push_back('three')
    returned = self.__deque.peek_back()
    self.assertEqual('three', str(self.__deque.peek_back()))

  def test_stack_length_three_elements(self):
    self.__stack.push('one')
    self.__stack.push('two')
    self.__stack.push('three')
    self.assertEqual(3, len(self.__stack))

  def test_stack_length_two_elements_after_pop(self):
    self.__stack.push('one')
    self.__stack.push('two')
    returned = self.__stack.pop()
    self.assertEqual(1, len(self.__stack))

  def test_one_element_string_stack(self):
    self.__stack.push('one')
    self.assertEqual('[ one ]', str(self.__stack))

  def test_two_element_string_stack(self):
    self.__stack.push('one')
    self.__stack.push('two')
    self.assertEqual('[ one, two ]', str(self.__stack))

  def test_push_one_element_stack(self):
    self.__stack.push('one')
    self.assertEqual('[ one ]', str(self.__stack))
  
  def test_push_three_elements_stack(self):
    self.__stack.push('one')
    self.__stack.push('two')
    self.__stack.push('three')
    self.assertEqual('[ one, two, three ]', str(self.__stack))

  def test_pop_element_empty_stack(self):
    try:
      returned = self.__stack.pop()
      self.assertEqual('[ ]', str(self.__deque))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__stack.pop()
      self.assertEqual('[ ]', str(self.__deque))

  def test_pop_three_element_stack(self):
    self.__stack.push('one')
    self.__stack.push('two')
    self.__stack.push('three')
    returned = self.__stack.pop()
    self.assertEqual('[ one, two ]', str(self.__stack))

  def test_peek_empty_stack(self):
    try:
      returned = self.__stack.peek()
      self.assertEqual('None', str(self.__stack.peek()))
    except IndexError:
      with self.assertRaises(IndexError):
        returned = self.__stack.peek()

  def test_peek_three_element_stack(self):
    self.__stack.push('one')
    self.__stack.push('two')
    self.__stack.push('three')
    returned = self.__stack.peek()
    self.assertEqual('three', str(self.__stack.peek()))

  def test_length_one_element_queue(self):
    self.__queue.enqueue('one')
    self.assertEqual(1, len(self.__queue))

  def test_length_three_element_queue(self):
    self.__queue.enqueue('one')
    self.__queue.enqueue('two')
    self.__queue.enqueue('three')
    self.assertEqual(3, len(self.__queue))

  def test_length_two_element_queue(self):
    self.__queue.enqueue('one')
    self.__queue.enqueue('two')
    self.__queue.enqueue('three')
    returned = self.__queue.dequeue()
    self.assertEqual(2, len(self.__queue))

  def test_string_enqueue_one_element_queue(self):
    self.__queue.enqueue('one')
    self.assertEqual('[ one ]', str(self.__queue))

  def test_string_enqueue_three_element_queue(self):
    self.__queue.enqueue('one')
    self.__queue.enqueue('two')
    self.__queue.enqueue('three')
    self.assertEqual('[ one, two, three ]', str(self.__queue))

  def test_enqueue_one_element_and_dequeue_one_element(self):
    self.__queue.enqueue('one')
    returned = self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_empty_queue(self):
    try:
      returned = self.__queue.dequeue()
      self.assertEqual('[ ]', str(self.__queue))
    except IndexError:
      with self.assertRaises(IndexError):    
        returned = self.__queue.dequeue()
      self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_three_element_queue(self):
    self.__queue.enqueue('one')
    self.__queue.enqueue('two')
    self.__queue.enqueue('three')
    returned = self.__queue.dequeue()
    self.assertEqual('[ two, three ]', str(self.__queue))

if __name__ == '__main__':
  unittest.main()

