try:
    def get_index(array, i):
        """
        get the index of the node/elemennet in the queue
        :param array:
        :param i:
        :return: index of an element if the element is in the queue
        """

        if i in list(array):
            index = array.index(i)
            return index


    def insert(array, i):
        """
        Gets size of priority queue, if the size is equal to zero or not append the element
        :param array:
        :param i:
        :return:
        """
        size = len(array)

        if size == 0:
            array.append(i)
        else:
            array.append(i)



    def move_up(array, elem):
        """
        Place the element within the array based on the priority while maintaining binary heap.
        N.B: Parent node is less than the children
        :param array:
        :param elem:
        :return: array
        """
        index_elem = get_index(array, elem)

        prev_node_index = (index_elem - 1) // 2
        curr_node = array[index_elem]
        prev_node = array[prev_node_index]

        if curr_node < prev_node:
            first_ele = array.pop(index_elem)
            second_ele = array.pop(prev_node_index)
            array.insert(index_elem, second_ele)
            array.insert(prev_node_index, first_ele)
            return array
        else:
            return array

except Exception as e:
    print(e)



nodes = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

tree = []

# Iterate through the elements while maintaining the priority queue
for i in nodes:
    insert(tree, i)

print("Priority Queue Given before inserting 12:", tree)

insert(tree, 12)

# Check if inserted node is greater than the parent node
move_up(tree, 12)

print("Final Priority Queue:", tree)
