import unittest


class BinarySearchTree:
    class _Node:
        def __init__(self, value, left_child=None, right_child=None):
            self.value = value
            self.left_child = left_child
            self.right_child = right_child

    def __init__(self):
        self.root = None
        self.left_child = None
        self.right_child = None
        self.values = []

    def add(self, value):
        new_node = self._Node(value)
        if not self.root:
            self.root = new_node
        else:
            curr_node = self.root

            while curr_node:
                parent_node = curr_node
                if new_node.value <= curr_node.value:
                    curr_node = curr_node.left_child
                    if not curr_node:
                        parent_node.left_child = new_node
                else:
                    curr_node = curr_node.right_child
                    if not curr_node:
                        parent_node.right_child = new_node

    def inorder_traversal_search(self, curr_node, value, parent=None):
        if not curr_node:
            return

        left_child_node = self.inorder_traversal_search(curr_node.left_child, value, curr_node)

        if curr_node.value == value:
            return curr_node, parent

        right_child_node = self.inorder_traversal_search(curr_node.right_child, value, curr_node)

        return left_child_node or right_child_node

    def remove(self, value):
        target_node = self._search(value)
        if not target_node.left_child and not target_node.right_child:
            self._remove_leaf(value)
        elif target_node.left_child and not target_node.right_child \
                or not target_node.left_child and target_node.right_child:
            self._remove_one_child_node(value)
        else:
            # min_node = self.get_max()
            cur = target_node.left_child
            prev = target_node
            while cur.right_child:
                prev = cur
                cur = cur.right_child

            min_node = cur

            target_node.value = min_node.value
            if not min_node.left_child and not min_node.right_child:
                self._remove_leaf(min_node.value, prev)
            elif min_node.left_child and not min_node.right_child \
                    or min_node.left_child and not min_node.right_child:
                self._remove_one_child_node(min_node.value, prev, min_node)

    def _remove_leaf(self, value, parent=None):
        if not parent:
            _, parent = self.inorder_traversal_search(curr_node=self.root, value=value)
        if not parent:
            self.root = None
            return
        if parent.left_child and parent.left_child.value == value:
            parent.left_child = None
        else:
            parent.right_child = None

    def _remove_one_child_node(self, value, parent=None, target_node=None):
        if not parent:
            target_node, parent = self.inorder_traversal_search(curr_node=self.root, value=value)
        if parent.left_child and parent.left_child.value == value:
            parent.left_child = target_node.left_child or target_node.right_child
        if parent.right_child and parent.right_child.value == value:
            parent.right_child = target_node.left_child or target_node.right_child

    def inorder_traversal(self, curr_node):
        if not curr_node:
            return

        self.inorder_traversal(curr_node.left_child)

        # print(curr_node.value)
        self.values.append(curr_node.value)
        self.inorder_traversal(curr_node.right_child)

    def _search(self, value):
        curr_node = self.root
        while curr_node:
            if curr_node.value == value:
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left_child
            else:
                curr_node = curr_node.right_child

        return None

    def get_min(self):
        curr_node = self.root

        while curr_node.left_child:
            curr_node = curr_node.left_child

        return curr_node

    def get_max(self):
        curr_node = self.root

        while curr_node.right_child:
            curr_node = curr_node.right_child

        return curr_node

    def get_values(self):
        self.values = []
        self.inorder_traversal(self.root)
        return self.values


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bt = BinarySearchTree()
        self.expected_values = [8, 7, 9, 11, 6, 0, 7.5, 8.5, 9.5, 10.5, 15, 20, 10]
        for val in self.expected_values:
            self.bt.add(val)

    def test_add(self):

        actual_values = self.bt.get_values()
        expected_values = [0, 6, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 15, 20]
        # print(actual_values)

        self.assertCountEqual(actual_values, expected_values, "The added vales are not as expected.")

    def test_remove(self):
        values_to_remove = [11, 10.5, 9, 8, 7, 9.5, 20, 8.5, 7.5, 10, 0, 15, 6]
        self.expected_values = sorted(self.expected_values)

        for i in values_to_remove:
            self.expected_values.remove(i)
            self.bt.remove(i)

            print(self.expected_values)
            print(self.bt.get_values())

            self.assertCountEqual(self.bt.get_values(), self.expected_values,
                                  "The lists should be equal after removal.")

    def remove_from_empty_tree(self):
        bt = BinarySearchTree()
        bt.remove(100)
        self.bt.remove(1000)

    def test_search(self):
        non_existing_values = [-100, 100, 300, 999, 42]
        for i in self.expected_values:
            self.assertEqual(self.bt._search(i).value, i)

        for i in non_existing_values:
            self.assertEqual(self.bt._search(i), None)

    def test_get_max(self):
        max_expected = max(self.expected_values)
        max_actual = self.bt.get_max().value

        self.assertEqual(max_actual, max_expected)

    def test_get_min(self):
        min_expected = min(self.expected_values)
        min_actual = self.bt.get_min().value

        self.assertEqual(min_actual, min_expected)


if __name__ == "__main__":
    unittest.main()
