"""
A Common-Sense Guide to Data Structures and Algorithms, Second Edition
Level Up Your Core Programming Skills
by Jay Wengrow
https://pragprog.com/titles/jwdsal2/a-common-sense-guide-to-data-structures-and-algorithms-second-edition/
"""

class Heap():
    """
    Implementation on Chapter:
    Keeping Your Priorities Straight with Heaps
    """
    def __init__(self):
        """
        Underlying a Python list is used
        to store the data
        """
        self.data_list = []

    def root_node(self):
        """
        returns first element in the list
        """
        return self.data_list[0]
    
    def last_node(self):
        """
        returns last element in the list
        """
        return self.data_list[-1]

    def get_left_child(self, index):
        """
        left_child = (index*2)+1
        """
        return (index*2)+1

    def get_right_child(self, index):
        """
        right_child = (index*2)+2
        """
        return (index*2)+2

    def get_parent_index(self, index):
        """
        parent_node = (index-1)//2
        """
        return (index-1)//2

    def insert(self, value):
        """
        Algorithm description:
        1. Add value as last element in the array
        2. Move all the way up until the parent is larger
        than the new value
        """
        # 1. Add value as last element in the array
        self.data_list.append(value)

        # Get the index of this last element in the array
        new_value_index = len(self.data_list) - 1

        # 2. Move all the way up until the parent is larger than the new value
        while new_value_index > 0 and\
            self.data_list[new_value_index] > self.data_list[self.get_parent_index(new_value_index)]:

            self.data_list[self.get_parent_index(new_value_index)], self.data_list[new_value_index] = self.data_list[new_value_index], self.data_list[self.get_parent_index(new_value_index)]

            new_value_index = self.get_parent_index(new_value_index)

    def delete(self):
        """
        Algorithm description:
        1. Make the last node the root node and remove the last node
        2. Compare this new root node with both children if any
        3. If any children is greater, swap with the largest children
        4. Go to step 2 until no children is greater or there are no children
        """
        #  Make the last node the root node and remove the last node
        self.data_list[0] = self.data_list.pop()
        trickle_node_index = 0

        while self.has_grater_child(trickle_node_index):
            larger_child_index = self.calculate_larger_child_index(trickle_node_index)

            self.data_list[trickle_node_index], self.data_list[larger_child_index] = self.data_list[larger_child_index], self.data_list[trickle_node_index]

            trickle_node_index = larger_child_index

    def has_grater_child(self, index):
        """
        Helper method
        """
        # No children
        if not (self.get_left_child(index) < len(self.data_list)):
            return False

        if self.data_list[self.calculate_larger_child_index(index)] > self.data_list[index]:
            return True
        else:
            return False

    def calculate_larger_child_index(self, index):
        """
        Helper method
        """
        # No right child (since we are at this line, there is a left child)
        if not (self.get_right_child(index) < len(self.data_list)):
            return self.get_left_child(index)
        # Left child is larger or equal than right child
        elif self.data_list[self.get_left_child(index)] >= self.data_list[self.get_right_child(index)]:
            return self.get_left_child(index)
        # Right child is larger
        else:
            return self.get_right_child(index)
