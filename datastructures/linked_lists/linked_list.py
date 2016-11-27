# First, we’ll create a new class called LinkedList. Its attributes are an integer
# that contains the length of the list and a reference to the first node. LinkedList
# objects serve as handles for manipulating lists of Node objects:

class LinkedList :
    def __init__(self) :
        self.length = 0
        self.head = None

    def printBackward(self):
        print("["),
        if self.head != None:
            self.head.printBackward()
        print("]"),


class Node:

    def printBackward(self):
        if self.next != None:
            tail = self.next
            tail.printBackward()
            print(self.cargo),