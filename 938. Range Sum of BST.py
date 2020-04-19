
# ===== Problem Statement ===== #
# Given the root node of a binary search tree, return the sum
# of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # Runtime: 304 ms
    # Memory: 22.1 MB
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        total = 0
        if root:
            # Only add to total value if root.val
            # meets the requested constraints
            if root.val >= L and root.val <= R:
                total += root.val

            # The total value on the current level of
            # recursion will be added with the total
            # values deeper in the recursion
            total += self.rangeSumBST(root.left, L, R)
            total += self.rangeSumBST(root.right, L, R)
        return total



if __name__ == "__main__":
    # Manyally build BST for testing from the leaves up
    # TODO: Write a BST class with insert() functionality
    #       for these leetcode exercises
    #             10
    #          /      \
    #        5         15
    #       / \      /   \
    #     3    7   null  18
    # Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    # Target Output: 32

    node18 = TreeNode(18)
    #nodeNull = TreeNode(None)  # No need
    node7 = TreeNode(7)
    node3 = TreeNode(3)
    node15 = TreeNode(15)
    #node15.left = nodeNull  # No need
    node15.right = node18
    node5 = TreeNode(5)
    node5.left = node3
    node5.right = node7
    node10 = TreeNode(10)
    node10.left = node5
    node10.right = node15

    sol = Solution()
    L, R = 7, 15
    result = sol.rangeSumBST(node10, L, R)
    print(result)
