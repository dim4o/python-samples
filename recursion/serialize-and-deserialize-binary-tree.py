# Given a root node for a binary tree, serialize the binary tree into a string representation.
# Deserialize that same string representation into a tree identical to the original tree given.
# For better context see: https://www.youtube.com/watch?v=suj1ro8TIVY


class Node:
    def __init__(self, data=None):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.left and data < self.data:
                self.left.insert(data)
            elif self.right and data > self.data:
                self.right.insert(data)

            if not self.left and data < self.data:
                self.left = Node(data)
            elif not self.right and data > self.data:
                self.right = Node(data)
        else:
            self.data = data


def serialize(node):
    if not node:
        return "X"

    return str(node.data) + "," + \
        serialize(node.left) + "," + \
        serialize(node.right)


def deserialize_var(serialized_list):
    serialized_list = serialized_list.split(",")
    tree = Node()
    des_helper_var(tree, serialized_list)
    return tree


def des_helper_var(node, value_list):
    if value_list:
        data = value_list.pop(0)
        if data != 'X':
            node.data = data

            if value_list[0] != 'X':
                node.left = Node()
            des_helper_var(node.left, value_list)

            if value_list[0] != 'X':
                node.right = Node()

            des_helper_var(node.right, value_list)


def deserialize(serialized):
    serialized_list = serialized.split(",")
    return des_helper(serialized_list)


def des_helper(value_list):
    data = value_list.pop(0)
    if data == "X":
        return None
    new_node = Node(data)

    new_node.left = des_helper(value_list)
    new_node.right = des_helper(value_list)

    return new_node


binary_tree = Node()
binary_tree.insert(3)
binary_tree.insert(1)
binary_tree.insert(5)
binary_tree.insert(8)
binary_tree.insert(12)
binary_tree.insert(7)

serialized_tree = serialize(binary_tree)
deserialized_tree_var = deserialize_var(serialized_tree)
deserialized_tree = deserialize(serialized_tree)

print("Serialized tree:                         ", serialized_tree)
print("Serialized tree after deserialization(1):", serialize(deserialized_tree))
print("Serialized tree after deserialization(2):", serialize(deserialized_tree_var))
