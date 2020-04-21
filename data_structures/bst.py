# This module contains the class definition for a BST


class BST:
    """
    A class that represents a binary search tree.
    """

    def __init__(self):
        """
        Initializes the contents of a BST.
        """
        self.num_nodes = 0
        self.root = None


    def insert(self, node):
        """
        Inserts a node into this BST.
        @param node: Node in tree
        type node: TreeNode
        return: None
        rtype: None
        """
        self.num_nodes += 1
        if self.num_nodes == 1:
            self.root = node
        else:
            cur_node = self.root
            prev_node = None
            side = ""
            while cur_node:
                prev_node = cur_node
                if node.val < cur_node.val:
                    cur_node = cur_node.left
                    side = "left"
                elif node.val >= cur_node.val:
                    cur_node = cur_node.right
                    side = "right"

            setattr(prev_node, side, node)



class TreeNode:
    """
    A class that represents a node in a binary tree.
    """

    def __init__(self, x):
        """
        Initializes the contents of a TreeNode
        """
        self.val = x
        self.left = None
        self.right = None




if __name__ == "__main__":
    pass
