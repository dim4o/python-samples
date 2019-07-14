import unittest


class Trie:
    class _TrieNode:
        def __init__(self):
            self.children = {}  # map: character -> _TrieNode
            self.end_of_word = False

    def __init__(self):
        self.root = self._TrieNode()

    def insert(self, word):
        curr_node = self.root
        word_len = len(word)
        for i in range(0, word_len):
            char = word[i]
            if char not in curr_node.children:
                new_node = self._TrieNode()
                curr_node.children[char] = new_node
                if i == word_len - 1:
                    new_node.end_of_word = True

            curr_node = curr_node.children[char]

        return

    def search_prefix(self, prefix):
        return self.__search(prefix)

    def search_word(self, word):
        return self.__search(word, hole_word=True)

    def __search(self, value, hole_word=False):
        curr_node = self.root
        pref_len = len(value)
        for i in range(0, pref_len):
            char = value[i]
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False

        if not curr_node.end_of_word and hole_word:
            return False

        return True

    def delete(self, word):
        curr_node = self.root
        prev_nodes = []
        word_len = len(word)
        for i in range(0, word_len):
            char = word[i]
            if char in curr_node.children:
                prev_nodes.append(curr_node)
                curr_node = curr_node.children[char]
            else:
                return False

        if curr_node.end_of_word:
            curr_node.end_of_word = False

        # reverse for loop
        # removes previous nodes with no children
        for i in range(word_len - 1, -1, -1):
            char = word[i]
            node = prev_nodes[i]
            if not node.children[char].children:
                node.children.pop(char)

        return True


class TestTrie(unittest.TestCase):
    insert_words = ["abc", "abgl", "cdf", "abcd", "lmn", "abcdefghijklmn"]
    error_true = "Should be True."
    error_false = "Should be False."

    def test_insert_and_contains(self):
        t = Trie()
        contains_words_false = ["ab", "a", "sdf", "lmnopq", "lm", "b", "m", "abcdefghijk"]
        contains_prefix_true = ["ab", "abg", "c", "cd", "abc", "l", "lm", "abcdefghijk", "abcdef"]
        contains_prefix_false = ["abd", "abl", "q", "cdff", "abcc", "lmo", "abcdeZghijk", "abcdeZ"]

        for w in self.insert_words:
            t.insert(word=w)

        for w in self.insert_words:
            self.assertEqual(t.search_word(w), True, self.error_true)

        for w in contains_words_false:
            self.assertEqual(t.search_word(w), False, self.error_false)

        for w in contains_prefix_true:
            self.assertEqual(t.search_prefix(w), True, self.error_true)

        for w in contains_prefix_false:
            self.assertEqual(t.search_prefix(w), False, self.error_false)

    def test_insert_and_delete_all_words(self):
        t = Trie()
        insert_words = ["abc", "abgl", "cdf", "abcd", "lmn", "abcdefghijklmn"]

        for w in insert_words:
            t.insert(word=w)

        for w in insert_words:
            t.delete(word=w)

        for w in insert_words:
            self.assertEqual(t.search_word(w), False, self.error_false)

    def test_insert_and_delete_some_words(self):
        t = Trie()
        delete_words = ["abgl", "lmn", "abc"]
        remaining_words = ["cdf", "abcd", "abcdefghijklmn"]
        prefix_search_true = ["c", "abc", "cd", "ab", "abcdefg", "abcdefghijklm", "abcd"]
        prefix_search_false = ["cdff", "abcb", "abcdeZghijk"]

        for w in self.insert_words:
            t.insert(word=w)

        for w in delete_words:
            t.delete(word=w)

        for w in delete_words:
            self.assertEqual(t.search_word(w), False, self.error_false)

        for w in remaining_words:
            self.assertEqual(t.search_word(w), True, self.error_true)

        for w in prefix_search_true:
            self.assertEqual(t.search_prefix(w), True, self.error_true)

        for w in prefix_search_false:
            self.assertEqual(t.search_prefix(w), False, self.error_false)

    def test_delete_from_empty_trie(self):
        t = Trie()
        for w in self.insert_words:
            t.delete(w)

        for w in self.insert_words:
            self.assertEqual(t.search_word(w), False, self.error_false)
            self.assertEqual(t.search_prefix(w), False, self.error_false)

    def test_search_empty_trie(self):
        t = Trie()

        for w in self.insert_words:
            self.assertEqual(t.search_word(w), False, self.error_false)
            self.assertEqual(t.search_prefix(w), False, self.error_false)


if __name__ == "__main__":
    unittest.main()
