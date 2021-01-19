from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1
    self.__contents = [None] * self.__capacity
    self.__front = 0
    self.__back = 0
    self.__size = 0
    
  def __str__(self):
    if self.__size == 0:
      return '[ ]'
    if self.__front == self.__back:
      return '[ ' + str(self.__contents[self.__front]) + ' ]'
    word = '[ '
    if self.__front < self.__back:
      for i in range(self.__front, self.__back + 1):
        word += str(self.__contents[i])
        if i != self.__back:
            word += ', '
    elif self.__back < self.__front:
      for i in range(self.__front, self.__capacity):
        word += str(self.__contents[i]) + ', '
      for i in range(self.__back + 1):
        word += str(self.__contents[i])
        if i != self.__back:
            word += ', '
    word += ' ]'
    return word
    
  def __len__(self):
    return self.__size

  def __grow(self):
    new_array = [None] * (self.__capacity * 2)
    j = 0
    if self.__capacity == 1:
      new_array[0] = self.__contents[0]
    elif self.__front < self.__back:
      for i in range(self.__front, self.__back + 1):
        new_array[j] = self.__contents[i]
        j += 1
    elif self.__back < self.__front:
      for i in range(self.__front, self.__capacity):
        new_array[j] = self.__contents[i]
        j += 1
      for i in range(self.__back + 1):
        new_array[j] = self.__contents[i]
        j += 1
    self.__capacity = self.__capacity * 2
    self.__contents = new_array
    self.__front = 0
    self.__back = self.__size - 1
    
  def push_front(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    if self.__size == 0 and self.__front == self.__back:
      self.__front = self.__front
    else:
      self.__front = (self.__front + self.__capacity - 1) % self.__capacity
    self.__contents[self.__front] = val
    self.__size += 1
    
  def pop_front(self):
    if self.__size > 0:
      temp = self.__contents[self.__front]
      self.__front = (self.__front + self.__capacity + 1) % self.__capacity
      self.__size -= 1
      return temp

  def peek_front(self):
    return self.__contents[self.__front]
    
  def push_back(self, val):
    if self.__size == self.__capacity:
      self.__grow()
    if self.__size == 0 and self.__front == self.__back:
      self.__back = self.__back
    else:
      self.__back = (self.__back + self.__capacity + 1) % self.__capacity
    self.__contents[self.__back] = val
    self.__size += 1

  def pop_back(self):
    if self.__size > 0:
      temp = self.__contents[self.__back]
      self.__back = (self.__back + self.__capacity - 1) % self.__capacity
      self.__size -= 1
      return temp

  def peek_back(self):
    # TODO replace pass with your implementation.
    return self.__contents[self.__back]

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#  pass
  