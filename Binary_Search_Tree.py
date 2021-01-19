class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value
      self.height = 0
      self.left_child = None
      self.right_child = None

  def __init__(self):
    self.__root = None
    self.__word = ""
  
  def __recursive_insert(self, value, root1):
    root = root1
    if root is None:
      root = Binary_Search_Tree.__BST_Node(value)
      root.height = 1
      return root
    else:
      if value < root.value:
        root.left_child = self.__recursive_insert(value, root.left_child)
        root.height = self.__update_height(root)
        return self.__balance(root)
      elif value > root.value:
        root.right_child = self.__recursive_insert(value, root.right_child)
        root.height = self.__update_height(root)
        return self.__balance(root)
      elif value == root.value:
        raise ValueError
      

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recursive_insert(value, self.__root)

  def __recursive_remove(self, value1, root1):
    value = value1
    root = root1
    if root is None:
      raise ValueError
    elif value == root.value:
      if root.left_child is not None and root.right_child is not None:
        temp = root.right_child
        parent = temp
        while temp.left_child is not None:
          if temp.left_child.left_child is None:
            parent = temp
          temp = temp.left_child
        root.value = temp.value
        if temp == root.right_child:
          root.right_child = root.right_child.right_child
          root.height = self.__update_height(root)
          return self.__balance(root)
        else:
          parent.left_child = None
          parent.height = self.__update_height(parent)
        return self.__balance(root)
      elif root.left_child is not None and root.right_child is None:
        root = root.left_child
        root.height = self.__update_height(root)
        return self.__balance(root)
      elif root.right_child is not None and root.left_child is None:
        root = root.right_child
        root.height = self.__update_height(root)
        return self.__balance(root)
    else:
      if value < root.value:
        root.left_child = self.__recursive_remove(value, root.left_child)
        root.height = self.__update_height(root)
        return self.__balance(root)
      elif value > root.value:
        root.right_child = self.__recursive_remove(value, root.right_child)
        root.height = self.__update_height(root)
        return self.__balance(root)

  
  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    self.__root = self.__recursive_remove(value, self.__root)

  def __recursive_in_order(self, root1):
    root = root1
    word = ""
    if root is None:
      return ""
    else:
        word += str(self.__recursive_in_order(root.left_child))
        word += str(root.value)
        word += ', '
        word += str(self.__recursive_in_order(root.right_child))
        return word

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    self.__word = '[ '
    self.__word += str(self.__recursive_in_order(self.__root.left_child))
    self.__word += str(self.__root.value) + ', '
    self.__word += str(self.__recursive_in_order(self.__root.right_child))
    self.__word = self.__word[0:len(self.__word)- 2]
    self.__word += ' ]'
    return self.__word


  def __recursive_pre_order(self, root1):
    root = root1
    word = ""
    if root is None:
      return ""
    else:
        word += str(root.value)
        word += ', '
        word += str(self.__recursive_pre_order(root.left_child))
        word += str(self.__recursive_pre_order(root.right_child))
        return word     
  
  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    self.__word = '[ '
    self.__word += str(self.__root.value) + ', '
    self.__word += str(self.__recursive_pre_order(self.__root.left_child))
    self.__word += str(self.__recursive_pre_order(self.__root.right_child))
    self.__word = self.__word[0:len(self.__word)- 2]
    self.__word += ' ]'
    return self.__word

  def __recursive_post_order(self, root1):
    root = root1
    word = ""
    if root is None:
      return ""
    else:
        word += str(self.__recursive_post_order(root.left_child))
        word += str(self.__recursive_post_order(root.right_child))
        word += str(root.value)
        word += ', '
        return word

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root is None:
      return '[ ]'
    self.__word = '[ '
    self.__word += str(self.__recursive_post_order(self.__root.left_child))
    self.__word += str(self.__recursive_post_order(self.__root.right_child))
    self.__word += str(self.__root.value) + ', '
    self.__word = self.__word[0:len(self.__word)- 2]
    self.__word += ' ]'
    return self.__word

  def __recursive_to_list(self, root1, my_list1):
    root = root1
    my_list = my_list1
    if root is not None:
      self.__recursive_to_list(root.left_child, my_list)
      my_list.append(root.value)
      self.__recursive_to_list(root.right_child, my_list)
    return my_list
  
  def to_list(self):
    my_list = []
    if self.__root is None:
      return my_list
    self.__recursive_to_list(self.__root, my_list)
    return my_list

  def __update_height(self, root1):
    root = root1
    if root.right_child is None and root.left_child is None:
      return 1
    elif root.right_child is None:
      root.height = root.left_child.height + 1
    elif root.left_child is None:
      root.height = root.right_child.height + 1
    elif root.right_child.height > root.left_child.height:
      root.height = root.right_child.height + 1
    else:
      root.height = root.left_child.height + 1
    return root.height

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root is None:
      return 0
    elif self.__root.right_child is None and self.__root.left_child is None:
      return 1
    elif self.__root.right_child is None:
      self.__root.height = self.__root.left_child.height + 1
    elif self.__root.left_child is None:
      self.__root.height = self.__root.right_child.height + 1
    elif self.__root.right_child.height > self.__root.left_child.height:
      self.__root.height = self.__root.right_child.height + 1
    else:
      self.__root.height = self.__root.left_child.height + 1
    return self.__root.height

  def __get_avl_number(self, root1):
    root = root1
    if root.left_child is None and root.right_child is None:
      return 0
    elif root.right_child is None:
      return 0 - root.left_child.height
    elif root.left_child is None:
      return root.right_child.height
    else:
      return root.right_child.height - root.left_child.height
  
  def __balance(self, t):
    root = t
    temp = root
    if root is None:
      return root
    elif self.__get_avl_number(root) == -2:
      if self.__get_avl_number(root.left_child) == 1:
        temp = root.left_child
        root.left_child = root.left_child.right_child
        temp.right_child = None
        temp.height = self.__update_height(temp)
        if root.left_child.left_child is not None:
          temp2 = root.left_child.left_child
          root.left_child.left_child = temp
          root.left_child.left_child.right_child = temp2
        else:
          root.left_child.left_child = temp
        root.left_child.height = self.__update_height(root.left_child)
      if self.__get_avl_number(root.left_child) == -1 or self.__get_avl_number(root.left_child) == 0:
        temp = root
        root = root.left_child
        temp.left_child = None
        temp.height = self.__update_height(temp)
        if root.right_child is not None:
          temp2 = root.right_child
          root.right_child = temp
          root.right_child.left_child = temp2
        else:
          root.right_child = temp
    elif self.__get_avl_number(root) == 2:
      if self.__get_avl_number(root.right_child) == -1:
        temp = root.right_child
        root.right_child = root.right_child.left_child
        temp.left_child = None
        temp.height = self.__update_height(temp)
        if root.right_child.right_child is not None:
          temp2 = root.right_child.right_child
          root.right_child.right_child = temp
          root.right_child.right_child.left_child = temp2
        else:
          root.right_child.right_child = temp
        root.right_child.height = self.__update_height(root.right_child)
      if self.__get_avl_number(root.right_child) == 1 or self.__get_avl_number(root.right_child) == 0:
        temp = root
        root = root.right_child
        temp.right_child = None
        temp.height = self.__update_height(temp)
        if root.left_child is not None:
          temp2 = root.left_child
          root.left_child = temp
          root.left_child.right_child = temp2
        else:
          root.left_child = temp
    self.__update_height(root)
    return root

  def __str__(self):
    return self.in_order()

#if __name__ == '__main__':
  #unit tests make the main section unnecessary.

