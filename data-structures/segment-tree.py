import unittest


class SegmentTee:
    def __init__(self, input_arr, query_func, no_overlap_default_value):
        """
        :param input_arr: an array that is an object of the query
        :param query_func: a lambda function that accept two arguments amd returns a number
        :param no_overlap_default_value: the default return value when the query interval
        does not overlap the interval from the tree
        """
        self.__input_size = len(input_arr)
        self.__query_func = query_func
        self.no_overlap_value = no_overlap_default_value
        self.seg_tree = self.__class__._create_empty_segment_tree(self.__input_size)
        self._build_segment_tree(input_arr, 0, len(input_arr) - 1, 0, query_func)

    def range_query(self, start_index, end_index):
        """ Apply a query in a given range of the SegmentTree
        :param start_index: the start index of the query
        :param end_index: the end index of the query
        :return: the result of the query (i.e. max, min, or sum of the segment elements)
        """
        return self._range_query(query_lo=start_index, query_hi=end_index, lo=0, hi=self.__input_size - 1, pos=0)

    def _range_query(self, query_lo, query_hi, lo, hi, pos):
        """ Apply a query in a given range of the SegmentTree
        :param query_lo: the lower index of the query
        :param query_hi: the higher index of the query
        :param lo: the current lower index
        :param hi: the current higher index
        :param pos: the current position in the SegmentTree
        :return: the result of the query
        """
        if query_lo <= lo and query_hi >= hi:
            return self.seg_tree[pos]
        if query_lo > hi or query_hi < lo:
            return self.no_overlap_value
        mid = int((lo + hi)/2)

        left = self._range_query(query_lo, query_hi, lo, mid, 2 * pos + 1)
        right = self._range_query(query_lo, query_hi, mid + 1, hi, 2 * pos + 2)

        return self.__query_func(left, right)

    def _build_segment_tree(self, input_list, lo, hi, pos, query_func):
        """ Builds a SegmentTree with recursion
        :param input_list: an array that is an object of the query
        :param lo: the lower bound of the current interval
        :param hi: the higher bound of the current interval
        :param pos: the current position in the segment tree array
        :param query_func: a lambda function that accept two arguments amd returns an integer value
        """
        if lo == hi:
            self.seg_tree[pos] = input_list[lo]
            return
        mid = int((lo + hi) / 2)

        self._build_segment_tree(input_list, lo, mid, 2 * pos + 1, query_func)
        self._build_segment_tree(input_list, mid + 1, hi, 2 * pos + 2, query_func)

        self.seg_tree[pos] = query_func(self.seg_tree[2 * pos + 1], self.seg_tree[2 * pos + 2])

    @staticmethod
    def _create_empty_segment_tree(size):
        """ Creates an empty segment tree
        :param size: the size of the initial list
        :return: a new list with size = 2 * (next power of 2) - 1, i. e
        if size = 4 (the next power of 2 is the number itself) the new length is 2*2^2 - 1 = 7,
        if size = 7 (the next power of two is 8) the new length is 3*2^3 - 1 = 15
        """
        import math

        next_pow_of_two = math.ceil(math.log(size, 2))
        new_size = 2 * math.pow(2, next_pow_of_two) - 1

        return [0] * int(new_size)


class TestSegmentTree(unittest.TestCase):
    def test_min_query(self):
        min_st = SegmentTee(
            [-1, 2, 4, 0],
            query_func=lambda x, y: min(x, y),
            no_overlap_default_value=float('inf'))

        self.assertEqual(min_st.range_query(1, 3), 0)
        self.assertEqual(min_st.range_query(0, 3), -1)
        self.assertEqual(min_st.range_query(0, 2), -1)
        self.assertEqual(min_st.range_query(1, 2), 2)
        self.assertEqual(min_st.range_query(2, 2), 4)

    def test_max_query(self):
        max_st = SegmentTee(
            [-1, 2, 4, 0],
            query_func=lambda x, y: max(x, y),
            no_overlap_default_value=float('-inf'))

        self.assertEqual(max_st.range_query(1, 3), 4)
        self.assertEqual(max_st.range_query(0, 3), 4)
        self.assertEqual(max_st.range_query(0, 2), 4)
        self.assertEqual(max_st.range_query(1, 2), 4)
        self.assertEqual(max_st.range_query(2, 2), 4)
        self.assertEqual(max_st.range_query(0, 1), 2)
        self.assertEqual(max_st.range_query(3, 3), 0)

    def test_sum_query(self):
        sum_st = SegmentTee(
            [1, 3, 5, 7, 9, 11],
            query_func=lambda x, y: x + y,
            no_overlap_default_value=0)

        self.assertEqual(sum_st.range_query(1, 4), 24)
        self.assertEqual(sum_st.range_query(0, 2), 9)
        self.assertEqual(sum_st.range_query(3, 5), 27)
        self.assertEqual(sum_st.range_query(2, 4), 21)
        self.assertEqual(sum_st.range_query(0, 5), 36)
        self.assertEqual(sum_st.range_query(3, 3), 7)


if __name__ == "__main__":
    unittest.main()
