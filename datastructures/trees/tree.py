class Tree:
    def __init__(self):
        self.root = None

    def levelOrderBinaryTree(self, arr):
        self.root = self.levelOrderBinaryTreeUtil(arr, 0)
        print(self.root.value)

    def levelOrderBinaryTreeUtil(self, arr, start):
        size = len(arr)

        curr = self.Node(arr[start])
        left = 2 * start + 1
        right = 2 * start + 2
        if left < size:
            curr.lChild = self.levelOrderBinaryTreeUtil(arr, left)
        if right < size:
            curr.rChild = self.levelOrderBinaryTreeUtil(arr, right)
        return curr


    @classmethod
    def main(cls, args):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        t2 = Tree()
        t2.levelOrderBinaryTree(arr)


class Node:
    def __init__(self, value, left_child, right_child):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child






































