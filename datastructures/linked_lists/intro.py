# attributes that refer to other objects, which we called embedded references

# Linked lists are made up of nodes, where each node contains a reference to the next node in the list.
# In addition, each node contains a unit of data called the cargo.

# A linked list is considered a recursive data structure because it has a recur-sive definition.
# A linked list is either:
#    • the empty list, represented by None, or
#    • a node that contains a cargo object and a reference to a linked list.

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.next)



node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
# print(node1)
# print(node2)
# print(node3)
#
# node1.next = node2
# node2.nest = node3
# print(node1)

def printList(node):
    while node:
        print(node),
        node = node.next
    print

printList(node1)