class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      self.value = val
      self.next = None
      self.prev = None

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    self.__header = Linked_List.__Node(None)
    self.__trailer = Linked_List.__Node(None)
    self.__header.next = self.__trailer
    self.__trailer.prev = self.__header
    self.__size = 0

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    new_node = Linked_List.__Node(val)
    current = self.__trailer.prev
    new_node.next = self.__trailer
    self.__trailer.prev = new_node
    new_node.prev = current
    current.next = new_node
    self.__size += 1


  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    if index >= self.__size or index < 0:
        raise IndexError
    new_node = Linked_List.__Node(val)
    current = self.__header.next
    if index == 0:
      current = self.__header
    elif index <= self.__size // 2: 
        for i in range(index-1):
            current = current.next
    elif index > self.__size // 2:
        current = self.__trailer.prev
        for i in range(self.__size - index):
            current = current.prev
    after_new_node = current.next
    new_node.next = after_new_node
    current.next = new_node
    new_node.prev = current
    after_new_node.prev = new_node
    self.__size += 1

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    if index >= self.__size or index < 0:
        raise IndexError
    current = self.__header.next
    if index == 0:
      current = self.__header
    if index <= self.__size // 2:
        for i in range(index - 1):
            current = current.next
    elif index > self.__size // 2:
        current = self.__trailer.prev
        for i in range(self.__size - index):
            current = current.prev
    after_removed_node = current.next.next
    removed_node = current.next
    current.next = current.next.next
    after_removed_node.prev = current
    self.__size -= 1
    return removed_node.value


  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    if index >= self.__size or index < 0:
        raise IndexError
    current = self.__header.next
    if index <= self.__size // 2:
        for i in range(index):
            current = current.next
    elif index > self.__size // 2:
        current = self.__trailer.prev
        for i in range(self.__size - index - 1):
            current = current.prev
    return current.value

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    if self.__size > 1:
      cur = self.__header.next
      self.__header.next = self.__header.next.next
      self.__header.next.prev = self.__header
      cur.next = self.__trailer
      self.__trailer.prev.next = cur
      cur.prev = self.__trailer.prev
      self.__trailer.prev = cur
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    if self.__size == 0:
      return '[ ]'
    word = "[ "
    current = self.__header.next
    while current is not self.__trailer:
        word += str(current.value)
        if current.next is not self.__trailer:
            word += ", "
        current = current.next
    word += " ]"
    return word

  def __iter__(self):
    # initialize a new attribute for walking through your list
    self.__cur = self.__header.next
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    if self.__cur is self.__trailer:
        raise StopIteration
    temp = self.__cur
    self.__cur = self.__cur.next
    return temp.value

if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.

  n = Linked_List()           #checks constructors/append element method/length method
  n.append_element(3)
  n.append_element(4)
  n.append_element(5)
  print(n)
  print(len(n))

  k = Linked_List()
  try:                        #checks insert element at method
    k.insert_element_at(0, 0)
    print(k)
  except IndexError:
    print('Correctly did not insert nodes in empty linked list')
    print()

  try: 
    n.insert_element_at(10, 0)
    n.insert_element_at(11, 1)
    n.insert_element_at(12, 1)
    n.insert_element_at(14, 2)
    print(n)
    print(len(n))
  except IndexError:
    print('Error: Should have been able to insert elements')
  
  try:
    n.insert_element_at(0, 7)
    print(k)
  except IndexError:
    print('Correctly did not insert nodes at end of list')
    print()

  try:                        #checks remove element at method
    n.remove_element_at(0)
    n.remove_element_at(1)
    print(n)
    print(len(n))
  except IndexError:
    print('Error: Should have removed elements')
  
  try:
    n.remove_element_at(20)
    print('Error: Should not have removed at out of bounds index')
  except IndexError:
    print('Successfully did not remove element at out of bounds index')
  
  try:
    n.remove_element_at(-1)
    print('Error: Should not have removed at negative index')
  except IndexError:
    print('Successfully did not remove element at negative index')

  try:                        #checks get element at method
    print(n.get_element_at(0))
    print(n.get_element_at(1))
    print('Successfully got elements')
  except IndexError:
    print('Error: Should have accessed elements')
  
  try:
    n.get_element_at(20)
    print('Error: Should not have gotten at out of bounds index')
  except IndexError:
    print('Successfully did not get element at out of bounds index')
  
  try:
    n.get_element_at(-1)
    print('Error: Should not have gotten at negative index')
  except IndexError:
    print('Successfully did not get element at negative index')
  
  s = Linked_List()           #checks the rotate left method
  s.rotate_left()
  print(s)
  s.append_element(3)
  s.rotate_left()
  print(s)
  s.append_element(4)
  s.append_element(5)
  print(s)
  s.rotate_left()
  print(s)
  
  m = Linked_List()           #checks the string method
  print(m)
  m.append_element(2)
  print(m)
  print(n)
  print(k)
  print(s)

  print('Iterator Test')      #checks iter and next
  for val in n:
    print(str(val))
  print('End of Iterator Test')
  print()

  l = Linked_List()
  for val in l:
    print(str(val))
  print("Nothing should have printed in the line directly above this")


