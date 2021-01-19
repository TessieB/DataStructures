import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Tester(unittest.TestCase):
    
  def setUp(self):
    self.__bst = Binary_Search_Tree()

  def test_empty_BST_string(self):
    returned = self.__bst.in_order()
    self.assertEqual('[ ]', str(self.__bst), 'Empty BST should print as "[ ]"')

  def test_empty_BST_list(self):
    returned = self.__bst.to_list()
    self.assertEqual([ ], self.__bst.to_list(), 'Empty BST should print as "[]"')

  def test_empty_BST_string_pre_order(self):
    returned = self.__bst.pre_order()
    self.assertEqual('[ ]', str(self.__bst.pre_order()), 'Empty BST should print as "[ ]"')

  def test_empty_BST_string_post_order(self):
    returned = self.__bst.post_order()
    self.assertEqual('[ ]', str(self.__bst.post_order()), 'Empty BST should print as "[ ]"')

  def test_insert_one_element_in_order(self):
    self.__bst.insert_element(1)
    returned = self.__bst.in_order()
    self.assertEqual('[ 1 ]', str(self.__bst))

  def test_insert_one_element_to_list(self):
    self.__bst.insert_element(1)
    returned = self.__bst.to_list()
    self.assertEqual([ 1 ], self.__bst.to_list())

  def test_insert_one_element_pre_order(self):
    self.__bst.insert_element(1)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 1 ]', str(self.__bst.pre_order()))

  def test_insert_one_element_post_order(self):
    self.__bst.insert_element(1)
    returned = self.__bst.post_order()
    self.assertEqual('[ 1 ]', str(self.__bst.post_order()))

  def test_insert_item_two_elements_in_order(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    returned = self.__bst.in_order()
    self.assertEqual('[ 1, 2 ]', str(self.__bst))

  def test_insert_item_two_elements_to_list(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    returned = self.__bst.to_list()
    self.assertEqual([ 1, 2 ], self.__bst.to_list())

  def test_insert_item_two_elements_pre_order(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 1, 2 ]', str(self.__bst.pre_order()))

  def test_insert_item_two_elements_post_order(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    returned = self.__bst.post_order()
    self.assertEqual('[ 2, 1 ]', str(self.__bst.post_order()))

  def test_in_order_three_elements_single_rotation_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    self.__bst.insert_element(3)
    returned = self.__bst.in_order()
    self.assertEqual('[ 1, 2, 3 ]', str(self.__bst))

  def test_to_list_three_elements_single_rotation_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    self.__bst.insert_element(3)
    returned = self.__bst.to_list()
    self.assertEqual([ 1, 2, 3 ], self.__bst.to_list())

  def test_pre_order_three_elements_single_rotation_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    self.__bst.insert_element(3)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 2, 1, 3 ]', str(self.__bst.pre_order()))

  def test_post_order_three_elements_single_rotation_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    self.__bst.insert_element(3)
    returned = self.__bst.post_order()
    self.assertEqual('[ 1, 3, 2 ]', str(self.__bst.post_order()))

  def test_in_order_three_elements_single_rotation_right(self):
    self.__bst.insert_element(3)
    self.__bst.insert_element(2)
    self.__bst.insert_element(1)
    returned = self.__bst.in_order()
    self.assertEqual('[ 1, 2, 3 ]', str(self.__bst.in_order()))

  def test_to_list_three_elements_single_rotation_right(self):
    self.__bst.insert_element(3)
    self.__bst.insert_element(2)
    self.__bst.insert_element(1)
    returned = self.__bst.to_list()
    self.assertEqual([ 1, 2, 3 ], self.__bst.to_list())

  def test_pre_order_three_elements_single_rotation_right(self):
    self.__bst.insert_element(3)
    self.__bst.insert_element(2)
    self.__bst.insert_element(1)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 2, 1, 3 ]', str(self.__bst.pre_order()))

  def test_post_order_three_elements_single_rotation_right(self):
    self.__bst.insert_element(3)
    self.__bst.insert_element(2)
    self.__bst.insert_element(1)
    returned = self.__bst.post_order()
    self.assertEqual('[ 1, 3, 2 ]', str(self.__bst.post_order()))

  def test_in_order_three_elements_double_rotation_right_then_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    returned = self.__bst.in_order()
    self.assertEqual('[ 1, 4, 5 ]', str(self.__bst))

  def test_ito_list_three_elements_double_rotation_right_then_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    returned = self.__bst.to_list()
    self.assertEqual([1, 4, 5], self.__bst.to_list())

  def test_pre_order_three_elements_double_rotation_right_then_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 4, 1, 5 ]', str(self.__bst.pre_order()))

  def test_post_order_three_elements_double_rotation_right_then_left(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    returned = self.__bst.post_order()
    self.assertEqual('[ 1, 5, 4 ]', str(self.__bst.post_order()))

  def test_in_order_three_elements_double_rotation_left_then_right(self):
    self.__bst.insert_element(5)
    self.__bst.insert_element(3)
    self.__bst.insert_element(4)
    returned = self.__bst.in_order()
    self.assertEqual('[ 3, 4, 5 ]', str(self.__bst))

  def test_to_list_three_elements_double_rotation_left_then_right(self):
    self.__bst.insert_element(5)
    self.__bst.insert_element(3)
    self.__bst.insert_element(4)
    returned = self.__bst.in_order()
    self.assertEqual([ 3, 4, 5 ], self.__bst.to_list())

  def test_pre_order_three_elements_double_rotation_left_then_right(self):
    self.__bst.insert_element(5)
    self.__bst.insert_element(3)
    self.__bst.insert_element(4)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 4, 3, 5 ]', str(self.__bst.pre_order()))

  def test_post_order_three_elements_double_rotation_left_then_right(self):
    self.__bst.insert_element(5)
    self.__bst.insert_element(3)
    self.__bst.insert_element(4)
    returned = self.__bst.post_order()
    self.assertEqual('[ 3, 5, 4 ]', str(self.__bst.post_order()))
    
  def test_insert_duplicate_item(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    with self.assertRaises(ValueError):
        self.__bst.insert_element(1)
    self.assertEqual('[ 1, 2 ]', str(self.__bst))
    
  def test_remove_from_empty_bst(self):
    with self.assertRaises(ValueError):
        self.__bst.remove_element(2)
    self.assertEqual('[ ]', str(self.__bst))

  def test_remove_from_one_element_bst(self):
    self.__bst.insert_element(1)
    self.__bst.remove_element(1)
    self.assertEqual('[ ]', str(self.__bst))

  def test_remove_non_existant_value(self):
    self.__bst.insert_element(2)
    self.__bst.insert_element(1)
    self.__bst.insert_element(3)
    with self.assertRaises(ValueError):
        self.__bst.remove_element(4)
    self.assertEqual('[ 1, 2, 3 ]', str(self.__bst))

  def test_remove_only_right_child_in_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(8)
    self.__bst.insert_element(9)
    self.__bst.insert_element(10)
    self.__bst.remove_element(9)
    returned = self.__bst.in_order()
    self.assertEqual('[ 7, 8, 10 ]', str(self.__bst))

  def test_remove_only_right_child_to_list(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(8)
    self.__bst.insert_element(9)
    self.__bst.insert_element(10)
    self.__bst.remove_element(9)
    returned = self.__bst.to_list()
    self.assertEqual([ 7, 8, 10 ], self.__bst.to_list())

  def test_remove_only_right_child_pre_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(8)
    self.__bst.insert_element(9)
    self.__bst.insert_element(10)
    self.__bst.remove_element(9)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 8, 7, 10 ]', str(self.__bst.pre_order()))

  def test_remove_only_right_child_post_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(8)
    self.__bst.insert_element(9)
    self.__bst.insert_element(10)
    self.__bst.remove_element(9)
    returned = self.__bst.post_order()
    self.assertEqual('[ 7, 10, 8 ]', str(self.__bst.post_order()))

  def test_remove_only_left_child_in_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(6)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    self.__bst.remove_element(5)
    returned = self.__bst.in_order()
    self.assertEqual('[ 4, 6, 7 ]', str(self.__bst))

  def test_remove_only_left_child_to_list(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(6)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    self.__bst.remove_element(5)
    returned = self.__bst.to_list()
    self.assertEqual([ 4, 6, 7 ], self.__bst.to_list())

  def test_remove_only_left_child_pre_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(6)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    self.__bst.remove_element(5)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 6, 4, 7 ]', str(self.__bst.pre_order()))

  def test_remove_only_left_child_post_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(6)
    self.__bst.insert_element(5)
    self.__bst.insert_element(4)
    self.__bst.remove_element(5)
    returned = self.__bst.post_order()
    self.assertEqual('[ 4, 7, 6 ]', str(self.__bst.post_order()))

  def test_remove_two_children_in_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(7)
    returned = self.__bst.in_order()
    self.assertEqual('[ 5, 8, 9 ]', str(self.__bst))

  def test_remove_two_children_to_list(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(7)
    returned = self.__bst.to_list()
    self.assertEqual([ 5, 8, 9 ], self.__bst.to_list())

  def test_remove_two_children_pre_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(7)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 8, 5, 9 ]', str(self.__bst.pre_order()))

  def test_remove_two_children_post_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(7)
    returned = self.__bst.post_order()
    self.assertEqual('[ 5, 9, 8 ]', str(self.__bst.post_order()))

  def test_remove_causing_rotation_in_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(5)
    returned = self.__bst.in_order()
    self.assertEqual('[ 7, 8, 9 ]', str(self.__bst))

  def test_remove_causing_rotation_to_list(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(5)
    returned = self.__bst.to_list()
    self.assertEqual([ 7, 8, 9 ], self.__bst.to_list())

  def test_remove_causing_rotation_pre_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(5)
    returned = self.__bst.pre_order()
    self.assertEqual('[ 8, 7, 9 ]', str(self.__bst.pre_order()))

  def test_remove_causing_rotation_post_order(self):
    self.__bst.insert_element(7)
    self.__bst.insert_element(5)
    self.__bst.insert_element(9)
    self.__bst.insert_element(8)
    self.__bst.remove_element(5)
    returned = self.__bst.post_order()
    self.assertEqual('[ 7, 9, 8 ]', str(self.__bst.post_order()))

  def test_height_of_empty_BST(self):
    returned = self.__bst.get_height()
    self.assertEqual(0, self.__bst.get_height())

  def test_height_single_element_BST(self):
    self.__bst.insert_element(1)
    returned = self.__bst.get_height()
    self.assertEqual(1, self.__bst.get_height())

  def test_height_larger_right_child(self):
    self.__bst.insert_element(0)
    self.__bst.insert_element(2)
    self.__bst.insert_element(4)
    self.__bst.insert_element(1)
    returned = self.__bst.get_height()
    self.assertEqual(3, self.__bst.get_height())

  def test_height_larger_left_child(self):
    self.__bst.insert_element(0)
    self.__bst.insert_element(-1)
    self.__bst.insert_element(4)
    self.__bst.insert_element(-3)
    returned = self.__bst.get_height()
    self.assertEqual(3, self.__bst.get_height())

  def test_height_with_rotation(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(2)
    self.__bst.insert_element(4)
    returned = self.__bst.get_height()
    self.assertEqual(2, self.__bst.get_height())

  def test_height_with_insertion_and_rotation(self):
    self.__bst.insert_element(1)
    self.__bst.insert_element(10)
    self.__bst.insert_element(8)
    self.__bst.insert_element(-3)
    self.__bst.insert_element(12)
    returned = self.__bst.get_height()
    self.assertEqual(3, self.__bst.get_height())

  def test_height_with_insertion_removal_and_rotation_changing_height(self):
    self.__bst.insert_element(10)
    self.__bst.insert_element(5)
    self.__bst.insert_element(20)
    self.__bst.insert_element(22)
    self.__bst.remove_element(5)
    returned = self.__bst.get_height()
    self.assertEqual(2, self.__bst.get_height())

  def test_height_with_double_rotation(self):
    self.__bst.insert_element(10)
    self.__bst.insert_element(5)
    self.__bst.insert_element(20)
    self.__bst.insert_element(4)
    self.__bst.remove_element(4)
    returned = self.__bst.get_height()
    self.assertEqual(2, self.__bst.get_height())

if __name__ == '__main__':
    unittest.main()
