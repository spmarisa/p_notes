# attributes that refer to other objects, which we called embedded references

# Linked lists are made up of nodes, where each node contains a reference to the next node in the list.
# In addition, each node contains a unit of data called the cargo.

# A linked list is considered a recursive data structure because it has a recur-sive definition.

class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)