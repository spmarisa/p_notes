class LinkedList:
    def __init__(self, elements=[]):
        self.head = None

        if len(elements) != 0:
            address = None

            for i in reversed(elements):
                node = Node(i, address)
                address = id(node)

            self.head = node

    def head(self):
        return self.head

class Node:
    def __init__(self, value, next_element):
        self.value = value
        self.next_element = next_element
