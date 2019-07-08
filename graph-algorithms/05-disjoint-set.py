class Node:
    def __init__(self, data, rank=0):
        self.data = data
        self.rank = rank
        self.parent = self


class DisjointSet:
    def __init__(self):
        self.map = {}

    def union(self, data1, data2):
        """ Applies union operation of two sets
        :return: whether the two representatives belongs to different sets
        """
        root1 = self.find_set(data1)
        root2 = self.find_set(data2)

        if root1 == root2:
            return False

        elif root1.rank >= root2.rank:
            if root1.rank == root2.rank:
                root1.rank = root1.rank + 1
            root2.parent = root1
        else:
            root1.parent = root2

        return True

    def find_set(self, data):
        """ Finds the root node and applies path compression
        :param data: node data
        :return: the representative of the set to which the data belongs
        """
        node = self.map[data]
        if node == node.parent:
            return node

        node.parent = self.find_set(node.parent.data)

        return node.parent

    def make_set(self, data):
        self.map[data] = Node(data)


list_data = [1, 2, 3, 4, 5, 6, 7]

ds = DisjointSet()
for i in list_data:
    ds.make_set(i)

ds.union(1, 2)
ds.union(2, 3)
ds.union(4, 5)
ds.union(6, 7)
ds.union(5, 6)
# ds.union(3, 7)

print(ds.find_set(1).data)
print(ds.find_set(2).data)
print(ds.find_set(3).data)
print(ds.find_set(4).data)
print(ds.find_set(5).data)
print(ds.find_set(6).data)
print(ds.find_set(7).data)

print()
print(ds.map[7].parent.data)
# # test find_set without path compression
# ds = DisJointSet()
#
# node5 = Node(5)
# node4 = Node(4)
# node3 = Node(3)
#
# node5.parent = node3
# node4.parent = node3
#
# node2 = Node(2)
# node1 = Node(1)
#
# node2.parent = node1
# node3.parent = node1
#
# print(ds.find_set(node5).data)
# print(ds.find_set(node4).data)
# print(ds.find_set(node3).data)
# print(ds.find_set(node2).data)
# print(ds.find_set(node1).data)


# map = {}
# ds = DisJointSet()
# data_list = [1, 2, 3, 4, 5, 6, 7]
#
# for data in data_list:
#     ds.make_set(data)
