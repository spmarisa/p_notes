class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addValue(self, value):
        node = Node(value)
        node.next_element = self.head
        self.head = node

    def printAll(self):
        tmp = self.head
        while tmp != None:
            print(tmp.value)
            tmp = tmp.next_element

    def removeDuplicates(self):
        print('banana')


class Node:
    def __init__(self, value, next_element=None):
        self.value = value
        self.next_element = next_element



# ll = SinglyLinkedList()
# ll.addValue(44)
# print(ll.head.value)
# ll.addValue(45)
# print(ll.head.value)

