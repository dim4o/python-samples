class MinBinaryHeap:
    def get_map(self):
        return self.heap_map

    def __init__(self):
        self.heap_map = {}

    def add(self, vertex):
        index = len(self.heap_map)
        self.heap_map[index] = vertex

        parent_index = int(index / 2)
        parent = self.heap_map[parent_index]

        while parent != vertex and parent > vertex:
            self.__swap(index, parent_index)

            index = parent_index
            parent_index = int(parent_index / 2)

            parent = self.heap_map[parent_index]
            vertex = self.heap_map[index]

    def extract_min(self):
        if not self.heap_map:
            raise Exception("You are trying to extract an element from empty Heap.")

        curr_index = 0
        min_element = self.heap_map[curr_index]
        last_index = len(self.heap_map) - 1

        # swaps the last added element with the top element
        self.__swap(curr_index, last_index)
        # removes the last added element (i.e. the target top element)
        self.heap_map.pop(last_index)

        # pull down the new top element to it's position
        while curr_index in self.heap_map.keys():
            curr = self.heap_map[curr_index]
            left_child = self.heap_map.get(2 * curr_index + 1, None)
            right_child = self.heap_map.get(2 * curr_index + 2, None)

            # if the left child is None hence the right child is also None
            if left_child is None:
                break

            min_child = min(left_child, right_child) if right_child else left_child

            if min_child < curr and min_child is left_child:
                self.__swap(2 * curr_index + 1, curr_index)
                curr_index = 2 * curr_index + 1
            elif right_child:
                self.__swap(2 * curr_index + 2, curr_index)
                curr_index = 2 * curr_index + 2
            else:
                break

        return min_element

    def get_min(self):
        return self.heap_map[0]

    def __swap(self, index1, index2):
        tmp = self.heap_map[index1]
        self.heap_map[index1] = self.heap_map[index2]
        self.heap_map[index2] = tmp


bh = MinBinaryHeap()
bh.add(16)
bh.add(2)
bh.add(20)
bh.add(19)
bh.add(15)
bh.add(-10)
bh.add(40)
bh.add(-15)
print(bh.get_map())

for i in range(0, len(bh.get_map())):
    print(bh.extract_min())
