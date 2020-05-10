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
        # Edge case where there are
        # no nodes in the tree
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


    def get_bst_list(self):
        """
        Gets a representation of this BST as a list
        where the elements are the values of the nodes
        and where the order of the elements within this list
        corresponds to the order of the nodes at each level.
        return: A list that represents this BST
        rtype: [values of BST's nodes]
        """
        queue = [self.root]
        result = []
        # BFS traversal:
        while queue:
            cur_node = queue.pop(0)
            if cur_node:
                result.append(cur_node.val)
                queue.extend([cur_node.left, cur_node.right])

        return result


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
    # Visual Representation of what I'm gonna make:
    #             10
    #          /      \
    #        5         15
    #       / \      /   \
    #     3    7   null  18
    bst = BST()
    tree_vals = [10,5,15,3,7,18]
    for val in tree_vals:
        bst.insert(TreeNode(val))

    print(bst.get_bst_list())
