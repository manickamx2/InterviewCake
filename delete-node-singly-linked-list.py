import unittest

# Delete the input node from the linked list
def delete_node(node_to_delete):
    next_node = node_to_delete.next

    if next_node:
        # set the value and pointer node_to_delete to the value and pointer of next_node
        node_to_delete.value = next_node.value
        node_to_delete.next = next_node.next
    else:
        # we're trying to delete the last node, so raise an exception
        raise Exception("Trying to delete the last node!")


# Tests
class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_node_at_beginning(self):
        delete_node(self.first)
        actual = self.first.get_values()
        expected = [2, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_in_middle(self):
        delete_node(self.second)
        actual = self.first.get_values()
        expected = [1, 3, 4]
        self.assertEqual(actual, expected)

    def test_node_at_end(self):
        with self.assertRaises(Exception):
            delete_node(self.fourth)

    def test_one_node_in_list(self):
        unique = Test.LinkedListNode(1)
        with self.assertRaises(Exception):
            delete_node(unique)


unittest.main(verbosity=2)

##### NOTES #####
# side effects can occur because of this implementation.
# consider: It doesn't work for deleting the last node in the list.
#   We could just set the last node to have a value of None and treat
#   it as a "dead" node and have our implementation stop traversing when
#   it reaches such a node. But this precludes nodes in the linked-list
#   from having None values. So we'll just raise an exception.

# consider: Any references to the node to be deleted now point to its "next."
#   If there were other pointers to the node to be deleted and we were expecting
#   the original value and pointer, we could cause issues.

# consider: We could have dangling nodes.
#   If there are references to the input node's next node, those references now
#   point to a dangling node (a node that can't be reached traversing the list).
