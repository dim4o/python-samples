import unittest


class LinkedList:

    class _Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None

    def __init__(self):
        self._tail = self._Node()
        self._head = self._tail
        self._size = 0

    def add(self, value):
        """ Adds a value to the list """
        self._tail.next = self._Node(value)
        self._tail = self._tail.next
        self._size += 1

    def get_head(self):
        """ Returns the first node """
        return self._head.next.value

    def get_tail(self):
        """ Returns the last node """
        return self._tail.value

    def remove_all(self, value):
        """ Removes all occurrences of a specific value """
        self.__remove(value)

    def remove_first(self, value):
        """ Removes the first occurrence of a specific value """
        self.__remove(value, first=True)

    def __remove(self, value, first=False):
        curr_node = self._head
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next
            if curr_node.value == value:
                prev_node.next = curr_node.next
                self._size -= 1
                if first:
                    break

    def reverse(self):
        """ Performs in place reverse """
        self._tail = self._head.next
        self._head = self._head.next
        prev = None
        curr = self._head  # the first non-empty value node

        while self._head:
            self._head = self._head.next
            curr.next = prev
            prev = curr
            curr = self._head

        self._head = self._Node()
        self._head.next = prev

    def size(self):
        return self._size

    def to_list(self):
        result_list = []
        curr_node = self._head
        while curr_node.next:
            curr_node = curr_node.next
            result_list.append(curr_node.value)
        return result_list

    def __str__(self):
        return str(self.to_list())


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.actual_elements = [5, 7, 1, 7, 2, 19, 5, -1, 8]
        self.ll = LinkedList()
        for el in self.actual_elements:
            self.ll.add(el)

    def test_add(self):
        added_elements = self.ll.to_list()

        # see: https://docs.python.org/3.2/library/unittest.html#unittest.TestCase.assertCountEqual
        self.assertCountEqual(added_elements, self.actual_elements, "The tow list should be equal.")

    def test_remove_first(self):
        self.ll.remove_first(7)
        self.actual_elements.remove(7)

        # see: https://docs.python.org/3.2/library/unittest.html#unittest.TestCase.assertCountEqual
        self.assertCountEqual(self.ll.to_list(), self.actual_elements, "The tow list should be equal.")

    def test_remove_all(self):
        self.ll.remove_all(7)
        actual_result = [x for x in self.actual_elements if x != 7]

        # see: https://docs.python.org/3.2/library/unittest.html#unittest.TestCase.assertCountEqual
        self.assertCountEqual(self.ll.to_list(), actual_result, "The tow list should be equal.")

    def test_get_head(self):
        tail = self.actual_elements[-1]

        self.assertEqual(self.ll.get_tail(), tail, "Wrong tail element.")

    def test_get_tail(self):
        head = self.actual_elements[0]

        self.assertEqual(self.ll.get_head(), head, "Wrong head element.")

    def test_reverse(self):
        self.ll.reverse()
        actual_reversed = list(reversed(self.actual_elements))

        # see: https://docs.python.org/3.2/library/unittest.html#unittest.TestCase.assertCountEqual
        self.assertCountEqual(self.ll.to_list(), actual_reversed, "The tow list should be equal.")

        one_element_list = [7]
        one_element_list.reverse()
        self.assertCountEqual(one_element_list, [7])

        no_element_list = []
        self.assertCountEqual(no_element_list, [])

    def test_size(self):
        self.assertEqual(self.ll.size(), len(self.actual_elements), "Wrong size.")

        self.ll.remove_all(7)

        self.assertEqual(self.ll.size(), len(self.actual_elements)-2, "Wrong size.")

        self.setUp()
        self.ll.remove_first(7)

        self.assertEqual(self.ll.size(), len(self.actual_elements) - 1, "Wrong size.")

        self.ll.remove_first(7)

        self.assertEqual(self.ll.size(), len(self.actual_elements) - 2, "Wrong size.")


if __name__ == "__main__":
    unittest.main()
