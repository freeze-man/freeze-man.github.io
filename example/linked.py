class Node(object):
    # Constructor to initilize class variables
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    #get data
    def get_data(self):
        return self.data

    # get next value
    def get_next(self):
        return self.next_node

    # set next data
    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    # Returns total numbers of node in list
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
        current = current.get_next()
        return count

    # Returns the node in list having nodeData, error occured if node not present
    def search(self, nodeData):
        current = self.head
        isPresent = False
        while current and isPresent is False:
            if current.get_data() == nodeData:
                isPresent = True
        else:
            current = current.get_next()
        if current is None:
            raise ValueError("Data not present in list")
        return current

    # Remove the node from linked list returns error if node not present
    def delete(self, nodeData):
        current = self.head
        previous = None
        isPresent = False
        while current and isPresent is False:
            if current.get_data() == nodeData:
                isPresent = True
        else:
            previous = current
        current = current.get_next()
        if current is None:
            raise ValueError("Data not present in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
